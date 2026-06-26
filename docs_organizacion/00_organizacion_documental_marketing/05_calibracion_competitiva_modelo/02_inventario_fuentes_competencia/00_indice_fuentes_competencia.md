# 02 — Inventario de fuentes de competencia

## Fase 0.0 — Organización documental de marketing

**Proyecto:** Taller Colaborativo Artesanal en Zaragoza
**Carpeta activa:** `docs_organizacion/00_organizacion_documental_marketing/05_calibracion_competitiva_modelo/`
**Bloque rector:** Bloque 6 — Competencia y benchmarking
**Estado:** Documento de trabajo para inventario y depuración de fuentes competitivas

---

## 1. Propósito del documento

Este documento registra y ordena las fuentes disponibles sobre competencia, referentes y modelos similares al **Coworking de Carpintería Artesanal (CCA)** en Zaragoza.

Su objetivo no es redactar conclusiones finales, sino crear una base limpia para analizar qué información tenemos, qué se repite, qué sirve para la Fase 1, qué está contaminado por modelos ajenos y qué debe conservarse solo como referencia futura.

Este inventario será la base para construir después:

* la matriz de referentes competitivos;
* la reducción de referentes núcleo;
* las decisiones preliminares del modelo mínimo viable;
* los rangos iniciales de precios;
* el modelo de acceso;
* la delimitación de servicios;
* la selección de maquinaria inicial;
* la exclusión de elementos que no deben entrar en el análisis financiero de arranque.

---

## 2. Criterio de lectura de las fuentes

Cada fuente debe revisarse con una pregunta central:

> ¿Qué información concreta aporta esta fuente para definir el modelo mínimo viable del Taller Colaborativo Artesanal en Zaragoza?

No se debe conservar todo por defecto. La información debe clasificarse según su utilidad.

---

## 3. Categorías de clasificación

### 3.1 Información útil para Fase 1

Se considera útil para Fase 1 la información relacionada con:

* carpintería artesanal;
* ebanistería;
* restauración de mobiliario;
* tapicería ligera vinculada al mueble;
* bancos de trabajo;
* alquiler por horas;
* bonos de uso;
* membresías;
* cursos prácticos;
* escuela de oficios;
* comunidad o club;
* almacenamiento de proyectos;
* herramientas manuales;
* maquinaria estacionaria convencional;
* inducción de seguridad;
* supervisión de usuarios;
* normas de uso del taller;
* economía circular;
* reutilización de madera;
* servicios complementarios básicos;
* precios públicos o rangos tarifarios;
* estructura de ingresos;
* modelo operativo replicable en una fase inicial.

### 3.2 Información repetida o redundante

Se considera repetida la información que aparece en varias fuentes y que debe consolidarse para evitar duplicidades.

Ejemplos:

* mismo referente analizado en varios documentos;
* mismos precios repetidos en chat, informe y tabla;
* misma descripción de servicios;
* mismas conclusiones sobre un competidor;
* mismas advertencias sobre CNC, makerspace o fabricación digital.

La información repetida no debe eliminarse de inmediato, pero sí debe marcarse como redundante y consolidarse en la matriz.

### 3.3 Información contaminante para Fase 1

Se considera contaminante para el modelo inicial toda información centrada en:

* CNC;
* corte láser;
* impresión 3D;
* fabricación digital avanzada;
* fablab tecnológico;
* makerspace digital;
* metal pesado;
* soldadura industrial;
* automatización logística;
* software de trazabilidad;
* producción industrial;
* maquinaria avanzada no esencial;
* modelos de negocio alejados del oficio artesanal en madera.

Esta información no debe entrar en la definición del modelo inicial ni en el análisis financiero de arranque.

### 3.4 Información útil solo para fase futura

Algunos elementos pueden conservarse como posibilidad posterior, pero no deben afectar el MVP.

Ejemplos:

* impresión 3D para accesorios o gadgets de carpintería;
* fabricación digital complementaria;
* prototipado;
* ampliación tecnológica;
* automatizaciones;
* incorporación de nuevos oficios;
* maquinaria avanzada;
* expansión a otras sedes;
* servicios industriales.

Esta información debe marcarse como:

`FASE_FUTURA_CONDICIONAL`

---

## 4. Inventario inicial de fuentes disponibles

