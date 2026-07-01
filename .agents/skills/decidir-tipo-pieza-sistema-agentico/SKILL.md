---
name: decidir-tipo-pieza-sistema-agentico
description: Usar antes de crear una nueva pieza del sistema agéntico para decidir si la necesidad corresponde a skill, script, skill+script, gate, regla, workflow, subagente, MCP, ajuste documental o si no debe crearse nada.
---

# Decidir tipo de pieza del sistema agéntico

## Propósito

Decidir la pieza mínima y correcta para resolver una necesidad nueva sin sobredimensionar el sistema.

La salida debe indicar si conviene crear una skill, un script, ambos, una gate, una regla transversal, un workflow, un subagente, un MCP, un ajuste documental o nada.

## Cuándo usarla

Usar antes de:

- crear una nueva pieza del sistema agéntico;
- convertir una necesidad en skill por defecto;
- decidir si algo debe ser código, regla o gobernanza;
- proponer cambios de arquitectura agéntica;
- evaluar si una demanda ya queda cubierta por una pieza existente.

## Cuándo NO usarla

No usarla para:

- implementar la pieza ya decidida;
- redactar contenido de negocio;
- abrir gates;
- tocar `respuestas_plan_empresa/`;
- decidir estrategia final de negocio;
- sustituir una auditoría de cierre o una validación técnica ya definida.

## Entradas

- Necesidad detectada.
- Objetivo operativo.
- Fase vigente.
- Alcance permitido.
- Restricciones activas.
- Piezas existentes candidatas.
- Nivel de determinismo requerido.
- Necesidad de juicio experto.
- Necesidad de validación automática.
- Dependencia de herramientas externas.

## Salidas

- `TIPO_RECOMENDADO`.
- `PIEZA_PROPUESTA`.
- `RAZON`.
- `ALTERNATIVAS_DESCARTADAS`.
- `RIESGO_SI_SE_CREA_MAL`.
- `EVIDENCIA_REQUERIDA`.
- `DECISION_HUMANA_REQUERIDA`.
- `DICTAMEN`.

## Criterios de decisión

- **SKILL**: cuando hace falta criterio experto, interpretación semántica, clasificación no determinista, auditoría de sentido, preparación de consultas, análisis de negocio, redacción o mejora de texto, o separación hecho / inferencia / hipótesis.
- **SCRIPT**: cuando hace falta validación determinista, comprobación exacta, existencia de archivos, frontmatter, rutas, nombres, conteos, placeholders, formatos, YAML/JSON, índices, anexos, exit codes o compilación.
- **SKILL + SCRIPT**: cuando hay una parte que exige criterio experto y otra parte exacta que debe validarse automáticamente.
- **GATE**: cuando lo que se necesita es aprobar, bloquear o rechazar un avance de fase o una transición crítica.
- **REGLA**: cuando la restricción debe aplicar de forma transversal a todo el sistema.
- **WORKFLOW**: cuando hay una secuencia repetible de varios pasos, roles o skills.
- **SUBAGENTE**: solo cuando hace falta responsabilidad propia, criterio autónomo, contexto propio, salida propia, capacidad de veto o coordinación recurrente que no cabe en una skill.
- **MCP**: cuando hay que consultar o actuar sobre una herramienta externa viva, la consulta es recurrente, no basta con lectura local y el permiso/seguridad están controlados.
- **AJUSTE_DOCUMENTAL**: cuando solo falta registrar o aclarar una decisión en una sede documental existente.
- **NO_CREAR**: cuando la pieza no aporta control, no reduce errores, duplica una pieza existente, sobredimensiona el sistema o pertenece a una fase futura.

## Matriz de decisión

| Señal dominante | Tipo probable | Regla práctica |
| --- | --- | --- |
| Juicio experto, lectura ambigua, análisis de negocio, redacción | `SKILL` | Priorizar si el resultado depende de interpretación humana guiada |
| Verificación exacta, formato, rutas, archivos, conteos, YAML/JSON | `SCRIPT` | Priorizar si la respuesta debe ser reproducible y comprobable |
| Parte semántica + parte exacta | `SKILL + SCRIPT` | Separar criterio experto y validación determinista |
| Aprobación o bloqueo de fase | `GATE` | No convertirlo en skill ni en script |
| Restricción transversal permanente | `REGLA` | No resolverlo con piezas puntuales |
| Secuencia repetible multietapa | `WORKFLOW` | No dividirlo en decisiones aisladas si el flujo es estable |
| Autonomía propia con veto y contexto persistente | `SUBAGENTE` | No envolver una skill sin necesidad real |
| Herramienta externa viva y recurrente | `MCP` | Usar solo si la integración externa es necesaria |
| Solo registrar o aclarar una decisión | `AJUSTE_DOCUMENTAL` | No crear pieza nueva si basta con sede documental |
| Duplicado, exceso o fase futura | `NO_CREAR` | Frenar la creación |

