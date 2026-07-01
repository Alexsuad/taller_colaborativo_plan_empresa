# PT-10L — Contrato operativo de Fase 2

## 1. Propósito

PT-10L es el contrato operativo de Fase 2.

Fase 2 = construir y validar la maquinaria.
Fase 3 = usar la maquinaria para producir el Plan de Empresa.

Este documento convierte el blueprint PT-10K en reglas prácticas de trabajo diario para evitar improvisación, sobrediseño y mezcla de capas.

## 2. Reglas de alcance

- No tocar `respuestas_plan_empresa/`.
- No abrir Gate 1D.
- No redactar capítulos finales.
- No compilar documento final.
- No crear piezas por intuición.
- No crear ramas sin autorización humana.
- No hacer push.

## 3. Orden operativo de Fase 2

Orden recomendado:

1. Contrato operativo de Fase 2.
2. Validadores deterministas mínimos.
3. Reglas/gates de paso a Fase 3.
4. Sistema repo primero / NotebookLM después.
5. Skills especialistas priorizadas.
6. Workflows mínimos.
7. Auditoría global de sistema.
8. Gate sistema agéntico listo para Fase 3.

## 4. Regla para crear cualquier pieza nueva

Toda pieza nueva debe pasar por `decidir-tipo-pieza-sistema-agentico`.

Clasificación posible:

- `SKILL`
- `SCRIPT`
- `SKILL+SCRIPT`
- `GATE`
- `REGLA`
- `WORKFLOW`
- `SUBAGENTE`
- `MCP`
- `AJUSTE_DOCUMENTAL`
- `NO_CREAR`

Si no encaja con claridad, se detiene y se pide decisión humana.

## 5. Regla específica para crear skills

Toda skill nueva debe seguir esta cadena:

`decidir-tipo-pieza-sistema-agentico`
→ `auditar-skill-antes-de-crear`
→ `crear-skill-desde-contrato`
→ `auditar-skill-creada`
→ revisión humana
→ commit

Una skill no se aprueba solo porque existe, ni porque Git esté limpio, ni porque el agente la reporte como completada.

## 6. Regla skill vs script

- Skill = juicio experto, análisis semántico, clasificación, redacción, auditoría de sentido.
- Script = validación exacta, repetible, verificable, rutas, frontmatter, conteos, placeholders, YAML/JSON, estructura.
- Skill + script = cuando hay criterio experto y validación mecánica.

## 7. Regla para gates

Un gate se usa cuando hay que aprobar o bloquear avance.

Un gate no es una skill y no se sustituye por una skill.

## 8. Regla para workflows

Un workflow se usa cuando hay una secuencia repetible de varios pasos.

No crear workflow si basta una instrucción simple.

## 9. Regla para subagentes

No crear subagente por skill.

Solo considerar subagente si hay:

- responsabilidad propia
- contexto propio
- salida propia
- capacidad de veto
- coordinación recurrente

## 10. Regla repo primero / NotebookLM después

Repositorio primero.
NotebookLM después.
NotebookLM solo para huecos concretos.
NotebookLM no decide.
NotebookLM no actualiza repo automáticamente.
MCP no se crea por defecto.
MCP solo si hay integración viva, recurrente, segura y necesaria.

## 11. Reglas de validación de cada PT

Todo PT debe cerrar con:

```bash
python3 scripts/auditar_estado_plan_empresa.py
git status --short
git diff --stat
```

Y si aplica:

```bash
grep -RIn "DICTAMEN_SKILL" .agents/skills || true
grep -RIn "una gate" .agents/skills || true
```

## 12. Reglas de commit

No hacer commit si:

- hay archivos fuera de alcance;
- se tocó `respuestas_plan_empresa/` sin autorización;
- no hay auditoría;
- no hay revisión humana;
- la skill no fue probada funcionalmente;
- el documento creado es temporal pero se quiere convertir en rector sin decisión.

## 13. Definition of Done de cada PT

Un PT queda cerrado cuando:

- cumple alcance;
- toca solo archivos autorizados;
- auditor ejecutado;
- estado Git reportado;
- riesgos declarados;
- revisión humana realizada;
- commit autorizado;
- no push.

## 14. Bloqueadores para pasar a Fase 3

- Gate 1D bloqueado.
- `respuestas_plan_empresa/` con placeholders.
- validadores mínimos faltantes.
- gates críticos faltantes.
- workflows mínimos faltantes.
- skills especialistas no creadas/probadas.
- sistema repo/NotebookLM no cerrado.

## 15. Dictamen final

Dictamen:

- `CONTRATO_OPERATIVO_FASE_2_COMPLETO`

Motivo:

- El contrato operativo queda completo como regla de trabajo. La Fase 2 sigue incompleta porque faltan validadores deterministas, gates críticos, workflows mínimos y skills especialistas probadas.

Siguiente PT recomendado:

- `PT-10M — Validadores deterministas mínimos de Fase 2`

Estado final del contrato:

- listo como contrato operativo de trabajo;
- no listo como autorización para Fase 3;
- pendiente de decisión humana para la siguiente prioridad técnica.
