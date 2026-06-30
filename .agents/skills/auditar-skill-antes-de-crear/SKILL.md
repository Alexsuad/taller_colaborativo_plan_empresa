---
name: auditar-skill-antes-de-crear
description: "Usar antes de crear una nueva skill para verificar si ya existe una skill equivalente, si hay solape funcional, si conviene ampliar una existente o si se requiere decisión humana."
---

# auditar-skill-antes-de-crear

## Propósito
Auditar si una skill propuesta ya existe, se solapa con una existente, debe ampliar una skill previa o realmente debe crearse como nueva.

## Cuándo usarla
Usarla antes de crear, duplicar o ampliar una skill documental del proyecto.

## Cuándo NO usarla
No usarla para decidir negocio, redactar el plan, crear subagentes o abrir Gate 1D.

## Entradas
- Nombre de la skill propuesta.
- Objetivo de la skill propuesta.
- Skills existentes candidatas.
- Alcance permitido actual.
- Restricciones activas del proyecto.

## Salidas
- `DICTAMEN_SKILL`.
- `CREAR_NUEVA`
- `AMPLIAR_EXISTENTE`
- `NO_CREAR_DUPLICADA`
- `REQUIERE_DECISION_HUMANA`
- Skill existente que cubre la necesidad, si aplica.
- Nivel de solape.
- Recomendación de acción.
- Decisión humana pendiente, si existe.

## Pasos obligatorios
1. Comparar la skill propuesta con las skills existentes.
2. Detectar duplicados, solapes y huecos reales.
3. Determinar si basta ampliar una skill previa.
4. Determinar si la creación nueva está justificada.
5. Emitir un dictamen explícito.

## Criterio de cierre
La skill queda cerrada cuando el dictamen identifica con claridad si crear, ampliar o no duplicar.

## Evidencia mínima
- Skill propuesta analizada.
- Skills existentes revisadas.
- Dictamen `DICTAMEN_SKILL`.
- Justificación breve.

## Prohibiciones
- No redacta contenido final del Plan de Empresa.
- No abre Gate 1D.
- No toca `respuestas_plan_empresa/`.
- No decide negocio, marketing, legal, RRSS ni viabilidad.
- No convierte hipótesis en hechos.