## Pasos obligatorios

1. Identificar la necesidad real.
2. Separar lo que exige juicio experto de lo que exige verificación exacta.
3. Comparar con piezas existentes.
4. Determinar si la necesidad es puntual, transversal o secuencial.
5. Decidir el tipo de pieza mínima suficiente.
6. Registrar alternativas descartadas.
7. Explicar el riesgo de crear la pieza equivocada.
8. Emitir el dictamen final.

## Formato de respuesta

```text
TIPO_RECOMENDADO:
PIEZA_PROPUESTA:
RAZON:
ALTERNATIVAS_DESCARTADAS:
RIESGO_SI_SE_CREA_MAL:
EVIDENCIA_REQUERIDA:
DECISION_HUMANA_REQUERIDA: SI/NO
DICTAMEN:
```

## Valores permitidos para `DICTAMEN`

La skill debe usar solo uno de estos valores:

- `CREAR_SKILL`
- `CREAR_SCRIPT`
- `CREAR_SKILL_Y_SCRIPT`
- `CREAR_GATE`
- `CREAR_REGLA`
- `CREAR_WORKFLOW`
- `CREAR_SUBAGENTE`
- `CREAR_MCP`
- `HACER_AJUSTE_DOCUMENTAL`
- `NO_CREAR`
- `REQUIERE_DECISION_HUMANA`
- `CREAR_GATE_Y_SCRIPT`
- `CREAR_SKILL_Y_GATE`
- `CREAR_REGLA_Y_GATE`
- `CREAR_WORKFLOW_Y_GATE`

## Ejemplos

### Ejemplo 1

Necesidad: validar que un archivo tenga frontmatter, nombre correcto y secciones obligatorias.

Resultado:

```text
TIPO_RECOMENDADO: SCRIPT
PIEZA_PROPUESTA: script de validación estructural
RAZON: La comprobación es determinista y repetible.
ALTERNATIVAS_DESCARTADAS: SKILL, GATE, WORKFLOW
RIESGO_SI_SE_CREA_MAL: Se delega una verificación exacta a criterio subjetivo.
EVIDENCIA_REQUERIDA: reglas de formato y rutas esperadas.
DECISION_HUMANA_REQUERIDA: NO
DICTAMEN: CREAR_SCRIPT
```

### Ejemplo 2

Necesidad: clasificar si una pregunta debe responderse con fuente interna, promotor o investigación.

Resultado:

```text
TIPO_RECOMENDADO: SKILL
PIEZA_PROPUESTA: skill de clasificación documental
RAZON: Hace falta criterio semántico y decisión guiada.
ALTERNATIVAS_DESCARTADAS: SCRIPT, GATE, REGLA
RIESGO_SI_SE_CREA_MAL: La clasificación se vuelve rígida o incompleta.
EVIDENCIA_REQUERIDA: ejemplos de preguntas y fuentes disponibles.
DECISION_HUMANA_REQUERIDA: NO
DICTAMEN: CREAR_SKILL
```

### Ejemplo 3

Necesidad: aprobar la apertura de una fase posterior.

Resultado:

```text
TIPO_RECOMENDADO: GATE
PIEZA_PROPUESTA: gate documental
RAZON: La necesidad es de aprobación o bloqueo, no de ejecución.
ALTERNATIVAS_DESCARTADAS: SKILL, SCRIPT
RIESGO_SI_SE_CREA_MAL: Se confunde control de avance con herramienta operativa.
EVIDENCIA_REQUERIDA: criterios de aprobación y bloqueos vigentes.
DECISION_HUMANA_REQUERIDA: SI
DICTAMEN: CREAR_GATE
```

### Ejemplo 4

Necesidad: bloquear Fase 3 si no hay evidencia.

Resultado:

