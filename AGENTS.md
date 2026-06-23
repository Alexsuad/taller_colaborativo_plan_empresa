# AGENTS.md — Contrato operativo agéntico de taller_colaborativo_plan_empresa

## Propósito

Este repositorio de `taller_colaborativo_plan_empresa` está destinado a la organización documental y elaboración del plan de empresa del Taller Colaborativo Artesanal en Zaragoza.

Antigravity, Codex u otros asistentes de IA deben tratar este repositorio con extremo cuidado técnico y de gobernanza para evitar contaminar el contenido de negocio con datos de otros proyectos o antecedentes no vigentes o narrativas ajenas a la opción activa.

## Reglas Centrales de Comportamiento

1. **Anticontaminación Estricta:** Queda prohibido copiar respuestas, cifras, narrativas, modelos de negocio o estructuras de clientes de otros proyectos (como caso legacy no reutilizable como contenido o datos de clientes de otros proyectos o proyectos ajenos). La contaminación conceptual se vigila de forma determinista con `scripts/auditar_contaminacion_conceptual.py`, configurable en `config/contaminacion_conceptual.yml`.
2. **Uso de Herramientas del Entorno:** La gestión de Python y dependencias se realiza exclusivamente a través de `uv` (`python-uv-baseline`).
3. **Limpieza del Repositorio:** Se deben respetar las exclusiones de `.gitignore` para evitar subir basura o entornos virtuales al repositorio.
4. **Verificación Determinista:** Toda finalización de fase de redacción o cambio de estructura requiere la ejecución del script correspondiente (por ejemplo, `compilar_plan_empresa.py` o `auditar_estado_plan_empresa.py`).
5. **No Autoaprobación:** El agente propone soluciones y reportes, pero la decisión de promocionar fases o validar gates es exclusiva de Alex.
6. **Límite de Entrega Técnica en Fase 3:** Ningún agente o script puede declarar terminado el plan de empresa en Fase 3. El cierre del entregable final, la maquetación y la exportación limpia pertenecen exclusivamente a la Fase 4.
7. **Sede Agéntica Única:** Reglas, skills y workflows de los agentes viven en `.agents/`. Fuera de esa sede solo se referencia, no se replica. El estado de fases y gates es fuente única en `docs_control/03_gates_documentales.md` y el de sedes de información en `docs_control/05_sedes_informacion_plan_empresa.yml`.

## Inicio de Tarea

Antes de modificar archivos o redactar respuestas:
1. Revisar `docs_control/00_contrato_identidad_negocio.md` y `docs_control/01_opcion_activa_taller.md` para conocer los límites de negocio.
2. Identificar el alcance exacto autorizado en la solicitud.
3. Asegurarse de que no existan marcadores `[PENDIENTE]` o `Pendiente de completar` antes de proceder a la consolidación de un gate.

## Evidencia Mínima al Cerrar Tareas

Cada intervención técnica o de redacción del agente debe reportar al final de su ejecución:
- Lista de archivos modificados.
- Salida del comando de auditoría (`uv run python scripts/auditar_estado_plan_empresa.py`).
- Estado final (`completado`, `pendiente_de_aprobación`, `pendiente_de_validación`).
