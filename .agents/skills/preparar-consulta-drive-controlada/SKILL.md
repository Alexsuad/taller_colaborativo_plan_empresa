---
name: preparar-consulta-drive-controlada
description: Prepara consultas concretas, trazables y acotadas para Drive Taller bajo el flujo Drive Taller → Repositorio procesado → Alex → Web. No valida respuestas, no integra cambios y no sustituye revisión humana.
---

# Preparar consulta Drive controlada

## Propósito
Preparar consultas concretas, acotadas y trazables para la carpeta de Google Drive del Taller (como biblioteca documental primaria) cuando se necesita explorar borradores, insumos o material bruto para resolver una pregunta puntual del Plan de Empresa.

## Cuándo usarla
Usar esta skill cuando haga falta formular una consulta para:
- localizar un borrador o insumo de Drive;
- contrastar un hueco documental ya identificado;
- ordenar preguntas antes de una revisión humana;
- preparar una consulta reproducible a Drive Taller sin tocar el repositorio.
- devolver la respuesta al repositorio como evidencia trazable o como hipótesis pendiente de validación.

Si se requiere explorar o recuperar información de Drive Taller, se puede preparar la consulta.
Si una pregunta queda clasificada como `[F-DRIVE]` o `CON_BASE_DRIVE` con un hueco documental en Drive, preparar la consulta antes de escalar al usuario.

## Cuándo NO usarla
No usarla cuando:
- falte todavía una decisión de gobernanza;
- se quiera modificar el repo;
- se pretenda validar contenido de negocio final directamente (debe pasar por depuración);
- se necesite abrir Gate 1D;
- la consulta vaya a sustituir la revisión humana o auditoría documental.

## Entradas
- necesidad concreta de consulta;
- bloque, pregunta o hueco a revisar;
- contexto documental relevante;
- restricciones vigentes del repo;
- evidencia disponible que acota la consulta.

## Salidas
- consulta preparada y lista para Drive Taller;
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
- PREPARAR_CONSULTA_DRIVE
- NO_CONSULTAR_DRIVE
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
4. Confirmar primero si la necesidad debe consultarse en Drive Taller y luego contrastar con el repositorio procesado.
5. Redactar la consulta con una sola intención principal.
6. Aclarar qué no debe inferirse ni decidirse con la respuesta.
7. Dejar trazado el uso previsto de la respuesta.
8. Marcar revisión humana posterior antes de cualquier acción en el repo.

## Ejemplos
### Ejemplo 1: localizar una fuente en Drive
- Objetivo: encontrar el borrador de Drive donde se definió un coste local.
- Resultado esperado: consulta breve, con referencia a carpeta y documento.
- ESTADO_REPO: REPO_RESPONDE_SUFICIENTE.
- ARCHIVO_DEL_REPO_RELACIONADO: docs_control/03_gates_documentales.md.
- TIPO_DE_ACCION_POSIBLE: PREPARAR_CONSULTA_DRIVE.
- DECISION_POSTERIOR_REQUERIDA: REVISAR_HUMANO.
- DICTAMEN: PREPARAR_CONSULTA_DRIVE.

### Ejemplo 2: revisar un hueco de mercado
- Objetivo: confirmar si un borrador de Drive tiene testimonios de clientes locales.
- Resultado esperado: consulta acotada a una única pregunta.
- ESTADO_REPO: REPO_RESPONDE_PARCIAL.
- ARCHIVO_DEL_REPO_RELACIONADO: plan_empresa_guia/03_3_estudio_mercado.md.
- TIPO_DE_ACCION_POSIBLE: PREPARAR_CONSULTA_DRIVE.
- DECISION_POSTERIOR_REQUERIDA: REVISAR_HUMANO.
- DICTAMEN: PREPARAR_CONSULTA_DRIVE.

### Ejemplo 3: consulta demasiado abierta
- Objetivo: "analiza todo el Drive y dime qué falta".
- Resultado esperado: rechazo por exceso de alcance.
- ESTADO_REPO: REPO_RESPONDE_PARCIAL.
- ARCHIVO_DEL_REPO_RELACIONADO: docs_preparacion/00_mapa_maestro_preparacion_plan_empresa.md.
- TIPO_DE_ACCION_POSIBLE: NO_CONSULTAR_DRIVE.
- DECISION_POSTERIOR_REQUERIDA: REFORMULAR_Y_ACOTAR.
- DICTAMEN: CONSULTA_DEMASIADO_AMPLIA.

### Ejemplo 4: repo contradice la consulta
- Objetivo: pedir a Drive una conclusión de aforo que ya está fijada por normativa en el repo.
- Resultado esperado: rechazo por contradicción de estado.
- ESTADO_REPO: REPO_CONTRADICTORIO.
- ARCHIVO_DEL_REPO_RELACIONADO: docs_control/03_gates_documentales.md.
- TIPO_DE_ACCION_POSIBLE: NO_CONSULTAR_DRIVE.
- DECISION_POSTERIOR_REQUERIDA: ACLARAR_GOBERNANZA.
- DICTAMEN: NO_CONSULTAR_DRIVE.

## Criterio operativo de prioridad documental
- Drive Taller es la primera biblioteca documental a consultar.
- El repositorio procesado actúa como memoria estructurada y memoria del trabajo previo.
- Si Drive contiene material, se prepara la consulta y se depura en el repositorio de preparación, no se copia directamente.
- Si existe contradicción en Drive, se resuelve en `docs_preparacion/preguntas_resueltas/` antes de promover cambios.

## Criterio de cierre
La skill queda lista cuando la consulta:
- está acotada;
- es reproducible;
- no mezcla capas;
- no modifica el repositorio;
- deja claro qué se espera y qué no se espera de Drive Taller.

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
- no usar Drive Taller como texto final (está prohibido copiar y pegar directamente);
- no mezclar la consulta con ejecución de cambios.
- NotebookLM queda como apoyo secundario/histórico, no fuente prioritaria.
