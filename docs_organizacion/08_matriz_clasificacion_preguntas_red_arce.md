# 08 — Matriz de clasificación de preguntas Red ARCE

> **Estado documental:** PENDIENTE_DE_DECISIÓN  
> **Decisión pendiente:** DEC-014.  
> **Uso permitido:** revisión y discusión técnica/metodológica.  
> **Uso prohibido:** no usar como matriz aprobada para habilitar redacción hasta aprobación humana.


**Estado:** Propuesta operativa inicial — pendiente de revisión y aprobación humana.  
**Propósito:** Clasificar las preguntas guía del plan antes de redactar, para separar qué ya puede extraerse de fuentes internas, qué debe decidir el promotor, qué requiere búsqueda simple, qué exige investigación profunda, qué es mixto y qué no debe responderse todavía.  
**Regla principal:** No redactar ningún apartado final hasta clasificar primero sus preguntas.

## 1. Regla madre

Ningún apartado de `respuestas_plan_empresa/` puede redactarse si antes no existe su pregunta guía clasificada.

La clasificación no equivale a respuesta. La clasificación solo indica el procedimiento correcto para resolver cada pregunta.

## 2. Matriz base

La matriz base tiene esta lógica:

| Pregunta guía | Estado | Clasificación | Fuente probable | Acción |
| ------------- | ------ | ------------- | --------------- | ------ |

Estados permitidos:

- Contestada
- Parcial
- Pendiente

## 2.1 Códigos de clasificación

| Código | Significado | Quién/qué responde | Uso correcto |
| ------ | ----------- | ------------------ | ------------ |
| `[F]` | Fuente interna del proyecto | Documentos ya existentes en el repo | No preguntar ni buscar de nuevo; extraer, adaptar y citar fuente |
| `[U]` | Usuario | Promotor / Alexander | Preguntar directamente porque sería peligroso inventarlo |
| `[I-SIMPLE]` | Investigación simple | Búsqueda puntual en internet o fuente oficial | Confirmar datos concretos, trámites, ayudas, CNAE, licencia, normativa básica |
| `[I-DEEP]` | Investigación profunda | Investigación amplia con varias fuentes | Competencia, mercado, benchmarking, demanda, barreras, precios, alianzas |
| `[M]` | Mixto | Fuente interna + usuario + investigación | Temas que no se pueden resolver desde una sola fuente |
| `[NO-RESPONDER-AÚN]` | No responder todavía | Validación futura real | No inventar datos que dependen de clientes reales, ventas, pruebas de mercado o validación futura |

## 3. Matriz Red ARCE → preguntas → clasificación

| ID | Sección Red ARCE | Pregunta guía / asunto | Estado | Clasificación | Fuente interna candidata | Fuente externa necesaria | Decisión del usuario | Acción siguiente | Responsable | Fase autorizada | Bloqueo / no bloqueo |
| -- | ---------------- | ---------------------- | ------ | ------------- | ------------------------ | ------------------------ | -------------------- | ---------------- | ----------- | --------------- | -------------------- |
| 0.1 | 0. Resumen ejecutivo | ¿Qué síntesis final del negocio puede construirse sin inventar capítulos que aún no existen? | Pendiente | `[M]+[NO-RESPONDER-AÚN]` | `docs_control/00_contrato_identidad_negocio.md`, `docs_control/01_opcion_activa_taller.md`, `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md`, `docs_organizacion/03_revision_critica_matriz_vacios.md` | No procede todavía | Sí: qué nivel de síntesis se quiere reservar para el cierre | ESPERAR_RESPUESTA_PREVIA | MIXTO | REDACCION_BLOQUEADA | BLOQUEA |
| 1.1 | 1. Equipo promotor | ¿Quién compone exactamente el equipo promotor y qué dedicación real tiene cada persona? | Parcial | `[U]` | `plan_empresa_guia/01_equipo_promotor.md`, `docs_organizacion/03_revision_critica_matriz_vacios.md` | No procede todavía | Sí, respuesta directa del promotor | PREGUNTAR_A_ALEXANDER | PROMOTOR | PREGUNTA_PROMOTOR | BLOQUEA |
| 2.1 | 2. Idea de negocio | ¿Cuál es el alcance inicial exacto del taller en fase 1 y qué queda fuera? | Contestada | `[F]+[U]` | `docs_control/00_contrato_identidad_negocio.md`, `docs_control/01_opcion_activa_taller.md` | No procede todavía | Sí, para confirmar límites operativos | EXTRAER_DE_FUENTE_INTERNA | MIXTO | CLASIFICACION | BLOQUEA_PARCIALMENTE |
| 3.1.1 | 3.1 Análisis externo | ¿Qué factores del entorno general y sectorial afectan al taller en Zaragoza? | Pendiente | `[I-DEEP]` | `docs_organizacion/03_revision_critica_matriz_vacios.md` | Estudios sectoriales, contexto local, referencias oficiales | No procede todavía | PREPARAR_INVESTIGACION_PROFUNDA | INVESTIGACION | INVESTIGACION_PROFUNDA | BLOQUEA |
| 3.2.1 | 3.2 Estudio de mercado | ¿Qué demanda, segmentos y competencia real existen para el taller colaborativo? | Pendiente | `[I-DEEP]+[M]` | `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md`, `docs_organizacion/03_revision_critica_matriz_vacios.md` | Competencia local, benchmarking, referencias de mercado | Sí: acotar segmento objetivo inicial | PREPARAR_INVESTIGACION_PROFUNDA | INVESTIGACION | INVESTIGACION_PROFUNDA | BLOQUEA |
| 3.3.1 | 3.3 Análisis interno | ¿Qué recursos, capacidades y límites operativos reales tiene el Taller para arrancar? | Parcial | `[F]+[U]` | `docs_control/00_contrato_identidad_negocio.md`, `docs_control/01_opcion_activa_taller.md`, `docs_organizacion/03_revision_critica_matriz_vacios.md` | No procede todavía | Sí: disponibilidad real de recursos y límites | PREGUNTAR_A_ALEXANDER | MIXTO | PREGUNTA_PROMOTOR | BLOQUEA |
| 4.1 | 4. DAFO / CAME | ¿Qué fortalezas, debilidades, oportunidades y amenazas pueden sostenerse con evidencia suficiente? | Pendiente | `[M]` | `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md`, `docs_organizacion/03_revision_critica_matriz_vacios.md` | Depende de análisis externo e interno | Sí, después de completar 3.1, 3.2 y 3.3 | ESPERAR_RESPUESTA_PREVIA | MIXTO | REDACCION_BLOQUEADA | BLOQUEA |
| 5.1 | 5. Objetivos y líneas estratégicas | ¿Qué objetivos cuantitativos y hitos de arranque quiere fijar el promotor? | Pendiente | `[U]+[M]` | `docs_control/01_opcion_activa_taller.md`, `docs_organizacion/03_revision_critica_matriz_vacios.md` | No procede todavía | Sí, definición directa del promotor | PREGUNTAR_A_ALEXANDER | PROMOTOR | PREGUNTA_PROMOTOR | BLOQUEA |
| 6.0.1 | 6.0 Marca, comunicación y naming | ¿Cómo se debe expresar la marca y qué tono de comunicación es coherente con el Taller? | Parcial | `[F]+[U]` | `docs_control/01_opcion_activa_taller.md`, `docs_control/04_registro_decisiones.md` | No procede todavía | Sí, para validar tono y enfoque | EXTRAER_DE_FUENTE_INTERNA | MIXTO | CLASIFICACION | NO_BLOQUEA |
| 6.1.1 | 6.1 Marketing y ventas | ¿Qué tarifas, canales y secuencia comercial son aceptables para el arranque? | Pendiente | `[U]+[I-DEEP]` | `docs_organizacion/03_revision_critica_matriz_vacios.md` | Competencia, precios de mercado, referencias sectoriales | Sí: umbrales y prioridades comerciales | PREPARAR_INVESTIGACION_PROFUNDA | MIXTO | INVESTIGACION_PROFUNDA | BLOQUEA |
| 6.2.1 | 6.2 Operaciones | ¿Qué local, layout, flujo y condiciones técnicas necesita realmente el taller? | Pendiente | `[M]+[I-SIMPLE]` | `docs_organizacion/03_revision_critica_matriz_vacios.md` | Licencias básicas, requisitos técnicos, normativa general | Sí: tipo de local y tolerancia al riesgo operativo | VALIDAR_EXTERNAMENTE | MIXTO | VALIDACION_EXTERNA | BLOQUEA |
| 6.3.1 | 6.3 Recursos humanos | ¿Qué organigrama mínimo y costes de personal son posibles al inicio? | Parcial | `[U]+[I-SIMPLE]` | `docs_organizacion/03_revision_critica_matriz_vacios.md`, `docs_control/01_opcion_activa_taller.md` | Referencias de costes laborales y figuras contractuales | Sí: qué roles asumirá el promotor | PREGUNTAR_A_ALEXANDER | MIXTO | PREGUNTA_PROMOTOR | BLOQUEA |
| 6.4.1 | 6.4 Jurídico-fiscal | ¿Qué forma jurídica, licencias y requisitos normativos aplican al taller? | Pendiente | `[I-SIMPLE]+[I-DEEP]` | `docs_organizacion/03_revision_critica_matriz_vacios.md` | Normativa municipal, requisitos de actividad, prevención y seguros | Sí: prioridad legal y alcance del local | VALIDAR_EXTERNAMENTE | ASESOR_EXTERNO | VALIDACION_EXTERNA | BLOQUEA |
| 6.5.1 | 6.5 Económico-financiero | ¿Qué inversión, costes, financiación e hipótesis de ingresos pueden sostenerse sin inventar? | Pendiente | `[M]+[NO-RESPONDER-AÚN]` | `docs_organizacion/03_revision_critica_matriz_vacios.md`, `docs_control/01_opcion_activa_taller.md` | Referencias de costes, financiación y mercado | Sí: umbral de inversión y tolerancia al riesgo | MARCAR_HIPOTESIS_NO_VALIDADA | MIXTO | REDACCION_BLOQUEADA | BLOQUEA |
| 7.1 | 7. Implantación y puesta en marcha | ¿Qué cronograma realista existe para reforma, licencias y apertura? | Pendiente | `[M]+[I-SIMPLE]` | `docs_organizacion/03_revision_critica_matriz_vacios.md` | Plazos de licencias y reforma | Sí: local y calendario objetivo | PREPARAR_BUSQUEDA_SIMPLE | MIXTO | REDACCION_BLOQUEADA | BLOQUEA |
| 8.1 | 8. Viabilidad y conclusiones | ¿Con qué evidencia puede cerrarse una conclusión de viabilidad sin sobreprometer? | Pendiente | `[NO-RESPONDER-AÚN]` | `docs_organizacion/03_revision_critica_matriz_vacios.md`, salidas de bloques anteriores | Resultados de bloques previos y validaciones reales | No procede todavía | ESPERAR_RESPUESTA_PREVIA | MIXTO | REDACCION_BLOQUEADA | BLOQUEA |

## 4. Preguntas clasificadas por origen de respuesta

### 4.1 `[F]` — Resolver desde fuente interna

| Pregunta / asunto | Fuente interna candidata | Acción recomendada | Bloque Red ARCE relacionado |
| ----------------- | ------------------------ | ------------------ | ---------------------------- |
| Alcance inicial de fase 1 | `docs_control/00_contrato_identidad_negocio.md`, `docs_control/01_opcion_activa_taller.md` | EXTRAER_DE_FUENTE_INTERNA | 2. Idea de negocio |
| Identidad base del taller | `docs_control/00_contrato_identidad_negocio.md` | EXTRAER_DE_FUENTE_INTERNA | 2. Idea de negocio |
| Base de marca y naming | `docs_control/01_opcion_activa_taller.md`, `docs_control/04_registro_decisiones.md` | EXTRAER_DE_FUENTE_INTERNA | 6.0 Marca, comunicación y naming |
| Restricciones de redacción y gateado | `docs_control/03_gates_documentales.md` | EXTRAER_DE_FUENTE_INTERNA | Todos los bloques |
| Vacíos y bloqueos ya identificados | `docs_organizacion/03_revision_critica_matriz_vacios.md` | EXTRAER_DE_FUENTE_INTERNA | 3.1 a 8 |

