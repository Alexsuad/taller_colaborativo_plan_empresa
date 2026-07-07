---
name: redactar-capitulo-plan-empresa-controlado
description: Genera un texto propuesto de un capítulo del Plan de Empresa solo cuando exista apertura parcial explícita de Gate 1D para ese capítulo. Si Gate 1D parcial no está abierto, devuelve bloqueo y no propone texto.
---

# Propósito

Usar esta skill para generar, de forma estrictamente controlada, texto propuesto para un capítulo concreto del Plan de Empresa.

Esta skill no autoriza redacción por sí sola. Solo puede operar cuando exista una apertura parcial explícita de Gate 1D para un capítulo concreto y para un archivo destino concreto.

Esta skill produce una salida estructurada para revisión. No escribe ni modifica directamente archivos en `respuestas_plan_empresa/` salvo que una misión operativa posterior lo autorice de forma explícita y acotada.

# Cuándo usar esta skill

Usar EXCLUSIVAMENTE cuando:

* exista un capítulo o bloque autorizado;
* exista el archivo guía exacto en `plan_empresa_guia/`;
* esté definido el archivo destino exacto en `respuestas_plan_empresa/`; si el archivo no existe, debe existir autorización operativa explícita para crearlo;
* Gate 1D parcial esté explícitamente abierto para ese capítulo;
* la pregunta ya esté clasificada;
* las fuentes permitidas estén acotadas;
* los vacíos aceptables estén identificados;
* el rol de Alex esté tipificado;
* las preguntas `[NO-RESPONDER-AÚN]` estén identificadas.

# Relación con otras skills

Esta skill se usa después de:

* `clasificar-pregunta-plan-empresa`;
* `preparar-bloque-para-redaccion`;
* `preparar-consulta-notebooklm-controlada`, si aplica.

Si el capítulo afecta cliente, propuesta de valor, marketing, ventas, comunicación, canales, redes sociales o posicionamiento, la salida debe declarar en `VALIDACIONES_REQUERIDAS` las skills comerciales pertinentes entre:

* `auditar-cliente-segmentos`;
* `auditar-producto-y-propuesta-valor`;
* `auditar-marketing`;
* `auditar-ventas`;
* `auditar-comunicacion`;
* `auditar-redes-sociales-calendario`;
* `auditar-marketing-ventas-comunicacion`;
* `validar-coherencia-cliente-propuesta-canales`;
* `validar-coherencia-comercial-global`.

No todas las validaciones comerciales son obligatorias siempre. Deben activarse según el contenido del capítulo.

Esta skill no reclasifica preguntas, no rehace la preparación del bloque y no sustituye la consulta controlada a NotebookLM. Consume las salidas de esas skills previas. Si detecta clasificación ausente, preparación insuficiente o consulta documental pendiente, debe declararlo en `PENDIENTES`, `OBSERVACIONES` o devolver `BLOQUEADO`, según corresponda.

Esta skill se usa antes de:

* auditoría documental;
* revisión QA;
* validaciones de formato;
* eventual compilación futura.

# Precondiciones obligatorias

No se puede operar sin confirmar:

1. capítulo o bloque autorizado;
2. archivo guía exacto;
3. archivo destino exacto definido, y autorización operativa explícita si hubiera que crearlo;
4. Gate 1D parcial abierto para ese capítulo;
5. clasificación disponible;
6. fuentes permitidas identificadas;
7. vacíos aceptados;
8. rol de Alex tipificado;
9. preguntas `[NO-RESPONDER-AÚN]` identificadas.

# Taxonomía de referencia

Esta skill debe respetar la taxonomía actual del Taller:

* `[F-REPO]`
* `[F-NOTEBOOKLM]`
* `[U-DATO]`
* `[U-VALIDA]`
* `[U-ELIGE]`
* `[U-AUTORIZA]`
* `[I-SIMPLE]`
* `[I-DEEP]`
* `[M]`
* `[NO-RESPONDER-AÚN]`

