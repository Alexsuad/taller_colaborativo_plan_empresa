---

name: preparar-bloque-para-redaccion
description: Prepara un bloque documental listo para redacción futura a partir de una pregunta clasificada, fuentes y decisiones pendientes, sin generar contenido final. Use when a block must be staged before drafting.
---

# Propósito

Usar esta skill para transformar una pregunta ya clasificada en un bloque documental preparado para redacción futura.

La función es dejar el bloque listo para trabajar después, con su evidencia y pendientes claros, sin escribir el texto final del Plan de Empresa.

# Cuándo usar esta skill

Usar cuando se necesite:

* preparar un bloque previo a la redacción;
* reunir la fuente existente, la dependencia del usuario y los vacíos;
* dejar el bloque listo para Gate 1D cuando exista decisión humana posterior;
* ordenar hipótesis, pendientes y nivel de certeza.

# Entradas esperadas

* Ficha de clasificación de la pregunta.
* Fuentes internas candidatas.
* Dependencias del usuario/promotor.
* Estado de certeza o hipótesis.
* Pendientes abiertos.
* Restricciones activas del proyecto.

# Salidas esperadas

Un bloque preparado con, como mínimo:

* ID del bloque;
* título del bloque;
* pregunta asociada;
* fuente base;
* nivel de certeza;
* hipótesis separadas;
* pendientes;
* siguiente paso;
* estado de preparación.

# Procedimiento

1. Confirmar que la pregunta ya está clasificada.
2. Reunir fuentes y dependencias relevantes.
3. Separar dato, hipótesis y pendiente.
4. Construir la estructura del bloque sin redactar contenido final.
5. Marcar el siguiente paso documental.
6. Emitir el bloque preparado para uso futuro.

# Reglas obligatorias

* Esta skill no redacta contenido final del Plan de Empresa.
* Esta skill no abre Gate 1D.
* Esta skill no toca `respuestas_plan_empresa/`.
* Esta skill no decide negocio, marketing, legal, RRSS ni viabilidad.
* Esta skill no convierte hipótesis en hechos.

# Límites / No hacer

No hacer:

* redactar el bloque final;
* mover información a respuestas;
* aprobar Gate 1D;
* inventar datos faltantes;
* crear skills expertas;
* crear subagentes o workflows.

# Criterio de utilidad para Marketing / Producto

La skill debe ayudar a Marketing a:

* dejar el bloque preparado sin escribirlo todavía;
* ver qué falta antes de redactar;
* separar evidencia, hipótesis y pendientes;
* reducir errores al pasar a redacción futura;
* mantener el documento vivo y trazable.

# Criterio de cierre

La skill se considera completada cuando el bloque queda listo para futura redacción, con evidencia y pendientes visibles, sin producir texto final.

# Evidencia esperada

* Bloque preparado.
* Fuente base identificada.
* Hipótesis separadas.
* Pendientes listados.
* Estado de preparación claro.
