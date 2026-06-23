# 01 — Manifest de fuentes y uso permitido

| Fuente | Categoría | Uso permitido | Uso prohibido | Requiere verificación | Política de copia | Estado |
|---|---|---|---|---|---|---|
| Guía Red ARCE | Base metodológica | Índice, estructura, lógica de plan | Datos del Taller | No | `adapt_required` | Activa |
| Preguntas caso legacy no reutilizable como contenido | Preguntas genéricas | Formular preguntas del plan | Copiar respuestas o narrativa | Revisión puntual | `adapt_required` (solo preguntas) | Activa parcial |
| Repositorio de referencia metodológica | Gobernanza | Fases, gates, manifest, control | Imponer arquitectura técnica prematura | Revisión puntual | `quarantine` / `adapt_required` | Activa parcial |
| Documentos del Taller | Fuente real | Alimentar respuestas y consolidados | Usar sin clasificar | Sí, según tipo | `copy_direct` / `adapt_required` | Pendiente |

---

## Directrices de Uso de Entregables de la FASE 4

Para los artefactos y entregables de maquetación final producidos en la **Fase 4**, se establecen los siguientes criterios:

*   **DOCX final y PDF final:** Su uso es estrictamente de salida y evaluación externa. Queda prohibido utilizarlos como base de edición directa para reintroducir cambios al repositorio. Toda edición debe realizarse sobre los archivos fuente `.md` en `respuestas_plan_empresa/`.
*   **Portada e Índice:** Se maquetarán usando las plantillas estandarizadas del Taller, sin arrastrar estilos corporativos heredados de otros repositorios.
*   **Anexos, Gráficos y Tablas:** Deben tener trazabilidad directa con los datos analizados y estar declarados en `anexos/manifest_anexos.yml`.
*   **Reportes de Auditoría:** Deben reflejar un veredicto de `PASS` absoluto antes de proceder con el cierre de la Fase 4.