Nota de normalización:

* `[NO-RESPONDER-AÚN]` es la etiqueta oficial de clasificación.
* `NO_RESPONDER_AUN:` es el nombre del campo técnico de salida dentro del formato obligatorio.
* No deben introducirse variantes intermedias como `NO_RESPONDER_AÚN`, `[NO_RESPONDER_AÚN]`, `NO-RESPONDER-AUN` o `[NO-RESPONDER-AUN]`.

# Regla sobre Alex

Los códigos `[U-*]` no significan preguntar inmediatamente.

Antes de preguntar a Alex en blanco, esta skill debe comprobar si puede preparar una propuesta, una opción o un contexto trazable desde:

* el repositorio;
* NotebookLM;
* una fuente web simple;
* investigación profunda.

Alex interviene para:

* aportar un dato único;
* validar una propuesta;
* elegir entre opciones;
* autorizar investigación;
* bloquear o corregir hipótesis.

# Regla de fuentes

* Repo primero.
* NotebookLM solo si hay fuente indexada o un hueco clasificado como `[F-NOTEBOOKLM]` o `[M]`.
* Web simple o investigación profunda solo si está clasificado y autorizado.
* No convertir hipótesis en hechos.

# Regla de Presupuesto Documental y Extensión

*   **Consulta Obligatoria:** Es obligatorio consultar el archivo `docs_control/limites_extension_plan_empresa.yml` antes de proponer la redacción de cualquier capítulo.
*   **Cumplimiento de Mínimos:** No se deben entregar capítulos por debajo del mínimo de palabras indicado en el presupuesto, excepto en casos donde la información esté explícitamente bloqueada o clasificada como pendiente de decisión del promotor.
*   **Límites Superiores:** No se debe superar el límite de `warning` o `fail` por archivo sin una justificación técnica o de mercado debidamente validada.
*   **Separación de Anexos:** Toda información de soporte extensa (tablas largas, listados completos de fuentes, cálculos detallados, comparativas extensas o transcripciones) debe ser enviada a anexos, manteniendo en el cuerpo principal solo las conclusiones, síntesis interpretativas y datos clave para la toma de decisiones.
*   **Densidad y Calidad:** El cumplimiento de las palabras mínimas del presupuesto no debe justificar en ningún caso el uso de relleno artificial o contenido repetitivo.

# Restricciones de contenido

* Diferenciar estrictamente entre hechos, hipótesis y pendientes.
* No inventar datos.
* No cerrar viabilidad sin evidencia.
* No redactar resumen ejecutivo antes de los capítulos base.
* No redactar el bloque económico-financiero o de viabilidad si falta base suficiente.
* No usar contenido de Zac/Sistreg.
* No abrir Fase 4.
* No dar `PASS` global.
* No tocar capítulos no autorizados.

# Calidad del texto propuesto

El campo `TEXTO_PROPUESTO` debe estar redactado como borrador de capítulo del Plan de Empresa, con tono:

* profesional;
* claro;
* sobrio;
* comprensible;
* útil para entidades de apoyo al emprendimiento, administraciones públicas, bancos, posibles inversores o aliados institucionales;
* específico del Taller Colaborativo Artesanal en Zaragoza;
* coherente con los capítulos previos y con el estado real de la información disponible.

El texto no debe sonar a:

* salida interna de agente;
* checklist técnico;
* nota de trabajo;
* explicación de workflow;
* justificación de gate;
* informe de trazabilidad;
* texto genérico de marketing;
# Profundidad mínima del capítulo

El `TEXTO_PROPUESTO` no se considera suficiente solo por estar limpio, ordenado, bien escrito y sin errores formales.

Un capítulo del Plan de Empresa debe aportar utilidad empresarial real. Debe ayudar a tomar decisiones, justificar criterios, detectar riesgos, explicar límites o conectar aprendizajes con el proyecto.

