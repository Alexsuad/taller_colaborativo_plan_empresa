#!/usr/bin/env python3
import os
import sys
import argparse
import yaml
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Audita el repositorio para detectar términos de contaminación conceptual."
    )
    parser.add_argument(
        "--config",
        default="config/contaminacion_conceptual.yml",
        help="Ruta al archivo YAML de configuración."
    )
    parser.add_argument(
        "--report",
        default="_build/reportes/auditoria_contaminacion_conceptual.md",
        help="Ruta donde se generará el reporte Markdown."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Imprime los hallazgos detallados por consola."
    )
    return parser.parse_args()

def load_config(config_path):
    if not os.path.exists(config_path):
        print(f"ERROR: El archivo de configuración no existe en '{config_path}'", file=sys.stderr)
        sys.exit(2)
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"ERROR: El archivo de configuración en '{config_path}' está mal formado. Detalle: {e}", file=sys.stderr)
        sys.exit(2)

def clean_relative_path(path):
    # Asegurar formato estándar de ruta relativa con barras inclinadas
    return str(path).replace("\\", "/")

def should_ignore(relative_path_str, ignored_paths, ignored_files):
    # Validar si el path coincide con carpetas ignoradas
    for path in ignored_paths:
        clean_p = path.strip("/")
        parts = relative_path_str.split("/")
        if clean_p in parts:
            return True
        if relative_path_str.startswith(clean_p + "/"):
            return True
            
    # Validar si el path coincide con archivos ignorados
    for f in ignored_files:
        if relative_path_str == f or relative_path_str.endswith("/" + f):
            return True
            
    return False

def determine_status(relative_path_str, term_def):
    allowed = term_def.get("allowed_paths", [])
    blocked = term_def.get("blocked_paths", [])
    
    # Comprobar coincidencia con rutas bloqueadas
    for b_path in blocked:
        b_clean = b_path.strip("/")
        if relative_path_str.startswith(b_clean) or (f"/{b_clean}/" in f"/{relative_path_str}/"):
            return "BLOCKED"
            
    # Comprobar coincidencia con rutas permitidas
    for a_path in allowed:
        a_clean = a_path.strip("/")
        if relative_path_str.startswith(a_clean) or (f"/{a_clean}/" in f"/{relative_path_str}/"):
            return "ALLOWED_LEGACY"
            
    return "REVIEW"