### 4.2 `[U]` — Preguntar al promotor

#### Prioridad alta

- ¿Quién forma exactamente el equipo promotor y qué dedicación real tiene cada persona?
- ¿Qué objetivos cuantitativos y hitos de arranque quieres fijar?
- ¿Qué local o tipo de local buscas realmente?
- ¿Qué inversión inicial máxima puedes asumir?

#### Prioridad media

- ¿Qué roles asumirás tú al inicio y cuáles no?
- ¿Qué tarifas base consideras aceptables para arrancar?
- ¿Qué nivel de ambición comercial es realista para el primer año?

#### Prioridad baja

- ¿Qué imagen de marca quieres transmitir?
- ¿Qué alianzas serían deseables pero no imprescindibles?

### 4.3 `[I-SIMPLE]` — Preparar búsqueda simple

| Consulta | Fuente esperada | Bloque relacionado | Prioridad |
| -------- | --------------- | ------------------ | --------- |
| CNAE y requisitos básicos de actividad | Fuente oficial | 6.4 Jurídico-fiscal | Alta |
| Normativa básica de licencias y actividad | Fuente oficial municipal / autonómica | 6.4 Jurídico-fiscal | Alta |
| Plazos orientativos de licencias y trámites | Fuente oficial | 7. Implantación y puesta en marcha | Alta |
| Referencias básicas de costes laborales | Fuente oficial o técnica | 6.3 Recursos humanos | Media |
| Confirmación básica de requisitos técnicos del local | Fuente oficial / técnica | 6.2 Operaciones | Alta |

### 4.4 `[I-DEEP]` — Preparar investigación profunda

| Tema | Pregunta central | Por qué no basta una búsqueda simple | Salida esperada | Prioridad |
| ---- | ---------------- | ------------------------------------ | --------------- | --------- |
| Mercado local del taller colaborativo | ¿Existe demanda suficiente y en qué segmentos? | Requiere contraste de múltiples fuentes y lectura contextual | Segmentación y lectura de demanda prudente | Alta |
| Competencia y benchmarking | ¿Cómo se posicionan competidores y referentes? | Exige comparación estructurada y criterio propio | Mapa de competencia y huecos de mercado | Alta |
| Modelo comercial inicial | ¿Qué combinación de tarifas y servicios es viable? | Depende de mercado, operación y validaciones del promotor | Hipótesis comerciales priorizadas | Alta |
| Viabilidad económica | ¿Qué supuestos financieros resisten mejor la comparación con datos reales? | Requiere integrar operación, mercado y costes | Hipótesis económicas con rango prudente | Alta |

### 4.5 `[M]` — Casos mixtos

| Asunto | Componentes necesarios | Orden sugerido de resolución | Bloqueo actual |
| ------ | ---------------------- | ---------------------------- | -------------- |
| Resumen ejecutivo | Fuentes internas + resultados de bloques 1 a 8 | Clasificar primero, redactar al final | Bloquea |
| Análisis interno | Fuente interna + promotor | Extraer, preguntar y contrastar | Bloquea parcialmente |
| Marketing y ventas | Promotor + investigación profunda | Definir umbrales, luego contrastar mercado | Bloquea |
| Operaciones | Fuente interna + validación externa | Revisar local, luego validar requisitos | Bloquea |
| Económico-financiero | Fuente interna + usuario + mercado | Fijar supuestos, luego validar prudencia | Bloquea |

