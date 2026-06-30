---

name: clasificar-pregunta-plan-empresa
description: Clasifica una pregunta del plan de empresa por fuente probable, dependencia del usuario/promotor, estado NO_RESPONDER_AÚN y siguiente acción documental. Use when a question must be prepared before redaction.
---

# Propósito

Usar esta skill para convertir una pregunta del plan en una clasificación documental clara, reutilizable y trazable.

Su función es decir qué tipo de respuesta necesita la pregunta, sin redactar el plan ni decidir negocio.

# Cuándo usar esta skill

Usar cuando se necesite:

* clasificar una pregunta guía del plan de empresa;
* determinar si depende del usuario/promotor;
* marcar si debe quedar en `NO_RESPONDER_AÚN`;
* señalar la fuente probable o el tipo de fuente requerida;
* preparar la pregunta para una fase posterior de redacción o investigación.

# Entradas esperadas

* Pregunta guía.
* Sección o bloque del plan.
* Fuentes candidatas disponibles.
* Dependencia conocida del usuario/promotor.
* Estado de evidencia disponible.
* Restricciones activas del proyecto.

# Salidas esperadas

Una ficha de clasificación con, como mínimo:

* ID;
* pregunta;
* sección;
* tipo de respuesta;
* fuente probable;
* dependencia de usuario/promotor;
* estado `NO_RESPONDER_AÚN` sí/no;
* siguiente acción;
* observaciones.

# Procedimiento

1. Leer la pregunta y ubicar la sección.
2. Identificar si existe fuente interna suficiente.
3. Determinar si la respuesta depende del usuario/promotor.
4. Determinar si la pregunta debe quedar en `NO_RESPONDER_AÚN`.
5. Marcar la fuente probable o el tipo de búsqueda requerido.
6. Registrar la siguiente acción documental.
7. Emitir la clasificación sin redactar contenido final.

# Reglas obligatorias

* Esta skill no redacta contenido final del Plan de Empresa.
* Esta skill no abre Gate 1D.
* Esta skill no toca `respuestas_plan_empresa/`.
* Esta skill no decide negocio, marketing, legal, RRSS ni viabilidad.
* Esta skill no convierte hipótesis en hechos.

# Límites / No hacer

No hacer:

* inventar respuestas;
* resolver estrategia;
* redactar apartados del plan;
* sustituir criterio humano;
* mover o importar archivos;
* crear skills expertas.

# Criterio de utilidad para Marketing / Producto

La skill debe ayudar a Marketing a:

* separar preguntas contestables de preguntas bloqueadas;
* saber qué depende del promotor;
* evitar que una duda se convierta en afirmación;
* ordenar el trabajo antes de redactar;
* reducir retrabajo en Gate 1D.

# Criterio de cierre

La skill se considera completada cuando cada pregunta queda clasificada con una salida clara y accionable, sin redactar el contenido final.

# Evidencia esperada

* Ficha de clasificación.
* Fuente probable.
* Dependencia de usuario/promotor.
* Marcado `NO_RESPONDER_AÚN` si aplica.
* Siguiente acción documental.
