# PT-10H — Auditoría de skills base documentales

## Contexto

- Fase 1 documental: cerrada operativamente.
- Gate 1C: operativo para continuar.
- Matriz activa: `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md`.
- Gate 1D: bloqueado.
- `respuestas_plan_empresa/`: bloqueado.
- Objetivo: cubrir capacidades documentales mínimas para preparar Gate 1D sin duplicar skills ni tocar contenido de negocio.

## Criterio de decisión

No se crea una skill nueva si una existente cubre al menos el 70% de la capacidad y puede ampliarse sin perder claridad.

## Tabla de cobertura

| Capacidad necesaria | Skill existente que la cubre | Cobertura | Acción recomendada |
| --- | --- | --- | --- |
| Clasificar preguntas del plan de empresa | `auditoria-documental-por-fases` + apoyo conceptual de la matriz 08 | 40% | Crear `clasificar-pregunta-plan-empresa` porque la skill de auditoría revisa intervenciones, pero no clasifica preguntas como salida operativa. |
| Detectar fuente existente | `inventario-clasificacion-fuentes` | 95% | No crear skill nueva. Ya cubre inventario, clasificación y propuesta de uso de fuentes existentes. |
| Marcar dependencia de usuario/promotor | `auditoria-documental-por-fases` + matriz 08 | 55% | No crear skill separada. Integrar esta salida dentro de `clasificar-pregunta-plan-empresa` para evitar duplicidad. |
| Marcar `NO_RESPONDER_AUN` | `auditoria-documental-por-fases` + matriz 08 | 55% | No crear skill separada. Integrar esta salida dentro de `clasificar-pregunta-plan-empresa` para mantener una sola skill de clasificación base. |
| Controlar anticontaminación conceptual | `control-anticontaminacion-fuentes` | 100% | No crear skill nueva. Ya cubre riesgo, uso permitido/prohibido y verificación. |
| Preparar bloque para redacción futura | `preparar-paquete-ejecucion-tecnica` | 60% | Crear `preparar-bloque-para-redaccion` porque la skill existente empaqueta ejecución técnica, pero no estructura bloques listos para redacción viva. |
| Auditar bloque previo a redacción | `auditoria-documental-por-fases` | 90% | No crear skill nueva. Ya audita intervenciones documentales y bloquea salidas fuera de fase. |

## Decisión de implementación

- Skills nuevas mínimas recomendadas:
  - `clasificar-pregunta-plan-empresa`
  - `preparar-bloque-para-redaccion`
- Skills no creadas por cobertura suficiente:
  - `detectar-fuente-existente`
  - `marcar-dependencia-usuario`
  - `marcar-no-responder-aun`
  - `controlar-anticontaminacion-conceptual`
  - `auditar-bloque-previo-redaccion`

## Implementación realizada

- Skills creadas:
  - `clasificar-pregunta-plan-empresa`
  - `preparar-bloque-para-redaccion`
- Skills absorbidas sin crear duplicado:
  - `marcar-dependencia-usuario` y `marcar-no-responder-aun` quedaron integradas dentro de `clasificar-pregunta-plan-empresa` como salidas de la misma clasificación base.

## Justificación de no duplicación

- `inventario-clasificacion-fuentes` ya resuelve la detección y clasificación de fuentes existentes.
- `control-anticontaminacion-fuentes` ya resuelve la protección frente a fuentes débiles, ajenas o contaminantes.
- `auditoria-documental-por-fases` ya resuelve la auditoría de intervenciones y el bloqueo de salidas fuera de fase.
- `clasificar-pregunta-plan-empresa` absorberá dependencia de usuario y `NO_RESPONDER_AUN` como salidas de la misma clasificación base, evitando tres skills separadas para una sola tarea documental.

## Resultado esperado

Las capacidades base para preparar Gate 1D quedan cubiertas por un conjunto mínimo y no redundante de skills:

- clasificación de preguntas;
- detección de fuentes existentes;
- marcaje de dependencia / no responder aún dentro de la clasificación;
- control de anticontaminación;
- preparación de bloques para redacción futura;
- auditoría previa a redacción.