| ID            | Fuente                                                  | Tipo de fuente                      | Referentes o tema principal               | Utilidad esperada                                                                                               | Estado                 |
| :------------ | :------------------------------------------------------ | :---------------------------------- | :---------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **COMP-F001** | `Investigacion-TMDC.txt`                                | Investigación individual            | TMDC Barcelona                            | Modelo maduro de taller compartido, membresías, inducción, escala, comunidad, posible contaminación tecnológica | `PENDIENTE_REVISION`   |
| **COMP-F002** | `Investigacion-The-CoMAKING-Space.txt`                  | Investigación individual            | The CoMAKING Space                        | Modelo de acceso, comunidad, uso compartido, estructura de servicios                                            | `PENDIENTE_REVISION`   |
| **COMP-F003** | `Investigación-A-tu-Madera.txt`                         | Investigación individual            | A tu Madera                               | Tarifas, bonos, alquiler de taller, servicios, posible referente cercano para Fase 1                            | `PENDIENTE_REVISION`   |
| **COMP-F004** | `Investigacion-T11-Sevilla-(Tejares-11).txt`            | Investigación individual            | T11 Sevilla / Tejares 11                  | Referente estratégico de espacio artesanal, comunidad y posible adaptación urbana                               | `PENDIENTE_REVISION`   |
| **COMP-F005** | `Investigacion-Cara-y-Canto.txt`                        | Investigación individual            | Cara y Canto                              | Cursos, bonos, restauración, ebanistería, embudo formación-práctica                                             | `PENDIENTE_REVISION`   |
| **COMP-F006** | `Análisis Competitivo Coworking Madera Aragón`          | Documento de análisis               | Zaragoza / Aragón / competencia local     | Ecosistema local, formación, alianzas, actores cercanos, huecos de mercado                                      | `PENDIENTE_REVISION`   |
| **COMP-F007** | `INFORME-DE-INTELIGENCIA-COMPETITIVA-Y-DE-ALIANZAS.txt` | Informe de inteligencia competitiva | Competencia y alianzas                    | Lectura estratégica, alianzas, actores locales, oportunidades y riesgos                                         | `PENDIENTE_REVISION`   |
| **COMP-F008** | `Chat01_taller Colaborativo.md`                         | Conversación consolidada            | Benchmarking amplio y decisiones previas  | Fuente amplia pero desordenada; puede contener precios, análisis comparativos y conclusiones repetidas          | `PENDIENTE_DEPURACION` |
| **COMP-F009** | `Análisis coworking carpintería.txt`                    | Análisis textual                    | Coworking carpintería / referentes varios | Información repetida o consolidada sobre precios, modelos y referentes                                          | `PENDIENTE_DEPURACION` |
| **COMP-F010** | `Analisis de Competencia.xlsx`                          | Hoja de cálculo                     | Comparativa de competidores               | Posible matriz previa de precios, servicios y referentes                                                        | `PENDIENTE_REVISION`   |

---

## 5. Inventario inicial de referentes identificados

Esta sección no analiza todavía los referentes. Solo registra los nombres que deben revisarse y cruzarse con las fuentes disponibles.

| ID Referente | Referente                 | Ciudad / País                 | Tipo preliminar                                   | Fuente(s) donde aparece         | Estado               |
| :----------- | :------------------------ | :---------------------------- | :------------------------------------------------ | :------------------------------ | :------------------- |
| **REF-001**  | TMDC                      | Barcelona, España             | Taller compartido / makerspace con área de madera | COMP-F001, COMP-F008, COMP-F009 | `PENDIENTE_ANALISIS` |
| **REF-002**  | A tu Madera               | Murcia, España                | Coworking de carpintería artesanal                | COMP-F003, COMP-F008, COMP-F009 | `PENDIENTE_ANALISIS` |
| **REF-003**  | Cara y Canto              | Madrid / Getafe, España       | Taller de madera, cursos y bonos                  | COMP-F005, COMP-F008, COMP-F009 | `PENDIENTE_ANALISIS` |
| **REF-004**  | The CoMAKING Space        | España / por verificar ciudad | Espacio compartido de fabricación/oficios         | COMP-F002, COMP-F008, COMP-F009 | `PENDIENTE_ANALISIS` |
| **REF-005**  | T11 Sevilla / Tejares 11  | Sevilla, España               | Espacio artesanal / referente estratégico         | COMP-F004, COMP-F008            | `PENDIENTE_ANALISIS` |
| **REF-006**  | The Workshop Madrid       | Madrid, España                | Taller / espacio de oficios                       | COMP-F008, COMP-F009            | `PENDIENTE_ANALISIS` |
| **REF-007**  | Made de Madera            | España / por verificar        | Taller o escuela de madera                        | COMP-F008                       | `PENDIENTE_ANALISIS` |
| **REF-008**  | TransfoLAB Barcelona      | Barcelona, España             | Espacio circular / fabricación / reutilización    | COMP-F008                       | `PENDIENTE_ANALISIS` |
| **REF-009**  | Artisano                  | Cataluña / España             | Espacio artesanal / formación                     | COMP-F008                       | `PENDIENTE_ANALISIS` |
| **REF-010**  | El Secadero de Reviverdes | Granada / España              | Taller, experiencias o formación                  | COMP-F008                       | `PENDIENTE_ANALISIS` |
| **REF-011**  | La Termita                | Zaragoza, España              | Taller local / restauración / formación           | COMP-F006, COMP-F007, COMP-F008 | `PENDIENTE_ANALISIS` |
| **REF-012**  | Garno Estudio             | Zaragoza, España              | Actor local / formación o restauración            | COMP-F006, COMP-F007            | `PENDIENTE_ANALISIS` |
| **REF-013**  | La Falsa                  | Zaragoza, España              | Actor local / artesanía o formación               | COMP-F006, COMP-F007            | `PENDIENTE_ANALISIS` |
| **REF-014**  | Working Restunearte       | Zaragoza, España              | Restauración / formación                          | COMP-F006, COMP-F007            | `PENDIENTE_ANALISIS` |
| **REF-015**  | Restaurarium              | Zaragoza, España              | Restauración / formación                          | COMP-F006, COMP-F007            | `PENDIENTE_ANALISIS` |
| **REF-016**  | La Corporación Taller     | Bogotá, Colombia              | Escuela-taller / carpintería / origen referencial | Fuentes históricas del proyecto | `PENDIENTE_ANALISIS` |
| **REF-017**  | Casa de Herramientas      | Bogotá, Colombia              | Taller compartido / antecedente histórico         | Fuentes históricas del proyecto | `PENDIENTE_ANALISIS` |

