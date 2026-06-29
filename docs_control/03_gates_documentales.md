# 03 — Gates documentales

## Gate 1A — Identidad, sede agéntica y anticontaminación

Consolida la identidad del taller, la opción activa de negocio, las reglas de anticontaminación y la sede agéntica.

**Estado:** COMPLETADO  
**Archivos asociados:**  
- `docs_control/00_contrato_identidad_negocio.md`  
- `docs_control/01_opcion_activa_taller.md`  
- `docs_control/02_reglas_anticontaminacion.md`  
- `docs_control/07_mapa_reutilizacion_repo.md`  
- `docs_control/06_fases_oficiales_proyecto.md`  
- `repo_identity.yml`  
- `artifact_manifest.yml`  
- `AGENTS.md`  
- `.agents/` (reglas, skills, workflows)  
- `scripts/auditar_contaminacion_conceptual.py`  
- `config/contaminacion_conceptual.yml`  

## Gate 1B — Inventario real de fuentes

Clasifica las fuentes reales del Taller (documentos propios, datos de mercado, convenios) y establece su política de uso permitido.

**Estado:** COMPLETADO_PROVISIONAL_OPERATIVO (Inventario provisional operativo. No implica importación de fuentes reales en `docs_fuentes/`, no valida definitivamente las fuentes, no autoriza redacción del plan, no autoriza poblar `respuestas_plan_empresa/` ni crear `docs_consolidados/`.)  
**Archivos asociados:**  
- `docs_manifest/01_manifest_fuentes_y_uso_permitido.md`  
- `docs_manifest/02_clasificacion_zonas_documentales.md`  
- `docs_organizacion/01_inventario_fuentes.md`  

## Gate 1C — Matriz Red ARCE → fuentes → vacíos

Cruza las preguntas de la guía con las fuentes disponibles para identificar vacíos de información que requerirán datos nuevos del Taller.

**Estado:** EN CURSO / EN REVISIÓN (Matriz Red ARCE → fuentes → vacíos en construcción. No se autoriza la redacción del plan.)  
**Nota:** La matriz inicial existe y DEC-011 está aprobada, y la revisión crítica de matriz y vacíos accionables existe y DEC-012 está aprobada. La matriz `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` opera como matriz activa de Gate 1C; `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md` y `docs_organizacion/03_revision_critica_matriz_vacios.md` quedan como apoyo temporal. Gate 1C sigue en revisión y Gate 1D sigue bloqueado.
**Archivos asociados:**  
- `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md`  
- `docs_organizacion/03_revision_critica_matriz_vacios.md`  
- `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md`  
- `plan_empresa_guia/00_indice_preguntas_guia.md`  

## Gate 1D — Autorización para poblar respuestas_plan_empresa/

Gate de autorización para comenzar la redacción de respuestas en `respuestas_plan_empresa/`. No se puede abrir hasta que Gate 1B y Gate 1C estén completados.

**Estado:** BLOQUEADO  
**Depende de:** Gate 1B (`COMPLETADO_PROVISIONAL_OPERATIVO`), Gate 1C (pendiente de completar). Gate 1D no puede abrirse mientras Gate 1C siga EN CURSO o en revisión. En esta etapa no se debe poblar `respuestas_plan_empresa/`.
**Archivos asociados:**  
- `respuestas_plan_empresa/` (todos los archivos, sin redactar aún)  

---

## Gate Fase 2 — Diseño del sistema/repositorio

Define la estructura física y lógica del repositorio, límites de extensión y diseño de validaciones de calidad.

**Estado:** PENDIENTE (Fase 2 parcialmente avanzada por el desarrollo inicial de matrices y gobernanza)  
**Archivos asociados:**  
- `scripts/auditar_estado_plan_empresa.py`  
- `scripts/auditar_linealidad_plan_empresa.py`  
- `scripts/compilar_plan_empresa.py`  
- `scripts/auditar_texto_corrupto_entrega.py`  
- `scripts/auditar_formato_markdown_entrega.py`  

## Gate Fase 3 — Implementación técnica del sistema

Construcción y alineación de scripts de compilación, linealidad, formato y entorno reproducible sin redactar ni compilar el plan de empresa final.

**Estado:** BLOQUEADO  
**Archivos asociados:**  
- `docs_consolidados/01_documento_rector_negocio.md`  
- `docs_consolidados/02_dossier_mercado_competencia_alianzas.md`  
- `docs_consolidados/03_dossier_operativo_legal_local.md`  
- `docs_consolidados/04_dossier_economico_comercial.md`  

## Gate Fase 4 — Producción editorial, anexos y cierre

Producción editorial final, maquetación, inserción de anexos/gráficos y consolidación limpia para evaluación externa.

**Estado:** BLOQUEADO  
**Archivos asociados:**  
- `respuestas_plan_empresa/` (todos los archivos)  
- `_build/plan_empresa_taller_colaborativo_completo.md`  

---

## Gate de coherencia por cambios vivos (Control Transversal)

Este gate de control transversal actúa como salvaguarda obligatoria antes de dar por cerrada cualquier sección individual de respuestas (`respuestas_plan_empresa/`) o compilar el documento final del plan de empresa. Garantiza la integridad del plan como **documento vivo**.

### Criterios de Verificación Obligatorios

Antes de cerrar una sección o compilar el entregable final, se debe auditar:
1. **Pivotes y cambios registrados:** Comprobar si existe algún `PIVOTE`, `DECISION`, `REVALIDACION`, `CORRECCION` o `BLOQUEO` pendiente en `docs_control/04_registro_decisiones.md`.
2. **Respuestas afectadas:** Verificar si las respuestas de la sección en cuestión coinciden con el estado actual de las decisiones y pivotes.
3. **Reapertura de preguntas:** Evaluar si hay preguntas de la guía que deban reabrirse debido a un cambio estratégico.
4. **Matriz de clasificación:** Confirmar que la clasificación de preguntas en `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` sigue siendo coherente con el pivote.
   Esta matriz es la activa de Gate 1C; no cierra Gate 1C por sí sola ni autoriza Gate 1D.
5. **Consistencia del documento final:** Asegurar que la regeneración del documento final completo no introduzca contradicciones lógicas ni estructurales.

### Reglas de Bloqueo Selectivo y General

- **Bloqueo a Nivel de Sección:** Una sección de respuestas individual no podrá darse por cerrada si existen registros en `docs_control/04_registro_decisiones.md` con estado `pendiente`, `en_revisión` o `bloqueado` que afecten directa o transversalmente a esa sección.
- **Bloqueo del Documento Final Completo:** La compilación y entrega del documento final completo (`_build/plan_empresa_taller_colaborativo_completo.md` u otros consolidados) quedará estrictamente **BLOQUEADA** si existe cualquier pivote, bloqueo, decisión o revalidación pendiente con impacto no resuelto (es decir, en estados `pendiente`, `en_revisión` o `bloqueado`) en el registro.
