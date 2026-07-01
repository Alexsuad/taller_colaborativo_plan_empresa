#!/usr/bin/env python3
"""Detectar placeholders pendientes en respuestas_plan_empresa/."""

from __future__ import annotations

import re
import sys
from pathlib import Path


RESPUESTAS_DIR = Path("respuestas_plan_empresa")
PATTERNS = [
    re.compile(r"\[PENDIENTE\]", re.IGNORECASE),
    re.compile(r"Pendiente de completar", re.IGNORECASE),
    re.compile(r"Estado: pendiente de respuesta\.", re.IGNORECASE),
    re.compile(r"_Pendiente\._", re.IGNORECASE),
    re.compile(r"pendiente de respuesta", re.IGNORECASE),
    re.compile(r"Vacíos / decisiones pendientes", re.IGNORECASE),
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
]


def main() -> int:
    if not RESPUESTAS_DIR.is_dir():
        print("ARCHIVOS_CON_PLACEHOLDERS:")
        print("TOTAL: 0")
        print("VERDICT: PENDIENTE")
        print(f"ERROR: no existe la carpeta {RESPUESTAS_DIR}")
        return 1

    files_with_placeholders: list[str] = []
    for path in sorted(RESPUESTAS_DIR.rglob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
        except OSError as exc:
            print("ARCHIVOS_CON_PLACEHOLDERS:")
            print("TOTAL: 0")
            print("VERDICT: PENDIENTE")
            print(f"ERROR: no se pudo leer {path}: {exc}")
            return 1

        if any(pattern.search(content) for pattern in PATTERNS):
            files_with_placeholders.append(str(path))

    print("ARCHIVOS_CON_PLACEHOLDERS:")
    if files_with_placeholders:
        for item in files_with_placeholders:
            print(f"- {item}")
    else:
        print("- ninguno")
    print(f"TOTAL: {len(files_with_placeholders)}")
    print("VERDICT: PENDIENTE" if files_with_placeholders else "VERDICT: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
