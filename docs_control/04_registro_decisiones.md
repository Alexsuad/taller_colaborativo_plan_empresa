# 04 — Registro de decisiones

Este documento es el registro oficial de cambios del proyecto. Aquí se asientan todas las resoluciones de diseño, cambios de rumbo, correcciones y bloqueos del plan de empresa.

## Reglas de Gobernanza de Cambios Vivos

1. **Prioridad de la Fuente:** El documento final consolidado nunca se edita como fuente principal. Todo cambio estructural o de contenido debe aplicarse primero en los archivos de respuestas individuales dentro de `respuestas_plan_empresa/` y, posteriormente, regenerarse o compilarse el documento final.
2. **Registro Obligatorio:** Cualquier pivote estratégico o revalidación con impacto en el plan debe documentarse primero en este registro antes de actualizar las respuestas.

## Tipos de Registro Admitidos

- **DECISION:** Acuerdos o resoluciones de diseño firmes del proyecto.
- **PIVOTE:** Cambios estratégicos o alteraciones de rumbo en el modelo de negocio.
- **REVALIDACION:** Confirmación formal de supuestos previos que estaban en duda.
- **CORRECCION:** Subsanación de errores materiales o de datos en secciones redactadas.
- **BLOQUEO:** Detención de una sección por falta de información clave o decisiones pendientes.

## Estados Permitidos

- `pendiente`: Cambio registrado pero aún no analizado o sin acciones tomadas.
- `en_revisión`: El cambio está siendo analizado o redactándose las respuestas.
- `aplicado`: El cambio ya se incorporó en `respuestas_plan_empresa/`.
- `revalidado`: El supuesto en duda ha sido confirmado y cerrado.
- `bloqueado`: El cambio o la sección se encuentra paralizada por dependencias externas.
- `descartado`: La propuesta de cambio o decisión ha sido desestimada.

## Tabla de Registro

