# Taller Colaborativo - Plan de Empresa

Repositorio para la organización documental y elaboración del plan de empresa del Taller Colaborativo Artesanal en Zaragoza.

Este repositorio está gobernado por una estructura de **4 fases oficiales** para asegurar la calidad y evitar improvisaciones técnicas de maquetación final:

1.  **FASE 1 — Negocio y documentación base:** Identidad de negocio, opción activa y control de fuentes.
2.  **FASE 2 — Diseño del sistema/repositorio:** Estructura de carpetas, matriz de vacíos y límites de palabras.
3.  **FASE 3 — Implementación técnica del sistema:** Configuración del entorno (`uv`, `.venv`), alineación de scripts y validación. *Nota: La Fase 3 no produce ni compila el plan de empresa final.*
4.  **FASE 4 — Producción Editorial, Anexos y Cierre:** Fase dedicada exclusivamente a la producción final de maquetación, gráficos, tablas, portada, índices y exportaciones finales limpias, evitando que estas tareas queden como trabajo manual improvisado al cierre.

## Estructura del Proyecto
- `.agent/`: Reglas y configuraciones de agentes de IA.
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
Para verificar que el plan esté completo, sin marcadores de prueba o textos pendientes:
```bash
uv run python scripts/auditar_estado_plan_empresa.py
```

Para verificar que no existan listas incrustadas ni problemas de formato:
```bash
uv run python scripts/auditar_formato_markdown_entrega.py
```
