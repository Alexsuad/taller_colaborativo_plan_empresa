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

**Estado:** COMPLETADO (Completado como inventario provisional operativo. No valida definitivamente las fuentes ni autoriza redacción del plan.)  
**Archivos asociados:**  
- `docs_manifest/01_manifest_fuentes_y_uso_permitido.md`  
- `docs_manifest/02_clasificacion_zonas_documentales.md`  
- `docs_organizacion/01_inventario_fuentes.md`  

## Gate 1C — Matriz Red ARCE → fuentes → vacíos

Cruza las preguntas de la guía con las fuentes disponibles para identificar vacíos de información que requerirán datos nuevos del Taller.

**Estado:** EN CURSO (Matriz Red ARCE → fuentes → vacíos en construcción. No se autoriza la redacción del plan.)  
**Nota:** La matriz inicial existe y DEC-011 está aprobada, y la revisión crítica de matriz y vacíos accionables existe y DEC-012 está aprobada, pero Gate 1C no se considera completado hasta resolver o clasificar formalmente las preguntas, investigaciones y validaciones pendientes.
**Archivos asociados:**  
- `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md`  
- `docs_organizacion/03_revision_critica_matriz_vacios.md`  
- `plan_empresa_guia/00_indice_preguntas_guia.md`  

## Gate 1D — Autorización para poblar respuestas_plan_empresa/

Gate de autorización para comenzar la redacción de respuestas en `respuestas_plan_empresa/`. No se puede abrir hasta que Gate 1B y Gate 1C estén completados.

**Estado:** BLOQUEADO  
**Depende de:** Gate 1B (COMPLETADO), Gate 1C (pendiente de completar). Gate 1D no puede abrirse mientras Gate 1C siga EN CURSO.  
**Archivos asociados:**  
- `respuestas_plan_empresa/` (todos los archivos, sin redactar aún)  

---

## Gate Fase 2 — Diseño del sistema/repositorio

Define la estructura física y lógica del repositorio, límites de extensión y diseño de validaciones de calidad.

**Estado:** Pendiente  
**Archivos asociados:**  
- `scripts/auditar_estado_plan_empresa.py`  
- `scripts/auditar_linealidad_plan_empresa.py`  
- `scripts/compilar_plan_empresa.py`  
- `scripts/auditar_texto_corrupto_entrega.py`  
- `scripts/auditar_formato_markdown_entrega.py`  

## Gate Fase 3 — Implementación técnica del sistema

Construcción y alineación de scripts de compilación, linealidad, formato y entorno reproducible sin redactar ni compilar el plan de empresa final.

**Estado:** Pendiente  
**Archivos asociados:**  
- `docs_consolidados/01_documento_rector_negocio.md`  
- `docs_consolidados/02_dossier_mercado_competencia_alianzas.md`  
- `docs_consolidados/03_dossier_operativo_legal_local.md`  
- `docs_consolidados/04_dossier_economico_comercial.md`  

## Gate Fase 4 — Producción editorial, anexos y cierre

Producción editorial final, maquetación, inserción de anexos/gráficos y consolidación limpia para evaluación externa.

**Estado:** Pendiente  
**Archivos asociados:**  
- `respuestas_plan_empresa/` (todos los archivos)  
- `_build/plan_empresa_taller_colaborativo_completo.md`  