Cuando exista un archivo de insumos saneados para el capítulo, ese archivo debe usarse como base sustantiva principal. No basta con mencionarlo como fuente. La redacción debe transformar sus datos en:

* análisis;
* aprendizajes;
* cautelas;
* implicaciones para el proyecto;
* decisiones o criterios que alimentan otros capítulos del Plan de Empresa.

Si el capítulo solo resume información sin extraer consecuencias útiles, debe considerarse insuficiente.

# Regla para benchmarking, mercado y marketing

En capítulos de benchmarking, mercado, competencia, marketing, ventas, comunicación, redes sociales, propuesta de valor o posicionamiento, la redacción debe seguir una lógica de utilidad empresarial.

No basta con describir referentes, competidores, canales, tendencias o ideas. La redacción debe convertirlos en aprendizaje aplicable.

Usar esta cadena de razonamiento siempre que corresponda:

```text
hecho observado → aprendizaje → aplicación al proyecto → decisión o cautela
```

Ejemplo de aplicación esperada:

* hecho observado: un referente cobra por horas, bonos o membresías;
* aprendizaje: el modelo combina acceso flexible con previsibilidad de ingresos;
* aplicación al proyecto: conviene analizar si el proyecto puede ofrecer bonos o membresías sin comprometer seguridad, capacidad ni disponibilidad de maquinaria;
* decisión o cautela: no copiar el modelo sin validar demanda, costes, control de acceso y supervisión.

Si no hay evidencia suficiente para convertir un dato en decisión, debe quedar como hipótesis o cautela, no como conclusión cerrada.

# Regla anti-capítulo genérico

Un capítulo es genérico si podría aplicarse a cualquier negocio cambiando solo el nombre.

La redacción debe evitar frases amplias que no aportan decisión, como:

* “esto aporta valor al proyecto”;
* “permite diferenciarse”;
* “mejora la experiencia del cliente”;
* “refuerza la propuesta de valor”;
* “ayuda al posicionamiento”;

si no explica de forma concreta:

* qué valor aporta;
* frente a qué alternativa;
* para qué cliente;
* con qué límite;
* con qué evidencia;
* qué decisión permite tomar.

Si el texto no puede responder esas preguntas, debe marcarse como `BORRADOR_PARCIAL_CON_VACIOS`, `REQUIERE_DECISION_ALEX`, `REQUIERE_INVESTIGACION` o `BLOQUEADO`, según corresponda.

# Separación entre control interno y texto final

Los campos:

* `HECHOS`;
* `HIPOTESIS`;
* `PENDIENTES`;
* `NO_RESPONDER_AUN`;
* `FUENTES_USADAS`;
* `OBSERVACIONES`;
* `VALIDACIONES_REQUERIDAS`;

son campos de control interno.

No deben mezclarse dentro de `TEXTO_PROPUESTO`.

`TEXTO_PROPUESTO` debe contener solo texto limpio del capítulo, sin:

* etiquetas de clasificación;
* códigos internos;
* notas al agente;
* trazabilidad operativa;
* comentarios al usuario;
* frases como "según la matriz";
* frases como "este punto está clasificado como";
* menciones a gates, workflows, skills o repositorio;
* pendientes incrustados como si fueran parte del texto final.

Si hay vacíos relevantes, deben declararse en `PENDIENTES`, `NO_RESPONDER_AUN` u `OBSERVACIONES`, no esconderse dentro de una redacción ambigua.

# Regla anti-genericidad comercial

No producir `TEXTO_PROPUESTO` con formulaciones genéricas, intercambiables o no sustentadas por evidencia del Taller, como:

* "empresa innovadora";
* "servicio de calidad";
* "experiencia única";
* "solución integral";
* "propuesta diferencial";
* "atención personalizada";
* "referente del sector";
* "modelo disruptivo";
* "alto potencial de crecimiento";

