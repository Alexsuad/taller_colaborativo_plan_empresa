#!/usr/bin/env python3
"""Comprobar que no haya cambios pendientes en rutas prohibidas."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PROHIBITED_PREFIXES = (
    "respuestas_plan_empresa/",
    "_build/",
    "docs_consolidados/",
)


def normalize_path(path: str) -> str:
    return path.replace("\\", "/").strip()


def extract_paths(status_line: str) -> list[str]:
    path_part = status_line[3:].strip()
    if " -> " in path_part:
        old_path, new_path = path_part.split(" -> ", 1)
        return [normalize_path(old_path), normalize_path(new_path)]
    return [normalize_path(path_part)]


def path_is_prohibited(path: str) -> bool:
    return any(path.startswith(prefix) for prefix in PROHIBITED_PREFIXES)


def main() -> int:
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        print("VERDICT: FAIL")
        print(f"ERROR: no se pudo ejecutar git status --short: {exc}")
        return 1

    offending_lines: list[str] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        for path in extract_paths(line):
            if path_is_prohibited(path):
                offending_lines.append(line)
                break

    print("RUTAS_PROHIBIDAS:")
    for prefix in PROHIBITED_PREFIXES:
        print(f"- {prefix}")

    print("CAMBIOS_PROHIBIDOS:")
    if offending_lines:
        for line in offending_lines:
            print(f"- {line}")
        print("VERDICT: FAIL")
        return 1

    print("- ninguno")
    print("VERDICT: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
