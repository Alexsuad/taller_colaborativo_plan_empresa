---
name: crear-skill-desde-contrato
description: Usar para redactar un SKILL.md nuevo solo cuando exista un contrato aprobado que justifique crear una skill y defina propósito, entradas, salidas, límites, evidencia y criterios de cierre.
---

# Crear skill desde contrato

## Propósito

Redactar una nueva skill únicamente cuando ya existe un contrato aprobado que justifica su creación.

## Cuándo usarla

Usarla solo después de:

- `decidir-tipo-pieza-sistema-agentico` con dictamen que permita crear skill;
- `auditar-skill-antes-de-crear` con dictamen favorable;
- contrato mínimo aprobado por una decisión humana.

## Cuándo NO usarla

No usarla para decidir si una skill hace falta.
No usarla si el caso es script, gate, regla, workflow, subagente, MCP o ajuste documental.
No usarla si falta contrato.

## Precondiciones obligatorias

- dictamen previo de `decidir-tipo-pieza-sistema-agentico`;
- dictamen previo de `auditar-skill-antes-de-crear`;
- nombre de skill aprobado;
- propósito claro;
- entradas;
- salidas;
- límites;
- cuándo usarla;
- cuándo no usarla;
- evidencia mínima;
- prohibiciones;
- criterio de cierre.

Si falta una precondición, devolver `NO_CREAR_SKILL_CONTRATO_INCOMPLETO`.

## Entradas

- contrato aprobado;
- nombre de skill;
- propósito;
- entradas;
- salidas;
- límites;
- ejemplos de uso;
- restricciones del proyecto.

## Salidas

- SKILL.md propuesto;
- dictamen de diseño;
- riesgos de diseño;
- evidencia requerida;
- decisión humana requerida.

## Estructura obligatoria de SKILL.md

- frontmatter válido;
- propósito;
- cuándo usarla;
- cuándo no usarla;
- entradas;
- salidas;
- pasos obligatorios;
- criterios de calidad;
- formato de respuesta;
- ejemplos;
- criterio de cierre;
- evidencia mínima;
- prohibiciones;
- criterio operativo del proyecto.

## Pasos obligatorios

1. Leer el contrato.
2. Verificar precondiciones.
3. Traducir el contrato a una skill mínima y clara.
4. Mantener la skill acotada a una sola función.
5. Escribir formato de respuesta cerrado.
6. Añadir ejemplos útiles.
7. Añadir criterio operativo del proyecto.
8. Emitir propuesta lista para revisión.

## Criterios de calidad

- una sola función principal;
- entradas y salidas claras;
- límites explícitos;
- no invade scripts, gates, reglas ni workflows;
- no mezcla redacción con validación determinista;
- no crea contradicciones con otras skills.

## Formato de respuesta

```text
NOMBRE_SKILL:
RUTA_PROPUESTA:
CONTRATO_RECIBIDO:
PRECONDICIONES_CUMPLIDAS: SI/NO
SKILL_MD_PROPUESTO:
RIESGOS_DE_DISEÑO:
EVIDENCIA_REQUERIDA:
DECISION_HUMANA_REQUERIDA: SI/NO
DICTAMEN:
```

## Valores permitidos para `DICTAMEN`

- `CREAR_SKILL_MD`
- `NO_CREAR_SKILL_CONTRATO_INCOMPLETO`
- `REQUIERE_AJUSTE_CONTRATO`
- `REQUIERE_DECISION_HUMANA`

## Ejemplos

### Ejemplo 1

Contrato completo y aprobable.

```text
NOMBRE_SKILL: clasificar-pregunta-plan-empresa
RUTA_PROPUESTA: .agents/skills/clasificar-pregunta-plan-empresa/SKILL.md
CONTRATO_RECIBIDO: completo
PRECONDICIONES_CUMPLIDAS: SI
SKILL_MD_PROPUESTO: propuesto
RIESGOS_DE_DISEÑO: bajos
EVIDENCIA_REQUERIDA: contrato y dictámenes previos
DECISION_HUMANA_REQUERIDA: NO
DICTAMEN: CREAR_SKILL_MD
```

### Ejemplo 2

Contrato incompleto.

```text
NOMBRE_SKILL: skill sin límites claros
RUTA_PROPUESTA: .agents/skills/skill-sin-limites/SKILL.md
CONTRATO_RECIBIDO: incompleto
PRECONDICIONES_CUMPLIDAS: NO
SKILL_MD_PROPUESTO: no procede
RIESGOS_DE_DISEÑO: alto solape y ambigüedad
EVIDENCIA_REQUERIDA: contrato completo
DECISION_HUMANA_REQUERIDA: SI
DICTAMEN: NO_CREAR_SKILL_CONTRATO_INCOMPLETO
```

### Ejemplo 3

Contrato que requiere ajuste.

```text
NOMBRE_SKILL: skill ambigua
RUTA_PROPUESTA: .agents/skills/skill-ambigua/SKILL.md
CONTRATO_RECIBIDO: parcial
PRECONDICIONES_CUMPLIDAS: NO
SKILL_MD_PROPUESTO: borrador
RIESGOS_DE_DISEÑO: duplicidad y exceso de alcance
EVIDENCIA_REQUERIDA: límites y criterios de cierre
DECISION_HUMANA_REQUERIDA: SI
DICTAMEN: REQUIERE_AJUSTE_CONTRATO
```

## Criterio operativo del proyecto

Una skill no se crea por ocurrencia. Se planifica, se conecta con negocio, se define con entradas y salidas, se usa para que la IA siga pasos constantes, se audita con checklist y se somete a revisión humana cuando afecta decisiones importantes.

## Criterio de cierre

La skill queda cerrada cuando el SKILL.md propuesto cumple el contrato y puede revisarse sin ambigüedad.

## Evidencia mínima

- contrato aprobado;
- dictámenes previos;
- SKILL.md propuesto;
- riesgos de diseño;
- decisión humana requerida, si aplica.

## Prohibiciones

- No decidir por sí misma que una skill hace falta.
- No crear scripts.
- No crear gates.
- No crear workflows.
- No crear subagentes.
- No tocar `respuestas_plan_empresa/`.
- No abrir Gate 1D.
- No convertir una validación determinista en skill.
- No crear skills sin contrato previo.
