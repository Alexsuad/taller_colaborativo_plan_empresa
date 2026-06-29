# 06 — Fases oficiales del proyecto

Este documento define la estructura de gobierno y avance del proyecto en 4 fases oficiales de trabajo.

La fase operativa de organización y limpieza documental queda `CERRADA_OPERATIVAMENTE`. Eso significa que ya es suficiente para avanzar, pero no que el repositorio esté perfecto ni que se autorice la redacción final del plan. La revisión de skills, harnés, SDD, subagentes y sistema técnico queda para una fase posterior separada.

---

## FASE 1 — Negocio y documentación base

*   **Estado actual:** CERRADA_OPERATIVAMENTE (Gates 1A y 1B completados; Gate 1C operativo para continuar; Gate 1D bloqueado)
*   **Objetivo:** Consolidar la identidad del taller, la opción activa de negocio y el inventario de fuentes documentales reales.
*   **Entregables:**
    *   Contrato de identidad (`docs_control/00_contrato_identidad_negocio.md`).
    *   Opción activa (`docs_control/01_opcion_activa_taller.md`).
    *   Inventario de fuentes y manifiesto de uso permitido.
*   **Criterios de cierre:**
    *   Sub-gates 1A, 1B, 1C y 1D marcados como Completados en la gobernanza (Gate 1D abre la redacción).
    *   Ningún documento de identidad contiene contradicciones de negocio.
*   **Qué NO se hace:** No se redacta contenido del plan de empresa ni respuestas finales, ni se define arquitectura de compilación técnica. No incluye skills, harnés, SDD, subagentes ni sistema técnico.

---

## FASE 2 — Diseño del sistema/repositorio

*   **Estado actual:** Parcialmente avanzada (Gate Fase 2 en curso/pendiente)
*   **Objetivo:** Definir la estructura física y lógica del repositorio, mapeo de sedes de información, límites de extensión y diseño de validaciones de calidad.
*   **Entregables:**
    *   Matriz de preguntas-fuentes-vacíos.
    *   Mapa maestro de fases y plantillas metodológicas.
    *   Definición de límites de extensión (`limites_extension_plan_empresa.yml`).
*   **Criterios de cierre:**
    *   Gate Fase 2 marcado como Completado.
    *   Todos los vacíos de información identificados y asignados a decisiones pendientes.
*   **Qué NO se hace:** No se implementan scripts de producción final ni compilación definitiva. Sí se pueden crear o ajustar scripts de auditoría, saneamiento y validación estructural cuando estén autorizados y acotados por misión.

---

## FASE 3 — Implementación técnica del sistema

*   **Estado actual:** Bloqueada (Gate Fase 3 bloqueado)
*   **Objetivo:** Construir los scripts de compilación y las herramientas de validación deterministas capaces de auditar y consolidar el plan.
*   **Entregables:**
    *   Scripts de compilación, linealidad, formato y texto corrupto usables y alineados.
    *   Dossiers consolidados puente de soporte.
    *   Entorno de ejecución reproducible (`uv`, `.venv`).
*   **Criterios de cierre:**
    *   Gate Fase 3 marcado como Completado.
    *   Los scripts validadores devuelven PASS en las estructuras locales.
*   **Qué NO se hace:** **No se entrega el plan de empresa final.** Esta fase entrega el *sistema técnico capaz de producirlo*, pero no el consolidado editorial limpio.

---

## FASE 4 — Producción Editorial, Anexos y Cierre del Plan de Empresa

*   **Estado actual:** Bloqueada (Gate Fase 4 bloqueado)
*   **Objetivo:** Realizar la producción editorial final, maquetación, control de extensión crítico, inserción de gráficos/tablas y exportación limpia para evaluación externa.
*   **Entregables:**
    *   Consolidado limpio del Plan de Empresa (` plan_empresa_taller_colaborativo_completo.md`).
    *   Exportación oficial a formatos finales (DOCX final, PDF final).
    *   Anexos, tablas, gráficos y portada finalizados.
    *   Reporte final de auditoría de linealidad y formato en PASS absoluto.
*   **Criterios de cierre:**
    *   Gate Fase 4 marcado como Completado.
    *   Aprobación manual y firma de cierre de Alex.
*   **Qué NO se hace:** No se modifica la estrategia base del negocio ni se alteran las preguntas estructurantes del plan.

---

## Relación entre Fases

```mermaid
graph TD
    F1[Fase 1: Negocio y Doc Base] --> F2[Fase 2: Diseño del Sistema]
    F2 --> F3[Fase 3: Implementación Técnica]
    F3 -->|Sistema Listo| F4[Fase 4: Producción Editorial y Cierre]
```
La salida de cada fase sirve como gate obligatorio para la siguiente. El plan final listo para evaluación externa solo puede producirse y cerrarse en la Fase 4.
