#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditor determinista de lenguaje en respuestas finales.
Este script analiza los archivos markdown en respuestas_plan_empresa/ para buscar
lenguaje interno del sistema (FAIL), lenguaje absoluto (WARNING) y frases comodín (WARNING).

Este script no corrige documentos; solo detecta patrones de riesgo para revisión.
"""

import os
import re
import argparse
from datetime import datetime

# Listas de patrones configuradas (fáciles de ampliar)
PATRONES_FAIL = [
    "Gate 1D",
    "workflow",
    "skill",
    "F-REPO",
    "F-NOTEBOOKLM",
    "REQUIERE_",
    "NO_RESPONDER",
    "BORRADOR_PARCIAL_CON_VACIOS",
    "BLOQUEADO",
    "LISTO_PARA_REVISION",
    "TEXTO_PROPUESTO",
    "VALIDACIONES_REQUERIDAS",
    "ESTADO_SALIDA"
]

PATRONES_WARNING_ABSOLUTO = [
    "se prohíbe",
    "se determina",
    "queda definido",
    "es obligatorio",
    "el único método",
    "ninguno de los modelos",
    "se descarta definitivamente",
    "debe ser",
    "indispensable"
]

PATRONES_WARNING_GENERICO = [
    "aporta valor",
    "permite diferenciarse",
    "mejora la experiencia del cliente",
    "refuerza la propuesta de valor",
    "ayuda al posicionamiento",
    "servicio de calidad",
    "experiencia única",
    "solución integral",
    "modelo disruptivo",
    "alto potencial de crecimiento"
]

PATRONES_WARNING_TONO_MECANICO = [
    "alta densidad",
    "propuesta de valor emocional",
    "sumamente potente",
    "ancla",
    "subordinación operativa",
    "garantiza la seguridad",
    "tasa de accidentes",
    "fuente de ingresos estables y recurrentes muy valiosa",
    "incapacidad física del usuario"
]

PATRONES_WARNING_RIESGO_LEGAL = [
    "exoneración de responsabilidad"
]

# Configuración de rutas
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
RESPUESTAS_DIR_DEFAULT = os.path.join(REPO_ROOT, "respuestas_plan_empresa")
REPORTES_DIR = os.path.join(REPO_ROOT, "_build", "reportes")
REPORTE_PATH = os.path.join(REPORTES_DIR, "auditoria_lenguaje_respuestas.md")

# Archivos a ignorar
ARCHIVOS_IGNORADOS = {
    "00_indice_preguntas_guia.md",
    "index.md"
}

def obtener_fragmento(linea, patron, max_len=100):
    """Extrae un fragmento de la línea que rodea al patrón detectado para dar contexto."""
    linea_strip = linea.strip()
    if len(linea_strip) <= max_len:
        return linea_strip
    
    # Buscar la posición del patrón de manera insensible a mayúsculas/minúsculas
    match = re.search(re.escape(patron), linea_strip, re.IGNORECASE)
    if not match:
        return linea_strip[:max_len] + "..."
    
    start_idx, end_idx = match.span()
    half_len = max_len // 2
    start = max(0, start_idx - half_len)
    end = min(len(linea_strip), end_idx + half_len)
    
    fragmento = linea_strip[start:end]
    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(linea_strip) else ""
    
    return f"{prefix}{fragmento}{suffix}"

def auditar_archivos(respuestas_dir):
    hallazgos = []
    archivos_analizados = 0

    if not os.path.exists(respuestas_dir):
        print(f"Error: La carpeta de respuestas no existe en: {respuestas_dir}")
        return hallazgos, archivos_analizados

    for filename in sorted(os.listdir(respuestas_dir)):
        if not filename.endswith(".md") or filename in ARCHIVOS_IGNORADOS:
            continue
        
        file_path = os.path.join(respuestas_dir, filename)
        archivos_analizados += 1
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line_idx, line in enumerate(f, 1):
                    # Comprobar FAIL
                    for patron in PATRONES_FAIL:
                        if patron.lower() in line.lower():
                            hallazgos.append({
                                "archivo": filename,
                                "linea": line_idx,
                                "severidad": "FAIL",
                                "patron": patron,
                                "fragmento": obtener_fragmento(line, patron)
                            })
                    
                    # Comprobar WARNING ABSOLUTO
                    for patron in PATRONES_WARNING_ABSOLUTO:
                        if patron.lower() in line.lower():
                            hallazgos.append({
                                "archivo": filename,
                                "linea": line_idx,
                                "severidad": "WARNING",
                                "patron": patron,
                                "fragmento": obtener_fragmento(line, patron)
                            })

                    # Comprobar WARNING GENÉRICO
                    for patron in PATRONES_WARNING_GENERICO:
                        if patron.lower() in line.lower():
                            hallazgos.append({
                                "archivo": filename,
                                "linea": line_idx,
                                "severidad": "WARNING",
                                "patron": patron,
                                "fragmento": obtener_fragmento(line, patron)
                            })

                    # Comprobar WARNING TONO MECÁNICO
                    for patron in PATRONES_WARNING_TONO_MECANICO:
                        if patron.lower() in line.lower():
                            hallazgos.append({
                                "archivo": filename,
                                "linea": line_idx,
                                "severidad": "WARNING_TONO_MECANICO",
                                "patron": patron,
                                "fragmento": obtener_fragmento(line, patron)
                            })

                    # Comprobar WARNING RIESGO LEGAL
                    for patron in PATRONES_WARNING_RIESGO_LEGAL:
                        if patron.lower() in line.lower():
                            hallazgos.append({
                                "archivo": filename,
                                "linea": line_idx,
                                "severidad": "WARNING_RIESGO_LEGAL",
                                "patron": patron,
                                "fragmento": obtener_fragmento(line, patron)
                            })
        except Exception as e:
            print(f"Error al leer el archivo {filename}: {e}")

    return hallazgos, archivos_analizados

def generar_reporte(hallazgos, archivos_analizados):
    os.makedirs(REPORTES_DIR, exist_ok=True)
    
    total_fails = sum(1 for h in hallazgos if h["severidad"] == "FAIL")
    total_warnings_general = sum(1 for h in hallazgos if h["severidad"] == "WARNING")
    total_warnings_mec = sum(1 for h in hallazgos if h["severidad"] == "WARNING_TONO_MECANICO")
    total_warnings_legal = sum(1 for h in hallazgos if h["severidad"] == "WARNING_RIESGO_LEGAL")
    
    total_warnings = total_warnings_general + total_warnings_mec + total_warnings_legal
    
    if total_fails > 0:
        estado_global = "FAIL"
    elif total_warnings > 0:
        estado_global = "WARNING"
    else:
        estado_global = "OK"
        
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    contenido = []
    contenido.append("# Auditoría de Lenguaje de Respuestas")
    contenido.append("")
    contenido.append("> [!IMPORTANT]")
    contenido.append("> Este script no corrige documentos; solo detecta patrones de riesgo para revisión.")
    contenido.append("")
    contenido.append(f"- **Fecha de ejecución**: {fecha_actual}")
    contenido.append(f"- **Estado global**: `{estado_global}`")
    contenido.append(f"- **Total de archivos revisados**: {archivos_analizados}")
    contenido.append("")
    contenido.append("## Resumen por Severidad")
    contenido.append("")
    contenido.append("| Severidad | Total |")
    contenido.append("| --- | --- |")
    contenido.append(f"| FAIL | {total_fails} |")
    contenido.append(f"| WARNING (General) | {total_warnings_general} |")
    contenido.append(f"| WARNING_TONO_MECANICO | {total_warnings_mec} |")
    contenido.append(f"| WARNING_RIESGO_LEGAL | {total_warnings_legal} |")
    contenido.append("")
    contenido.append("## Tabla de Hallazgos")
    contenido.append("")
    
    if not hallazgos:
        contenido.append("No se detectaron patrones de riesgo en los archivos revisados.")
    else:
        contenido.append("| Archivo | Línea | Severidad | Patrón Detectado | Fragmento Breve |")
        contenido.append("| --- | --- | --- | --- | --- |")
        for h in hallazgos:
            # Limpiar caracteres que puedan romper la tabla markdown
            fragmento_limpio = h["fragmento"].replace("|", "\\|").replace("\n", " ").replace("\r", " ")
            contenido.append(f"| {h['archivo']} | {h['linea']} | `{h['severidad']}` | `{h['patron']}` | {fragmento_limpio} |")
            
    contenido.append("")
    
    try:
        with open(REPORTE_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(contenido))
        print(f"Reporte generado con éxito en: {REPORTE_PATH}")
    except Exception as e:
        print(f"Error al escribir el reporte: {e}")
        
    return total_fails, total_warnings, total_warnings_general, total_warnings_mec, total_warnings_legal, estado_global

def main():
    parser = argparse.ArgumentParser(description="Auditor de lenguaje en respuestas.")
    parser.add_argument(
        "--dir",
        type=str,
        default=RESPUESTAS_DIR_DEFAULT,
        help="Directorio que contiene las respuestas a auditar."
    )
    args = parser.parse_args()

    print(f"Iniciando auditoría de lenguaje en respuestas desde: {args.dir}")
    hallazgos, archivos_analizados = auditar_archivos(args.dir)
    total_fails, total_warnings, total_warnings_general, total_warnings_mec, total_warnings_legal, estado_global = generar_reporte(hallazgos, archivos_analizados)
    
    print(f"\nAuditoría finalizada.")
    print(f"Archivos revisados: {archivos_analizados}")
    print(f"Total FAILs: {total_fails}")
    print(f"Total WARNINGs: {total_warnings} (General: {total_warnings_general}, Tono Mecánico: {total_warnings_mec}, Riesgo Legal: {total_warnings_legal})")
    print(f"Estado global: {estado_global}")
    
    # Retornar exit code 1 si hay al menos un FAIL
    if total_fails > 0:
        return 1
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
