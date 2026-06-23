# Reporte de Auditoría de Contaminación Conceptual

Generado a partir del archivo de configuración: `config/contaminacion_conceptual.yml`.

## Resumen Estadístico

| Estado | Cantidad | Descripción |
| :--- | :---: | :--- |
| 🔴 **BLOCKED** | 18 | Términos en rutas no permitidas. Requiere acción inmediata. |
| 🟡 **REVIEW** | 3 | Términos detectados en rutas neutras o sin definir. |
| 🟢 **ALLOWED_LEGACY** | 4 | Términos en rutas permitidas (histórico / legacy). |

## 🔴 Hallazgos Bloqueantes (BLOCKED)

| Archivo | Línea | Término | Severidad | Contexto | Recomendación |
| :--- | :---: | :--- | :---: | :--- | :--- |
| [`.agents/rules/01-rutas-fuente-verdad.md`](file:///.agents/rules/01-rutas-fuente-verdad.md) | 1 | `sistreg` | **HIGH** | `<!-- Migrado desde repo SISTREG. Revisado parcialmente para Fase 1. -->` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`.agents/rules/02-no-inventar-fuentes.md`](file:///.agents/rules/02-no-inventar-fuentes.md) | 1 | `sistreg` | **HIGH** | `<!-- Migrado desde repo SISTREG. Revisado parcialmente para Fase 1. -->` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`.agents/rules/03-aprobacion-explicita.md`](file:///.agents/rules/03-aprobacion-explicita.md) | 1 | `sistreg` | **HIGH** | `<!-- Migrado desde repo SISTREG. Revisado parcialmente para Fase 1. -->` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`.agents/rules/04-entrega-limpia.md`](file:///.agents/rules/04-entrega-limpia.md) | 1 | `sistreg` | **HIGH** | `<!-- Migrado desde repo SISTREG. Revisado parcialmente para Fase 1. -->` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`.agents/rules/05-linealidad-documental.md`](file:///.agents/rules/05-linealidad-documental.md) | 1 | `sistreg` | **HIGH** | `<!-- Migrado desde repo SISTREG. Revisado parcialmente para Fase 1. -->` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`.agents/skills/control-anticontaminacion-fuentes/SKILL.md`](file:///.agents/skills/control-anticontaminacion-fuentes/SKILL.md) | 65 | `sistreg` | **HIGH** | `* No usar SISTREG como contenido del Taller.` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`AGENTS.md`](file:///AGENTS.md) | 11 | `sistreg` | **HIGH** | `...as de clientes de otros proyectos (como SISTREG o proyectos logísticos).` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`AGENTS.md`](file:///AGENTS.md) | 11 | `logístico` | **HIGH** | `...ros proyectos (como SISTREG o proyectos logísticos).` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`docs_control/04_registro_decisiones.md`](file:///docs_control/04_registro_decisiones.md) | 5 | `sistreg` | **HIGH** | `...aller a partir de lo mejor de los repos SISTREG y Proyecto Automatizaciones | Ev...` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`docs_control/04_registro_decisiones.md`](file:///docs_control/04_registro_decisiones.md) | 7 | `sistreg` | **HIGH** | `...ar respuestas ni contenido sectorial de SISTREG | Prevenir contaminación del pla...` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`docs_manifest/01_manifest_fuentes_y_uso_permitido.md`](file:///docs_manifest/01_manifest_fuentes_y_uso_permitido.md) | 6 | `sistreg` | **HIGH** | `| Preguntas SISTREG | Preguntas genéricas | Formular preguntas del plan | Copiar...` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`docs_organizacion/01_inventario_fuentes.md`](file:///docs_organizacion/01_inventario_fuentes.md) | 6 | `sistreg` | **HIGH** | `| DOC-002 | Repo SISTREG — plan_empresa | Preguntas guía | Repo anterior | Migra...` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`docs_organizacion/07_propuesta_inventario_puente_fuentes_externas.md`](file:///docs_organizacion/07_propuesta_inventario_puente_fuentes_externas.md) | 106 | `sistreg` | **HIGH** | `| PUENTE-002 | `plan_empresa_sistreg_completo (V2)`                             ...` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`repo_identity.yml`](file:///repo_identity.yml) | 10 | `sistreg` | **HIGH** | `created_from: "SISTREG / Proyecto Automatizaciones (base metodológica)"` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`scripts/auditar_formato_markdown_entrega.py`](file:///scripts/auditar_formato_markdown_entrega.py) | 2 | `sistreg` | **HIGH** | `# Script copiado desde repo SISTREG como base técnica.` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`scripts/auditar_linealidad_plan_empresa.py`](file:///scripts/auditar_linealidad_plan_empresa.py) | 2 | `sistreg` | **HIGH** | `# Script copiado desde repo SISTREG como base técnica.` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`scripts/auditar_texto_corrupto_entrega.py`](file:///scripts/auditar_texto_corrupto_entrega.py) | 2 | `sistreg` | **HIGH** | `# Script copiado desde repo SISTREG como base técnica.` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`scripts/compilar_plan_empresa.py`](file:///scripts/compilar_plan_empresa.py) | 2 | `sistreg` | **HIGH** | `# Script copiado desde repo SISTREG como base técnica.` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |

## 🟡 Hallazgos en Revisión (REVIEW)

| Archivo | Línea | Término | Severidad | Contexto | Recomendación |
| :--- | :---: | :--- | :---: | :--- | :--- |
| [`plan_empresa_guia/00_resumen_ejecutivo.md`](file:///plan_empresa_guia/00_resumen_ejecutivo.md) | 14 | `logístico` | **HIGH** | `- No debe contener respuestas reales del Proyecto Logístico.` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`plan_empresa_guia/06_0_marca_comunicacion_naming.md`](file:///plan_empresa_guia/06_0_marca_comunicacion_naming.md) | 6 | `logístico` | **HIGH** | `- ¿Cuál es el nombre provisional? (Ej: Proyecto Logístico).` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`plan_empresa_guia/06_1_marketing_ventas.md`](file:///plan_empresa_guia/06_1_marketing_ventas.md) | 428 | `logística` | **HIGH** | `* Logística.` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |

## 🟢 Hallazgos Permitidos (ALLOWED_LEGACY)

| Archivo | Línea | Término | Severidad | Contexto | Recomendación |
| :--- | :---: | :--- | :---: | :--- | :--- |
| [`_build/reportes/00_reporte_creacion_repo.md`](file:///_build/reportes/00_reporte_creacion_repo.md) | 4 | `sistreg` | **HIGH** | `- Preguntas guía migradas desde SISTREG y saneadas parcialmente.` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`_build/reportes/01_revision_tecnica_inicial_antigravity.md`](file:///_build/reportes/01_revision_tecnica_inicial_antigravity.md) | 15 | `sistreg` | **HIGH** | `...al de archivos desde repositorios como `SISTREG` y `Proyecto Automatizaciones`.` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |
| [`_build/reportes/01_revision_tecnica_inicial_antigravity.md`](file:///_build/reportes/01_revision_tecnica_inicial_antigravity.md) | 42 | `logístico` | **HIGH** | `...anticontaminación porque busca términos logísticos heredados como `e-CMR`, `eCMR...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/01_revision_tecnica_inicial_antigravity.md`](file:///_build/reportes/01_revision_tecnica_inicial_antigravity.md) | 52 | `sistreg` | **HIGH** | `...as obsoletas heredadas del repositorio `SISTREG` que representan una desalineaci...` | Sustituir por 'caso legacy' o eliminar si está en documento activo. (review_or_replace) |

