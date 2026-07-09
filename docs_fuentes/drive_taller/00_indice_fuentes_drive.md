# 00_indice_fuentes_drive — Copia local de Drive Taller

## Propósito

Esta carpeta contiene una copia local de trabajo de documentos procedentes de Google Drive Taller.

Su función es permitir que Antigravity y los validadores lean fuentes documentales sin depender de conexión directa a Google Drive.

## Regla principal

Estos documentos son fuente bruta o semibruta.

No se deben copiar directamente a `respuestas_plan_empresa/`.

Todo contenido debe pasar por:

Drive local → extracción → clasificación → depuración → contraste → grado de certeza → insumos saneados → redacción controlada.

## Inventario de fuentes locales

> [!NOTE]
> Todos los archivos de Drive están almacenados en una estructura plana en esta carpeta (`docs_fuentes/drive_taller/`). La clasificación lógica y la resolución por capítulos no se realiza moviendo físicamente estos archivos, sino mediante las capas de trabajo y matrices de resolución ubicadas en `docs_preparacion/preguntas_resueltas/<capitulo>/`.

| Nº | Fuente                                                                        | Carpeta sugerida             | Qué trata / uso                                                                                                                                                                           |
| -: | ----------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  1 | **Taller Colaborativo Artesanal.pdf**                                         | `01_origen_historia_equipo/` | Documento narrativo de origen del proyecto. Explica la necesidad de un espacio para aprender, practicar y trabajar oficios sin taller propio. Útil para motivación, problema y propósito. |
|  2 | **La historia detrás del Taller Colaborativo Artesanal.pdf**                  | `01_origen_historia_equipo/` | Relato más personal del origen, motivación y problema vivido. Sirve para explicar por qué nace el proyecto, pero debe limpiarse si usa nombres o enfoques antiguos.                       |
|  3 | **Chat Analisis documentacion**                                               | `99_otros/`                  | Conversación/auditoría documental antigua. Contiene análisis útil, pero también contaminación de Claudia Bautista. No debe usarse como fuente final sin depuración. [CONTAMINACIÓN_HISTÓRICA_NO_VIGENTE] |
|  4 | **Auditoría Documental Taller Colaborativo**                                  | `99_otros/`                  | Auditoría de fuentes, estructura y vacíos documentales. Útil como control metodológico, pero contiene menciones legacy a Claudia Bautista. Debe sanearse. [CONTAMINACIÓN_HISTÓRICA_NO_VIGENTE] |
|  5 | **Copia de Canvas Proyecto.pdf**                                              | `02_modelo_negocio_canvas/`  | Canvas inicial del proyecto: propuesta de valor, actividades, clientes, recursos, ingresos e impacto. Fuente base para modelo de negocio.                                                 |
|  6 | **Modelo operativo y de negocio híbrido**                                     | `02_modelo_negocio_canvas/`  | Define el modelo híbrido: cursos, taller compartido, servicios, materiales, comunidad y operación. Fuente clave para oferta y líneas de ingreso.                                          |
|  7 | **03_Mapa de temas y subtemas del plan de empresa**                           | `99_otros/`                  | Mapa metodológico del plan. No es contenido final, sino guía para saber qué buscar, clasificar y responder en cada capítulo.                                                              |
|  8 | **Fatiga Digital**                                                            | `06_marketing_marca/`        | Fuente secundaria sobre desconexión digital, vuelta a actividades manuales y necesidad de experiencias tangibles. Útil como tendencia, no como eje principal.                             |
|  9 | **Estudio Comparativo Coworking madera.pdf**                                  | `03_mercado_competencia/`    | Benchmark de La Corporación Taller, A Tu Madera y Cara y Canto. Fuente clave para `03_4_benchmarking_inspiradores.md`.                                                                    |
| 10 | **Análisis Competitivo Coworking Madera Aragón**                              | `03_mercado_competencia/`    | Análisis competitivo local/regional: Zaragoza, Aragón, actores, huecos, alternativas y alianzas. Fuente base para competencia.                                                            |
| 11 | **Investigación avanzada sobre un coworking artesanal de madera en Zaragoza** | `03_mercado_competencia/`    | Investigación amplia sobre viabilidad, competencia, referentes y oportunidad en Zaragoza. Útil para mercado, competencia y modelo.                                                        |
| 12 | **Chat01_Competencia**                                                        | `03_mercado_competencia/`    | Conversación larga de análisis competitivo. Útil como insumo bruto, pero contiene contaminación legacy con Claudia y otros proyectos. Revisar antes de usar. [CONTAMINACIÓN_HISTÓRICA_NO_VIGENTE] |
| 13 | **03_2 Competencia y alternativas**                                           | `03_mercado_competencia/`    | Borrador/capítulo ya trabajado sobre competencia, sustitutos, referentes y huecos competitivos. Debe tratarse como respuesta del plan, no fuente bruta.                                   |
| 14 | **Documento sin título**                                                      | `03_mercado_competencia/`    | Es un borrador controlado de `03_2_competencia_y_alternativas.md`, con mapa de fuentes y actores. Parece duplicado de trabajo frente al `03_2` actual.                                    |
| 15 | **03_3_estudio_mercado.md**                                                   | `03_mercado_competencia/`    | Borrador/capítulo de estudio de mercado: clientes, segmentos, demanda y validación. Debe sanearse por hipótesis no confirmadas.                                                           |
| 16 | **03_4. Benchmarking de inspiradores clave**                                  | `03_mercado_competencia/`    | Capítulo de benchmarking de La Corporación Taller, A Tu Madera y Cara y Canto. Debe conservarse, pero sin mezclar análisis interno.                                                       |
| 17 | **03_1 Análisis externo**                                                     | `03_mercado_competencia/`    | Borrador/capítulo de entorno externo: Zaragoza, contexto social, económico, legal, ambiental y formativo. Alimenta DAFO.                                                                  |
| 18 | **03_5 Análisis interno**                                                     | `01_origen_historia_equipo/` | Borrador/capítulo de capacidades internas, equipo, recursos, límites y riesgos internos. Debe revisarse por datos que solo tú puedes confirmar.                                           |
| 19 | **04_DAFO / CAME**                                                            | `99_otros/`                  | Capítulo estratégico que sintetiza fortalezas, debilidades, oportunidades y amenazas. Depende de que 03_1 a 03_5 estén saneados.                                                          |
| 20 | **05_objetivos_lineas_estrategicas**                                          | `99_otros/`                  | Capítulo de objetivos, líneas estratégicas y fases. Debe revisarse porque puede contener plazos e indicadores como hipótesis.                                                             |
| 21 | **6.0. Marca, comunicación y naming**                                         | `06_marketing_marca/`        | Versión anterior del capítulo de marca/naming. Posible duplicado de `06_0_marca_comunicacion_naming.md`.                                                                                  |
| 22 | **06_0_marca_comunicacion_naming.md**                                         | `06_marketing_marca/`        | Versión nueva del capítulo de marca, comunicación y naming. Debe ser la versión preferente si se sanea.                                                                                   |
| 23 | **6.1. Plan de marketing, comunicación y ventas**                             | `06_marketing_marca/`        | Versión anterior del plan de marketing/ventas. Posible duplicado de `06_1_marketing_ventas.md`.                                                                                           |
| 24 | **06_1_marketing_ventas.md**                                                  | `06_marketing_marca/`        | Versión nueva del plan de marketing y ventas. Requiere sanear hipótesis comerciales no confirmadas.                                                                                       |
| 25 | **06_2_operaciones**                                                          | `04_operaciones_legal/`      | Capítulo operativo: servicios, niveles de usuario, reservas, maquinaria, seguridad, almacenamiento y fases. Contiene muchas hipótesis a validar.                                          |
| 26 | **06_3_recursos_humanos**                                                     | `01_origen_historia_equipo/` | Capítulo de roles, dedicación, apoyos externos y organización humana. Muy sensible: debe marcar como pendiente lo que dependa de ti.                                                      |
| 27 | **06_4 Plan jurídico-fiscal**                                                 | `04_operaciones_legal/`      | Capítulo legal/fiscal: forma jurídica, licencias, seguros, contratos, RGPD, fiscalidad y riesgos. Debe validarse con gestoría/técnico.                                                    |
| 28 | **Forma jurídica recomendada**                                                | `04_operaciones_legal/`      | Documento específico sobre forma jurídica. Sirve como insumo legal, pero no debe imponerse sin confirmar socios, riesgos y fiscalidad.                                                    |
| 29 | **BORRADOR DE ACUERDO DE SOCIOS**                                             | `04_operaciones_legal/`      | Borrador de pacto o acuerdo entre socios. Muy sensible: requiere revisión jurídica y confirmar quiénes son realmente socios.                                                              |
| 30 | **Taller Artesanal: Viabilidad y Marco Legal**                                | `04_operaciones_legal/`      | Informe de viabilidad estratégica, legal y operativa. Útil para permisos, precios, riesgos, fases y marco normativo.                                                                      |
| 31 | **Taller Artesanal Zaragoza_ Guía Completa.docx**                             | `04_operaciones_legal/`      | Guía amplia sobre montar taller artesanal en Zaragoza. Puede contener legal, mercado, operación y fiscalidad. Usar como fuente de apoyo, no como verdad final.                            |
| 32 | **Copia de Plan Económico-Financiero COWORKING.xlsx**                         | `05_finanzas/`               | Hoja económica-financiera preliminar. Es la base financiera, pero falta información crítica confirmada por ti.                                                                            |
| 33 | **6.5. Monetización, fijación de precios**                                    | `05_finanzas/`               | Documento anterior sobre precios, monetización e ingresos. No debe usarse como plan financiero final; sirve como hipótesis.                                                               |
| 34 | **Copia de Guía elaboración del Plan de Negocio (Red ARCE) 09.04.2018.docx**  | `99_otros/`                  | Guía general para elaborar planes de negocio. Es metodología externa, no fuente específica del proyecto. Útil como plantilla de control.                                                  |


## Advertencia de contaminación documental

Claudia Bautista no forma parte del proyecto vigente.

Si aparece en documentos antiguos, debe tratarse como información histórica no vigente / contaminación documental y no como integrante actual del equipo promotor.

### Fuentes con contaminación histórica identificadas

Las siguientes fuentes contienen menciones u organización basada en el equipo no vigente (incluyendo a Claudia Bautista) y deben ser tratadas con cautela o saneadas en su correspondiente matriz de preparación:
- `Auditoría Documental Taller Colaborativo.docx` (Nº 4 en el inventario)
- `Chat Analisis documentacion.docx` (Nº 3 en el inventario)
- `Chat01_Competencia.docx` (Nº 12 en el inventario)
