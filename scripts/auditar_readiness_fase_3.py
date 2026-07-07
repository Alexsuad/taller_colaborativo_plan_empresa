#!/usr/bin/env python3
"""Auditor minimo de readiness por capitulo para Fase 3."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GUIDE_DIR = ROOT / "plan_empresa_guia"
RESPUESTAS_DIR = ROOT / "respuestas_plan_empresa"
MATRIX_PATH = ROOT / "docs_organizacion" / "08_matriz_clasificacion_preguntas_red_arce.md"

PLACEHOLDER_PATTERNS = [
    re.compile(r"\[PENDIENTE\]", re.IGNORECASE),
    re.compile(r"Pendiente de completar", re.IGNORECASE),
    re.compile(r"Estado: pendiente de respuesta\.", re.IGNORECASE),
    re.compile(r"_Pendiente\._", re.IGNORECASE),
    re.compile(r"pendiente de respuesta", re.IGNORECASE),
    re.compile(r"Vacíos / decisiones pendientes", re.IGNORECASE),
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
]

TAXONOMY_PATTERNS = {
    "[F-REPO]": re.compile(r"\[F-REPO\]"),
    "[F-NOTEBOOKLM]": re.compile(r"\[F-NOTEBOOKLM\]"),
    "[U-DATO]": re.compile(r"\[U-DATO\]"),
    "[U-VALIDA]": re.compile(r"\[U-VALIDA\]"),
    "[U-ELIGE]": re.compile(r"\[U-ELIGE\]"),
    "[U-AUTORIZA]": re.compile(r"\[U-AUTORIZA\]"),
    "[I-SIMPLE]": re.compile(r"\[I-SIMPLE\]"),
    "[I-DEEP]": re.compile(r"\[I-DEEP\]"),
    "[M]": re.compile(r"\[M\]"),
    "[NO-RESPONDER-AÚN]": re.compile(r"\[NO-RESPONDER-AÚN\]"),
    "[F]": re.compile(r"\[F\]"),
    "[U]": re.compile(r"\[U\]"),
}

SECTION_PREFIX_TO_STEM = {
    "0.": "00_resumen_ejecutivo",
    "1.": "01_equipo_promotor",
    "2.": "02_idea_negocio",
    "3.1": "03_1_analisis_externo",
    "3.2": "03_2_estudio_mercado",
    "3.3": "03_3_analisis_interno",
    "3.4": "03_4_benchmarking_inspiradores",
    "4.": "04_dafo_came",
    "5.": "05_objetivos_lineas_estrategicas",
    "6.0": "06_0_marca_comunicacion_naming",
    "6.1": "06_1_marketing_ventas",
    "6.2": "06_2_operaciones",
    "6.3": "06_3_recursos_humanos",
    "6.4": "06_4_juridico_fiscal",
    "6.5": "06_5_economico_financiero",
    "7.": "07_implantacion_puesta_marcha",
    "8.": "08_viabilidad_conclusiones",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def list_markdown_files(directory: Path) -> dict[str, Path]:
    if not directory.is_dir():
        raise FileNotFoundError(f"No existe la carpeta {directory}")

    files: dict[str, Path] = {}
    for path in sorted(directory.glob("*.md")):
        if path.name == "index.md":
            continue
        files[path.stem] = path
    return files


def has_placeholders(content: str) -> bool:
    return any(pattern.search(content) for pattern in PLACEHOLDER_PATTERNS)


def extract_tags(text: str) -> list[str]:
    tags: list[str] = []
    for tag, pattern in TAXONOMY_PATTERNS.items():
        if pattern.search(text):
            tags.append(tag)
    return tags


def parse_matrix_entries(matrix_text: str) -> dict[str, dict[str, object]]:
    entries: dict[str, dict[str, object]] = {}
    in_main_table = False

    for raw_line in matrix_text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("| ID | Sección Red ARCE |"):
            in_main_table = True
            continue
        if in_main_table and line.startswith("## 4."):
            break
        if not in_main_table or not line.startswith("|"):
            continue
        if re.match(r"^\|\s*-+\s*\|", line):
            continue

        cols = [col.strip() for col in line.split("|")[1:-1]]
        if len(cols) < 11:
            continue

        section_label = cols[1]
        classification = cols[4]
        action = cols[8]
        question = cols[2]
        tags = extract_tags(classification)

        for prefix, stem in SECTION_PREFIX_TO_STEM.items():
            if section_label.startswith(prefix):
                data = entries.setdefault(
                    stem,
                    {
                        "section": section_label,
                        "questions": [],
                        "classifications": [],
                        "actions": [],
                        "tags": set(),
                    },
                )
                data["questions"].append(question)
                data["classifications"].append(classification)
                data["actions"].append(action)
                data["tags"].update(tags)
                break

    return entries


def derive_dependency_flags(tags: set[str]) -> dict[str, bool]:
    has_repo = "[F-REPO]" in tags or "[F]" in tags
    has_notebooklm = "[F-NOTEBOOKLM]" in tags
    has_alex = any(
        tag in tags
        for tag in ("[U-DATO]", "[U-VALIDA]", "[U-ELIGE]", "[U-AUTORIZA]", "[U]")
    )
    has_investigation = "[I-SIMPLE]" in tags or "[I-DEEP]" in tags
    has_no_responder = "[NO-RESPONDER-AÚN]" in tags
    has_mixed = "[M]" in tags
    return {
        "repo": has_repo,
        "notebooklm": has_notebooklm,
        "alex": has_alex,
        "investigacion": has_investigation,
        "no_responder": has_no_responder,
        "mixto": has_mixed,
    }


def base_status_from_flags(flags: dict[str, bool], tags: set[str]) -> str:
    if not tags:
        return "PENDIENTE_CLASIFICACION"
    if flags["no_responder"]:
        return "NO_RESPONDER_AUN"
    if flags["investigacion"]:
        return "REQUIERE_INVESTIGACION"
    if flags["notebooklm"]:
        return "REQUIERE_NOTEBOOKLM"
    if flags["alex"]:
        return "REQUIERE_ALEX"
    if flags["repo"]:
        return "PREPARABLE_CON_REPO"
    return "PENDIENTE_CLASIFICACION"


def recommended_action(status: str) -> str:
    actions = {
        "PREPARABLE_CON_REPO": "PREPARAR_EXTRACCION_DESDE_REPO",
        "REQUIERE_ALEX": "PREPARAR_PAQUETE_PARA_ALEX",
        "REQUIERE_NOTEBOOKLM": "PREPARAR_CONSULTA_NOTEBOOKLM",
        "REQUIERE_INVESTIGACION": "PREPARAR_INVESTIGACION_CONTROLADA",
        "NO_RESPONDER_AUN": "MANTENER_BLOQUEADO_HASTA_VALIDACION",
        "PENDIENTE_CLASIFICACION": "CLASIFICAR_EN_MATRIZ_08",
        "CON_PLACEHOLDERS": "PREPARAR_SIN_REDACCION_Y_MANTENER_PLACEHOLDER",
        "SIN_ARCHIVO_RESPUESTA": "CREAR_CORRESPONDENCIA_OPERATIVA_SIN_REDACTAR",
        "SIN_ARCHIVO_GUIA": "REVISAR_CORRESPONDENCIA_Y_MANTENER_COMO_ADVERTENCIA",
        "BLOQUEADO": "NO_AVANZAR_SIN_DECISION_O_EVIDENCIA",
    }
    return actions.get(status, "REVISAR_MANUALMENTE")


def build_entry(
    stem: str,
    guide_path: Path | None,
    response_path: Path | None,
    matrix_entry: dict[str, object] | None,
) -> dict[str, object]:
    reasons: list[str] = []
    tags: set[str] = set()
    dependencies: list[str] = []

    if matrix_entry:
        tags = set(matrix_entry["tags"])  # type: ignore[index]
        reasons.append(f"clasificación detectada en matriz 08 para {matrix_entry['section']}")
    else:
        reasons.append("sin evidencia de clasificación suficiente en matriz 08")

    flags = derive_dependency_flags(tags)
    if flags["repo"]:
        dependencies.append("REPO")
    if flags["alex"]:
        dependencies.append("ALEX")
    if flags["notebooklm"]:
        dependencies.append("NOTEBOOKLM")
    if flags["investigacion"]:
        dependencies.append("INVESTIGACION")
    if flags["no_responder"]:
        dependencies.append("NO_RESPONDER_AUN")
    if flags["mixto"]:
        dependencies.append("MIXTO")

    base_status = base_status_from_flags(flags, tags)
    status = base_status

    if guide_path is None:
        status = "SIN_ARCHIVO_GUIA"
        reasons.append("hay archivo de respuesta sin guía asociada")
    elif response_path is None:
        status = "SIN_ARCHIVO_RESPUESTA"
        reasons.append("no existe archivo de respuesta asociado")
    else:
        content = read_text(response_path)
        if has_placeholders(content):
            if not tags:
                status = "BLOQUEADO"
                reasons.append("hay placeholders y no existe clasificación suficiente")
            else:
                status = "CON_PLACEHOLDERS"
                reasons.append("el archivo de respuesta contiene placeholders o marcadores pendientes")

    if base_status == "PENDIENTE_CLASIFICACION" and status not in {
        "SIN_ARCHIVO_GUIA",
        "SIN_ARCHIVO_RESPUESTA",
        "BLOQUEADO",
    }:
        reasons.append("falta clasificación accionable para preparar el capítulo")

    if base_status == "NO_RESPONDER_AUN":
        reasons.append("la matriz marca este bloque como no respondible todavía")

    if not dependencies:
        dependencies = ["SIN_DEPENDENCIAS_IDENTIFICADAS"]

    return {
        "capitulo": stem,
        "guia": str(guide_path.relative_to(ROOT)) if guide_path else "-",
        "respuesta": str(response_path.relative_to(ROOT)) if response_path else "-",
        "status": status,
        "base_status": base_status,
        "reasons": reasons,
        "dependencies": dependencies,
        "next_action": recommended_action(status),
        "preparable_con_repo": flags["repo"] and not flags["no_responder"],
        "requiere_alex": flags["alex"],
        "requiere_notebooklm": flags["notebooklm"],
        "requiere_investigacion": flags["investigacion"],
        "no_responder_aun": flags["no_responder"],
    }


def derive_global_verdict(entries: list[dict[str, object]]) -> str:
    matched_pairs = [
        item
        for item in entries
        if item["guia"] != "-" and item["respuesta"] != "-"
    ]
    if not matched_pairs:
        return "FASE_3_SIN_CORRESPONDENCIA_GUIA_RESPUESTA"

    if any(item["preparable_con_repo"] for item in entries):
        return "FASE_3_PREPARABLE_PARCIALMENTE"
    if any(item["status"] == "PENDIENTE_CLASIFICACION" for item in entries):
        return "FASE_3_REQUIERE_CLASIFICACION"
    if any(item["requiere_alex"] for item in entries):
        return "FASE_3_REQUIERE_ALEX"
    if any(item["requiere_notebooklm"] for item in entries):
        return "FASE_3_REQUIERE_NOTEBOOKLM"
    if any(item["requiere_investigacion"] for item in entries):
        return "FASE_3_REQUIERE_INVESTIGACION"
    return "FASE_3_BLOQUEADA"


def print_report(entries: list[dict[str, object]], verdict: str, total_guides: int, total_responses: int) -> None:
    count_preparable = sum(1 for item in entries if item["preparable_con_repo"])
    count_blocked = sum(1 for item in entries if item["status"] in {"BLOQUEADO", "SIN_ARCHIVO_GUIA", "SIN_ARCHIVO_RESPUESTA"})
    count_alex = sum(1 for item in entries if item["requiere_alex"])
    count_notebooklm = sum(1 for item in entries if item["requiere_notebooklm"])
    count_investigacion = sum(1 for item in entries if item["requiere_investigacion"])
    count_no_responder = sum(1 for item in entries if item["no_responder_aun"])

    print(f"VERDICT: {verdict}")
    print(f"TOTAL_GUIAS: {total_guides}")
    print(f"TOTAL_RESPUESTAS: {total_responses}")
    print(f"CAPITULOS_PREPARABLES: {count_preparable}")
    print(f"CAPITULOS_BLOQUEADOS: {count_blocked}")
    print(f"CAPITULOS_REQUIEREN_ALEX: {count_alex}")
    print(f"CAPITULOS_REQUIEREN_NOTEBOOKLM: {count_notebooklm}")
    print(f"CAPITULOS_REQUIEREN_INVESTIGACION: {count_investigacion}")
    print(f"CAPITULOS_NO_RESPONDER_AUN: {count_no_responder}")
    print("DETALLE:")

    for item in entries:
        print(f"- capitulo: {item['capitulo']}")
        print(f"  guia: {item['guia']}")
        print(f"  respuesta: {item['respuesta']}")
        print(f"  estado: {item['status']}")
        print(f"  razones: {'; '.join(item['reasons'])}")
        print(f"  dependencias: {', '.join(item['dependencies'])}")
        print(f"  siguiente_accion_recomendada: {item['next_action']}")


def main() -> int:
    try:
        guides = list_markdown_files(GUIDE_DIR)
        responses = list_markdown_files(RESPUESTAS_DIR)
        matrix_text = read_text(MATRIX_PATH)
    except OSError as exc:
        print(f"ERROR: {exc}")
        return 1

    matrix_entries = parse_matrix_entries(matrix_text)
    entries: list[dict[str, object]] = []

    all_stems = sorted(set(guides) | set(responses))
    for stem in all_stems:
        guide_path = guides.get(stem)
        response_path = responses.get(stem)
        matrix_entry = matrix_entries.get(stem)
        entries.append(build_entry(stem, guide_path, response_path, matrix_entry))

    verdict = derive_global_verdict(entries)
    print_report(entries, verdict, len(guides), len(responses))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
