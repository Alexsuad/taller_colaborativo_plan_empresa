---

# COMP-F010 — Análisis de Competencia.xlsx

* **ID de fuente:** COMP-F010
* **Fuente original:** `Analisis de Competencia.xlsx`
* **Tipo de fuente:** Hoja comparativa / inventario tabular de competencia y referentes
* **Ámbito cubierto:** Referentes competitivos, modelos, precios, aplicabilidad y observaciones comparativas
* **Estado de revisión:** `REVISADA`
* **Nivel de utilidad para Fase 1:** `MEDIO-ALTO`
* **Nivel de contaminación:** `MEDIO`

---

## 1. Información útil para Fase 1

### 1.1 Naturaleza de la fuente

`Analisis de Competencia.xlsx` funciona como una fuente de apoyo tabular para ordenar información competitiva.

No debe tratarse como una investigación independiente completa, sino como una herramienta de consolidación para comparar referentes, precios, modelos y observaciones.

Su utilidad principal está en:

* estructurar información dispersa;
* facilitar comparación entre competidores;
* ordenar datos de precios;
* detectar patrones de acceso;
* identificar referentes más aplicables;
* apoyar la construcción de la matriz competitiva;
* servir como control cruzado frente a las fichas narrativas.

La fuente debe usarse como:

```text
FUENTE_TABULAR_DE_CONSOLIDACION
```

No como fuente primaria definitiva.

---

### 1.2 Tipo de información que aporta

La hoja puede aportar información útil sobre:

* nombre del referente;
* ubicación;
* tipo de modelo;
* servicios ofrecidos;
* precios visibles;
* bonos;
* membresías;
* formación;
* acceso a taller;
* maquinaria;
* almacenamiento;
* comunidad;
* observaciones estratégicas;
* aplicabilidad al proyecto Zaragoza;
* posibles riesgos o limitaciones.

Esta información es especialmente útil para alimentar documentos posteriores donde haga falta comparar de forma sintética.

---

### 1.3 Uso dentro de la fase de calibración competitiva

Dentro de la fase de calibración competitiva, esta fuente debe cumplir tres funciones:

```text
1. Control de consistencia entre referentes.
2. Apoyo para la matriz comparativa.
3. Resumen tabular de patrones comerciales.
```

No debe convertirse en sustituto de las fichas individuales.

La ficha narrativa de cada referente sigue siendo necesaria para entender matices, riesgos, contaminaciones y decisiones de uso.

---

## 2. Relación con otras fuentes

### 2.1 Fuentes que complementa

Esta hoja debe cruzarse con:

* `COMP-F001_investigacion_tmdc.md`;
* `COMP-F002_investigacion_the_comaking_space.md`;
* `COMP-F003_investigacion_a_tu_madera.md`;
* `COMP-F004_investigacion_t11_sevilla.md`;
* `COMP-F005_investigacion_cara_y_canto.md`;
* `COMP-F006_analisis_competitivo_madera_aragon.md`;
* `COMP-F007_informe_inteligencia_competitiva_alianzas.md`;
* `COMP-F008_chat01_taller_colaborativo.md`;
* `COMP-F009_analisis_coworking_carpinteria.md`.

Su valor aumenta cuando se usa para verificar si las conclusiones narrativas coinciden con los datos tabulares.

---

### 2.2 Información que no debe duplicar

No conviene trasladar todo el contenido de la hoja al repositorio en forma narrativa.

La información detallada ya debe quedar distribuida en:

* fichas individuales por referente;
* matriz de referentes competitivos;
* reducción de referentes núcleo;
* decisiones preliminares del MVP.

Por tanto, esta ficha debe limitarse a explicar qué aporta la hoja y cómo debe usarse.

---

## 3. Información útil para la matriz competitiva

### 3.1 Campos que debería alimentar

La hoja puede alimentar columnas como:

| Campo de matriz          | Uso                                                   |
| ------------------------ | ----------------------------------------------------- |
| Referente                | Identificación del competidor o modelo                |
| Ubicación                | Ciudad / zona                                         |
| Tipo de modelo           | Coworking, escuela-taller, maker, cooperativa, etc.   |
| Servicios                | Cursos, bonos, taller, maquinaria, almacenamiento     |
| Precios visibles         | Datos comparables, siempre pendientes de verificación |
| Modelo de acceso         | Bono, membresía, pago por uso, créditos, etc.         |
| Aplicabilidad a Zaragoza | Alta, media, baja, futura                             |
| Riesgos                  | Contaminación, escala, complejidad, falta de datos    |
| Acción recomendada       | Copiar, adaptar, descartar, fase futura               |

---

### 3.2 Uso recomendado

La hoja debe usarse para comprobar:

* si los referentes núcleo aparecen de forma consistente;
* si los precios están alineados con las fichas individuales;
* si hay datos contradictorios;
* si algún referente está sobrevalorado;
* si algún competidor secundario merece pasar a núcleo parcial;
* si faltan campos necesarios para la matriz final.

---

## 4. Información contaminante para Fase 1

### 4.1 Datos sin trazabilidad suficiente

* **Elemento contaminante:** precios o afirmaciones sin fuente primaria visible.
* **Motivo:** una hoja comparativa puede condensar datos sin mostrar claramente de dónde proceden.
* **Acción:** `VERIFICAR_ANTES_DE_PLAN_FINANCIERO`

Los precios no deben usarse directamente en el plan financiero sin validación actualizada.

---

### 4.2 Riesgo de falsa precisión

* **Elemento contaminante:** convertir datos tabulares en conclusiones definitivas.
* **Motivo:** una tabla puede parecer más objetiva de lo que realmente es si no contiene fecha, fuente y condiciones.
* **Acción:** `USAR_COMO_APOYO_NO_COMO_PRUEBA_FINAL`

---

### 4.3 Referentes mezclados

* **Elemento contaminante:** mezclar competidores directos, referentes lejanos, makerspaces, escuelas y actores locales en una misma tabla.
* **Motivo:** puede dar la impresión de que todos compiten en el mismo plano.
* **Acción:** `CLASIFICAR_POR_TIPO_DE_REFERENTE`

Separar al menos:

* competidores directos;
* competencia formativa;
* referentes comerciales;
* referentes comunitarios;
* referentes de fase futura;
* aliados potenciales;
* actores contextuales.

---

### 4.4 Fabricación digital y modelos industriales

* **Elemento contaminante:** CNC, láser, impresión 3D, metal, soldadura o makerspace industrial.
* **Motivo:** estos elementos ya quedaron fuera de la Fase 1.
* **Acción:** `DESCARTAR_FASE_1 / FASE_FUTURA_CONDICIONAL`

---

## 5. Información útil para fase futura

### 5.1 Control comparativo posterior

La hoja puede ser útil más adelante para:

* actualizar tarifas;
* añadir nuevos referentes;
* marcar fecha de verificación;
* comparar modelos de precios;
* controlar competidores locales;
* registrar contactos realizados;
* añadir resultado de entrevistas;
* alimentar una matriz viva.

---

### 5.2 Validación de pricing

En fase futura, la hoja podría evolucionar hacia una herramienta de pricing, incluyendo:

* precio del referente;
* unidad de cobro;
* IVA incluido o no;
* caducidad del bono;
* horas incluidas;
* coste por hora equivalente;
* coste de almacenamiento;
* coste de inducción;
* condiciones de maquinaria;
* observaciones;
* fuente y fecha de consulta.

Esto sería útil para construir una hipótesis de tarifas propia con más rigor.

---

### 5.3 Actualización periódica

La hoja puede servir como documento vivo si se mantiene actualizada.

Campos recomendables para futuras versiones:

| Campo recomendado | Motivo                               |
| ----------------- | ------------------------------------ |
| Fecha de consulta | Evita usar precios desactualizados   |
| Fuente primaria   | Permite trazabilidad                 |
| URL o captura     | Facilita verificación                |
| Estado del dato   | Confirmado / pendiente / inferido    |
| IVA               | Evita errores financieros            |
| Condiciones       | Explica límites de uso               |
| Aplicabilidad     | Evita comparar modelos incomparables |
| Acción            | Copiar / adaptar / descartar         |

---

## 6. Vacíos detectados

### 6.1 Información pendiente de verificar

Antes de usar la hoja para conclusiones finales, falta comprobar:

* fecha de actualización;
* fuente original de cada dato;
* si los precios incluyen IVA;
* si los referentes siguen activos;
* si las tarifas siguen vigentes;
* condiciones exactas de bonos y membresías;
* si los datos proceden de web, conversación, inferencia o investigación previa;
* si hay duplicados;
* si hay referentes mezclados sin clasificación;
* si faltan notas sobre contaminación para Fase 1.

---

### 6.2 Fuente posible para completarlo

* páginas oficiales de cada referente;
* capturas fechadas;
* contacto directo;
* revisión manual de fichas individuales;
* comparación con `COMP-F008`;
* comparación con `COMP-F009`;
* futuras entrevistas de validación local.

---

### 6.3 Prioridad de verificación

`MEDIA-ALTA`

Motivo: la hoja puede ayudar mucho a la matriz, pero no debe usarse como fuente final de pricing sin depuración.

---

## 7. Síntesis de la fuente

### 7.1 Qué aporta realmente

`Analisis de Competencia.xlsx` aporta orden tabular.

Su principal valor es permitir ver, en una sola estructura, patrones y diferencias entre referentes:

* quién ofrece cursos;
* quién ofrece coworking;
* quién cobra por horas;
* quién usa membresías;
* quién incluye almacenamiento;
* qué modelos parecen más aplicables;
* qué referentes conviene filtrar o descartar.

Es una fuente útil para comparar, no para decidir sola.

---

### 7.2 Qué no aporta

No aporta por sí sola:

* evidencia primaria completa;
* explicación estratégica profunda;
* validación local;
* demanda real;
* datos financieros propios;
* condiciones jurídicas;
* prueba de disposición a pagar;
* confirmación actualizada de tarifas;
* justificación suficiente para CAPEX.

Tampoco debe usarse para reabrir elementos excluidos de Fase 1 como CNC, láser, impresión 3D o fabricación digital.

---

### 7.3 Cómo debe usarse en la matriz

Esta fuente debe usarse como:

```text
FUENTE_TABULAR_DE_APOYO
```

Debe alimentar:

* matriz de referentes competitivos;
* tabla de precios comparables;
* control de consistencia;
* identificación de huecos de información;
* preparación de verificación externa.

Debe filtrarse para no copiar:

* precios sin fecha;
* referentes mezclados;
* modelos industriales;
* fabricación digital;
* conclusiones sin trazabilidad;
* datos duplicados de otras fuentes.

---

## 8. Conclusión operativa

`Analisis de Competencia.xlsx` debe clasificarse como:

```text
FUENTE_TABULAR_DE_CONSOLIDACION
```

Conclusión prudente:

```text
La hoja es útil para ordenar y comparar,
pero las decisiones deben apoyarse en las fichas narrativas,
la matriz competitiva y la verificación posterior de precios y condiciones.
```

Su función principal dentro del repositorio debe ser servir como puente entre las investigaciones individuales y la futura matriz competitiva.

---
