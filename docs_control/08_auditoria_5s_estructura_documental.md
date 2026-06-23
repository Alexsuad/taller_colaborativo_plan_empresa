# 08 — Auditoría 5S de estructura documental

**Estado:** Diagnóstico inicial — no ejecuta cambios.  
**Propósito:** Detectar problemas de orden, numeración, duplicidad, documentos consolidados, sedes confusas y archivos que deberían reclasificarse antes de seguir avanzando.

## 1. Criterio Lean / 5S aplicado

- **Seiri:** separar necesario, histórico, duplicado, consolidado y pendiente.
- **Seiton:** ordenar rutas y numeraciones para que el flujo sea claro.
- **Seiso:** detectar ruido documental, residuos y archivos fuera de lugar.
- **Seiketsu:** proponer reglas estándar de nombres, numeración y sedes.
- **Shitsuke:** definir cómo mantener el orden cuando se creen nuevos documentos.

## 2. Inventario de carpetas revisadas

| Carpeta | Función esperada | Estado observado | Riesgo 5S | Recomendación |
|---|---|---|---|---|
| `docs_control/` | Gobernanza, gates, decisiones, fases y sedes | Ordenada en general; numeración continua `00` a `08` con documentos de control y mapa de reutilización | Bajo | Mantener como sede de control; evitar mezclar diagnósticos operativos con decisiones del negocio |
| `docs_organizacion/` | Diagnósticos de trabajo, inventarios, matrices y revisiones operativas | Con ruido moderado: conviven matrices activas, propuestas previas y documentos consolidados/históricos | Alto | Separar mejor activos, históricos y consolidaciones; clarificar qué documento manda en cada tema |
| `docs_manifest/` | Manifiestos y políticas de uso de fuentes | Estructura pequeña y relativamente estable | Bajo | Mantener como sede de políticas; revisar que no absorba contenido operativo del inventario |
| `docs_fuentes/` | Fuentes reales y clasificadas | No inspeccionada en detalle aquí, pero su función de sede de fuentes debe mantenerse aislada | Medio | No mezclar con matrices ni con consolidaciones; proteger como sede de evidencia |
| `docs_consolidados/` | Dossiers consolidados y redactables | Sede de contenido ya absorbido o consolidado; no debe competir con diagnósticos | Medio-Alto | Tratar como salida o destino de consolidación, no como área de trabajo diario |
| `respuestas_plan_empresa/` | Respuestas del plan | Sede bloqueada y aún no autorizada para redacción completa | Alto | Mantener cerrada hasta que gates y clasificaciones estén completas |
| `plan_empresa_guia/` | Preguntas guía y estructura Red ARCE | Estructura clara, pero con múltiples archivos de preguntas que condicionan el flujo de clasificación | Medio | Conservar como sede de preguntas; no convertirla en repositorio de respuestas |
| `scripts/` | Validación y automatización documental | Conjunto útil y coherente para el sistema técnico | Bajo | Mantener como capa técnica; evitar duplicados de funciones sin justificación |
| `config/` | Configuración de reglas y auditoría | Pequeña y funcional | Bajo | Mantener como capa de parámetros; evitar mezclar contenido de negocio |
| `.agents/` | Reglas, skills y workflows agénticos | Sede agéntica clara, aunque necesita limpieza de menciones específicas del Taller para reuso futuro | Medio | Mantener como sede única de reglas; no duplicar instrucciones fuera de esta carpeta |
| `_build/` | Reportes y outputs generados | Sede de salida generada; no debe usarse como entrada documental | Medio | Mantener como output; regenerar cuando haga falta y no como fuente de verdad |

## 3. Auditoría de numeración por carpeta

