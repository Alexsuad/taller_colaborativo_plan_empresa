# Reporte de Auditoría de Contaminación Conceptual

Generado a partir del archivo de configuración: `config/contaminacion_conceptual.yml`.

## Resumen Estadístico

| Estado | Cantidad | Descripción |
| :--- | :---: | :--- |
| 🔴 **BLOCKED** | 0 | Términos en rutas no permitidas. Requiere acción inmediata. |
| 🟡 **REVIEW** | 3 | Términos detectados en rutas neutras o sin definir. |
| 🟢 **ALLOWED_LEGACY** | 0 | Términos en rutas permitidas (histórico / legacy). |

## 🔴 Hallazgos Bloqueantes (BLOCKED)

No se encontraron hallazgos bloqueantes en las rutas prohibidas. ¡Excelente!

## 🟡 Hallazgos en Revisión (REVIEW)

| Archivo | Línea | Término | Severidad | Contexto | Recomendación |
| :--- | :---: | :--- | :---: | :--- | :--- |
| [`plan_empresa_guia/00_resumen_ejecutivo.md`](file:///plan_empresa_guia/00_resumen_ejecutivo.md) | 14 | `logístico` | **HIGH** | `- No debe contener respuestas reales del Proyecto Logístico.` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`plan_empresa_guia/06_0_marca_comunicacion_naming.md`](file:///plan_empresa_guia/06_0_marca_comunicacion_naming.md) | 6 | `logístico` | **HIGH** | `- ¿Cuál es el nombre provisional? (Ej: Proyecto Logístico).` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |
| [`plan_empresa_guia/06_1_marketing_ventas.md`](file:///plan_empresa_guia/06_1_marketing_ventas.md) | 428 | `logística` | **HIGH** | `* Logística.` | Eliminar o sustituir por una formulación neutra no asociada al proyecto anterior. (review_or_replace) |

## 🟢 Hallazgos Permitidos (ALLOWED_LEGACY)

No hay registros de uso legacy permitidos en el repositorio.

