---
name: auditar-skill-antes-de-crear
description: Usar antes de crear una nueva skill para verificar si ya existe una skill equivalente, si hay solape funcional, si conviene ampliar una existente o si se requiere decisión humana.
---

# auditar-skill-antes-de-crear

## Propósito
Auditar una propuesta de skill antes de crearla. Debe decidir si hace falta crearla, si ya existe algo equivalente, si basta ampliar una existente o si la necesidad corresponde a script, gate, regla, workflow, subagente, MCP, ajuste documental o no crear nada.

## Cuándo usarla

Usarla solo después de que `decidir-tipo-pieza-sistema-agentico` haya devuelto `CREAR_SKILL`, `CREAR_SKILL_Y_SCRIPT` o `CREAR_SKILL_Y_GATE`.

Usarla antes de crear, duplicar o ampliar una skill del proyecto.

## Cuándo NO usarla

No usarla para decidir negocio, redactar el plan, crear subagentes o abrir Gate 1D.
No usarla si la decisión previa indicó `CREAR_SCRIPT`, `CREAR_GATE`, `CREAR_REGLA`, `CREAR_WORKFLOW`, `CREAR_SUBAGENTE`, `CREAR_MCP`, `HACER_AJUSTE_DOCUMENTAL` o `NO_CREAR`.

## Entradas

- Nombre de la skill propuesta.
- Objetivo de la skill propuesta.
- Skills existentes candidatas.
- Alcance permitido actual.
- Restricciones activas del proyecto.
- Dictamen previo de `decidir-tipo-pieza-sistema-agentico`.

## Salidas

- `DICTAMEN`.
- Skill existente que cubre la necesidad, si aplica.
- Nivel de solape.
- Recomendación de acción.
- Decisión humana pendiente, si existe.

Valores permitidos para `DICTAMEN`:

- `CREAR_NUEVA`
- `AMPLIAR_EXISTENTE`
- `NO_CREAR_DUPLICADA`
- `NO_ES_SKILL`
- `REQUIERE_DECISION_HUMANA`

## Relación obligatoria con `decidir-tipo-pieza-sistema-agentico`

- Si la primera skill no propone crear una skill, esta skill no actúa.
- Si la primera skill propone `CREAR_SKILL`, `CREAR_SKILL_Y_SCRIPT` o `CREAR_SKILL_Y_GATE`, esta skill audita solo la parte de skill.
- Si detecta que el caso real es script, gate, regla, workflow, subagente, MCP o ajuste documental, devuelve `NO_ES_SKILL`.
- Si la propuesta nueva duplica una existente, devuelve `NO_CREAR_DUPLICADA` o `AMPLIAR_EXISTENTE`.

## Pasos obligatorios

1. Leer el dictamen previo de `decidir-tipo-pieza-sistema-agentico`.
2. Comparar la skill propuesta con las skills existentes.
3. Detectar duplicados, solapes y huecos reales.
4. Revisar si la necesidad en realidad pertenece a script, gate, regla, workflow, subagente, MCP o ajuste documental.
5. Determinar si basta ampliar una skill previa.
6. Determinar si la creación nueva está justificada.
7. Emitir un dictamen explícito.

## Matriz de solape

| Señal | Dictamen probable | Acción |
| --- | --- | --- |
| Ya existe una skill equivalente | `NO_CREAR_DUPLICADA` | Reutilizar o ampliar la existente |
| La skill actual cubre la mayoría pero le falta precisión | `AMPLIAR_EXISTENTE` | Extender la skill base |
| La propuesta no es una skill | `NO_ES_SKILL` | Reencaminar a script, gate, regla u otra pieza |
| La creación está justificada y no duplica | `CREAR_NUEVA` | Crear con contrato claro |
| Falta juicio humano para cerrar | `REQUIERE_DECISION_HUMANA` | Bloquear hasta decisión |

## Criterios para `CREAR_NUEVA`

- no existe una skill equivalente;
- la necesidad es reutilizable y acotada;
- la salida depende de criterio experto o semántico;
- la skill no invade scripts, gates, reglas, workflows o subagentes.

## Criterios para `AMPLIAR_EXISTENTE`

- existe una skill base con al menos cobertura parcial clara;
- ampliar no rompe la claridad;
- la nueva capacidad sigue siendo la misma familia funcional;
- la ampliación no crea solape nuevo innecesario.

## Criterios para `NO_CREAR_DUPLICADA`

- ya existe una skill equivalente o suficientemente cercana;
- la nueva propuesta repite propósito, entradas o salidas;
- crearla aumentaría confusión o mantenimiento sin aportar control.

## Criterios para `REQUIERE_DECISION_HUMANA`

- hay empate razonable entre ampliar y crear;
- falta contrato claro de la propuesta;
- la propuesta puede sobredimensionar la sede de skills;
- existe impacto organizativo o de gobernanza que no se debe resolver solo por IA.

## Revisión contra otras piezas

- **Script**: si la necesidad es exacta, verificable o determinista, no se crea skill.
- **Gate**: si la necesidad es aprobar o bloquear avance, no se crea skill.
- **Regla**: si el control debe ser transversal, no se crea skill.
- **Workflow**: si la secuencia es repetible y multietapa, no se crea skill aislada.
- **Subagente**: si hace falta autonomía persistente, no se envuelve una skill.
- **MCP**: si hay integración externa viva y recurrente, no se finge como skill.

## Criterio de cierre

La skill queda cerrada cuando el dictamen identifica con claridad si crear, ampliar, no duplicar o rechazar la propuesta como no skill.

## Formato de respuesta