### 4.6 `[NO-RESPONDER-AÚN]` — Hipótesis no validables todavía

| Asunto | Estado correcto | Bloque Red ARCE |
| ------ | --------------- | ---------------- |
| Disposición real de pago | Hipótesis o pendiente de validación futura | 6.1, 6.5 |
| Clientes confirmados | No responder todavía | 3.2, 6.1 |
| Tasa de conversión | No responder todavía | 6.1, 6.5 |
| Ocupación mensual | Hipótesis no validada | 6.5, 7 |
| Recurrencia | Hipótesis no validada | 6.1, 6.5 |
| Aceptación real del modelo | Pendiente de validación futura | 3.2, 8 |
| Resultados de piloto | Pendiente de validación futura | 8 |

## 5. Bloques que no pueden redactarse todavía

| Bloque Red ARCE | Motivo del bloqueo | Clasificación dominante | Qué debe ocurrir antes de redactar |
| --------------- | ------------------ | ----------------------- | ---------------------------------- |
| 0. Resumen ejecutivo | Depende de capítulos previos y de una síntesis final coherente | `[M]` / `[NO-RESPONDER-AÚN]` | Completar y clasificar el resto de bloques |
| 1. Equipo promotor | Faltan datos directos del promotor | `[U]` | Responder preguntas del promotor |
| 3.1 Análisis externo | Requiere investigación amplia | `[I-DEEP]` | Preparar y ejecutar investigación profunda |
| 3.2 Estudio de mercado | Requiere contraste de mercado y competencia | `[I-DEEP]` | Ejecutar investigación profunda |
| 4. DAFO / CAME | Depende de 3.1, 3.2 y 3.3 | `[M]` | Completar bloques previos |
| 6.1 Marketing y ventas | Faltan precios y posicionamiento contrastado | `[U]` / `[I-DEEP]` | Preguntar al promotor y contrastar mercado |
| 6.2 Operaciones | Faltan local y validación técnica | `[M]` / `[I-SIMPLE]` | Identificar local y validar requisitos |
| 6.4 Jurídico-fiscal | Requiere validación externa | `[I-SIMPLE]` / `[I-DEEP]` | Confirmar normativa con fuente oficial o técnica |
| 6.5 Económico-financiero | Faltan supuestos prudentes y validados | `[M]` / `[NO-RESPONDER-AÚN]` | Completar operación, mercado y validación financiera |
| 7. Implantación y puesta en marcha | Faltan cronograma y plazos reales | `[M]` / `[I-SIMPLE]` | Definir local, licencias y secuencia |
| 8. Viabilidad y conclusiones | Requiere base concluida y validada | `[NO-RESPONDER-AÚN]` | Completar y validar bloques anteriores |

## 6. Uso operativo de esta matriz

1. Leer pregunta guía.
2. Revisar fuentes internas.
3. Clasificar la pregunta.
4. Separar contestadas, parciales y pendientes.
5. Buscar solo lo necesario.
6. Preparar investigación profunda si hace falta.
7. Preguntar al usuario solo lo que depende del usuario.
8. Marcar lo que no debe responderse todavía.
9. Redactar solo cuando la matriz esté clara y el gate lo autorice.

## 7. Estado recomendado de Gate 1C

Gate 1C sigue EN CURSO.  
Esta matriz mejora la capacidad de diagnóstico, pero no cierra Gate 1C.  
Gate 1D sigue BLOQUEADO.  
No se autoriza redacción de `respuestas_plan_empresa/`.  
El siguiente paso será revisar y aprobar esta matriz, luego responder preguntas del promotor y preparar búsquedas e investigaciones.
