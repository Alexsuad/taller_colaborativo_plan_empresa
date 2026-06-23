# 07 — Propuesta de inventario puente de fuentes externas reales

> **Estado documental:** ABSORBIDO  
> **Sede activa:** `docs_organizacion/01_inventario_fuentes.md`  
> **Decisión relacionada:** DEC-010.  
> **Uso permitido:** consulta histórica de propuesta puente.  
> **Uso prohibido:** no usar como inventario vigente ni como instrucción de importación de fuentes.


**Estado:** Consolidado con `01_inventario_fuentes.md` — Este documento se mantiene como puente hacia fuentes externas reales. La sede única del inventario autorizado es `docs_organizacion/01_inventario_fuentes.md`.
**Fase:** Fase 1.1.C — Inventario puente de fuentes externas reales.
**Fecha:** 2026-06-22.
**Actualización:** 2026-06-23 — Marcado como consolidado (DEC-010).
**Autoría de contenido:** Orquestador del proyecto / ChatGPT, para revisión humana.
**Rol de Codex/Antigravity:** ejecución técnica, pegado de contenido, verificación de rutas y auditoría.
**Alcance:** Fuentes reales disponibles fuera de `docs_fuentes/` que podrían poblar el repositorio en una fase posterior.
**Restricción aplicada:** Este documento no autoriza mover, copiar, renombrar, eliminar ni importar fuentes reales.

> [!IMPORTANT]
> Este documento no sustituye a `docs_organizacion/01_inventario_fuentes.md`.
> El inventario final y autorizado seguirá siendo `docs_organizacion/01_inventario_fuentes.md` cuando Alex apruebe qué fuentes se importan, cuáles se descartan y con qué reglas de uso.

> [!NOTE]
> `docs_organizacion/06_propuesta_inventario_general_fuentes.md` se mantiene como diagnóstico técnico del repo madre y de sus placeholders vacíos.
> Este documento `07` funciona como puente entre ese diagnóstico y las fuentes externas reales ya disponibles en el entorno de trabajo del proyecto.

> [!WARNING]
> Este documento no autoriza crear carpetas nuevas. Todas las rutas destino deben coincidir con la estructura vigente de `docs_fuentes/`.

---

## 1. Objetivo

Preparar una propuesta ordenada para identificar fuentes externas reales disponibles antes de poblar `docs_fuentes/`.

Esta propuesta permite decidir después:

* qué fuentes importar primero;
* en qué carpeta de `docs_fuentes/` deberían quedar;
* qué fuentes solo deben usarse como referencia;
* qué fuentes requieren verificación externa antes de alimentar respuestas del plan;
* qué fuentes históricas deben quedar en legacy para evitar contaminación del modelo urbano Zaragoza;
* qué fuentes metodológicas sirven para ordenar el trabajo, pero no para redactar contenido de negocio;
* qué fuentes legales sirven como checklist preliminar, pero no sustituyen verificación normativa o profesional.

---

## 2. Estructura vigente de `docs_fuentes/`

La estructura oficial vigente es:

```text
docs_fuentes/
  01_base_metodologica/
  02_identidad_origen/
  03_competencia_benchmarking/
  04_mercado_tendencias/
  05_zaragoza_aragon/
  06_legal_operativo/
  07_instalaciones_local_producto/
  08_seguridad_responsabilidad_usuarios/
  09_finanzas_activos/
  10_ayudas_financiacion/
  11_legacy_no_usar_directo/
```

Cualquier documento, agente o script que use rutas distintas debe corregirse antes de importar fuentes reales.

---

## 3. Criterios usados

### 3.1 Estados documentales

| Estado                           | Significado operativo                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------- |
| Fuente real con contenido        | Archivo existente con texto, datos, tabla, PDF, DOCX, XLSX o investigación aprovechable.     |
| Placeholder vacío                | Archivo o ubicación prevista sin contenido real. No debe alimentar el plan.                  |
| Fuente histórica                 | Documento útil para entender origen, pero no válido como base directa del modelo vigente.    |
| Benchmark operativo              | Referente de competencia, precios, servicios, operación o comunidad.                         |
| Fuente legal/normativa           | Documento sobre licencias, permisos, seguridad, forma jurídica, normativa o responsabilidad. |
| Estudio de mercado               | Fuente con datos o metodología sobre demanda, tendencias, sector artesanal o clientes.       |
| Fuente financiera                | Fuente sobre activos, inversión, CAPEX/OPEX, precios, ingresos o estructura económica.       |
| Fuente de ayudas o convocatorias | Documento sobre subvenciones, incentivos, financiación pública o programas.                  |
| Fuente metodológica              | Guía, plantilla, plan ejemplo, aprendizaje o regla de trabajo.                               |

### 3.2 Escala de riesgo de contaminación

