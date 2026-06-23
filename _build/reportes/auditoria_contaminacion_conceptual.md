# Reporte de Auditoría de Contaminación Conceptual

Generado a partir del archivo de configuración: `config/contaminacion_conceptual.yml`.

## Resumen Estadístico

| Estado | Cantidad | Descripción |
| :--- | :---: | :--- |
| 🔴 **BLOCKED** | 0 | Términos en rutas no permitidas. Requiere acción inmediata. |
| 🟡 **REVIEW** | 3 | Términos detectados en rutas neutras o sin definir. |
| 🟢 **ALLOWED_LEGACY** | 12 | Términos en rutas permitidas (histórico / legacy). |

## 🔴 Hallazgos Bloqueantes (BLOCKED)

No se encontraron hallazgos bloqueantes en las rutas prohibidas. ¡Excelente!

## 🟡 Hallazgos en Revisión (REVIEW)

| Archivo | Línea | Término | Severidad | Contexto | Recomendación |
| :--- | :---: | :--- | :---: | :--- | :--- |
| [`plan_empresa_guia/00_resumen_ejecutivo.md`](file:///plan_empresa_guia/00_resumen_ejecutivo.md) | 14 | `logístico` | **HIGH** | `- No debe contener respuestas reales del Proyecto Logístico.` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`plan_empresa_guia/06_0_marca_comunicacion_naming.md`](file:///plan_empresa_guia/06_0_marca_comunicacion_naming.md) | 6 | `logístico` | **HIGH** | `- ¿Cuál es el nombre provisional? (Ej: Proyecto Logístico).` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`plan_empresa_guia/06_1_marketing_ventas.md`](file:///plan_empresa_guia/06_1_marketing_ventas.md) | 428 | `logística` | **HIGH** | `* Logística.` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |

## 🟢 Hallazgos Permitidos (ALLOWED_LEGACY)

| Archivo | Línea | Término | Severidad | Contexto | Recomendación |
| :--- | :---: | :--- | :---: | :--- | :--- |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 21 | `logístico` | **HIGH** | `...a_guia/00_resumen_ejecutivo.md) | 14 | `logístico` | **HIGH** | `- No debe conte...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 22 | `logístico` | **HIGH** | `..._0_marca_comunicacion_naming.md) | 6 | `logístico` | **HIGH** | `- ¿Cuál es el n...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 23 | `logística` | **HIGH** | `...guia/06_1_marketing_ventas.md) | 428 | `logística` | **HIGH** | `* Logística.` |...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 29 | `logístico` | **HIGH** | `...ia_contaminacion_conceptual.md) | 21 | `logístico` | **HIGH** | `...a_guia/00_re...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 30 | `logístico` | **HIGH** | `...ia_contaminacion_conceptual.md) | 22 | `logístico` | **HIGH** | `..._0_marca_com...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 31 | `logística` | **HIGH** | `...ia_contaminacion_conceptual.md) | 23 | `logística` | **HIGH** | `...guia/06_1_ma...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 32 | `logístico` | **HIGH** | `...ia_contaminacion_conceptual.md) | 29 | `logístico` | **HIGH** | `...ia_contamina...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 33 | `logístico` | **HIGH** | `...ia_contaminacion_conceptual.md) | 30 | `logístico` | **HIGH** | `...ia_contamina...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 34 | `logística` | **HIGH** | `...ia_contaminacion_conceptual.md) | 31 | `logística` | **HIGH** | `...ia_contamina...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 35 | `logístico` | **HIGH** | `...ia_contaminacion_conceptual.md) | 32 | `logístico` | **HIGH** | `...ia_contamina...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 36 | `logístico` | **HIGH** | `...ia_contaminacion_conceptual.md) | 33 | `logístico` | **HIGH** | `...ia_contamina...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`_build/reportes/auditoria_contaminacion_conceptual.md`](file:///_build/reportes/auditoria_contaminacion_conceptual.md) | 37 | `logística` | **HIGH** | `...ia_contaminacion_conceptual.md) | 34 | `logística` | **HIGH** | `...ia_contamina...` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |

