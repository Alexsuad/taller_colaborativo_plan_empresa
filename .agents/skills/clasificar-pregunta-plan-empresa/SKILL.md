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

## Formato de salida obligatorio

La respuesta debe usar exactamente estas claves, en este orden:

```text
ID:
PREGUNTA:
SECCION:
CLASIFICACION:
FUENTE_SIGUIENTE:
ROL_ALEX:
PREPARABLE_ANTES_DE_PREGUNTAR:
SIGUIENTE_ACCION:
NO_RESPONDER_AUN:
OBSERVACIONES:
```

## Tabla obligatoria de etiquetas

| Código | Significado | Uso obligatorio |
| --- | --- | --- |
| `[F-REPO]` | Fuente interna local del repositorio | Extraer primero del repo antes de preguntar |
| `[F-NOTEBOOKLM]` | Fuente indexada del proyecto en NotebookLM | Consultar solo si el repo no basta y la fuente ya está indexada |
| `[U-DATO]` | Dato que solo puede aportar Alex/promotor | Usar solo si el sistema no puede prepararlo de forma trazable |
| `[U-VALIDA]` | Alex valida una propuesta preparada | Pedir validación de una propuesta, no una pregunta en blanco |
| `[U-ELIGE]` | Alex elige entre opciones preparadas | Ofrecer alternativas cerradas antes de preguntar |
| `[U-AUTORIZA]` | Alex autoriza una investigación web o profunda | Pedir permiso solo después de preparar el contexto |
| `[I-SIMPLE]` | Investigación web puntual o fuente oficial simple | Búsqueda acotada y verificable |
| `[I-DEEP]` | Investigación profunda | Requiere varias fuentes y contraste |
| `[M]` | Mixto | Combina repo, NotebookLM, usuario e investigación |
| `[NO-RESPONDER-AÚN]` | No responder todavía | Depende de validación futura real o de hitos no disponibles |

# Procedimiento

1. Leer la pregunta y ubicar la sección.
2. Identificar si existe fuente interna suficiente.
3. Comprobar si antes de preguntar al usuario se puede preparar una opción trazable con fuentes internas, NotebookLM o investigación controlada.
4. Determinar si la respuesta depende del usuario/promotor y, si es así, si el rol es aportar dato, validar propuesta, elegir entre opciones o autorizar investigación.
5. Determinar si la pregunta debe quedar en `NO_RESPONDER_AÚN`.
6. Marcar la fuente probable o el tipo de búsqueda requerido.
7. Registrar la siguiente acción documental.
8. Emitir la clasificación sin redactar contenido final.

# Reglas obligatorias

* Esta skill no redacta contenido final del Plan de Empresa.
* Esta skill no abre Gate 1D.
* Esta skill no toca `respuestas_plan_empresa/`.
* Esta skill no decide negocio, marketing, legal, RRSS ni viabilidad.
* Esta skill no convierte hipótesis en hechos.
* Esta skill no pregunta al usuario en blanco si todavía puede preparar opciones con repositorio, NotebookLM o investigación controlada.

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