| Carpeta | Archivos numerados encontrados | Saltos o conflictos | Interpretación | Acción recomendada |
|---|---|---|---|---|
| `docs_control/` | `00` a `08` | Sin saltos graves; solo crecimiento natural | Numeración clara para la sede de control | Seguir numerando por extensión funcional; mantener un archivo por decisión/gate/criterio |
| `docs_organizacion/` | `01`, `02`, `03`, `04`, `05`, `06`, `07` | Conflictos de secuencia y paralelismo: `02_matriz_preguntas_fuentes_vacios.md` convive con `02_matriz_red_arce_fuentes_vacios.md`; `03_mapa_duplicados.md` convive con `03_revision_critica_matriz_vacios.md`; `06` y `07` son propuestas ya consolidadas en `01` | La carpeta mezcla documentos activos, diagnósticos antiguos, consolidaciones y borradores metodológicos | Aislar histórico o marcado `consolidado_`/`historico_` en el futuro; dejar una sola sede activa por concepto |
| `docs_manifest/` | `01`, `02` | Sin conflicto aparente | Secuencia corta y estable | Mantener la secuencia y evitar duplicar el mismo manifiesto en otras sedes |
| `plan_empresa_guia/` | `00`, `01`, `02`, `03_1`, `03_2`, `03_3`, `04`, `05`, `06_0`, `06_1`, `06_2`, `06_3`, `06_4`, `06_5`, `07`, `08` | Sin conflicto crítico, aunque hay mucha granularidad | Secuencia funcional para preguntas del plan | Conservar como guía y no mezclarla con respuestas o consolidaciones |

## 4. Documentos activos vs documentos consolidados/históricos

| Archivo | Estado aparente | ¿Sigue activo? | Problema detectado | Recomendación |
|---|---|---|---|---|
| `docs_organizacion/01_inventario_fuentes.md` | Consolidado operativo | Sí | Convive con propuestas antiguas que ya absorbió | Tratarlo como sede principal del inventario; no duplicar su contenido en otros archivos |
| `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md` | Matriz activa de diagnóstico | Sí | Coexiste con una versión previa más simple (`02_matriz_preguntas_fuentes_vacios.md`) | Mantenerla como referencia vigente y marcar la anterior como historial o precursor |
| `docs_organizacion/03_revision_critica_matriz_vacios.md` | Revisión activa de vacíos accionables | Sí | Comparte numeración con `03_mapa_duplicados.md` | Mantenerla como documento activo y relegar el mapa de duplicados a soporte histórico o técnico |
| `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` | Matriz activa de clasificación previa a redacción | Sí | Aún pendiente de aprobación y sin asociación clara previa en el árbol físico | Mantenerla como diagnóstico activo; no copiar su lógica a respuestas |
| `docs_organizacion/06_propuesta_inventario_general_fuentes.md` | Propuesta consolidada con `01_inventario_fuentes.md` | No como activo principal | Ya consolidado, pero sigue visible como documento largo y detallado | Marcarlo más claramente como histórico/consolidado o archivar en el futuro |
| `docs_organizacion/07_propuesta_inventario_puente_fuentes_externas.md` | Propuesta consolidada con `01_inventario_fuentes.md` | No como activo principal | Mismo problema que `06`: útil como diagnóstico, pero no como sede de trabajo diario | Considerar reclasificación histórica o archivo en futuro si deja de consultarse |
| `docs_organizacion/02_matriz_preguntas_fuentes_vacios.md` | Precursor simple | Parcialmente | Duplicidad funcional con la matriz ARCE más completa | Señalarlo como precursor histórico o absorbido por `02_matriz_red_arce_fuentes_vacios.md` |
| `docs_organizacion/03_mapa_duplicados.md` | Placeholder / pendiente | No todavía | Contenido casi vacío, puede confundir como documento vivo sin función real | Completarlo o archivarlo; mientras tanto, no usarlo como sede funcional |
| `docs_organizacion/05_propuesta_clasificacion_instalaciones_seguridad.md` | Propuesta temática específica | Parcialmente | Se solapa con el inventario consolidado y con las matrículas de fuente sobre local/seguridad | Decidir si pasa a soporte histórico, si se absorbe o si se mantiene como propuesta especializada |

### Observación específica sobre `06` y `07`

- `06_propuesta_inventario_general_fuentes.md` y `07_propuesta_inventario_puente_fuentes_externas.md` ya están absorbidos conceptualmente por `01_inventario_fuentes.md`.
- Hoy aportan contexto de origen y trazabilidad, pero no deberían competir con `01` como sede operativa.
- A medio plazo conviene que queden marcados de forma más explícita como consolidados o históricos.
- En un futuro, si el repositorio crece, podría interesar moverlos a una carpeta de archivo histórico; por ahora eso no debe ejecutarse.