si no existe base concreta que las sostenga.

Cuando se hable de valor, diferenciación, cliente, canales, ventas, comunicación o redes, el texto debe apoyarse en elementos concretos del Taller, sus fuentes, decisiones aprobadas o hipótesis declaradas.

# Coherencia comercial y narrativa

Antes de proponer texto, verificar que no contradice dependencias narrativas y comerciales relevantes:

* cliente objetivo;
* problema o necesidad;
* propuesta de valor;
* oferta;
* posicionamiento;
* canales;
* marketing;
* ventas;
* comunicación;
* redes sociales;
* recursos disponibles;
* limitaciones reales del proyecto.

Especialmente, mantener coherencia entre:

```text
cliente -> problema/necesidad -> propuesta de valor -> oferta -> canales -> ventas -> comunicación -> redes sociales
```

Si el capítulo depende de otra sección todavía no validada, la salida debe declararlo en `PENDIENTES` o `OBSERVACIONES`, y el estado debe tender a:

* `BORRADOR_PARCIAL_CON_VACIOS`;
* `REQUIERE_DECISION_ALEX`;
* `REQUIERE_INVESTIGACION`;
* `BLOQUEADO`.

No debe marcarse como `LISTO_PARA_REVISION` si hay contradicciones comerciales relevantes o falta una base mínima de cliente, propuesta, canales o viabilidad.

# Tono y voz

El tono del `TEXTO_PROPUESTO` debe ser profesional, directo y realista.

Debe evitar:

* tono demasiado técnico;
* tono de sistema agéntico;
* lenguaje interno del repositorio;
* frases infladas;
* promesas comerciales no sustentadas;
* exceso de entusiasmo;
* lenguaje publicitario vacío;
* afirmaciones absolutas sin evidencia;
* conclusiones de viabilidad no demostradas.

La redacción debe actuar como la de un asesor profesional de creación de empresas: clara, honesta, exigente y útil.

# Grado de certeza de las afirmaciones

Antes de redactar una afirmación fuerte en `TEXTO_PROPUESTO`, la skill debe clasificar internamente su grado de certeza.

Categorías:

1. **Hecho verificado**
   Puede redactarse como hecho si procede de una fuente válida y trazable.

2. **Decisión aprobada**
   Puede redactarse como decisión del proyecto si existe decisión explícita del promotor o del repositorio.

3. **Criterio preliminar**
   Debe redactarse como orientación prudente, no como decisión cerrada.

4. **Hipótesis razonable**
   Debe redactarse como hipótesis pendiente de validación.

5. **Pendiente de validación externa**
   Debe marcarse como pendiente cuando dependa de costes, local, seguros, licencias, demanda, precios, inversión, financiación, normativa, proveedores o viabilidad.

6. **No sustentado**
   No debe redactarse como conclusión. Debe quedar en `PENDIENTES`, `CAUTELAS_RELEVANTES` u `OBSERVACIONES`.

Regla:
Toda afirmación fuerte debe estar respaldada por una fuente, una decisión aprobada, una restricción legal/técnica real o evidencia suficiente. Si no lo está, debe formularse como criterio preliminar, hipótesis o cautela.

# Lenguaje prudente para Plan de Empresa

La redacción debe evitar lenguaje rígido, absoluto o interno cuando la decisión no esté cerrada.

No usar expresiones como:

* “se prohíbe”;
* “se determina”;
* “queda definido”;
* “es obligatorio”;
* “se descarta definitivamente”;
* “debe ser”;

si la afirmación no está respaldada por una decisión aprobada, una restricción legal/técnica real o evidencia suficiente.

Cuando se trate de criterios preliminares, hipótesis o decisiones condicionadas, usar fórmulas como:

* “se recomienda evitar”;
* “se establece como criterio preliminar”;
* “queda fuera del alcance de la Fase 1”;
* “deberá validarse antes de su implantación”;
* “se considera prudente”;
* “la opción más razonable inicialmente es”;
* “la decisión queda condicionada a”;
* “no se recomienda en esta fase”.