```text
PROPUESTA_ANALIZADA:
DICTAMEN:
SKILL_EXISTENTE_RELACIONADA:
TIPO_DE_SOLAPE:
ACCION_RECOMENDADA:
RAZON:
RIESGO_SI_SE_CREA:
RIESGO_SI_NO_SE_CREA:
EVIDENCIA_REQUERIDA:
DECISION_HUMANA_REQUERIDA: SI/NO
```

## Ejemplos

### Ejemplo 1

Propuesta realmente nueva.

Resultado:

```text
PROPUESTA_ANALIZADA: skill para clasificar preguntas del plan
DICTAMEN: CREAR_NUEVA
SKILL_EXISTENTE_RELACIONADA: ninguna
TIPO_DE_SOLAPE: ninguno
ACCION_RECOMENDADA: crear skill nueva
RAZON: No existe una skill equivalente y la capacidad es reutilizable.
RIESGO_SI_SE_CREA: se pierde control documental.
RIESGO_SI_NO_SE_CREA: la tarea queda sin cobertura clara.
EVIDENCIA_REQUERIDA: contrato aprobado y objetivos claros.
DECISION_HUMANA_REQUERIDA: NO
```

### Ejemplo 2

Propuesta duplicada.

Resultado:

```text
PROPUESTA_ANALIZADA: skill para controlar anticontaminación de fuentes
DICTAMEN: NO_CREAR_DUPLICADA
SKILL_EXISTENTE_RELACIONADA: control-anticontaminacion-fuentes
TIPO_DE_SOLAPE: total
ACCION_RECOMENDADA: reutilizar la existente
RAZON: La capacidad ya está cubierta.
RIESGO_SI_SE_CREA: duplicidad y confusión.
RIESGO_SI_NO_SE_CREA: ninguno material.
EVIDENCIA_REQUERIDA: comparación de cobertura.
DECISION_HUMANA_REQUERIDA: NO
```

### Ejemplo 3

Propuesta que debería ser script.

Resultado:

```text
PROPUESTA_ANALIZADA: skill para validar frontmatter y secciones
DICTAMEN: NO_ES_SKILL
SKILL_EXISTENTE_RELACIONADA: ninguna
TIPO_DE_SOLAPE: con validación determinista
ACCION_RECOMENDADA: pasar a script
RAZON: La tarea es exacta y comprobable automáticamente.
RIESGO_SI_SE_CREA: se sustituye validación mecánica por criterio subjetivo.
RIESGO_SI_NO_SE_CREA: ninguno; debe ir a script.
EVIDENCIA_REQUERIDA: reglas exactas de validación.
DECISION_HUMANA_REQUERIDA: NO
```

### Ejemplo 4

Propuesta que debería ser gate.

Resultado:

```text
PROPUESTA_ANALIZADA: skill para autorizar Gate 1D
DICTAMEN: NO_ES_SKILL
SKILL_EXISTENTE_RELACIONADA: decidir-tipo-pieza-sistema-agentico
TIPO_DE_SOLAPE: gobernanza
ACCION_RECOMENDADA: crear gate o usar el existente
RAZON: La necesidad es aprobar o bloquear avance.
RIESGO_SI_SE_CREA: se crea una skill que hace de gate.
RIESGO_SI_NO_SE_CREA: ninguno; el control debe ser gate.
EVIDENCIA_REQUERIDA: criterios de apertura y bloqueo.
DECISION_HUMANA_REQUERIDA: SI
```

### Ejemplo 5

Propuesta que debería ampliar una skill existente.

Resultado:

```text
PROPUESTA_ANALIZADA: ampliar clasificar-pregunta-plan-empresa con mejor salida de fuente
DICTAMEN: AMPLIAR_EXISTENTE
SKILL_EXISTENTE_RELACIONADA: clasificar-pregunta-plan-empresa
TIPO_DE_SOLAPE: parcial
ACCION_RECOMENDADA: ampliar la skill base
RAZON: La familia funcional es la misma y la ampliación no rompe claridad.
RIESGO_SI_SE_CREA: duplicidad innecesaria.
RIESGO_SI_NO_SE_CREA: la skill existente queda algo corta.
EVIDENCIA_REQUERIDA: cobertura faltante concreta.
DECISION_HUMANA_REQUERIDA: NO
```

### Ejemplo 6

Propuesta que requiere decisión humana.

Resultado:

```text
PROPUESTA_ANALIZADA: nueva skill de coordinación para un caso ambiguo
DICTAMEN: REQUIERE_DECISION_HUMANA
SKILL_EXISTENTE_RELACIONADA: varias candidatas parciales
TIPO_DE_SOLAPE: incierto
ACCION_RECOMENDADA: pedir decisión humana
RAZON: No está claro si conviene ampliar o crear.
RIESGO_SI_SE_CREA: sobredimensionar la sede de skills.
RIESGO_SI_NO_SE_CREA: dejar un hueco funcional.
EVIDENCIA_REQUERIDA: comparación de cobertura y contrato breve.
DECISION_HUMANA_REQUERIDA: SI
```

## Criterio operativo del proyecto

Una skill no se crea por ocurrencia. Se planifica, se conecta con negocio, se define con entradas y salidas, se usa para que la IA siga pasos constantes, se audita con checklist y se somete a revisión humana cuando afecta decisiones importantes.

## Evidencia mínima
- Skill propuesta analizada.
- Skills existentes revisadas.
- Dictamen `DICTAMEN`.
- Justificación breve.

## Prohibiciones
- No redacta contenido final del Plan de Empresa.
- No abre Gate 1D.
- No toca `respuestas_plan_empresa/`.
- No decide negocio, marketing, legal, RRSS ni viabilidad.
- No sustituye `decidir-tipo-pieza-sistema-agentico`.
- No convierte hipótesis en hechos.