| ID | Fecha | Tipo | Decisión / cambio | Motivo | Preguntas afectadas | Respuestas afectadas | Acción requerida | Estado |
|---|---|---|---|---|---|---|---|---|
| DEC-001 | 2026-06-22 | DECISION | Crear repo propio del Taller a partir de patrones útiles de repositorios de referencia, sin reutilizar contenido sectorial ajeno | Evitar rehacer trabajo y reducir contaminación | N/A | N/A | Separar carpetas y estructurar ramas | aplicado |
| DEC-002 | 2026-06-22 | DECISION | Trabajar en tres fases: negocio, sistema/repositorio, output | Evitar automatizar o producir antes de clarificar el negocio | N/A | N/A | Definir hitos iniciales de fases | revalidado |
| DEC-003 | 2026-06-22 | DECISION | No reutilizar respuestas ni contenido sectorial de casos legacy no reutilizables | Prevenir contaminación del plan del Taller | N/A | N/A | Copiar solo estructura limpia y scripts base | aplicado |
| DEC-004 | 2026-06-23 | DECISION | Normalizar la sede agéntica en `.agents/` | Centralizar el comportamiento agéntico en una sede única | N/A | N/A | Migrar `.agent/` a `.agents/` y refinar skills | aplicado |
| DEC-005 | 2026-06-23 | DECISION | Añadir auditor de contaminación conceptual (`scripts/auditar_contaminacion_conceptual.py`) | Detectar residuos heredados de forma determinista | N/A | N/A | Implementar script y configuraciones | aplicado |
| DEC-006 | 2026-06-23 | DECISION | Limpiar residuos visibles de contaminación conceptual | Confirmar que los artefactos no arrastran narrativa legacy | N/A | N/A | Retirar reportes de revisión inicial | aplicado |
| DEC-007 | 2026-06-23 | DECISION | Excluir `_build/` del escaneo del auditor de contaminación | Evitar que el reporte se cite a sí mismo generando falsos positivos | N/A | N/A | Añadir a `ignored_paths` en `config/contaminacion_conceptual.yml` | aplicado |
| DEC-008 | 2026-06-23 | DECISION | Sustituir menciones a "Proyecto Automatizaciones" por "repositorio de referencia metodológica" | Eliminar nombres de proyectos externos del corpus activo | N/A | N/A | Actualizar manifest e inventario de fuentes | aplicado |
| DEC-009 | 2026-06-23 | DECISION | Reconciliar gates documentales desglosando Gate Fase 1 en sub-gates | Los gates por fase eran demasiado gruesos para controlar progreso real | N/A | N/A | Reescribir `03_gates_documentales.md` con sub-gates | aplicado |
| DEC-010 | 2026-06-23 | DECISION | Aprobar `docs_organizacion/01_inventario_fuentes.md` como provisional operativo | Unificar inventarios dispersos sin validar fuentes definitivamente ni abrir redacción | N/A | N/A | Reescritura del inventario consolidado | aplicado |
| DEC-011 | 2026-06-23 | DECISION | Inicio de matriz Red ARCE -> fuentes -> vacíos | Crear `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md` para identificar vacíos de información | N/A | N/A | Construir la matriz inicial sin poblar respuestas | aplicado |
| DEC-012 | 2026-06-23 | DECISION | Inicio de revisión crítica de matriz y vacíos accionables | Crear `docs_organizacion/03_revision_critica_matriz_vacios.md` para ordenar vacíos reales | N/A | N/A | Elaborar revisión crítica de vacíos | aplicado |
| DEC-013 | 2026-06-23 | DECISION | Crear un mapa vivo de reutilización del repositorio | Distinguir capa metodológica de la capa específica del Taller | N/A | N/A | Redactar `docs_control/07_mapa_reutilizacion_repo.md` | aplicado |
| DEC-014 | 2026-06-23 | DECISION | Adoptar `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` como matriz activa de Gate 1C; `02` y `03` quedan como apoyo temporal | Evitar redacción prematura o respuestas sin evidencias y avanzar con una matriz viva | `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md`, `docs_organizacion/03_revision_critica_matriz_vacios.md`, `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` | N/A | Mantener Gate 1C operativo sin abrir Gate 1D | aplicado |
| DEC-015 | 2026-06-28 | DECISION | Incorporar el bloque 3.4 de benchmarking de inspiradores clave como ampliación propia del Taller | Ordenar inspiradores reales sin convertirlos en Red ARCE puro ni contaminar el plan | `plan_empresa_guia/00_indice_preguntas_guia.md`, `plan_empresa_guia/03_4_benchmarking_inspiradores.md`, `respuestas_plan_empresa/03_4_benchmarking_inspiradores.md`, `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` | `https://www.instagram.com/lacorporaciontaller/`, `https://atumaderacoworking.es/`, `https://www.instagram.com/cara.y.canto/` | Documentar bloque, espejo de respuestas y clasificación mixta | aplicado |
| DEC-016 | 2026-06-28 | DECISION | Alinear respuestas por subapartados y limitar la guía a viabilidad | Reducir ruido genérico y evitar convertir el plan en manual operativo | `plan_empresa_guia/00_indice_preguntas_guia.md`, `respuestas_plan_empresa/`, `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md`, `plan_empresa_guia/06_2_operaciones.md`, `plan_empresa_guia/06_4_juridico_fiscal.md` | `respuestas_plan_empresa/00_resumen_ejecutivo.md`, `respuestas_plan_empresa/01_equipo_promotor.md`, `respuestas_plan_empresa/02_idea_negocio.md`, `respuestas_plan_empresa/03_1_analisis_externo.md`, `respuestas_plan_empresa/03_2_estudio_mercado.md`, `respuestas_plan_empresa/03_3_analisis_interno.md`, `respuestas_plan_empresa/04_dafo_came.md`, `respuestas_plan_empresa/05_objetivos_lineas_estrategicas.md`, `respuestas_plan_empresa/06_0_marca_comunicacion_naming.md`, `respuestas_plan_empresa/06_1_marketing_ventas.md`, `respuestas_plan_empresa/06_2_operaciones.md`, `respuestas_plan_empresa/06_3_recursos_humanos.md`, `respuestas_plan_empresa/06_4_juridico_fiscal.md`, `respuestas_plan_empresa/06_5_economico_financiero.md`, `respuestas_plan_empresa/07_implantacion_puesta_marcha.md`, `respuestas_plan_empresa/08_viabilidad_conclusiones.md` | Respuestas alineadas por bloques, guía podada y enfoque de viabilidad | aplicado |
| DEC-017 | 2026-06-29 | DECISION | Cerrar operativamente la Fase 1 documental | La limpieza documental ya es suficiente para continuar sin seguir perfeccionando el repositorio | `docs_control/03_gates_documentales.md`, `docs_control/06_fases_oficiales_proyecto.md` | N/A | Mantener Fase 1 cerrada operativamente sin autorizar redacción final ni Gate 1D | aplicado |
| DEC-018 | 2026-06-30 | DECISION | Continuidad post-Gate 1C y autorización de PT-10H | La Fase 1 documental está cerrada operativamente; Gate 1C está operativo para continuar; Gate 1D permanece bloqueado; el control pesado pre-Gate 1C ya no aporta valor operativo | `docs_control/09_plan_maestro_saneamiento_pre_gate_1c.md` | N/A | No poblar `respuestas_plan_empresa/`, no redactar el Plan de Empresa, no compilar entregables, no crear skills expertas, no crear subagentes ni workflows; autorizar solo PT-10H como intervención técnica mínima para skills base documentales utilitarias | aplicado |
| DEC-019 | 2026-07-14 | DECISION | Aclaración de perfiles del equipo promotor, estado de relación jurídica pendiente e incorporación de UPTA Zaragoza | Evitar suposiciones societarias en el bloque 01 y explicitar que el Plan de Empresa es un documento vivo | `docs_control/00_contrato_identidad_negocio.md`, `docs_preparacion/preguntas_resueltas/01_equipo_promotor/*` | N/A | Corregir perfiles, marcar relación jurídica societaria como pendiente y registrar revisión viva con UPTA | aplicado |
| DEC-020 | 2026-07-14 | DECISION | Crear sistema de notas aclaratorias vigentes y control de pivotajes | Prevenir asunción de datos históricos corruptos y controlar el impacto de cambios estratégicos | `docs_control/05_registro_pivotajes_y_cambios_relevantes.md`, `docs_fuentes/drive_taller/00_notas_aclaratorias_vigentes.md`, `AGENTS.md`, `README.md` | N/A | Crear archivos de notas y pivotajes y actualizar reglas operativas agénticas | aplicado |

---

## Control de Pivotajes Transversales
A partir de la decisión **DEC-020**, la gestión, plantillas, registro y ejemplos de pivotajes estratégicos que afecten de forma transversal a múltiples áreas del Plan de Empresa se delegan de manera exclusiva al documento de control:
- [05_registro_pivotajes_y_cambios_relevantes.md](file:///docs_control/05_registro_pivotajes_y_cambios_relevantes.md)

Este registro (04_registro_decisiones.md) se mantiene exclusivamente como el diario oficial de decisiones metodológicas del repositorio y el estado general de los gates documentales. Queda prohibida la duplicidad de registros operativos de pivotajes aquí.