```text
TIPO_RECOMENDADO: GATE + SCRIPT
PIEZA_PROPUESTA: gate de bloqueo con auditoría determinista previa
RAZON: La decisión de bloqueo es de gobernanza y la verificación de evidencia es exacta.
ALTERNATIVAS_DESCARTADAS: SKILL, REGLA
RIESGO_SI_SE_CREA_MAL: Se mezcla control de fase con análisis subjetivo y se deja pasar una entrega insuficiente.
EVIDENCIA_REQUERIDA: criterio de bloqueo, evidencia mínima y archivos válidos.
DECISION_HUMANA_REQUERIDA: SI
DICTAMEN: CREAR_GATE_Y_SCRIPT
```

### Ejemplo 5

Necesidad: revisar coherencia mercado -> ventas -> financiero.

Resultado:

```text
TIPO_RECOMENDADO: SKILL + GATE
PIEZA_PROPUESTA: skill de coherencia documental más gate de validación de bloque
RAZON: La revisión necesita criterio experto y la decisión de avance requiere control de fase.
ALTERNATIVAS_DESCARTADAS: SCRIPT, REGLA
RIESGO_SI_SE_CREA_MAL: Se valida una incoherencia como si fuera suficiente con formato.
EVIDENCIA_REQUERIDA: bloques relacionados, dependencias entre secciones y criterio de aprobación.
DECISION_HUMANA_REQUERIDA: SI
DICTAMEN: CREAR_SKILL_Y_GATE
```

### Ejemplo 6

Necesidad: consultar NotebookLM para hueco concreto.

Resultado:

```text
TIPO_RECOMENDADO: SKILL
PIEZA_PROPUESTA: skill de preparación o consulta documental
RAZON: La necesidad principal es criterio experto sobre qué buscar y cómo usarlo.
ALTERNATIVAS_DESCARTADAS: SCRIPT, GATE, WORKFLOW
RIESGO_SI_SE_CREA_MAL: Se crea una integración innecesaria o se sobredimensiona el sistema.
EVIDENCIA_REQUERIDA: hueco concreto, fuente probable y canal de consulta.
DECISION_HUMANA_REQUERIDA: NO
DICTAMEN: CREAR_SKILL
```

### Ejemplo 7

Necesidad: regla "no tocar `respuestas_plan_empresa/` antes de Gate 1D".

Resultado:

```text
TIPO_RECOMENDADO: REGLA / GATE
PIEZA_PROPUESTA: regla transversal o gate de autorización
RAZON: La restricción aplica a todo el sistema y también puede apoyarse en la aprobación de gate.
ALTERNATIVAS_DESCARTADAS: SKILL, SCRIPT
RIESGO_SI_SE_CREA_MAL: Se convierte una restricción global en una instrucción local fácil de saltar.
EVIDENCIA_REQUERIDA: ámbito de aplicación y referencia al gate vigente.
DECISION_HUMANA_REQUERIDA: SI
DICTAMEN: CREAR_REGLA_Y_GATE
```

### Ejemplo 8

Necesidad: crear un subagente para cada skill.

Resultado:

```text
TIPO_RECOMENDADO: NO_CREAR
PIEZA_PROPUESTA: ninguna
RAZON: Crear un subagente por skill sobredimensiona el sistema y duplica responsabilidades.
ALTERNATIVAS_DESCARTADAS: SUBAGENTE, WORKFLOW
RIESGO_SI_SE_CREA_MAL: El sistema se vuelve más complejo, más caro de mantener y menos trazable.
EVIDENCIA_REQUERIDA: ninguna; la decisión correcta es no crear.
DECISION_HUMANA_REQUERIDA: NO
DICTAMEN: NO_CREAR
```

## Criterio de cierre

La skill queda cerrada cuando el dictamen permite decidir la pieza mínima correcta sin ambigüedad y sin crear duplicados.

## Evidencia mínima

- Necesidad analizada.
- Piezas existentes comparadas.
- Tipo recomendado.
- Alternativas descartadas.
- Riesgo de mala creación.

## Prohibiciones

- No redacta contenido final del Plan de Empresa.
- No abre Gate 1D.
- No toca `respuestas_plan_empresa/`.
- No decide negocio, marketing, legal, RRSS ni viabilidad.
- No crea subagentes para envolver una skill.
- No convierte hipótesis en hechos.
