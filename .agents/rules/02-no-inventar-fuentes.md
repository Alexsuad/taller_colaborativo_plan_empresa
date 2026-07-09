<!-- Adaptado para Taller Colaborativo. Revisado parcialmente para Fase 1. -->

# 02. No Inventar Fuentes ni Datos

- El agente tiene estrictamente **prohibido inventar o alucinar** métricas, costes, fuentes documentales, citas, leyes, o proyecciones financieras.
- Toda afirmación que requiera un respaldo cuantitativo o legal debe tener su base en la biblioteca de Google Drive de Taller, en `docs_fuentes/` cuando existan fuentes reales, en anexos validados, o en referencias protegidas como `COMP-F001` a `COMP-F010` mientras sigan autorizadas.
- `docs_organizacion/01_inventario_fuentes.md` solo actúa como mapa de fuentes, no como evidencia primaria.
- Si un dato requerido no está disponible, el agente **debe marcar el texto explícitamente con "[Pendiente de completar: motivo]"** y notificar al usuario.
- En fases de consolidación, no se puede avanzar si hay un marcador de pendiente, salvo autorización expresa.

## Uso de Drive Taller como biblioteca primaria

La carpeta de Google Drive del Taller es la primera biblioteca documental que debe consultarse para resolver preguntas del Plan de Empresa:
- URL de la Carpeta Drive: https://drive.google.com/drive/folders/1tYj8zsKhIqYkN7GdsKr1VWdw06pbFWcR
- Los documentos de Drive no son texto final. Deben tratarse como borradores, insumos, investigaciones o material bruto.
- **Regla anti-copia**: Está prohibido copiar y pegar contenido bruto de Drive directamente en `respuestas_plan_empresa/`.
- Si una pregunta está respondida en Drive, significa que existe material para resolverla; no significa que el texto esté listo para pegar.
- Todo contenido de Drive debe pasar por extracción, clasificación, depuración, contraste, detección de duplicidades, grado de certeza, síntesis e insumos saneados antes de su redacción controlada final.
- Si Drive contiene versiones repetidas o contradictorias, debe señalarse la contradicción y resolverla en `docs_preparacion/preguntas_resueltas/`, no en el capítulo final.

## Prioridad de Fuentes Internas y Protocolo de Contradicción

1. **Prioridad Documental**:
   `Drive Taller → Repositorio procesado → Alex → Web / investigación externa`
   *NotebookLM queda relegado como apoyo secundario/histórico (legacy), no es fuente prioritaria para trabajo nuevo.*

2. Antes de modificar conclusiones sobre competidores, inspiradores, referentes núcleo, precios, servicios, cursos, bonos, modelo de acceso, marketing, comunicación, cliente objetivo o propuesta de valor, se deben consultar primero:
   - Documentos y borradores brutos de Drive Taller.
   - Fichas internas `COMP-Fxxx` y repositorio procesado.
   - Documentos de `docs_organizacion/`.
   - Historial secundario de NotebookLM si fuera necesario por consistencia.

3. **Si la carpeta Drive no está disponible:**
   - No marcar `REQUIERE_DRIVE = 0` por defecto.
   - Reportar `DRIVE_NO_DISPONIBLE`.
   - Trabajar solo con fuentes volcadas al repositorio y dejar explícito qué queda pendiente de contraste.

4. Las fuentes externas o documentos nuevos sirven para contrastar, no para reemplazar automáticamente una fuente interna revisada.
5. Si una fuente nueva contradice una fuente interna consolidada, no modificar directamente. Reportar la discrepancia, indicar ambas fuentes y pedir decisión del usuario.
6. No modificar fichas `COMP-Fxxx` salvo autorización explícita.
