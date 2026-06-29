# Taller Colaborativo - Plan de Empresa

Repositorio para la organización documental y elaboración del plan de empresa del Taller Colaborativo Artesanal en Zaragoza.

## Modo LEAN/5S activo

El repositorio está en una fase de limpieza y señalización operativa, no de redacción del plan.

- NotebookLM es la biblioteca documental principal del proyecto.
- `COMP-F001` a `COMP-F010` se conservan como consulta inmediata protegida.
- No se siguen copiando fuentes desde NotebookLM al repositorio.
- La limpieza actual busca clasificar, ordenar y reducir ambigüedad, no borrar masivamente.
- `respuestas_plan_empresa/` sigue congelada hasta la apertura de Gate 1D.
- Durante Fase 1 / Gate 1C solo están operativos `scripts/auditar_estado_plan_empresa.py` y `scripts/auditar_contaminacion_conceptual.py`.
- `scripts/auditar_contaminacion_conceptual.py` se interpreta sobre superficie activa; material pasivo o congelado no debe tratarse como evidencia activa.
- `scripts/auditar_linealidad_plan_empresa.py`, `scripts/compilar_plan_empresa.py`, `scripts/auditar_formato_markdown_entrega.py` y `scripts/auditar_texto_corrupto_entrega.py` son POST-F1 y no operativos ahora.

## Estado de trabajo

Todavía no se redacta el plan de empresa final.

Este repositorio está gobernado por una estructura de **4 fases oficiales** para asegurar la calidad y evitar improvisaciones técnicas de maquetación final:

1.  **FASE 1 — Negocio y documentación base:** Identidad de negocio, opción activa y control de fuentes.
2.  **FASE 2 — Diseño del sistema/repositorio:** Estructura de carpetas, matriz de vacíos y límites de palabras.
3.  **FASE 3 — Implementación técnica del sistema:** Configuración del entorno (`uv`, `.venv`), alineación de scripts y validación. *Nota: La Fase 3 no produce ni compila el plan de empresa final.*
4.  **FASE 4 — Producción Editorial, Anexos y Cierre:** Fase dedicada exclusivamente a la producción final de maquetación, gráficos, tablas, portada, índices y exportaciones finales limpias, evitando que estas tareas queden como trabajo manual improvisado al cierre.

## Estructura del Proyecto
- `.agents/`: Reglas, skills y configuraciones de agentes de IA.
- `docs_control/`: Contrato de identidad, opción activa, reglas de anticontaminación, definición de fases y gates de calidad.
- `docs_manifest/`: Manifiestos de fuentes y clasificación de zonas documentales.
- `plan_empresa_guia/`: Estructura y preguntas guía del plan de empresa.
- `respuestas_plan_empresa/`: Respuestas de trabajo, actualmente vacías/controladas como placeholders.
- `scripts/`: Scripts en Python para compilación y auditoría de linealidad, formato y estado.
- `_build/`: Reportes generados y entregables compilados de Fase 4.

## Requisitos de Entorno
Este proyecto utiliza `uv` como gestor de paquetes y dependencias Python (alineado con la directriz global `python-uv-baseline`).

### Sincronización del Entorno
Para crear el entorno virtual e instalar las dependencias necesarias (`PyYAML`):
```bash
uv sync
```

### Validaciones y Auditoría
En Fase 1 / Gate 1C:
```bash
uv run python scripts/auditar_estado_plan_empresa.py
uv run python scripts/auditar_contaminacion_conceptual.py
```
Las auditorías de linealidad, formato, compilación y texto corrupto quedan para POST-F1 y no deben usarse como validación actual.
