<!-- Adaptado para Taller Colaborativo. Revisado parcialmente para Fase 1. -->

# 02. No Inventar Fuentes ni Datos

- El agente tiene estrictamente **prohibido inventar o alucinar** métricas, costes, fuentes documentales, citas, leyes, o proyecciones financieras.
- Toda afirmación que requiera un respaldo cuantitativo o legal debe tener su base en NotebookLM / fuentes externas citadas, en `docs_fuentes/` cuando existan fuentes reales, en anexos validados, o en referencias protegidas como `COMP-F001` a `COMP-F010` mientras sigan autorizadas.
- `docs_organizacion/01_inventario_fuentes.md` solo actúa como mapa de fuentes, no como evidencia primaria.
- Si un dato requerido no está disponible, el agente **debe marcar el texto explícitamente con "[Pendiente de completar: motivo]"** y notificar al usuario.
- En fases de consolidación, no se puede avanzar si hay un marcador de pendiente, salvo autorización expresa.

## Prioridad de Fuentes Internas y Protocolo de Contradicción

1. Las fuentes internas consolidadas del repositorio tienen prioridad como memoria curada del proyecto.
2. Antes de modificar conclusiones sobre competidores, inspiradores, referentes núcleo, precios, servicios, cursos, bonos, modelo de acceso, marketing, comunicación, cliente objetivo o propuesta de valor, se deben consultar primero:
   - Fichas internas `COMP-Fxxx`.
   - Documentos de `docs_organizacion/`.
   - Extracciones documentales volcadas desde NotebookLM al repositorio.
   - Cuaderno NotebookLM oficial del proyecto (si el acceso está disponible).
3. **Cuaderno NotebookLM oficial del proyecto:**
   - Nombre: `Taller Colaborativo Zaragoza — Organización Documental Marketing`
   - ID: `06898506-212a-4331-86b8-cf11901eb65d`
   - Uso: fuente de contraste y memoria curada para marketing, competencia, inspiradores, propuesta de valor, modelo de acceso, cliente, comunicación y documentación de apoyo del Plan de Empresa.
4. **Si NotebookLM no está disponible:**
   - No asumir que no contiene información.
   - No marcar `REQUIERE_NOTEBOOKLM = 0` por defecto.
   - Reportar `NOTEBOOKLM_NO_DISPONIBLE`.
   - Trabajar solo con fuentes volcadas al repositorio y dejar explícito qué queda pendiente de contraste.
5. Las fuentes externas o documentos nuevos sirven para contrastar, no para reemplazar automáticamente una fuente interna revisada.
6. Si una fuente nueva contradice una fuente interna consolidada, no modificar directamente. Reportar la discrepancia, indicar ambas fuentes y pedir decisión del usuario.
7. No modificar fichas `COMP-Fxxx` salvo autorización explícita.