## 5. Sedes documentales confusas

| Tema | Sede actual | Sede recomendada | Riesgo | Acción futura |
|---|---|---|---|---|
| Inventario de fuentes | `docs_organizacion/01_inventario_fuentes.md`, con propuestas `06` y `07` aún visibles | `docs_organizacion/01_inventario_fuentes.md` como única sede activa | Alto | Marcar `06` y `07` como absorbidos o históricos para evitar competencia semántica |
| Matriz de fuentes y vacíos | `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md` y `docs_organizacion/02_matriz_preguntas_fuentes_vacios.md` | `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md` | Alto | Señalar la versión simple como precursor o histórico |
| Revisión de vacíos | `docs_organizacion/03_revision_critica_matriz_vacios.md` y `docs_organizacion/03_mapa_duplicados.md` | `docs_organizacion/03_revision_critica_matriz_vacios.md` | Medio | Convertir `03_mapa_duplicados.md` en soporte técnico/histórico si sigue aportando algo |
| Clasificación previa a redacción | `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` | `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` | Bajo | Mantener como sede única y no duplicar su lógica en respuestas |
| Fuentes reales | `docs_fuentes/` | `docs_fuentes/` | Medio | No mezclar con matrices ni con consolidaciones |
| Consolidación final | `docs_consolidados/` | `docs_consolidados/` | Medio-Alto | Mantener solo contenido ya consolidado y no mezclarlo con trabajo en curso |

## 6. Propuesta de reglas de orden

- La numeración se controla por carpeta.
- Los documentos activos deben mantener secuencia clara.
- Los documentos consolidados deben marcarse como consolidados o archivarse.
- Las propuestas absorbidas no deben competir con documentos operativos.
- Ningún documento nuevo se numera sin listar antes la carpeta.
- Los documentos de control van en `docs_control/`.
- Las matrices y diagnósticos de trabajo van en `docs_organizacion/`.
- Los manifiestos de fuentes van en `docs_manifest/`.
- Las fuentes reales van en `docs_fuentes/`.
- Los consolidados redactables van en `docs_consolidados/`.
- Las respuestas del plan van en `respuestas_plan_empresa/`.

## 7. Recomendaciones priorizadas

### Alta prioridad

- Resolver la dualidad entre `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md` y `docs_organizacion/02_matriz_preguntas_fuentes_vacios.md`.
- Marcar `06_propuesta_inventario_general_fuentes.md` y `07_propuesta_inventario_puente_fuentes_externas.md` como absorbidos por `01_inventario_fuentes.md`.
- Decidir el destino funcional de `03_mapa_duplicados.md`, porque ahora aporta poco valor operativo.
- Mantener una sola sede activa para cada concepto crítico: inventario, matriz de vacíos y clasificación de preguntas.

### Media prioridad

- Diferenciar visualmente documentos activos de históricos en `docs_organizacion/`.
- Revisar si `05_propuesta_clasificacion_instalaciones_seguridad.md` sigue siendo una propuesta viva o solo material de apoyo.
- Establecer un patrón de nombres para documentos consolidados o históricos.

### Baja prioridad

- Simplificar futuras numeraciones en documentos de apoyo.
- Homogeneizar encabezados y estados para reducir la sensación de “carpeta mixta”.
- Valorar una carpeta de archivo histórico solo cuando el volumen lo justifique.

## 8. Qué NO se debe hacer todavía

- No renombrar archivos aún.
- No mover documentos aún.
- No borrar documentos aún.
- No cerrar Gate 1C.
- No abrir Gate 1D.
- No modificar `respuestas_plan_empresa/`.
- No modificar `docs_fuentes/`.
- No modificar `docs_consolidados/`.

## 9. Dictamen preliminar

**Dictamen recomendado:** `ORDENADO_CON_RUIDO`

Motivo:

- La estructura general existe y es reconocible.
- Las sedes principales están bien separadas a nivel macro.
- Sin embargo, `docs_organizacion/` acumula versiones previas, propuestas consolidadas y matrices activas que pueden confundir el flujo.
- El problema no parece exigir una reestructuración grande ahora mismo, pero sí una limpieza controlada y futura reclasificación.