Estas expresiones no son sustituciones mecánicas. La elección depende del grado de certeza de la afirmación.

# Decisiones condicionadas

Cuando una conclusión dependa de información todavía no cerrada, no debe redactarse como decisión definitiva.

Aplica especialmente cuando dependa de:

* local;
* metros cuadrados;
* costes;
* seguros;
* licencias;
* normativa;
* demanda;
* precios;
* inversión;
* maquinaria;
* capacidad operativa;
* financiación;
* viabilidad económica.

Ejemplo incorrecto:

```text
Se prohíbe dimensionar el local por encima de 300 m².
```

Ejemplo correcto:

```text
Como criterio preliminar de prudencia, se recomienda evitar locales superiores a 300 m² en la Fase 1, salvo que el análisis financiero, el coste del alquiler y la capacidad operativa justifiquen lo contrario.
```

Si una decisión queda condicionada, la dependencia debe aparecer también en `CAUTELAS_RELEVANTES`, `PENDIENTES` u `OBSERVACIONES`.

# Revisión final de tono y certeza

Antes de entregar `TEXTO_PROPUESTO`, revisar si contiene afirmaciones absolutas.

Si aparecen decisiones fuertes, comprobar que tienen base en:

* fuente verificable;
* decisión explícita del promotor;
* límite aprobado de fase;
* restricción legal o técnica real;
* evidencia económica suficiente.

Si no tienen esa base, suavizar la redacción y marcar la dependencia en `CAUTELAS_RELEVANTES`, `PENDIENTES` u `OBSERVACIONES`.

# Hipótesis dentro del texto

Las hipótesis pueden mencionarse en `TEXTO_PROPUESTO` solo si se formulan claramente como hipótesis, supuestos de trabajo, decisiones pendientes o elementos por validar.

Nunca deben redactarse como hechos cerrados.

Ejemplo permitido:

```text
Una hipótesis inicial del proyecto es que existe un grupo de personas interesadas en acceder a un espacio compartido de trabajo artesanal, aunque esta demanda deberá validarse con evidencia específica antes de cerrar el análisis comercial.
```

Ejemplo prohibido:

```text
Existe una alta demanda de espacios artesanales colaborativos en Zaragoza.
```

si no hay fuente suficiente.

# Procedimiento

1. Confirmar que existe Gate 1D parcial abierto para el capítulo concreto.
2. Confirmar el archivo guía exacto y el archivo destino exacto.
3. Revisar la clasificación de la pregunta y los bloques preparados.
4. Revisar las fuentes permitidas y los vacíos aceptados.
5. Verificar el rol de Alex y las preguntas `[NO-RESPONDER-AÚN]`.
6. Preparar el texto propuesto solo si el gate parcial lo permite.
7. Si falta la precondición de Gate 1D parcial, devolver bloqueo sin texto propuesto.
8. Mantener trazabilidad total entre fuente, decisión, hipótesis y pendiente.

# Reglas obligatorias

* Esta skill no abre Gate 1D.
* Esta skill no autoriza redacción por sí sola.
* Esta skill no toca `respuestas_plan_empresa/` si el gate parcial no está abierto.
* Esta skill no pregunta a Alex en blanco si antes puede preparar opciones o contexto trazable.
* Esta skill no mezcla preparación con validación final.
* Esta skill no transforma hipótesis en hechos.
* Esta skill no utiliza contenido sectorial de otros proyectos.
* Esta skill no introduce lenguaje interno dentro del texto limpio del capítulo.
* Esta skill no produce texto genérico sin evidencia concreta.
* Esta skill no declara listo un capítulo comercialmente débil.
* Esta skill no sustituye auditorías comerciales posteriores cuando apliquen.

# Estados de salida permitidos

