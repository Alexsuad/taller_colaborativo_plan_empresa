# PT-10O — Sistema repo primero / NotebookLM después

## 1. Propósito

PT-10O define el protocolo operativo para usar NotebookLM sin desplazar al repositorio como fuente principal de trabajo.

La regla base es simple:

- Repositorio primero.
- NotebookLM después.

## 2. Alcance

Este documento no es un inventario de fuentes.
No es una extracción de NotebookLM.
No es un gate.
No es una skill.
No es un workflow.
No es un subagente.

Su función es fijar el orden correcto de consulta y evitar que NotebookLM se convierta en autoridad primaria.

## 3. Protocolo operativo

1. Buscar primero en el repositorio.
2. Comprobar si el hueco ya está resuelto en documentos, matrices, reportes o skills.
3. Si el repo responde, no salir fuera.
4. Si el repo no responde, preparar una consulta controlada a NotebookLM.
5. Validar cualquier salida de NotebookLM antes de usarla.
6. Integrar solo lo que esté verificado y trazado.

## 4. Reglas de uso

- NotebookLM no decide.
- NotebookLM no modifica el repo automáticamente.
- NotebookLM no abre Gate 1D.
- NotebookLM no rellena `respuestas_plan_empresa/`.
- NotebookLM no justifica crear MCP ahora.
- MCP no se crea por defecto.

## 5. Cuándo usarlo

Usar este protocolo cuando aparezca un hueco documental, una duda de negocio o una necesidad de contraste y primero haya que comprobar si el propio repo ya contiene la respuesta.

## 6. Qué no hace

- No sustituye a `PT-10L`.
- No sustituye a gates.
- No sustituye a scripts.
- No sustituye a skills.
- No sustituye a la revisión humana.
- No convierte NotebookLM en fuente única viva.

## 7. Siguiente paso

Si este protocolo queda aprobado, el siguiente PT recomendado es:

- `PT-10P — Skill preparar consulta NotebookLM controlada`

## 8. Dictamen final

- `PT_10O_COMPLETO`

Estado final:

- documento de control operativo;
- sin duplicar inventarios ni extracciones;
- deja claro que el repositorio manda y NotebookLM solo complementa.
