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
TEXTO_PROPUESTO:
VALIDACIONES_REQUERIDAS:
ESTADO_SALIDA:
OBSERVACIONES:
```

# Reglas de bloqueo

Si no existe Gate 1D parcial abierto:

* `TEXTO_PROPUESTO` debe quedar vacío;
* `ESTADO_SALIDA` debe ser `NO_REDACTAR_AUN` o `BLOQUEADO`.

# Criterio de cierre

La skill se considera completada cuando:

* el capítulo propuesto queda trazado con sus fuentes y pendientes; o
* se emite formalmente un `NO_REDACTAR_AUN` o `BLOQUEADO` fundamentado.

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
