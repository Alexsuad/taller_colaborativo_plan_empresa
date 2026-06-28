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
| DEC-014 | 2026-06-23 | DECISION | Evaluar matriz de clasificación de preguntas Red ARCE | Evitar redacción prematura o respuestas sin evidencias | N/A | N/A | Analizar e integrar propuesta de clasificación | pendiente |

## Ejemplos de Uso del Registro para Pivotes y Cambios Vivos

*Estos ejemplos sirven como guía metodológica sobre cómo registrar pivotes y qué áreas del plan se verían impactadas.*

### Ejemplo 1: Cambio de Ubicación
- **Tipo:** `PIVOTE`
- **Descripción:** Decisión de trasladar el local propuesto de la zona industrial a una ubicación céntrica en el casco histórico de Zaragoza.
- **Motivo:** Atraer a un mayor volumen de artesanos locales y clientes de paso, compensando el mayor coste de alquiler.
- **Preguntas/Secciones afectadas:** Sección de Operaciones (requisitos del local), Sección Jurídico-fiscal (licencias municipales específicas), Sección Económico-financiero (costes de alquiler y fianza).
- **Acción requerida:** Modificar las respuestas relativas al local y actualizar las hipótesis de costes recurrentes en el presupuesto.

### Ejemplo 2: Cambio de Cliente Objetivo
- **Tipo:** `PIVOTE`
- **Descripción:** Redefinición del segmento prioritario: pasar de enfocarse en aficionados del bricolaje a artesanos profesionales de media jornada.
- **Motivo:** Maximizar el valor de la suscripción mensual y reducir la tasa de rotación.
- **Preguntas/Secciones afectadas:** Sección de Estudio de Mercado (segmentación), Sección de Marketing y ventas (tarifas y estrategia de adquisición).
- **Acción requerida:** Ajustar la segmentación de la demanda y rediseñar los paquetes de precios.

### Ejemplo 3: Cambio de Inversión Inicial
- **Tipo:** `PIVOTE`
- **Descripción:** Reducción del presupuesto de inversión inicial un 30% mediante alquiler de maquinaria en vez de compra.
- **Motivo:** Restricción de financiación bancaria en el arranque del proyecto.
- **Preguntas/Secciones afectadas:** Sección Económico-financiero (plan de inversión, balance inicial, plan de tesorería), Sección de Operaciones (equipamiento y activos).
- **Acción requerida:** Actualizar la hoja de cálculo financiera y los apartados de inversión y financiación.

### Ejemplo 4: Cambio de Servicios de Fase 1
- **Tipo:** `PIVOTE`
- **Descripción:** Cancelación del servicio de cafetería integrada en Fase 1, posponiéndolo a la Fase 2.
- **Motivo:** Reducir la complejidad de licencias sanitarias y el coste de adecuación inicial del local.
- **Preguntas/Secciones afectadas:** Sección de Idea de Negocio (alcance de Fase 1), Sección de Operaciones (flujos de trabajo y licencias), Sección de Recursos Humanos (personal de barra).
- **Acción requerida:** Re-acotar el alcance en el modelo de negocio y eliminar el perfil de camarero del organigrama inicial.

### Ejemplo 5: Cambio de Forma Jurídica
- **Tipo:** `PIVOTE`
- **Descripción:** Cambiar la estructura propuesta de Cooperativa a Sociedad Limitada Unipersonal (SLU).
- **Motivo:** Agilizar los trámites de constitución y simplificar la toma de decisiones al inicio.
- **Preguntas/Secciones afectadas:** Sección Jurídico-fiscal (forma jurídica y trámites de constitución), Sección de Equipo Promotor (responsabilidad legal).
- **Acción requerida:** Reescribir el apartado de forma jurídica y actualizar los trámites en el cronograma de implantación.

### Ejemplo 6: Cambio de Modelo de Precios
- **Tipo:** `PIVOTE`
- **Descripción:** Transición de un modelo de pago por uso por horas a una suscripción mensual con tres tramos de acceso.
- **Motivo:** Incrementar la previsibilidad de los ingresos y asegurar la recurrencia.
- **Preguntas/Secciones afectadas:** Sección de Marketing y ventas (tarifas y comercialización), Sección Económico-financiero (hipótesis de ingresos).
- **Acción requerida:** Modificar la estructura tarifaria y los flujos de caja del modelo financiero.