---

## 6. Ficha de revisión por fuente

Cada fuente debe revisarse con esta ficha mínima.

### Fuente: `[NOMBRE DE LA FUENTE]`

* **ID de fuente:**
* **Tipo de fuente:**
* **Referentes cubiertos:**
* **Estado de revisión:** `PENDIENTE_REVISION / REVISADA / DEPURADA / DESCARTADA`
* **Nivel de utilidad para Fase 1:** `ALTO / MEDIO / BAJO`
* **Nivel de contaminación:** `ALTO / MEDIO / BAJO / NULO`

#### 6.1 Información útil para Fase 1

* Servicios:
* Precios:
* Membresías:
* Bonos:
* Cursos:
* Alquiler de bancos:
* Seguridad:
* Maquinaria convencional:
* Comunidad:
* Almacenamiento:
* Economía circular:
* Otros datos útiles:

#### 6.2 Información repetida

* Información duplicada:
* Fuente donde también aparece:
* Acción recomendada:

#### 6.3 Información contaminante para Fase 1

* Elemento contaminante:
* Motivo:
* Acción: `DESCARTAR_FASE_1 / PASAR_A_FASE_FUTURA / VERIFICAR`

#### 6.4 Información útil para fase futura

* Elemento:
* Posible uso futuro:
* Condición para reconsiderarlo:

#### 6.5 Vacíos detectados

* Qué falta:
* Fuente posible para completarlo:
* Prioridad:

#### 6.6 Síntesis de la fuente

* Qué aporta realmente:
* Qué no aporta:
* Cómo debe usarse en la matriz:

---

## 7. Criterios para pasar una fuente a la matriz

Una fuente solo debe alimentar la matriz comparativa si aporta al menos uno de estos elementos:

* precio o rango tarifario;
* estructura de membresía o bono;
* descripción clara de servicios;
* modelo de acceso;
* cursos o escuela formativa;
* reglas de seguridad;
* descripción de maquinaria;
* almacenamiento;
* comunidad;
* operación del espacio;
* diferenciación competitiva;
* evidencia de demanda;
* información útil para definir qué copiar, adaptar o descartar.

Si una fuente solo contiene opinión general, inspiración o información demasiado vaga, debe quedar como fuente contextual.

---

## 8. Estados de revisión

Usar los siguientes estados:

| Estado                  | Significado                                                           |
| :---------------------- | :-------------------------------------------------------------------- |
| `PENDIENTE_REVISION`    | La fuente está identificada pero aún no se ha revisado.               |
| `PENDIENTE_DEPURACION`  | La fuente contiene material amplio o desordenado y requiere limpieza. |
| `REVISADA`              | La fuente fue leída y sus datos útiles fueron identificados.          |
| `DEPURADA`              | La fuente fue clasificada en útil, repetida, contaminante y futura.   |
| `DESCARTADA`            | La fuente no aporta información útil para esta fase.                  |
| `CONSOLIDADA_EN_MATRIZ` | La información útil ya fue trasladada a la matriz comparativa.        |

---

## 9. Regla de uso para la siguiente fase

Una vez depuradas las fuentes, la matriz comparativa no debe copiar textos largos.

La matriz debe extraer solo datos útiles:

* qué hace cada referente;
* cómo cobra;
* qué servicios ofrece;
* qué público atiende;
* qué reglas aplica;
* qué maquinaria muestra;
* qué puede copiarse;
* qué debe adaptarse;
* qué debe descartarse;
* qué tan aplicable es a Zaragoza.

---

## 10. Resultado esperado de este inventario

Al cerrar este documento, debe quedar claro:

* qué fuentes existen;
* qué referentes aparecen;
* qué fuentes están limpias;
* qué fuentes están contaminadas;
* qué información se repite;
* qué información sirve para Fase 1;
* qué información queda para fase futura;
* qué fuentes deben alimentar la matriz;
* qué vacíos deben investigarse después.

Este inventario se considera completo cuando todas las fuentes principales estén, como mínimo, en estado:

`REVISADA`

y las fuentes complejas o desordenadas estén en estado:

`DEPURADA`

Cuando lo pegues, el siguiente será el `03_matriz_referentes_competitivos.md`.
