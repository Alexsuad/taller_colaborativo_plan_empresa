---
description: Workflow para resolver preguntas de un capítulo del Plan de Empresa antes de redactar respuestas finales. Clasifica preguntas, valida fuentes y genera insumos saneados en docs_preparacion/preguntas_resueltas/<capitulo>/.
---

# Workflow: Procedimiento de Resolución de Preguntas por Capítulo

## 1. Propósito
El objetivo de este workflow es establecer el procedimiento operativo estándar para resolver las preguntas de cada capítulo de la guía del Plan de Empresa antes de proceder a la redacción final de las respuestas. Esto evita que anotaciones de control, preguntas al promotor, investigaciones previas, autorizaciones y análisis preliminares queden expuestos dentro del directorio definitivo `respuestas_plan_empresa/`.

---

## 2. Sedes Documentales y Gobernanza
Cada nivel de información tiene una sede documental exclusiva conforme a `docs_control/05_sedes_informacion_plan_empresa.yml`:

1.  **`plan_empresa_guia/`:** Sede de las preguntas guía oficiales del Plan de Empresa. Es únicamente de lectura.
2.  **`docs_preparacion/preguntas_resueltas/<capitulo>/`:** Sede obligatoria de la capa de preparación intermedia por capítulo. Contiene el análisis operativo previo, la matriz de resolución de preguntas y el insumo saneado correspondiente.
3.  **`respuestas_plan_empresa/`:** Sede exclusiva para las respuestas finales o casi finales limpias. No debe albergar lógica interna del agente ni control de procesos.

---

## 3. Estructura de Trabajo por Capítulo
Para procesar un capítulo, el agente debe generar secuencialmente los siguientes tres archivos intermedios en la carpeta de preparación de dicho capítulo antes de redactar en respuestas finales:

*   **`01_preguntas_extraidas.md`:** Listado limpio de preguntas reales necesarias para el capítulo.
*   **`02_matriz_resolucion_preguntas.md`:** Matriz de control, clasificación, fuentes y trazabilidad de cada pregunta extraída.
*   **`03_insumos_saneados.md`:** Documento de base que consolida hechos y decisiones técnicas depuradas antes de redactar.

Solo cuando se haya completado este proceso previo, y con la debida autorización de gate o fase, se podrá escribir o actualizar el archivo definitivo:
*   **`respuestas_plan_empresa/<capitulo>.md`**

---

## 4. Regla Madre de Limpieza
La carpeta `respuestas_plan_empresa/` **no es zona de pensamiento**. Queda estrictamente prohibido incluir en ella:
*   Preguntas operativas o procedimentales del tipo "Preguntar a Alex" o "Buscar en internet".
*   Notas de investigación o autorizaciones pendientes de búsqueda web.
*   Etiquetas o clasificaciones internas tales como `[I-SIMPLE]`, `[I-DEEP]`, `[U-VALIDA]`, `[U-ELIGE]`, `[U-AUTORIZA]`.
*   Anotaciones sobre estado de la fase, paquetes de preparación del agente o debates agénticos.

---

## 5. Extracción y Agrupación de Preguntas
*   **Foco en preguntas reales:** Deben extraerse únicamente las preguntas reales y accionables de la guía que exigen desarrollo analítico.
*   **Exclusión de bloques didácticos:** Se prohíbe explícitamente tratar como preguntas reales las secciones descriptivas, introductorias o didácticas de la guía, tales como:
    *   *"Preguntas para responder"*
    *   *"Explicación sencilla"*
    *   *"Qué parte del plan se rellena con esto"*
    *   *"Ejemplo útil / respuesta débil"*
    *   Instrucciones internas del documento de guía.
*   **Consolidación viable:** Si el volumen de preguntas es elevado (cientos de filas), se deben agrupar temáticamente por subsección de la guía para mantener la matriz operativa.

---