| Riesgo  | Criterio                                                                                                                                                        |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bajo    | Puede usarse con pocas restricciones, citando origen y verificando vigencia cuando aplique.                                                                     |
| Medio   | Útil, pero mezcla hipótesis, análisis no verificado o datos que deben contrastarse.                                                                             |
| Alto    | Puede contaminar el proyecto vigente si se copia como verdad: caso distinto, rural, histórico, otra geografía o documento generado sin trazabilidad suficiente. |
| Crítico | No debe usarse como contenido activo hasta decisión humana expresa.                                                                                             |

### 3.3 Reglas de interpretación

```text
Benchmark operativo ≠ fuente legal.
Matriz interna vacía ≠ evidencia.
Ubicación potencial ≠ local validado.
Fuente antigua ≠ fuente vigente.
Análisis generado por IA ≠ fuente primaria.
Documento metodológico ≠ respuesta del plan.
```

---

## 4. Tabla de inventario puente

| ID         | Archivo externo / nombre de fuente                                         | Ubicación actual conocida                                                           | Tipo de fuente                                  | Tema principal                                                                                  | Carpeta destino propuesta en `docs_fuentes/`                                                                                               | Uso permitido                                                               | Riesgo de contaminación | Vigencia                                                                     | Requiere verificación externa                                          | Duplicados o relacionados                                                                 | Prioridad de importación | Observaciones                                                                                    |
| ---------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------ |
| PUENTE-001 | `Copia de Guía elaboración del Plan de Negocio (Red ARCE) 09.04.2018.docx` | `/mnt/data/` / fuente externa del proyecto                                          | Fuente metodológica                             | Estructura base, preguntas y lógica de plan de empresa                                          | `docs_fuentes/01_base_metodologica/`                                                                                                       | Usar como estructura, no como contenido de negocio                          | Bajo                    | Estable como metodología, aunque antigua                                     | No para estructura; sí si se citan requisitos institucionales actuales | Relacionada con `plan_empresa_guia/`                                                      | Alta                     | Debe alimentar la arquitectura del plan, no respuestas del Taller.                               |
| PUENTE-002 | `plan_empresa_caso_legacy_no_reutilizable_como_contenido (V2)`              | `/mnt/data/` / Google Drive                                                         | Fuente metodológica / ejemplo de entrega        | Nivel de profundidad, orden, estilo formal y control anticontaminación                          | `docs_fuentes/01_base_metodologica/`                                                                                                       | Usar solo como referencia formal                                            | Alto                    | Vigente como ejemplo interno 2026                                            | No para formato; sí para cualquier dato externo reutilizado            | Relacionada con Guía Red ARCE                                                             | Media                    | No copiar contenido de caso legacy no reutilizable como contenido. Es un caso de negocio ajeno.   |
| PUENTE-003 | `Proyecto taller colaborativo.docx`                                        | `/mnt/data/`                                                                        | Fuente histórica / identidad-origen             | Idea fundacional, problema, propósito, igualdad, economía circular, primeras líneas de servicio | `docs_fuentes/02_identidad_origen/` y posible copia controlada en `docs_fuentes/11_legacy_no_usar_directo/`                               | Usar parcialmente para origen e identidad, no para mercado vigente          | Alto                    | Histórica; requiere depuración por cambio de enfoque rural a urbano Zaragoza | Sí                                                                     | Relacionada con pitch rural y chats de análisis                                           | Alta                     | Debe entrar con etiqueta histórica para no reactivar supuestos rurales obsoletos.                |
| PUENTE-004 | `_Co Working Artesanal 2 pueblos Sn Maricel.pdf`                           | Fuente de proyecto / referencia externa detectada en biblioteca                     | Fuente histórica / pitch                        | Presentación inicial del emprendimiento rural y propuesta visual                                | `docs_fuentes/11_legacy_no_usar_directo/`                                                                                                  | Usar solo como antecedente histórico                                        | Crítico                 | Histórica                                                                    | Sí                                                                     | Relacionada con `Proyecto taller colaborativo.docx`                                       | Baja                     | Riesgo alto de contaminar con narrativa rural ya descartada.                                     |
| PUENTE-005 | `Chat Analisis documentacion`                                              | `/mnt/data/` / Google Drive                                                         | Fuente metodológica / auditoría documental      | Inventario previo, criterios de organización, separación de fases                               | `docs_fuentes/01_base_metodologica/`                                                                                                       | Usar como memoria de organización, no como verdad final                     | Medio                   | 2026                                                                         | No, salvo datos de terceros                                            | Relacionada con `01_inventario_fuentes.md` y `06_propuesta_inventario_general_fuentes.md` | Alta                     | Útil para reconstruir decisiones y evitar mezclar redacción con inventario.                      |
| PUENTE-006 | `documento_maestro_lecciones_aprendidas_08_05_v1.3.md`                     | `/mnt/data/`                                                                        | Fuente metodológica                             | Lecciones aprendidas, anti-errores, gates, trazabilidad, control de contaminación               | `docs_fuentes/01_base_metodologica/`                                                                                                       | Usar como reglas de trabajo y control de calidad                            | Bajo                    | 2026                                                                         | No                                                                     | Relacionada con consolidado de aprendizajes                                               | Alta                     | Fuente clave para gobernanza documental.                                                         |
| PUENTE-007 | `documento_consolidado_aprendizajes_fuentes_taller_colaborativo.md`        | `/mnt/data/`                                                                        | Fuente metodológica                             | Aprendizajes aplicables al proyecto, fases, sedes documentales, gates                           | `docs_fuentes/01_base_metodologica/`                                                                                                       | Usar como memoria operativa del proyecto                                    | Bajo                    | 2026                                                                         | No                                                                     | Relacionada con documento maestro                                                         | Alta                     | Debe ayudar a convertir reglas en decisiones documentales.                                       |
| PUENTE-008 | `Perfil de Marketing Estratégico.txt`                                      | `/mnt/data/`                                                                        | Fuente metodológica / rol                       | Criterios de marketing, producto, posicionamiento y auditoría comercial                         | `docs_fuentes/01_base_metodologica/`                                                                                                       | Usar como criterio de revisión, no como fuente de mercado                   | Medio                   | 2026                                                                         | No                                                                     | Relacionada con chats de marketing                                                        | Media                    | Puede ser útil para auditar respuestas, no para inventar estrategia.                             |
| PUENTE-009 | `Analisis de Competencia.xlsx`                                             | `/mnt/data/`                                                                        | Benchmark operativo / fuente financiera parcial | Competidores, comparación, precios o atributos tabulados                                        | `docs_fuentes/03_competencia_benchmarking/`                                                                                                | Usar parcialmente tras revisar hojas y metadatos                            | Medio                   | Pendiente de inspección                                                      | Sí                                                                     | Relacionada con investigaciones de competencia TXT                                        | Alta                     | Requiere abrir con herramienta de hojas antes de importar o resumir.                             |
| PUENTE-010 | `Análisis coworking carpintería.txt`                                       | `/mnt/data/`                                                                        | Benchmark operativo / estudio de mercado        | Comparativas de coworking, servicios, tarifas y referentes                                      | `docs_fuentes/03_competencia_benchmarking/`                                                                                                | Usar parcialmente, separando datos verificados de lectura estratégica       | Medio                   | 2026 aparente                                                                | Sí                                                                     | Relacionada con TMDC, CoMAKING, A tu Madera, T11, Cara y Canto                            | Alta                     | Puede ser un consolidado o duplicado de varias investigaciones; revisar antes de importar.       |
| PUENTE-011 | `Investigacion-TMDC.txt`                                                   | `/mnt/data/`                                                                        | Benchmark operativo                             | Modelo TMDC, fabricación compartida, comunidad maker, membresías/créditos                       | `docs_fuentes/03_competencia_benchmarking/`                                                                                                | Usar como referente, no como modelo inicial a copiar                        | Medio                   | 2026 aparente                                                                | Sí                                                                     | Relacionada con tabla maestra benchmarking                                                | Alta                     | Diferenciar qué es dato externo y qué es interpretación.                                         |
| PUENTE-012 | `Investigacion-The-CoMAKING-Space.txt`                                     | `/mnt/data/`                                                                        | Benchmark operativo                             | Taller industrial compartido, vivero empresarial, camperización, costes variables               | `docs_fuentes/03_competencia_benchmarking/`                                                                                                | Usar como referente de operación industrial flexible                        | Medio                   | 2026 aparente                                                                | Sí                                                                     | Relacionada con benchmarking España                                                       | Media                    | Útil para entender modelo industrial, quizá pesado para fase inicial.                            |
| PUENTE-013 | `Investigación-A-tu-Madera.txt`                                            | `/mnt/data/`                                                                        | Benchmark operativo                             | Referente de ciudad media, acceso por horas, comunidad, barrera económica                       | `docs_fuentes/03_competencia_benchmarking/`                                                                                                | Usar como benchmark prioritario para Zaragoza                               | Medio                   | 2026 aparente                                                                | Sí                                                                     | Relacionada con tabla maestra benchmarking                                                | Alta                     | Alta aplicabilidad por tamaño de ciudad y enfoque madera.                                        |
| PUENTE-014 | `Investigacion-T11-Sevilla-(Tejares-11).txt`                               | `/mnt/data/`                                                                        | Benchmark operativo                             | Cooperativa, taller compartido, comunidad, modelo de referencia Sevilla                         | `docs_fuentes/03_competencia_benchmarking/`                                                                                                | Usar como referente estratégico, no como copia jurídica automática          | Medio                   | 2026 aparente                                                                | Sí                                                                     | Relacionada con documentos T11 en Drive                                                   | Alta                     | Distinguir T11 real de interpretaciones derivadas.                                               |
| PUENTE-015 | `Investigacion-Cara-y-Canto.txt`                                           | `/mnt/data/`                                                                        | Benchmark operativo                             | Escuela-taller, coworking por horas, cursos, CNC, formación                                     | `docs_fuentes/03_competencia_benchmarking/`                                                                                                | Usar para pricing, servicios y modelo formación + uso                       | Medio                   | 2026 aparente                                                                | Sí                                                                     | Relacionada con análisis de competencia                                                   | Alta                     | Verificar tarifas actuales antes de usar en plan.                                                |
| PUENTE-016 | `Análisis Competitivo Coworking Madera Aragón`                             | `/mnt/data/` / Google Drive                                                         | Benchmark operativo / estudio de mercado local  | Competencia directa e indirecta en Aragón                                                       | `docs_fuentes/05_zaragoza_aragon/` y `docs_fuentes/03_competencia_benchmarking/`                                                           | Usar parcialmente tras separar hechos, hipótesis y recomendaciones          | Medio                   | 2026                                                                         | Sí                                                                     | Relacionada con informe de inteligencia y requisitos Zaragoza                             | Alta                     | Fuente clave para mapa local, pero debe tener trazabilidad.                                      |
| PUENTE-017 | `INFORME-DE-INTELIGENCIA-COMPETITIVA-Y-DE-ALIANZAS.txt`                    | `/mnt/data/`                                                                        | Estudio de mercado / alianzas                   | Ecosistema formativo de madera en Aragón, socios, huecos, formación                             | `docs_fuentes/05_zaragoza_aragon/`                                                                                                         | Usar como base preliminar de alianzas y competencia formativa               | Medio                   | 2026                                                                         | Sí                                                                     | Relacionada con análisis competitivo Aragón | Alta | Prioritaria, pero revisar afirmaciones absolutas como “no existe”. |
| PUENTE-018 | `Referente Estratégico: T11 Sevilla (Análisis para Zaragoza)`              | `/mnt/data/` / Google Drive                                                         | Benchmark operativo                             | Lectura estratégica de T11 aplicada a Zaragoza                                                  | `docs_fuentes/03_competencia_benchmarking/`                                                                                                | Usar como análisis secundario, no como fuente primaria                      | Medio-Alto              | 2026                                                                         | Sí                                                                     | Relacionada con investigación T11                                                         | Media                    | Importar después de fuente primaria o investigación externa verificable.                         |
| PUENTE-019 | `T11 Sevilla: Análisis y Comparativa`                                      | `/mnt/data/` / Google Drive                                                         | Benchmark operativo                             | Comparación T11 con Zaragoza y otros referentes                                                 | `docs_fuentes/03_competencia_benchmarking/`                                                                                                | Usar como análisis complementario                                           | Medio-Alto              | 2026                                                                         | Sí                                                                     | Relacionada con PUENTE-014 y PUENTE-018                                                   | Media                    | Posible duplicado parcial; revisar antes de importar.                                            |
| PUENTE-020 | `Fatiga-Digital.txt`                                                       | `/mnt/data/`                                                                        | Estudio de mercado / tendencia                  | Unplugging, trabajo manual, bienestar, hobbies, saturación digital                              | `docs_fuentes/04_mercado_tendencias/`                                                                                                      | Usar solo como hipótesis/tendencia hasta verificar fuentes                  | Alto                    | 2026 aparente                                                                | Sí                                                                     | Relacionada con Craft Council y tendencias de experiencia                                 | Media                    | Riesgo de datos no trazables; no usar cifras sin comprobar.                                      |
| PUENTE-021 | `Estudio de Mercado sobre artesanía.pdf`                                   | `/mnt/data/`                                                                        | Estudio de mercado                              | Sector artesanal, oferta, demanda, comercialización, DAFO, metodología                          | `docs_fuentes/04_mercado_tendencias/`                                                                                                      | Usar como metodología y contexto sectorial, no como dato local Zaragoza     | Medio                   | Histórica / requiere fecha exacta                                            | Sí                                                                     | Relacionada con Market for Craft 2020                                                     | Media                    | Útil por metodología; cuidado con geografía o supuestos no aplicables.                           |
| PUENTE-022 | `Market_for_craft_full_report_2020.pdf`                                    | `/mnt/data/`                                                                        | Estudio de mercado                              | Mercado craft, compradores, tendencias, experiencia, canales online                             | `docs_fuentes/04_mercado_tendencias/`                                                                                                      | Usar como contexto internacional y tendencias, no como dato España/Zaragoza | Medio                   | 2020, útil para tendencias pero no actual                                    | Sí                                                                     | Relacionada con Fatiga Digital y mercado artesanía                                        | Media                    | No extrapolar cifras UK directamente a Zaragoza.                                                 |
| PUENTE-023 | `Taller Artesanal_ Viabilidad y Marco Legal.md`                            | `/mnt/data/`                                                                        | Fuente legal/normativa / operativa              | Licencias, actividad, seguridad, forma jurídica, viabilidad operativa                           | `docs_fuentes/06_legal_operativo/` y `docs_fuentes/08_seguridad_responsabilidad_usuarios/`                                                 | Usar parcialmente y siempre con verificación normativa                      | Alto                    | 2026 aparente                                                                | Sí                                                                     | Relacionada con requisitos Zaragoza                                                       | Alta                     | Legal y normativa no pueden quedar solo en análisis IA; requieren contraste oficial/profesional. |
| PUENTE-024 | `Requisitos taller carpintería Zaragoza.txt`                               | `/mnt/data/`                                                                        | Fuente legal/normativa / operativa              | Requisitos técnicos para taller de carpintería en Zaragoza                                      | `docs_fuentes/06_legal_operativo/`, `docs_fuentes/07_instalaciones_local_producto/`, `docs_fuentes/08_seguridad_responsabilidad_usuarios/` | Usar como checklist preliminar, no como dictamen legal                      | Alto                    | 2026 aparente                                                                | Sí                                                                     | Relacionada con viabilidad legal                                                          | Alta                     | Prioritaria antes de redactar operaciones, local y seguridad.                                    |
| PUENTE-025 | `Guia de Ayudas para Emprendedores.pdf`                                    | `/mnt/data/`                                                                        | Fuente de ayudas o convocatorias                | Ayudas e incentivos para creación de empresas                                                   | `docs_fuentes/10_ayudas_financiacion/`                                                                                                     | Usar solo como referencia histórica/metodológica                            | Alto                    | 2022, probablemente caducada                                                 | Sí                                                                     | Relacionada con convocatorias y financiación                                              | Baja                     | No usar convocatorias 2022 como vigentes. Sirve para aprender estructura de búsqueda.            |
| PUENTE-026 | `Convocatoria_2-2021_VIGENTE.pdf`                                          | `/mnt/data/`                                                                        | Fuente de ayudas o convocatorias                | LEADER / convocatoria territorial Castilla-La Mancha                                            | `docs_fuentes/10_ayudas_financiacion/` o `docs_fuentes/11_legacy_no_usar_directo/`                                                         | Usar solo como ejemplo documental de convocatoria                           | Crítico                 | 2021/2022, no aplicable directamente a Zaragoza                              | Sí                                                                     | Relacionada con ayudas                                                                    | Baja                     | Geografía y plazo no aplican al proyecto vigente. Mantener fuera de contenido activo.            |
| PUENTE-027 | `Activos Fijos Coworking.xlsx`                                             | `/mnt/data/`                                                                        | Fuente financiera                               | Inventario de activos, maquinaria, inversión inicial                                            | `docs_fuentes/09_finanzas_activos/`                                                                                                        | Usar tras revisar hojas, supuestos y precios                                | Medio                   | Pendiente de inspección                                                      | Sí                                                                     | Relacionada con operaciones, local y CAPEX                                                | Alta                     | Importación prioritaria para modelo económico, pero no copiar sin validar precios actuales.      |
| PUENTE-028 | `Taller Artesanal Zaragoza: Guía Completa`                                 | `/mnt/data/` / Google Drive                                                         | Fuente legal/normativa / estudio local          | Guía integral sobre taller artesanal Zaragoza                                                   | `docs_fuentes/05_zaragoza_aragon/`, `docs_fuentes/06_legal_operativo/`, `docs_fuentes/07_instalaciones_local_producto/`                    | Usar parcialmente, separando hechos de recomendaciones                      | Medio-Alto              | 2026 aparente                                                                | Sí                                                                     | Relacionada con requisitos Zaragoza y viabilidad legal                                    | Alta                     | Puede ser fuente transversal; conviene dividir o etiquetar por tema al importar.                 |
| PUENTE-029 | `docs_fuentes/*/.gitkeep`                                                  | Repositorio actual                                                                  | Placeholder vacío                               | Marcadores de carpetas destino                                                                  | No aplica                                                                                                                                  | No usar como fuente                                                         | Crítico                 | Actual                                                                       | No                                                                     | Relacionado con diagnóstico `06`                                                          | No importar              | Confirma que `docs_fuentes/` aún no contiene fuentes reales.                                     |
| PUENTE-030 | Placeholders vacíos del repo madre `../taller_colaborativo/`               | Diagnóstico técnico previo descrito en `06_propuesta_inventario_general_fuentes.md` | Placeholder vacío                               | Estructura documental anterior sin contenido                                                    | No aplica                                                                                                                                  | No usar como fuente                                                         | Crítico                 | No aplica                                                                    | No                                                                     | Relacionado con respaldo zip del repo madre                                               | No importar              | Mantener el diagnóstico en `06`; no convertir placeholders en inventario global.                 |
| PUENTE-031 | Archivos `*Zone.Identifier*`                                               | Residuos del sistema Windows/WSL                                                    | Basura técnica / metadato de zona               | Metadatos generados por Windows al descargar/copiar archivos                                    | No aplica                                                                                                                                  | NO USAR EN PLAN FINAL                                                       | Crítico                 | No aplica                                                                    | No                                                                     | Relacionado con higiene del repo                                                          | No importar              | Deben eliminarse del repo y añadirse al `.gitignore`. No son fuentes documentales.               |

---

## 5. Lectura por carpeta destino propuesta

### 5.1 `docs_fuentes/01_base_metodologica/`

Importación sugerida en primera tanda:

* Guía Red ARCE.
* Documento maestro de lecciones aprendidas.
* Consolidado de aprendizajes del Taller.
* Chat de análisis documental, solo si se conserva como memoria metodológica.
* Perfil de Marketing Estratégico, si se usa como criterio de revisión y no como fuente de mercado.

Uso permitido:

* método;
* fases;
* gates;
* estructura;
* criterios de calidad;
* control anticontaminación;
* separación entre fuente, análisis, decisión y redacción.

Uso no permitido:

* inventar contenido de negocio;
* sustituir decisiones humanas;
* usar casos ajenos como datos del Taller.

### 5.2 `docs_fuentes/02_identidad_origen/`

Importación sugerida con cautela:

* `Proyecto taller colaborativo.docx`.

Uso permitido:

* origen;
* propósito;
* problema fundacional;
* economía circular;
* inclusión;
* primera formulación del servicio.

Uso no permitido:

* reactivar enfoque rural;
* usar supuestos de mercado antiguos;
* trasladar decisiones ya superadas al modelo urbano Zaragoza.

### 5.3 `docs_fuentes/04_mercado_tendencias/`

Importación sugerida:

* `Market_for_craft_full_report_2020.pdf`.
* `Estudio de Mercado sobre artesanía.pdf`.
* `Fatiga-Digital.txt`, solo como hipótesis hasta verificar fuentes.

Uso permitido:

* tendencias;
* metodología de análisis;
* comportamiento de consumidores;
* experiencia;
* canales;
* valor de lo artesanal;
* lectura macro del interés por oficios, trabajo manual y consumo experiencial.

Uso no permitido:

* extrapolar cifras de otros países o regiones como si fueran Zaragoza;
* usar datos antiguos como si fueran actuales;
* convertir tendencias genéricas en demanda validada local.

### 5.4 `docs_fuentes/03_competencia_benchmarking/`

Importación prioritaria:

* `Analisis de Competencia.xlsx`.
* Investigaciones individuales de TMDC, The CoMAKING Space, A tu Madera, T11, Cara y Canto.
* Análisis Competitivo Coworking Madera Aragón, si se etiqueta como análisis local/competitivo.

Uso permitido:

* comparar modelos;
* precios;
* servicios;
* barreras de entrada;
* complejidad operativa;
* reglas de uso;
* prácticas de seguridad;
* modelos de reserva, formación y acceso a maquinaria;
* aplicabilidad a Zaragoza.

Uso no permitido:

* copiar modelos completos sin validación de demanda local;
* tratar tarifas de competidores como precios óptimos propios;
* usar benchmark como fuente legal;
* afirmar inexistencia de competencia sin verificación actual.

### 5.5 `docs_fuentes/05_zaragoza_aragon/`

Importación prioritaria:

* `INFORME-DE-INTELIGENCIA-COMPETITIVA-Y-DE-ALIANZAS.txt`.
* `Análisis Competitivo Coworking Madera Aragón`.
* `Taller Artesanal Zaragoza: Guía Completa`.

Uso permitido:

* mapa local;
* formación;
* aliados;
* huecos;
* entorno urbano;
* oportunidad regional;
* instituciones y posibles alianzas;
* lectura de ecosistema de madera, oficios, FP, artesanía y restauración.

Uso no permitido:

* afirmaciones absolutas sin verificar;
* asumir disponibilidad de alianzas;
* afirmar que no existe competencia sin búsqueda actualizada;
* convertir hipótesis de oportunidad en prueba de mercado.

### 5.6 `docs_fuentes/06_legal_operativo/`

Importación prioritaria, pero con control estricto:

* `Taller Artesanal_ Viabilidad y Marco Legal.md`.
* `Requisitos taller carpintería Zaragoza.txt`.
* Fragmentos aplicables de `Taller Artesanal Zaragoza: Guía Completa`.
* Normativa PRL / lugares de trabajo / primeros auxilios, cuando se incorpore como fuente oficial.

Uso permitido:

* checklist preliminar de permisos;
* licencias;
* forma jurídica;
* actividad clasificada;
* prevención;
* primeros auxilios;
* botiquín;
* seguridad;
* ventilación;
* incendios;
* accesibilidad;
* obligaciones mínimas.

Uso no permitido:

* tratar análisis IA como dictamen legal definitivo;
* sustituir Ayuntamiento, técnico competente, OCA, asesoría legal, PRL, seguros o normativa oficial vigente;
* usar benchmarks como prueba de cumplimiento legal.

### 5.7 `docs_fuentes/07_instalaciones_local_producto/`

Importación sugerida:

* Partes de requisitos de local, instalaciones, zonificación, extracción, ruido, PCI y maquinaria.
* Activos vinculados a local y producto.
* Criterios de accesibilidad, carga y descarga, almacenamiento, layout, zonas limpias/sucias y experiencia de usuario.

Uso permitido:

* evaluar el local como parte del producto;
* definir criterios mínimos de ubicación;
* separar necesidades operativas de deseos comerciales;
* analizar compatibilidad entre maquinaria, seguridad y experiencia de usuario.

Uso no permitido:

* cerrar ubicación sin visita;
* cerrar inversión sin validar precios;
* aprobar layout sin contraste técnico;
* asumir que cualquier local comercial sirve para taller compartido de madera.

