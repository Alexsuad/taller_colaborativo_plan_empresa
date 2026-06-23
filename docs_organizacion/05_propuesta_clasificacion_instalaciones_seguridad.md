# 05 — Propuesta de Clasificación de Fuentes: Instalaciones y Seguridad

> **Estado documental:** ABSORBIDO  
> **Sede activa:** `docs_organizacion/01_inventario_fuentes.md`  
> **Uso permitido:** consulta histórica sobre razonamiento inicial de clasificación.  
> **Uso prohibido:** no usar como sede vigente de instalaciones, seguridad, legal o PRL.


**Estado:** Propuesta — Pendiente de aprobación humana.  
**Fecha:** 2026-06-22  
**Autor:** Antigravity  

> [!IMPORTANT]
> **Nota de Control de Gobernanza:** Este documento representa una propuesta estratégica de clasificación. **No se ha movido ninguna fuente de información real** en el sistema de archivos físicos del repositorio. Los movimientos y la importación de contenido real permanecen en suspenso hasta la aprobación explícita de esta propuesta.
> 
> *“Esta propuesta no acredita todavía la existencia, vigencia ni suficiencia de los archivos origen. Antes de mover fuentes reales, debe verificarse que cada archivo existe, que su contenido corresponde al tema y que no está vacío.”*

---

## Objetivo

Definir la política de clasificación y destino de los archivos de origen disponibles en el repositorio madre (`taller_colaborativo/`) hacia las categorías documentales en `docs_fuentes/` que afecten a:
- **Instalaciones, local y requisitos del producto físico** (`docs_fuentes/07_instalaciones_local_producto/`).
- **Seguridad, responsabilidad civil y gestión de accidentes de usuarios** (`docs_fuentes/08_seguridad_responsabilidad_usuarios/`).
- **Aspectos Legales y Normativos** (`docs_fuentes/06_legal_normativo/`).

---

## Tabla de Clasificación de Fuentes (Fase 1.1)

| Archivo Origen (en `taller_colaborativo/`) | Carpeta Destino Propuesta | Tipo de Fuente | Tema Principal | Uso Permitido | Riesgo de Contaminación | Requiere Verificación Externa | Afecta Instalaciones | Afecta Seguridad/ Responsabilidad | Observaciones / Estado de Trabajo |
|---|---|---|---|---|---|---|---|---|---|
| `docs_base/09_matriz_seguridad_y_prevencion.md` | `docs_fuentes/08_seguridad_responsabilidad_usuarios/` | Interna base | Plan de prevención de riesgos y EPIs del taller | Estructurar capacitación, EPIs obligatorios y protocolos | Bajo — fuente interna vacía; requiere completar con evidencia normativa o decisión aprobada. | **Sí** (por mutua o asesor de prevención) | Sí | Sí | Matriz en blanco a rellenar en Fase 2 con normativa específica. |
| `docs_base/08_matriz_permisos_y_licencias.md` | `docs_fuentes/06_legal_normativo/` | Interna base | Licencias municipales y actividad calificada | Identificar requisitos para extracción de polvo y ventilación | Bajo — fuente interna vacía; requiere completar con evidencia normativa o decisión aprobada. | **Sí** (por Ayuntamiento o entidad OCA) | Sí | Sí | Puede referenciarse también desde instalaciones y seguridad si afecta extracción, ventilación, incendios, actividad clasificada o uso de maquinaria. |
| `docs_base/11_matriz_ubicaciones_y_criterios.md` | `docs_fuentes/07_instalaciones_local_producto/` | Interna base | Criterios de layout del local (zonas limpias/sucias) | Definir zonas del taller y accesos para carga/descarga | Bajo — fuente interna vacía; requiere completar con evidencia normativa o decisión aprobada. | No | Sí | No | Define el local como parte de la UX y la propuesta de valor. |
| `docs_investigacion_externa/zaragoza/05_ubicaciones_potenciales.md` | `docs_fuentes/07_instalaciones_local_producto/` | Investigación externa | Locales comerciales disponibles en Zaragoza | Evaluar la accesibilidad, transporte público y precios de alquiler | Bajo — fuente interna vacía; requiere completar con evidencia normativa o decisión aprobada. | **Sí** | Sí | No | Requiere verificación de mercado, disponibilidad, normativa municipal y visita/local real. Precios, disponibilidad, normativa municipal, accesibilidad y condiciones del local cambian con el tiempo. |
| `docs_investigacion_externa/benchmarking_espana/02_tmdc.md` | `docs_fuentes/03_competencia_benchmarking/` | Benchmark | Modelo operativo de taller compartido de carpintería | Analizar capacitación previa y reserva de maquinaria | Bajo | No | Sí | Sí | Referente operativo relevante, no modelo único ni fuente legal. Benchmark operativo, no fuente legal. Sirve para mejores prácticas, no para justificar cumplimiento normativo. |
| `docs_investigacion_externa/benchmarking_europa/03_la_planche.md` | `docs_fuentes/03_competencia_benchmarking/` | Benchmark | Reglas de comunidad y uso de EPIs en taller francés | Aprender sobre normas de seguridad comunitaria | Bajo | No | Sí | Sí | Benchmark operativo, no fuente legal. Sirve para mejores prácticas, no para justificar cumplimiento normativo. |
| “Normativa PRL / lugares de trabajo / primeros auxilios” | `docs_fuentes/06_legal_normativo/` | Legal externa | Seguridad laboral, botiquín y evacuación de locales | Verificar botiquín, primeros auxilios, señalización, emergencias y obligaciones mínimas | Bajo (fuente pública) | **Sí** | Sí | Sí | Base legal obligatoria para el cumplimiento de seguridad en el taller y lugares de trabajo. |