* `NO_REDACTAR_AUN`
* `BORRADOR_CONTROLADO`
* `BORRADOR_PARCIAL_CON_VACIOS`
* `REQUIERE_NOTEBOOKLM`
* `REQUIERE_INVESTIGACION`
* `REQUIERE_DECISION_ALEX`
* `LISTO_PARA_REVISION`
* `BLOQUEADO`

# Formato de salida obligatorio

La respuesta debe usar exactamente estas claves, en este orden:

```text
CAPITULO:
ARCHIVO_GUIA:
ARCHIVO_DESTINO:
GATE_1D_PARCIAL:
CLASIFICACION_USADA:
FUENTES_USADAS:
HECHOS:
HIPOTESIS:
PENDIENTES:
NO_RESPONDER_AUN:
ROL_ALEX:
INSUMOS_CLAVE_USADOS:
APRENDIZAJES_APLICADOS:
DECISIONES_O_CRITERIOS_DERIVADOS:
CAUTELAS_RELEVANTES:
TEXTO_PROPUESTO:
VALIDACIONES_REQUERIDAS:
ESTADO_SALIDA:
OBSERVACIONES:
```

Los campos `INSUMOS_CLAVE_USADOS`, `APRENDIZAJES_APLICADOS`, `DECISIONES_O_CRITERIOS_DERIVADOS` y `CAUTELAS_RELEVANTES` son campos de control interno. Sirven para demostrar que el texto no se limitó a resumir fuentes, sino que transformó los insumos en utilidad empresarial.

Estos campos no deben mezclarse dentro de `TEXTO_PROPUESTO`.

# Reglas de bloqueo

Si no existe Gate 1D parcial abierto:

* `TEXTO_PROPUESTO` debe quedar vacío;
* `ESTADO_SALIDA` debe ser `NO_REDACTAR_AUN` o `BLOQUEADO`.

Si el capítulo afecta cliente, propuesta, marketing, ventas, comunicación, redes, canales o posicionamiento y no hay base suficiente:

* no usar tono genérico para rellenar;
* no cerrar como listo;
* declarar el vacío;
* activar validaciones comerciales necesarias;
* devolver `BORRADOR_PARCIAL_CON_VACIOS`, `REQUIERE_DECISION_ALEX`, `REQUIERE_INVESTIGACION` o `BLOQUEADO`, según corresponda.

# Criterio de cierre

La skill se considera completada cuando:

* el capítulo propuesto queda trazado con sus fuentes y pendientes; o
* se emite formalmente un `NO_REDACTAR_AUN` o `BLOQUEADO` fundamentado.

No se considera completada si:

* mezcla control interno con texto final;
* presenta hipótesis como hechos;
* oculta vacíos relevantes;
* produce texto genérico;
* omite validaciones comerciales necesarias;
* invade Fase 4.

# Evidencia esperada

* Capítulo identificado.
* Archivo guía identificado.
* Archivo destino identificado.
* Gate 1D parcial verificado.
* Fuentes usadas.
* Hipótesis separadas.
* Pendientes listados.
* Rol de Alex tipificado.
* Texto propuesto, solo si el gate parcial lo permite.

# Criterio de bloqueo cualitativo

Si el bloque o capítulo queda formalmente correcto pero no aporta utilidad empresarial, debe marcarse como insuficiente.

Se considera insuficiente cuando:

* resume sin analizar;
* enumera datos sin extraer aprendizajes;
* menciona referentes sin explicar qué se aprende;
* habla de mercado sin traducirlo a decisiones;
* habla de marketing sin conectar cliente, propuesta, canales o ventas;
* habla de benchmarking sin indicar qué aplicar, qué adaptar y qué no copiar;
* oculta vacíos bajo redacción fluida;
* usa frases profesionales pero intercambiables.

En ese caso, no debe cerrarse como listo. Debe devolver un estado de salida conservador y explicar qué falta.
