#!/usr/bin/env python3
"""Gate determinista mínimo para evaluar si Fase 2 está lista para Fase 3."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VALIDATOR_COMMANDS = [
    ("skills_frontmatter", ["python3", "scripts/validar_skills_frontmatter.py"]),
    ("rutas_prohibidas", ["python3", "scripts/validar_no_rutas_prohibidas.py"]),
    ("placeholders_respuestas", ["python3", "scripts/validar_placeholders_respuestas.py"]),
    ("auditor_estado_plan_empresa", ["python3", "scripts/auditar_estado_plan_empresa.py"]),
]


def run_command(command: list[str]) -> tuple[int, str, str]:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def parse_verdict(output: str) -> str:
    match = re.findall(r"^VERDICT:\s*([A-Z_]+)\s*$", output, re.MULTILINE)
    if match:
        return match[-1]
    return "DESCONOCIDO"


def read_gate_1d_status() -> str:
    gate_file = ROOT / "docs_control" / "03_gates_documentales.md"
    try:
        text = gate_file.read_text(encoding="utf-8")
    except OSError:
        return "DESCONOCIDO"

    gate_section = re.search(
        r"Gate 1D.*?(?:\n## |\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if not gate_section:
        return "DESCONOCIDO"

    section = gate_section.group(0)
    if re.search(r"BLOQUEADO", section, re.IGNORECASE):
        return "BLOQUEADO"
    if re.search(r"ABIERTO", section, re.IGNORECASE):
        return "ABIERTO"
    return "DESCONOCIDO"


def extract_placeholder_total(output: str) -> str:
    match = re.search(r"^TOTAL:\s*(\d+)\s*$", output, re.MULTILINE)
    if match:
        return match.group(1)
    return "desconocido"



def main() -> int:
    results: dict[str, dict[str, str | int]] = {}
    blockers: list[str] = []

    for name, command in VALIDATOR_COMMANDS:
        code, stdout, stderr = run_command(command)
        verdict = parse_verdict(stdout)
        results[name] = {
            "exit_code": code,
            "verdict": verdict,
            "stdout": stdout.strip(),
            "stderr": stderr.strip(),
        }

    gate_1d_status = read_gate_1d_status()
    placeholder_total = extract_placeholder_total(results["placeholders_respuestas"]["stdout"])

    if results["skills_frontmatter"]["exit_code"] != 0 or results["skills_frontmatter"]["verdict"] != "OK":
        blockers.append("validar_skills_frontmatter.py falla o no devuelve VERDICT: OK")
    if results["rutas_prohibidas"]["exit_code"] != 0 or results["rutas_prohibidas"]["verdict"] != "OK":
        blockers.append("validar_no_rutas_prohibidas.py falla o no devuelve VERDICT: OK")
    if results["placeholders_respuestas"]["exit_code"] != 0:
        blockers.append("validar_placeholders_respuestas.py falló técnicamente")
    elif results["placeholders_respuestas"]["verdict"] == "PENDIENTE":
        if placeholder_total.isdigit():
            blockers.append(f"{placeholder_total} placeholders pendientes en respuestas_plan_empresa/")
        else:
            blockers.append("placeholders pendientes en respuestas_plan_empresa/")
    elif results["placeholders_respuestas"]["verdict"] != "OK":
        blockers.append("validar_placeholders_respuestas.py no devuelve VERDICT: OK")

    if results["auditor_estado_plan_empresa"]["exit_code"] != 0:
        blockers.append("auditor_estado_plan_empresa.py falló técnicamente")
    elif results["auditor_estado_plan_empresa"]["verdict"] == "PENDIENTE":
        blockers.append("auditor general en VERDICT: PENDIENTE")
    elif results["auditor_estado_plan_empresa"]["verdict"] != "PASS":
        blockers.append("auditor_estado_plan_empresa.py no devuelve VERDICT: PASS")

    if gate_1d_status == "BLOQUEADO":
        blockers.append("Gate 1D sigue bloqueado")
    elif gate_1d_status != "ABIERTO":
        blockers.append("no se pudo confirmar el estado de Gate 1D")

    blockers.append("Fase 2 no tiene todavía todos los componentes mínimos cerrados")

    gate_verdict = "GATE_ABIERTO" if not blockers else "GATE_BLOQUEADO"

    print("VALIDADORES:")
    print(f"- skills_frontmatter: exit={results['skills_frontmatter']['exit_code']} verdict={results['skills_frontmatter']['verdict']}\n"
          f"- rutas_prohibidas: exit={results['rutas_prohibidas']['exit_code']} verdict={results['rutas_prohibidas']['verdict']}\n"
          f"- placeholders_respuestas: exit={results['placeholders_respuestas']['exit_code']} verdict={results['placeholders_respuestas']['verdict']}\n"
          f"- auditor_estado_plan_empresa: exit={results['auditor_estado_plan_empresa']['exit_code']} verdict={results['auditor_estado_plan_empresa']['verdict']}\n"
          f"- gate_1d: {gate_1d_status}\n"
          f"- fase_2: INCOMPLETA_POR_CONDICION_MANUAL")
    print("\nBLOQUEADORES:")
    if blockers:
        for blocker in blockers:
            print(f"- {blocker}")
    else:
        print("- ninguno")
    print(f"\nVERDICT: {gate_verdict}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
