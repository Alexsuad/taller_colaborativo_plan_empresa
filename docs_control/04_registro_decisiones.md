# 04 — Registro de decisiones

| ID | Fecha | Decisión | Motivo | Impacto | Estado |
|---|---:|---|---|---|---|
| DEC-001 | 2026-06-22 | Crear repo propio del Taller a partir de patrones útiles de repositorios de referencia, sin reutilizar contenido sectorial ajeno | Evitar rehacer trabajo y reducir contaminación | Se separan preguntas, respuestas, fuentes, metodología y output | Aprobada |
| DEC-002 | 2026-06-22 | Trabajar en tres fases: negocio, sistema/repositorio, output | Evitar automatizar o producir antes de clarificar el negocio | La fase actual se limita a organización del negocio | Aprobada |
| DEC-003 | 2026-06-22 | No reutilizar respuestas ni contenido sectorial de casos legacy no reutilizables | Prevenir contaminación del plan del Taller | Solo se copian preguntas, estructura y scripts base pendientes de adaptación | Aprobada |
| DEC-004 | 2026-06-23 | Normalizar la sede agéntica en `.agents/` (reglas, skills y workflows) y registrar skills iniciales | Centralizar el comportamiento agéntico en una sede única y reutilizable | `.agent/` queda sustituida por `.agents/`; se añaden 5 skills (auditoría por fases, control anticontaminación, higiene 5S, inventario de fuentes, paquete de ejecución) | Aprobada |
| DEC-005 | 2026-06-23 | Añadir auditor configurable de contaminación conceptual (`scripts/auditar_contaminacion_conceptual.py` + `config/contaminacion_conceptual.yml`) | Detectar residuos conceptuales heredados de forma determinista y configurable | El control de contaminación deja de ser manual y se incorpora a las validaciones del repositorio | Aprobada |
| DEC-006 | 2026-06-23 | Limpiar residuos visibles de contaminación conceptual del repositorio | Confirmar que la gobernanza y los artefactos no arrastran narrativa de otros proyectos | Reportes de creación y revisión inicial retirados; diccionario y auditor refinados | Aprobada |