## 6. Clasificación de Preguntas Permitida
Toda pregunta en la matriz debe tener asignada una única clasificación principal usando este conjunto de etiquetas cerradas:
*   `[F-REPO]`: La respuesta ya está en documentos internos del repositorio.
*   `[F-NOTEBOOKLM]`: La respuesta está en fuentes indexadas en el cuaderno de NotebookLM.
*   `[I-SIMPLE]`: Requiere dato externo puntual y actualizado (tarifas, CNAE, dirección, licencias).
*   `[I-DEEP]`: Requiere investigación amplia o comparativa sectorial de mercado.
*   `[U-DATO]`: Solo el promotor (Alex) puede aportar el dato real.
*   `[U-VALIDA]`: Propuesta del agente que el promotor debe ratificar.
*   `[U-ELIGE]`: Opciones razonables donde el promotor debe tomar la decisión final.
*   `[M]`: Mixta (combina varias de las anteriores, requiriendo definir dependencias secundarias en su columna).
*   `[NO-RESPONDER-AÚN]`: Requiere datos futuros o fases posteriores no disponibles.

*Queda prohibido crear etiquetas personalizadas como `[F-REPO_NOTEBOOKLM]`.*

---

## 7. Estados Permitidos en la Matriz
Las preguntas de la matriz solo pueden adoptar los siguientes estados:
*   `CON_BASE` / `PARCIAL` / `PENDIENTE`
*   `REQUIERE_NOTEBOOKLM` / `REQUIERE_WEB_SIMPLE` / `REQUIERE_INVESTIGACION_PROFUNDA`
*   `REQUIERE_ALEX_DATO` / `REQUIERE_ALEX_VALIDACION`
*   `BLOQUEADA` / `NO_RESPONDER_AUN`
*   `LISTA_PARA_INSUMO_SANEADO`

---

## 8. Regla de Fuentes y Resguardo de NotebookLM
Antes de formular conclusiones de mercado, precios, competencia, operaciones o propuesta de valor, se debe priorizar la consulta a las fuentes del repositorio y de NotebookLM conforme a la regla `.agents/rules/02-no-inventar-fuentes.md`.

*   **Cuaderno NotebookLM Oficial:**
    *   **Nombre:** `Taller Colaborativo Zaragoza — Organización Documental Marketing`
    *   **ID:** `06898506-212a-4331-86b8-cf11901eb65d`
*   **Gobernanza ante indisponibilidad:** Si el acceso al cuaderno falla:
    1.  No asumir que no hay información.
    2.  Registrar el tag `NOTEBOOKLM_NO_DISPONIBLE`.
    3.  Trabajar con las fuentes y extracciones ya volcadas al repositorio (marcándolas como `FUENTES_REPO_DERIVADAS_NOTEBOOKLM` o similar).
    4.  Dejar los pendientes que requieran obligatoriamente el cuaderno en estado `REQUIERE_NOTEBOOKLM`.

---

## 9. Criterio de Consultas a Alex (Promotor)
*   **Filtro de autonomía:** No se debe preguntar a Alex sobre aspectos que puedan resolverse mediante análisis del repositorio, NotebookLM o búsquedas web.
*   **Uso estricto de etiquetas de usuario:** Las consultas al promotor (`[U-DATO]`, `[U-VALIDA]`, `[U-ELIGE]`) deben restringirse a decisiones estratégicas, validación de tarifas locales finales frente a costes del local o riesgos reales de la actividad comercial.

---

## 10. Criterios de Avance y Bloqueo Operativo

### El capítulo puede avanzar a respuestas finales si:
*   Todas las preguntas de la matriz tienen sus fuentes trazadas (e.g. `COMP-Fxxx`, `docs_preparacion/...`).
*   Los vacíos e incertidumbres locales están identificados en `03_insumos_saneados.md`.
*   El insumo saneado separa claramente hechos consolidados de asunciones pendientes de validar.
*   No hay contradicciones con las reglas de marcas y sedes.

### El proceso se bloquea si:
*   Se detecta inclusión de bloques didácticos tratados como preguntas reales.
*   Se genera una matriz inmanejable de cientos de filas por no agrupar preguntas.
*   Se aplican clasificaciones o estados no admitidos.
*   Se marca una pregunta como `CON_BASE` sin justificación ni fuente asociada.
*   Se simula consulta directa a NotebookLM estando inactivo.
*   Se intenta escribir en la carpeta definitiva `respuestas_plan_empresa/` sin haber generado previamente los insumos saneados en `docs_preparacion/`.
