# Producción controlada de capítulo del plan

## Propósito
Encadenar los pasos obligatorios y dependencias lógicas necesarias para preparar y redactar un capítulo del Plan de Empresa, garantizando la consistencia estratégica de negocio y evitando la generación de respuestas de forma desordenada o sin base.

## Flujo Secuencial Comercial
El workflow debe seguir y exigir este flujo estricto de desarrollo para evitar incoherencias:
1. Entrada/Fuentes.
2. Diagnóstico/Clasificación.
3. Verificación de dependencias.
4. Apertura parcial de Gate 1D, si aplica y está autorizada para ese capítulo.
5. Preparación de bloque.
6. Redacción controlada, únicamente si Gate 1D está abierto parcialmente para ese capítulo.
7. Auditoría de especialistas.
8. Reviewer QA.
9. Gate transversal / cierre del bloque.
10. Bloqueo de compilación y Fase 4 mientras existan pendientes.

## Tabla de Dependencias Obligatorias de Información
Queda prohibido iniciar la preparación de un bloque si no se han satisfecho previamente sus dependencias de información:

| Capítulo o sección | Depende de (Requisito previo obligatorio) | Razón de negocio |
| --- | --- | --- |
| **02. Idea de negocio / Propuesta** | `01. Cliente objetivo y segmentos` | No se puede diseñar la oferta ni propuesta de valor sin saber a quién va dirigida. |
| **03. Canales de atracción** | `02. Propuesta de valor clara` | No se puede definir cómo atraer tráfico si no se tiene la propuesta diferencial de valor. |
| **04. Acciones comerciales** | `03. Canales priorizados y definidos` | Las acciones de marketing se ejecutan únicamente sobre canales previamente elegidos. |
| **05. Presupuesto de marketing** | `04. Acciones comerciales de marketing` | El presupuesto de marketing debe ser el reflejo cuantificado de las acciones a realizar. |
| **06. KPIs de marketing** | `05. Presupuesto y recursos de marketing` | Los KPIs de éxito deben estar directamente asociados a los recursos y presupuesto real del Taller. |
| **07. Tono y mensaje de comunicación** | `02. Propuesta de valor` y `01. Cliente` | La narrativa del taller debe hablar al cliente del taller con su propuesta diferencial. |
| **08. Redes sociales y calendario** | `07. Tono y mensaje de comunicación` | Las redes sociales están subordinadas al plan de comunicación general y capacidad real. |
| **09. Objetivos estratégicos** | `DAFO/CAME` | Los objetivos de negocio deben nacer de las debilidades y fortalezas reales del Taller. |
| **10. Proceso de ventas completo** | `Modelo de ingresos` | La forma de captación y conversión depende del modelo de cobro y de facturación. |
| **11. Viabilidad y conclusiones** | `Base económico-financiera y supuestos` | No se puede concluir la viabilidad sin contar con el plan de tesorería y punto de equilibrio. |
| **00. Resumen Ejecutivo** | *Todos los capítulos del plan de empresa* | Debe ser estrictamente la última pieza a redactar al finalizar el plan. |

## Reglas de Control del Workflow
- **Bloqueo de Redacción sin Puertas (Gate 1D):** El workflow no autoriza ni ejecuta la redacción de respuestas definitivas si el Gate 1D de control no está abierto de forma parcial y explícita para el capítulo correspondiente.
- **No cierre sin Reviewer QA:** Ningún capítulo del plan puede considerarse finalizado o completado si no cuenta con el veredicto del Reviewer QA.
- **No compilación prematura:** Queda prohibido compilar el plan de empresa completo o avanzar a Fase 4 de producción editorial si existe algún bloque con dependencias pendientes o bloqueos de consistencia.
- **Detección de dependencias:** Antes de iniciar cualquier preparación, el workflow comprobará si los capítulos precedentes listados en la tabla de dependencias han superado su correspondiente gate transversal.