### 5.8 `docs_fuentes/08_seguridad_responsabilidad_usuarios/`

Importación prioritaria:

* Requisitos de seguridad.
* Responsabilidad de usuarios.
* Uso de maquinaria.
* EPIs.
* Formación obligatoria.
* Protocolos de accidente.
* Botiquín.
* Primeros auxilios.
* Seguros.
* Normas de uso.
* Mantenimiento preventivo.
* Operación segura.

Uso permitido:

* diseñar gates de acceso al taller;
* definir reglas de uso;
* identificar riesgos antes de abrir;
* preparar preguntas para PRL, seguros, técnico competente y asesoría legal.

Uso no permitido:

* sustituir prevención de riesgos;
* sustituir ingeniería;
* sustituir seguros;
* sustituir asesoría legal;
* permitir uso libre de maquinaria sin sistema de capacitación, registro y control.

### 5.9 `docs_fuentes/09_finanzas_activos/`

Importación prioritaria:

* `Activos Fijos Coworking.xlsx`.
* Partes financieras de benchmark y precios.
* Costes de maquinaria, herramientas, adecuación, extracción, seguridad, mobiliario, almacenamiento y software.

Uso permitido:

* inventario preliminar de inversión;
* rangos de activos;
* hipótesis CAPEX/OPEX;
* comparación de escenarios;
* detección de partidas olvidadas.

Uso no permitido:

* usar precios sin fecha;
* usar precios sin proveedor;
* cerrar presupuesto sin contraste actual;
* convertir una lista de deseos en inversión obligatoria.

### 5.10 `docs_fuentes/10_ayudas_financiacion/`

Importación condicionada:

* Guía de ayudas 2022 como referencia histórica/metodológica.
* Convocatoria LEADER 2021/2022 solo como ejemplo de expediente, no como ayuda vigente.

Uso permitido:

* aprender estructura de convocatorias;
* identificar campos típicos;
* entender criterios de evaluación;
* preparar búsquedas futuras de ayudas vigentes.

Uso no permitido:

* citar ayudas caducadas como oportunidad actual;
* asumir elegibilidad;
* basar viabilidad económica en subvenciones no concedidas;
* mezclar convocatorias de otra geografía con Zaragoza sin advertencia.

### 5.11 `docs_fuentes/11_legacy_no_usar_directo/`

Importación sugerida solo si se quiere conservar memoria histórica:

* Presentación rural inicial.
* Documentos antiguos.
* Narrativas no vigentes.
* Material de inspiración que no debe alimentar directamente el modelo urbano Zaragoza.

Uso permitido:

* antecedente histórico breve;
* memoria de origen;
* explicación de evolución del proyecto, si fuera necesario.

Uso no permitido:

* alimentar mercado;
* alimentar cliente;
* alimentar operaciones;
* alimentar estrategia;
* alimentar viabilidad vigente;
* reactivar el modelo rural como opción activa.

---

## 6. Riesgos detectados

1. **Riesgo de contaminación histórica:** el origen del proyecto tiene valor fundacional, pero el modelo vigente es urbano/Zaragoza. La importación debe etiquetar claramente lo no vigente como legacy.

2. **Riesgo de datos sin trazabilidad:** varias investigaciones TXT parecen contener análisis externo, pero deben separar fuente primaria, dato citado e interpretación.

3. **Riesgo legal/normativo:** los documentos legales son útiles como checklist, pero no pueden sustituir verificación con Ayuntamiento, normativa vigente, técnico competente, PRL, seguros o asesoría legal.

4. **Riesgo de ayudas caducadas:** las guías y convocatorias 2021/2022 no deben usarse como financiación vigente.

5. **Riesgo de duplicados:** hay múltiples documentos sobre T11, coworking carpintería, competencia y Zaragoza. Antes de importar físicamente, conviene decidir si se conserva fuente primaria + consolidado o si se importan todos con etiquetas.