def scan_repository(config):
    default_policy = config.get("default_policy", {})
    case_sensitive = default_policy.get("case_sensitive", False)
    report_context_chars = default_policy.get("report_context_chars", 80)
    
    ignored_paths = config.get("ignored_paths", [])
    ignored_files = config.get("ignored_files", [])
    terms = config.get("terms", [])
    
    # Extensiones de archivo a escanear
    valid_extensions = {".md", ".txt", ".yml", ".yaml", ".py"}
    
    hallazgos = []
    
    for root, dirs, files in os.walk("."):
        # Filtrar directorios en os.walk para evitar recorrerlos si están en ignored_paths
        dirs[:] = [d for d in dirs if not should_ignore(clean_relative_path(Path(root) / d), ignored_paths, ignored_files)]
        
        for file in files:
            file_path = Path(root) / file
            rel_path_str = clean_relative_path(file_path.relative_to("."))
            
            if should_ignore(rel_path_str, ignored_paths, ignored_files):
                continue
                
            if file_path.suffix not in valid_extensions:
                continue
                
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
            except Exception:
                # Si no se puede abrir el archivo, lo omitimos silenciosamente
                continue
                
            for line_idx, line in enumerate(lines, 1):
                for term in terms:
                    term_id = term.get("id")
                    severity = term.get("severity", "MEDIUM")
                    action = term.get("action", "review_or_replace")
                    replacement_hint = term.get("replacement_hint", "")
                    patterns = term.get("patterns", [])
                    
                    for pattern in patterns:
                        matched = False
                        if case_sensitive:
                            if pattern in line:
                                matched = True
                        else:
                            if pattern.lower() in line.lower():
                                matched = True
                                
                        if matched:
                            status = determine_status(rel_path_str, term)
                            
                            # Obtener contexto
                            context = line.strip()
                            if len(context) > report_context_chars:
                                # Truncar centrándose en la palabra clave si es posible
                                idx = context.lower().find(pattern.lower())
                                if idx != -1:
                                    start = max(0, idx - (report_context_chars // 2))
                                    end = min(len(context), start + report_context_chars)
                                    context = ("..." if start > 0 else "") + context[start:end] + ("..." if end < len(context) else "")
                                else:
                                    context = context[:report_context_chars] + "..."
                                    
                            hallazgos.append({
                                "file": rel_path_str,
                                "line": line_idx,
                                "term_id": term_id,
                                "pattern": pattern,
                                "severity": severity,
                                "status": status,
                                "context": context,
                                "action": action,
                                "replacement_hint": replacement_hint
                            })
                            
    return hallazgos

def generate_markdown_report(report_path, hallazgos, config_path):
    report_file = Path(report_path)
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Contadores
    blocked_count = sum(1 for h in hallazgos if h["status"] == "BLOCKED")
    review_count = sum(1 for h in hallazgos if h["status"] == "REVIEW")
    allowed_count = sum(1 for h in hallazgos if h["status"] == "ALLOWED_LEGACY")
    
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    
    # Agrupar hallazgos
    blocked_hallazgos = sorted(
        [h for h in hallazgos if h["status"] == "BLOCKED"],
        key=lambda x: (severity_order.get(x["severity"], 99), x["file"], x["line"])
    )
    review_hallazgos = sorted(
        [h for h in hallazgos if h["status"] == "REVIEW"],
        key=lambda x: (severity_order.get(x["severity"], 99), x["file"], x["line"])
    )
    allowed_hallazgos = sorted(
        [h for h in hallazgos if h["status"] == "ALLOWED_LEGACY"],
        key=lambda x: (severity_order.get(x["severity"], 99), x["file"], x["line"])
    )
    
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("# Reporte de Auditoría de Contaminación Conceptual\n\n")
        f.write(f"Generado a partir del archivo de configuración: `{config_path}`.\n\n")
        
        f.write("## Resumen Estadístico\n\n")
        f.write("| Estado | Cantidad | Descripción |\n")
        f.write("| :--- | :---: | :--- |\n")
        f.write(f"| 🔴 **BLOCKED** | {blocked_count} | Términos en rutas no permitidas. Requiere acción inmediata. |\n")
        f.write(f"| 🟡 **REVIEW** | {review_count} | Términos detectados en rutas neutras o sin definir. |\n")
        f.write(f"| 🟢 **ALLOWED_LEGACY** | {allowed_count} | Términos en rutas permitidas (histórico / legacy). |\n\n")
        
        f.write("## 🔴 Hallazgos Bloqueantes (BLOCKED)\n\n")
        if not blocked_hallazgos:
            f.write("No se encontraron hallazgos bloqueantes en las rutas prohibidas. ¡Excelente!\n\n")
        else:
            f.write("| Archivo | Línea | Término | Severidad | Contexto | Recomendación |\n")
            f.write("| :--- | :---: | :--- | :---: | :--- | :--- |\n")
            for h in blocked_hallazgos:
                f.write(f"| [`{h['file']}`](file:///{h['file']}) | {h['line']} | `{h['pattern']}` | **{h['severity']}** | `{h['context']}` | {h['replacement_hint']} ({h['action']}) |\n")
            f.write("\n")
            
        f.write("## 🟡 Hallazgos en Revisión (REVIEW)\n\n")
        if not review_hallazgos:
            f.write("No hay hallazgos pendientes de revisión en rutas neutras.\n\n")
        else:
            f.write("| Archivo | Línea | Término | Severidad | Contexto | Recomendación |\n")
            f.write("| :--- | :---: | :--- | :---: | :--- | :--- |\n")
            for h in review_hallazgos:
                f.write(f"| [`{h['file']}`](file:///{h['file']}) | {h['line']} | `{h['pattern']}` | **{h['severity']}** | `{h['context']}` | {h['replacement_hint']} ({h['action']}) |\n")
            f.write("\n")
            
        f.write("## 🟢 Hallazgos Permitidos (ALLOWED_LEGACY)\n\n")
        if not allowed_hallazgos:
            f.write("No hay registros de uso legacy permitidos en el repositorio.\n\n")
        else:
            f.write("| Archivo | Línea | Término | Severidad | Contexto | Recomendación |\n")
            f.write("| :--- | :---: | :--- | :---: | :--- | :--- |\n")
            for h in allowed_hallazgos:
                f.write(f"| [`{h['file']}`](file:///{h['file']}) | {h['line']} | `{h['pattern']}` | **{h['severity']}** | `{h['context']}` | {h['replacement_hint']} ({h['action']}) |\n")
            f.write("\n")

def main():
    args = parse_arguments()
    config = load_config(args.config)
    
    if args.verbose:
        print(f"Iniciando escaneo con configuración: {args.config}")
        
    hallazgos = scan_repository(config)
    
    if args.verbose:
        print(f"Escaneo finalizado. Hallazgos encontrados: {len(hallazgos)}")
        for h in hallazgos:
            print(f"[{h['status']}] {h['file']}:{h['line']} - Término: '{h['pattern']}' ({h['severity']}) -> Contexto: '{h['context']}'")
            
    generate_markdown_report(args.report, hallazgos, args.config)
    
    # Determinar exit code
    blocked_count = sum(1 for h in hallazgos if h["status"] == "BLOCKED")
    if blocked_count > 0:
        if args.verbose:
            print(f"\nAUDITORÍA FALLIDA: Se encontraron {blocked_count} hallazgos bloqueantes (BLOCKED).")
        sys.exit(1)
    else:
        if args.verbose:
            print("\nAUDITORÍA EXITOSA: No hay hallazgos bloqueantes.")
        sys.exit(0)

if __name__ == "__main__":
    main()
