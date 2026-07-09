# Workflow para Resolución de Preguntas por Capítulo

Este flujo sirve para preparar, depurar y resolver las preguntas del Plan de Empresa antes de iniciar la redacción final, basándose en la biblioteca de Google Drive Taller como fuente primaria.

---

## 1. Secuencia Operativa de Fuentes

El sistema debe resolver las preguntas en este orden estricto de fuentes:
1. **Revisar Drive Taller**: Consultar borradores, notas e insumos en la carpeta de Google Drive.
2. **Revisar Repositorio Procesado**: Consultar fichas `COMP-Fxxx`, `docs_control/` y memoria previa.
3. **Clasificar rol de Alex**: Determinar si requiere un dato único, validación o elección de Alex.
4. **Clasificar si requiere web simple**: Para datos normativos, CNAE o tarifas públicas sencillas.
5. **Clasificar si requiere investigación profunda**: Para estudios amplios del sector.
6. **Crear Insumos Saneados**: Generar el diagnóstico consolidado en `docs_preparacion/`.
7. **Redactar**: Escribir la propuesta de capítulo en `respuestas_plan_empresa/` solo cuando exista base suficiente y Gate 1D parcial esté habilitado.

---

## 2. Clasificación de Preguntas Permitida
Toda pregunta en la matriz de preparación debe clasificarse con una de estas etiquetas cerradas:
*   `[F-REPO]`: La respuesta ya está en documentos internos del repositorio.
*   `[F-DRIVE]`: La respuesta está en la biblioteca de Google Drive Taller.
*   `[I-SIMPLE]`: Requiere dato externo puntual y actualizado (tarifas, CNAE, dirección).
*   `[I-DEEP]`: Requiere investigación amplia o comparativa sectorial de mercado.
*   `[U-DATO]`: Solo el promotor (Alex) puede aportar el dato real.
*   `[U-VALIDA]`: Propuesta del agente que el promotor debe ratificar.
*   `[U-ELIGE]`: Opciones razonables donde el promotor debe tomar la decisión final.
*   `[M]`: Mixta (combina varias, requiriendo detallar en observaciones).
*   `[NO-RESPONDER-AÚN]`: Requiere datos futuros o fases posteriores no disponibles.

*Queda prohibido crear etiquetas personalizadas.*

---

## 3. Estados Permitidos en la Matriz
Las preguntas de la matriz solo pueden adoptar los siguientes estados:
*   `CON_BASE_DRIVE` / `CON_BASE_REPO` / `PARCIAL` / `PENDIENTE`
*   `REQUIERE_DRIVE` / `REQUIERE_WEB_SIMPLE` / `REQUIERE_INVESTIGACION_PROFUNDA`
*   `REQUIERE_ALEX_DATO` / `REQUIERE_ALEX_VALIDACION`
*   `BLOQUEADA` / `NO_RESPONDER_AUN`
*   `LISTA_PARA_INSUMO_SANEADO`

---

## 4. Regla de Fuentes y Resguardo de Drive Taller
Antes de formular conclusiones, se debe consultar primero la carpeta de Google Drive del Taller.
- **URL Carpeta Drive**: https://drive.google.com/drive/folders/1tYj8zsKhIqYkN7GdsKr1VWdw06pbFWcR
- **Regla anti-copia**: Está prohibido copiar y pegar directamente contenido bruto de Drive en las respuestas finales. Todo debe ser depurado, contrastado y resumido en la fase de insumos saneados.
- **Gobernanza ante indisponibilidad:** Si el acceso a Drive falla:
    1.  Registrar el tag `DRIVE_NO_DISPONIBLE`.
    2.  Trabajar con las fuentes y extracciones ya volcadas al repositorio.
    3.  Dejar los pendientes que requieran la carpeta de Drive en estado `REQUIERE_DRIVE`.
- **Apoyo secundario**: NotebookLM queda únicamente para apoyo secundario o histórico (legacy).

---

## 5. Capítulos Diferidos al Final
Estos capítulos no deben desarrollarse de forma prioritaria en la fase actual, salvo para registrar dependencias, por estar subordinados a números y decisiones de viabilidad finales:
*   `00_resumen_ejecutivo`
*   `06_5_economico_financiero`
*   `07_implantacion_puesta_marcha`
*   `08_viabilidad_conclusiones`

---

## 6. Criterio de Consultas a Alex (Promotor)
*   **Filtro de autonomía:** No preguntar a Alex sobre aspectos que puedan resolverse mediante análisis de Drive Taller, repositorio o búsquedas web.
*   **Propuestas preparadas:** Presentar propuestas o alternativas cerradas para validar, evitando preguntas abiertas o en blanco siempre que sea posible.
