---
name: verificar-evidencia-minima-cierre
description: "Usar antes de cerrar una tarea para comprobar que existe evidencia mínima: archivos tocados, comandos ejecutados, estado Git, auditor o validación aplicable, rutas prohibidas respetadas y estado final claro."
---

# verificar-evidencia-minima-cierre

## Propósito
Verificar que una tarea tiene evidencia mínima suficiente antes de cerrarse.

## Cuándo usarla
Usarla antes de dar por cerrada una intervención, skill, reporte o paquete técnico.

## Cuándo NO usarla
No usarla para aprobar negocio, abrir Gates ni validar contenido de fondo.

## Entradas
- Archivos tocados.
- Comandos ejecutados.
- Estado Git.
- Auditoría o validación aplicada.
- Rutas prohibidas.
- Estado final propuesto.

## Salidas
- Veredicto de cierre.
- `DICTAMEN_CIERRE`.
- `CIERRE_VALIDO`
- `CIERRE_INSUFICIENTE`
- `REQUIERE_EVIDENCIA`
- `REQUIERE_DECISION_HUMANA`
- Evidencia mínima presente o faltante.
- Riesgos de cierre prematuro.
- Acción humana requerida, si aplica.

## Pasos obligatorios
1. Comprobar archivos tocados.
2. Comprobar comandos ejecutados.
3. Comprobar estado Git.
4. Comprobar auditorías o validaciones aplicadas.
5. Comprobar respeto de rutas prohibidas.
6. Comprobar que el estado final sea claro.
7. Emitir veredicto.

## Criterio de cierre
La skill queda cerrada cuando la tarea puede justificarse con evidencia mínima verificable.

## Evidencia mínima
- Lista de archivos tocados.
- Lista de comandos ejecutados.
- Estado Git.
- Validación o auditoría, si aplica.
- Estado final claro.

## Prohibiciones
- No redacta contenido final del Plan de Empresa.
- No abre Gate 1D.
- No toca `respuestas_plan_empresa/`.
- No decide negocio, marketing, legal, RRSS ni viabilidad.
- No convierte hipótesis en hechos.
