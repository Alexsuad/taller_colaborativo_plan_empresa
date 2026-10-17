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

1. **Consulta Obligatoria de Notas y Aclaraciones:**
   Antes de utilizar cualquier fuente o borrador de Drive Taller, el agente debe leer obligatoriamente:
   - `docs_fuentes/drive_taller/00_notas_aclaratorias_vigentes.md`
   - `docs_fuentes/drive_taller/00_indice_fuentes_drive.md`

2. **Prevalencia de Aclaraciones:**
   Si una fuente o documento bruto de Drive contradice una aclaración vigente registrada en `00_notas_aclaratorias_vigentes.md`:
   - Prevalece la aclaración vigente.
   - La fuente original solo puede utilizarse como antecedente histórico o evidencia de una versión anterior. Los documentos brutos originales de Drive no se editan ni borran para adaptarlos al estado actual.
   - Las aclaraciones corrigen la interpretación de fuentes pero no modifican por sí solas el modelo de negocio.

3. **Gobernanza de Pivotajes y Cambios Estratégicos:**
   - Todo cambio que afecte el equipo promotor, servicios, forma jurídica, inversión, precios, ubicación, operaciones o mercado debe registrarse obligatoriamente en `docs_control/05_registro_pivotajes_y_cambios_relevantes.md`.
   - Ningún agente puede aplicar o tratar un pivotaje propuesto como si estuviera aprobado. Solo se aplicarán aquellos con estado `aprobado` validado por el promotor.
   - Un pivotaje aprobado debe generar obligatoriamente un **Análisis de Impacto** antes de realizar cualquier modificación documental.
   - El análisis de impacto debe identificar con precisión: capítulos afectados en respuestas, documentos de preparación, documentos legales, archivo/Excel financiero, anexos, decisiones y supuestos que deben recalcularse o actualizarse.

4. **Prioridad Documental:**
   `Drive Taller → Repositorio procesado → Alex → Web / investigación externa`
   *NotebookLM queda relegado como apoyo secundario/histórico (legacy), no es fuente prioritaria para trabajo nuevo.*

5. **Si la carpeta Drive no está disponible:**
   - No marcar `REQUIERE_DRIVE = 0` por defecto.
   - Reportar `DRIVE_NO_DISPONIBLE`.
   - Trabajar solo con fuentes volcadas al repositorio y dejar explícito qué queda pendiente de contraste.

6. **Normas de Contradicción General:**
   - Las fuentes externas sirven para contrastar, no para reemplazar de forma automática una fuente interna revisada.
   - Si una fuente nueva contradice una fuente consolidada o aclaración vigente, reportar la discrepancia y pedir decisión al promotor.
   - No modificar fichas `COMP-Fxxx` ni documentos históricos del repositorio.
