---
name: preparar-consulta-notebooklm-controlada
description: Prepara consultas concretas, trazables y acotadas para NotebookLM bajo la regla repo primero / NotebookLM después. No valida respuestas, no integra cambios y no sustituye revisión humana.
---

# Preparar consulta NotebookLM controlada

## Propósito
Preparar consultas concretas, acotadas y trazables para NotebookLM cuando ya existe una base documental suficiente en el repositorio y se necesita explorar un hueco puntual sin mezclar capas ni convertir la consulta en decisión de contenido.

## Cuándo usarla
Usar esta skill cuando haga falta formular una consulta de apoyo para:
- localizar una fuente concreta;
- contrastar un hueco documental ya identificado;
- ordenar preguntas antes de una revisión humana;
- preparar una consulta reproducible para NotebookLM sin tocar el repositorio.

## Cuándo NO usarla
No usarla cuando:
- falte todavía una decisión de gobernanza;
- se quiera modificar el repo;
- se pretenda validar contenido de negocio como si fuera hecho;
- se necesite abrir Gate 1D;
- la consulta vaya a sustituir revisión humana o auditoría documental.

## Entradas
- necesidad concreta de consulta;
- bloque, pregunta o hueco a revisar;
- contexto documental relevante;
- restricciones vigentes del repo;
- evidencia disponible que acota la consulta.

## Salidas
- consulta preparada y lista para NotebookLM;
- alcance de la consulta;
- evidencia usada para acotarla;
- clasificación del estado del repo;
- archivo del repo relacionado;
- tipo de acción posible;
- decisión posterior requerida;
- límites explícitos de lo que no debe responderse;
- recomendación de revisión humana posterior.

## Formato de respuesta
CONSULTA_PROPUESTA:
OBJETIVO:
ALCANCE:
ESTADO_REPO:
ARCHIVO_DEL_REPO_RELACIONADO:
TIPO_DE_ACCION_POSIBLE:
DECISION_POSTERIOR_REQUERIDA:
EVIDENCIA_USADA:
LIMITES:
RIESGO_DE_CONTAMINACION:
REVISION_HUMANA_REQUERIDA: SI/NO
DICTAMEN:

Valores permitidos para `DICTAMEN`:
- PREPARAR_CONSULTA_NOTEBOOKLM
- NO_CONSULTAR_NOTEBOOKLM
- CONSULTA_DEMASIADO_AMPLIA
- FALTA_INFORMACION
- REQUIERE_DECISION_HUMANA

## Clasificación del estado del repo
- REPO_RESPONDE_SUFICIENTE
- REPO_RESPONDE_PARCIAL
- REPO_NO_RESPONDE
- REPO_CONTRADICTORIO

## Pasos obligatorios
1. Confirmar que la consulta nace de una necesidad concreta y no de una búsqueda abierta.
2. Identificar qué bloque o pregunta se quiere tratar.
3. Recoger solo la evidencia documental mínima necesaria.
4. Clasificar primero el estado del repo.
5. Redactar la consulta con una sola intención principal.
6. Aclarar qué no debe inferirse ni decidirse con la respuesta.
7. Dejar trazado el uso previsto de la respuesta.
8. Marcar revisión humana posterior antes de cualquier acción en el repo.

## Ejemplos
### Ejemplo 1: localizar una fuente concreta
- Objetivo: encontrar la fuente documental donde se definió una restricción.
- Resultado esperado: consulta breve, con referencia a carpeta y documento.
- ESTADO_REPO: REPO_RESPONDE_SUFICIENTE.
- ARCHIVO_DEL_REPO_RELACIONADO: docs_control/03_gates_documentales.md.
- TIPO_DE_ACCION_POSIBLE: PREPARAR_CONSULTA_NOTEBOOKLM.
- DECISION_POSTERIOR_REQUERIDA: REVISAR_HUMANO.
- DICTAMEN: PREPARAR_CONSULTA_NOTEBOOKLM.

### Ejemplo 2: revisar un hueco puntual
- Objetivo: confirmar si un bloque ya tiene respuesta documental o sigue pendiente.
- Resultado esperado: consulta acotada a una única pregunta.
- ESTADO_REPO: REPO_RESPONDE_PARCIAL.
- ARCHIVO_DEL_REPO_RELACIONADO: docs_control/reportes/PT-10O_sistema_repo_primero_notebooklm_despues.md.
- TIPO_DE_ACCION_POSIBLE: PREPARAR_CONSULTA_NOTEBOOKLM.
- DECISION_POSTERIOR_REQUERIDA: REVISAR_HUMANO.
- DICTAMEN: PREPARAR_CONSULTA_NOTEBOOKLM.

### Ejemplo 3: consulta demasiado abierta
- Objetivo: "analiza todo el plan y dime qué falta".
- Resultado esperado: rechazo por exceso de alcance.
- ESTADO_REPO: REPO_RESPONDE_PARCIAL.
- ARCHIVO_DEL_REPO_RELACIONADO: docs_control/reportes/PT-10K_blueprint_fase_2_sistema_agentico.md.
- TIPO_DE_ACCION_POSIBLE: NO_CONSULTAR_NOTEBOOKLM.
- DECISION_POSTERIOR_REQUERIDA: REFORMULAR_Y_ACOTAR.
- DICTAMEN: CONSULTA_DEMASIADO_AMPLIA.

### Ejemplo 4: repo contradice la consulta
- Objetivo: pedir a NotebookLM una conclusión ya bloqueada por el repo.
- Resultado esperado: rechazo por contradicción de estado.
- ESTADO_REPO: REPO_CONTRADICTORIO.
- ARCHIVO_DEL_REPO_RELACIONADO: docs_control/03_gates_documentales.md.
- TIPO_DE_ACCION_POSIBLE: NO_CONSULTAR_NOTEBOOKLM.
- DECISION_POSTERIOR_REQUERIDA: ACLARAR_GOBERNANZA.
- DICTAMEN: NO_CONSULTAR_NOTEBOOKLM.

## Criterio operativo del proyecto
Una skill no se crea por ocurrencia. Se planifica, se conecta con el negocio, se define con entradas y salidas, se usa para que la IA siga pasos constantes, se audita con checklist y se somete a revisión humana cuando afecta decisiones importantes.

## Criterio operativo del protocolo repo primero / NotebookLM después
- El repo responde primero.
- NotebookLM solo se consulta después de clasificar el estado del repo.
- Si el repo responde suficiente, la consulta se prepara solo para acotar o localizar.
- Si el repo responde parcial, se consulta solo el hueco residual.
- Si el repo no responde o contradice, no se consulta todavía.

## Criterio de cierre
La skill queda lista cuando la consulta:
- está acotada;
- es reproducible;
- no mezcla capas;
- no modifica el repositorio;
- deja claro qué se espera y qué no se espera de NotebookLM.

## Evidencia mínima
- objetivo concreto de la consulta;
- bloque o pregunta de origen;
- límites de la consulta;
- consulta final preparada;
- nota de revisión humana posterior.

## Prohibiciones
- no redactar contenido final del Plan de Empresa;
- no abrir Gate 1D;
- no tocar `respuestas_plan_empresa/`;
- no decidir negocio, marketing, legal, RRSS ni viabilidad;
- no convertir hipótesis en hechos;
- no usar NotebookLM como sustituto del repo;
- no mezclar la consulta con ejecución de cambios.
