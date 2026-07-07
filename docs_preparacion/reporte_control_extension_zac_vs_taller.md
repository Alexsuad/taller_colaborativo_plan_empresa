# Reporte — Control de extensión y calidad editorial ZAC vs Taller

## 1. Alcance
Este reporte analiza los mecanismos de control de extensión, profundidad y calidad editorial aplicados en el proyecto de referencia `zac_plan_empresa` como guía metodológica, comparándolos con el estado actual del repositorio `taller_colaborativo_plan_empresa` para proponer un presupuesto documental adaptado al Taller Colaborativo Artesanal en Zaragoza (CCA). Este análisis se realiza con fines estrictamente metodológicos y no implica copiar contenido sectorial de ZAC.

## 2. Qué controlaba ZAC
El proyecto ZAC disponía de un control determinista y normativo compuesto por:
*   **`docs_control/politica_extension_plan_empresa.md`:** Define las métricas globales del plan (objetivo ideal: 50 páginas, bloqueo de entrega: >70 páginas, y un ratio estándar de 300 palabras por página).
*   **`docs_control/limites_extension_plan_empresa.yml`:** Fija límites duros de palabras por archivo (warning normal a 1800 palabras, fail a 2500 palabras) con excepciones explícitas para marketing (3500), económico-financiero (3500) y estudio de mercado (3000).
*   **`.agent/rules/05-linealidad-documental.md`:** Exige redactar con perspectiva de "capítulo único" (sin repetir intros ni resúmenes del proyecto), respetar sedes oficiales de información y emplear referencias cruzadas.
*   **`scripts/auditar_linealidad_plan_empresa.py`:** Script determinista que calcula palabras netas por archivo (ignorando notas internas e inventarios de datos) y analiza la duplicidad de párrafos (alerta si la similitud supera el 88%).

## 3. Qué controla actualmente Taller
El repositorio de Taller dispone de:
*   **`docs_control/05_sedes_informacion_plan_empresa.yml`:** Organiza dónde deben vivir los datos y prohíbe que en respuestas finales conviva el pensamiento o investigación.
*   **`.agents/rules/02-no-inventar-fuentes.md`:** Obliga a basar conclusiones de mercado exclusivamente en hechos internos del repo o del cuaderno de NotebookLM.
*   **`.agents/workflows/resolucion-preguntas-por-capitulo.md`:** Garantiza la separación física entre la capa de preparación y el resultado definitivo.
*   *Brecha:* Actualmente no existen límites mínimos ni máximos de palabras, no se cuantifica la densidad ni profundidad de las respuestas, y no se controla de forma automática la linealidad del entregable final.

## 4. Brecha detectada
El problema en Taller se traduce en **respuestas limpias pero superficiales** (pobres en datos, análisis y extensión). Las herramientas de Taller validan eficazmente la ausencia de contaminación (tags internos y notas de agente), pero carecen de métricas para forzar la profundidad y evitar el texto infra-desarrollado. Falta una directriz que cuantifique el "presupuesto documental" esperado y defina qué volumen de análisis debe integrarse en el cuerpo de cada capítulo frente a los anexos de detalle técnico.

## 5. Propuesta mínima de mejora
Se propone implementar una solución en tres partes:
1.  **Presupuesto Documental:** Crear `docs_control/presupuesto_documental_plan_empresa.yml` para fijar límites de palabras mínimos, objetivos y máximos por capítulo.
2.  **Ajuste de Skill de Redacción:** Modificar `.agents/skills/redactar-capitulo-plan-empresa-controlado/SKILL.md` para exigir el cumplimiento del presupuesto documental y la perspectiva de capítulo único.
3.  **Script de Verificación:** Crear `scripts/verificar_extension_linealidad.py` para automatizar la medición de palabras y la detección de contenido repetitivo.
*   *Qué NO crear:* No crear nuevas skills ni duplicar las políticas generales de control de ZAC.

## 6. Presupuesto documental preliminar sugerido

| Tipo de capítulo | Palabras objetivo | Mínimo aceptable | Máximo razonable | Qué debe ir al cuerpo | Qué debe ir a anexos | Observaciones |
| :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **Resumen ejecutivo** | 600 | 450 | 800 | Síntesis de propuesta, promotor, mercado y cifras clave. | No aplica | Se redacta al final. |
| **Equipo promotor** | 800 | 500 | 1200 | Perfiles, habilidades y vacíos formativos. | CVs detallados | Foco en capacidades de oficio. |
| **Idea de negocio** | 1200 | 800 | 1800 | Propuesta híbrida, catálogo MVP y layout preliminar. | Especificaciones técnicas | Exclusión explícita de CNC. |
| **Mercado / análisis externo** | 1500 | 1000 | 2200 | Análisis PESTEL local, licencias y competidores indirectos. | Estudios censales completos | Foco en Zaragoza. |
| **Benchmarking** | 1800 | 1200 | 2500 | Análisis detallado de los 3 referentes y patrones adaptados. | Fichas COMP-Fxxx completas | Base operativa de Fase 1. |
| **DAFO / CAME** | 1000 | 700 | 1500 | Matriz DAFO y planes de acción resultantes. | No aplica | Cruce explícito de variables. |
| **Objetivos** | 600 | 400 | 900 | Metas estratégicas comerciales y de aforo. | No aplica | Coherencia con mercado. |
| **Marketing y ventas** | 2000 | 1500 | 3000 | Canales de captación, bonos de horas y embudo de alumnos. | Tarifarios detallados | Clave para monetización. |
| **Operaciones** | 2000 | 1400 | 3000 | Plan de maquinaria convencional, seguridad, limpieza y accesos. | Layout a escala | Núcleo del taller físico. |
| **RRHH** | 900 | 600 | 1400 | Perfil del operario de taller y costes de contratación. | Convenios oficiales | Convenio Madera/Aragón. |
| **Jurídico-fiscal** | 800 | 500 | 1200 | Forma de sociedad elegida y trámites de apertura. | Formularios oficiales | Autónomo vs S.L. |
| **Económico-financiero** | 2500 | 1500 | 3500 | Supuestos de ingresos/gastos, flujos de caja y VAN/TIR. | Hojas de cálculo auxiliares | **Fase Financiera Especial**. |
| **Implantación** | 800 | 500 | 1200 | Cronograma de hitos críticos y dependencias físicas. | No aplica | Ruta crítica de apertura. |
| **Viabilidad** | 1000 | 600 | 1500 | Conclusiones cualitativas y de riesgo del proyecto. | No aplica | Se nutre del financiero. |

## 7. Recomendación de implementación
En la siguiente misión, se recomienda:
1.  Crear el archivo de límites de presupuesto `docs_control/presupuesto_documental_plan_empresa.yml` basado en la tabla preliminar.
2.  Ampliar la regla `.agents/rules/02-no-inventar-fuentes.md` con un apartado dedicado a la linealidad, prohibiendo las introducciones genéricas repetitivas en cada capítulo.