6. **Riesgo de confundir análisis con fuente:** documentos generados por IA o investigaciones secundarias deben entrar como análisis, no como evidencia primaria.

7. **Riesgo financiero:** hojas Excel de activos y competencia requieren revisión de supuestos, fechas, fórmulas y precios antes de alimentar conclusiones.

8. **Riesgo de rutas inconsistentes:** cualquier discrepancia entre rutas documentadas y carpetas físicas de `docs_fuentes/` debe resolverse antes de importar fuentes reales.

9. **Riesgo de basura técnica:** archivos `*Zone.Identifier*` no son fuentes documentales y no deben entrar al control de conocimiento del proyecto.

---

## 7. Propuesta de prioridad de importación

### 7.1 Prioridad alta

1. Guía Red ARCE.
2. Documento maestro de lecciones aprendidas.
3. Consolidado de aprendizajes del Taller.
4. Proyecto taller colaborativo original, etiquetado como histórico/controlado.
5. Análisis competitivo local Aragón.
6. Informe de inteligencia competitiva y alianzas.
7. Requisitos taller carpintería Zaragoza.
8. Viabilidad y marco legal.
9. Activos Fijos Coworking.xlsx.
10. Analisis de Competencia.xlsx.

### 7.2 Prioridad media

1. Investigaciones individuales de benchmarks nacionales.
2. Market for Craft 2020.
3. Estudio de mercado sobre artesanía.
4. Fatiga Digital, solo si se verifican datos.
5. Referentes estratégicos derivados de T11.
6. Perfil de Marketing Estratégico, si se usará como criterio de revisión.

### 7.3 Prioridad baja

1. Guía de ayudas 2022.
2. Convocatoria LEADER 2021/2022.
3. Presentación rural inicial, si se conserva solo como legacy.
4. Material visual histórico sin vigencia operativa.

---

## 8. Relación con inventarios existentes

* `docs_organizacion/01_inventario_fuentes.md`: debe seguir siendo el inventario final de fuentes aprobado.
* `docs_organizacion/06_propuesta_inventario_general_fuentes.md`: debe seguir siendo diagnóstico técnico del repo madre, especialmente de placeholders vacíos.
* `docs_organizacion/07_propuesta_inventario_puente_fuentes_externas.md`: este documento propone qué fuentes externas reales deberían entrar después, pero no ejecuta importación.

Regla:

```text
06 diagnostica el repo madre.
07 propone puente hacia fuentes externas reales.
01 será la fuente de verdad final aprobada.
```

---

## 9. Decisión humana requerida

Alex debe decidir:

1. Qué fuentes de prioridad alta se autorizan para importación física a `docs_fuentes/`.
2. Si los documentos históricos se importan a `docs_fuentes/11_legacy_no_usar_directo/` o se mantienen fuera del repo.
3. Si los análisis generados por IA se aceptan como fuentes secundarias o solo como notas de apoyo.
4. Qué fuentes legales requieren verificación profesional antes de usarse en respuestas del plan.
5. Si se consolida competencia en una sola fuente maestra o se conservan investigaciones individuales más un consolidado.
6. Si se autoriza limpiar archivos `*Zone.Identifier*` y añadir esa regla al `.gitignore`.
7. Si se autoriza alinear físicamente las carpetas de `docs_fuentes/` con la estructura oficial cuando solo contengan `.gitkeep`.

---

## 10. Acciones físicas no autorizadas todavía

Este documento no autoriza:

```text
- mover fuentes reales;
- copiar fuentes reales;
- crear carpetas nuevas no aprobadas;
- eliminar archivos de contenido;
- rellenar respuestas_plan_empresa/;
- crear docs_consolidados/;
- generar plan final;
- generar DOCX/PDF/anexos;
- declarar Fase 1.1 completada;
- pasar a Fase 1.2.
```

---

## 11. Veredicto documental de esta propuesta

```text
VEREDICTO_PROPUESTA: LISTA_PARA_REVISION_HUMANA
ACCION_FISICA_SOBRE_FUENTES: NO_REALIZADA
IMPORTACION_A_DOCS_FUENTES: NO_REALIZADA
PLAN_REDACTADO: NO
RESPUESTAS_PLAN_EMPRESA_MODIFICADAS: NO
DOCS_CONSOLIDADOS_CREADOS: NO
FUENTE_DE_VERDAD_FINAL: docs_organizacion/01_inventario_fuentes.md
```

---

## 12. Siguiente paso recomendado

Antes de importar fuentes reales, se recomienda cerrar tres decisiones técnicas mínimas:

1. Confirmar que las carpetas físicas de `docs_fuentes/` coinciden con la estructura oficial de este documento.
2. Eliminar residuos `*Zone.Identifier*`, si existen.
3. Sustituir la lógica de “Codex redacta propuestas” por “Codex ejecuta contenido exacto aprobado”.

Después de eso, la siguiente acción humana será aprobar una primera tanda de importación controlada de fuentes reales.
