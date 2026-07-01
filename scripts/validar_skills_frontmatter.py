#!/usr/bin/env python3
"""Validar frontmatter mínimo de las skills del repositorio."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SKILLS_ROOT = Path(".agents/skills")


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1].strip()
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    lines = text.splitlines()
    index = 0

    while index < len(lines) and not lines[index].strip():
        index += 1

    if index >= len(lines) or lines[index].strip() != "---":
        return {}, "no existe frontmatter YAML al inicio del archivo"

    index += 1
    frontmatter_lines: list[str] = []
    while index < len(lines):
        current = lines[index].strip()
        if current == "---":
            break
        frontmatter_lines.append(lines[index])
        index += 1
    else:
        return {}, "frontmatter sin cierre '---'"

    data: dict[str, str] = {}
    for raw_line in frontmatter_lines:
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", stripped)
        if not match:
            return {}, f"línea de frontmatter inválida: {raw_line!r}"
        key, value = match.group(1), strip_quotes(match.group(2))
        if key in data:
            return {}, f"clave duplicada en frontmatter: {key}"
        data[key] = value

    return data, None


def validate_skill_folder(folder: Path) -> list[str]:
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        return [f"falta SKILL.md en {folder.name}"]

    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"no se pudo leer {skill_md}: {exc}"]

    data, error = parse_frontmatter(text)
    if error:
        return [f"{skill_md}: {error}"]

    folder_name = folder.name
    name = data.get("name", "").strip()
    description = data.get("description", "").strip()
    errors: list[str] = []

    if "name" not in data:
        errors.append(f"{skill_md}: falta name")
    elif name != folder_name:
        errors.append(f"{skill_md}: name '{name}' no coincide con la carpeta '{folder_name}'")

    if "description" not in data:
        errors.append(f"{skill_md}: falta description")
    elif not description:
        errors.append(f"{skill_md}: description vacía")

    return errors


def main() -> int:
    if not SKILLS_ROOT.is_dir():
        print(f"SKILLS_REVISADAS: 0")
        print(f"ERRORES:\n- no existe la carpeta {SKILLS_ROOT}")
        print("VERDICT: FAIL")
        return 1

    skill_folders = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    all_errors: list[str] = []

    for skill_folder in skill_folders:
        all_errors.extend(validate_skill_folder(skill_folder))

    print(f"SKILLS_REVISADAS: {len(skill_folders)}")
    print("ERRORES:")
    if all_errors:
        for error in all_errors:
            print(f"- {error}")
    else:
        print("- ninguno")

    verdict = "OK" if not all_errors else "FAIL"
    print(f"VERDICT: {verdict}")
    return 0 if not all_errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
