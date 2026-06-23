# 07 — Mapa de reutilización del repositorio

**Estado:** Documento vivo. Debe actualizarse cuando se creen, eliminen o reclasifiquen carpetas, scripts, skills, gates, plantillas o documentos relevantes.  
**Propósito:** Diferenciar la capa reutilizable del repositorio de la capa específica del Taller Colaborativo, para que en el futuro pueda servir como base de arranque para otros planes de empresa sin arrastrar contenido sectorial, legal, comercial o estratégico del Taller.  
**Regla principal:** Este documento no convierte el repositorio actual en un framework general. Solo identifica qué partes podrían reutilizarse, limpiarse o extraerse más adelante.

## 1. Principio de separación

- **Capa reutilizable:** metodología, estructura, gates, scripts, skills, reglas, auditorías y plantillas.
- **Capa específica del Taller:** fuentes reales, decisiones de negocio, mercado Zaragoza, competencia, activos fijos, legalidad del taller, preguntas al promotor y contenido sectorial.
- **Capa futura opcional:** posible framework base si más adelante se decide extraer la metodología a otro repositorio.

## 2. Clasificación de carpetas actuales

| Ruta | Clasificación | Uso en este proyecto | Reutilización futura | Acción recomendada al clonar |
| ---- | ------------- | -------------------- | -------------------- | ---------------------------- |
| `.agents/` | REUTILIZABLE_CON_LIMPIEZA | Sede agéntica con reglas, skills y workflows del Taller | Sí, revisando menciones específicas del Taller | REVISAR_ANTES_DE_COPIAR |
| `.agents/skills/` | REUTILIZABLE_CON_LIMPIEZA | Skills operativas y de gobernanza del proyecto | Sí, pero revisando menciones, rutas, gates y reglas específicas del Taller | REVISAR_ANTES_DE_COPIAR |
| `config/` | REUTILIZABLE_CON_LIMPIEZA | Configuración de auditoría y reglas conceptuales | Sí, pero ajustando diccionarios y rutas | REVISAR_ANTES_DE_COPIAR |
| `scripts/` | REUTILIZABLE_CON_LIMPIEZA | Auditores, compiladores y validadores deterministas | Sí, con nombres, rutas y reglas adaptadas | REVISAR_ANTES_DE_COPIAR |
| `docs_control/` | REUTILIZABLE_CON_LIMPIEZA | Gobernanza, gates y decisiones del Taller | Sí, como esqueleto documental | COPIAR_COMO_PLANTILLA_VACIA |
| `docs_manifest/` | PLANTILLA_VACIABLE | Inventarios y clasificación de uso permitido | Sí, vaciando fuentes reales | COPIAR_COMO_PLANTILLA_VACIA |
| `docs_organizacion/` | PLANTILLA_VACIABLE | Inventario, matriz y revisión crítica del Taller | Sí, como estructura diagnóstica | COPIAR_COMO_PLANTILLA_VACIA |
| `plan_empresa_guia/` | REUTILIZABLE_CON_LIMPIEZA | Preguntas base de Red ARCE y estructura del plan | Sí, limpiando referencias específicas | REVISAR_ANTES_DE_COPIAR |
| `respuestas_plan_empresa/` | PLANTILLA_VACIABLE | Respuestas del Taller, aún bloqueadas | Sí, solo como estructura vacía | COPIAR_COMO_PLANTILLA_VACIA |
| `docs_consolidados/` | NO_REUTILIZAR_CONTENIDO | Dossiers consolidados del Taller | Solo estructura si algún día procede, nunca contenido | NO_COPIAR_CONTENIDO |
| `docs_fuentes/` | NO_REUTILIZAR_CONTENIDO | Fuentes reales del Taller y material asociado | No copiar como contenido entre proyectos | NO_COPIAR_CONTENIDO |
| `_build/` | OUTPUT_GENERADO | Entregables y reportes generados | No se reutiliza como base documental | REGENERAR |
| `artifact_manifest.yml` | REUTILIZABLE_CON_LIMPIEZA | Trazabilidad de artefactos del repo | Sí, como plantilla de control | REVISAR_ANTES_DE_COPIAR |
| `repo_identity.yml` | REUTILIZABLE_CON_LIMPIEZA | Identidad operativa y estado global del repositorio | Sí, reescribiéndolo para el nuevo proyecto | COPIAR_Y_RENOMBRAR |
| `AGENTS.md` | REUTILIZABLE_CON_LIMPIEZA | Contrato operativo de agentes del repositorio | Sí, limpiando nombres y referencias del Taller | REVISAR_ANTES_DE_COPIAR |
| `README.md` | REUTILIZABLE_CON_LIMPIEZA | Presentación general del proyecto activo | Sí, como base de arranque | COPIAR_Y_RENOMBRAR |

## 3. Qué se puede reutilizar como base

- lógica de gates documentales;
- registro de decisiones;
- inventario de fuentes;
- matriz guía → fuentes → vacíos;
- revisión crítica de vacíos;
- reglas de anticontaminación;
- auditor conceptual;
- auditor de estado del plan;
- skills agénticas;
- separación entre fuentes, organización, respuestas, consolidados y output;
- protocolo de no redactar antes de completar gates.

## 4. Qué no debe reutilizarse como contenido

- fuentes reales del Taller;
- análisis de mercado de Zaragoza;
- competencia del coworking artesanal/carpintería;
- activos fijos y maquinaria del Taller;
- decisiones estratégicas del Taller;
- preguntas personales del promotor;
- validaciones legales/financieras específicas;
- cualquier texto redactado para el plan del Taller;
- outputs generados en `_build/`.

## 5. Cómo clonar este repositorio para un futuro proyecto

1. Copiar estructura base.
2. Vaciar o sustituir fuentes específicas.
3. Reescribir `repo_identity.yml`.
4. Reescribir `README.md`.
5. Reiniciar registro de decisiones o marcarlo como histórico no transferible.
6. Vaciar inventarios, matrices y revisiones críticas.
7. Adaptar reglas de contaminación conceptual.
8. Revisar skills y scripts.
9. Regenerar `_build/`.
10. No comenzar a redactar hasta completar gates equivalentes.

## 6. Mantenimiento del mapa

Este documento se actualizará cuando:

- se cree una nueva carpeta;
- se cree un nuevo script;
- se cree una nueva skill;
- se cambie la función de una carpeta;
- se creen plantillas reutilizables;
- se incorporen fuentes reales;
- se produzcan outputs finales;
- se decida extraer un framework base en el futuro.

| Fecha | Cambio en el repo | Impacto en reutilización | Acción sobre este mapa |
| ----- | ----------------- | ------------------------ | ---------------------- |
| 2026-06-23 | Creación del primer mapa de reutilización. | Se separa conceptualmente la capa metodológica reusable de la capa específica del Taller. | Crear versión inicial mantenible. |

## 7. Estado recomendado

- El repositorio sigue siendo el repositorio activo del Taller Colaborativo.
- No se convierte todavía en framework general.
- La reutilización futura queda documentada.
- La redacción del plan sigue bloqueada por Gate 1D.
- Gate 1C sigue EN CURSO.
- Este documento no autoriza mover, borrar ni copiar archivos.
