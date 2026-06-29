# 01 — Inventario consolidado de fuentes y uso permitido

**Estado:** Aprobado como inventario oficial provisional operativo.
**Fase:** Fase 1.1.B — Gate 1B completado provisionalmente.
**Fecha:** 2026-06-23.
**Nota de alcance:** Este inventario no importa fuentes reales, no valida definitivamente el contenido de las fuentes, no autoriza redacción del plan, no autoriza poblar `respuestas_plan_empresa/`, no autoriza crear `docs_consolidados/`, no cierra Gate 1C ni abre Gate 1D.

> [!IMPORTANT]
> Este documento consolida diagnósticos previos y el manifest original (`docs_manifest/01_manifest_fuentes_y_uso_permitido.md`). Ningún archivo fuente real se ha movido, copiado ni modificado. Este inventario es provisional operativo, no importa fuentes reales, no valida definitivamente el contenido y no autoriza redacción del plan, poblar `respuestas_plan_empresa/` ni crear `docs_consolidados/`.

---

## 1. Categorías de fuentes

| Categoría | Definición | Ejemplos en este inventario |
|---|---|---|
| Fuentes legales / normativas | Documentos sobre licencias, permisos, seguridad, forma jurídica, normativa o responsabilidad | PUENTE-023, PUENTE-024, PUENTE-028 |
| Fuentes de mercado | Estudios, informes y análisis sobre demanda, tendencias, sector artesanal, clientes o comportamiento de consumidores | PUENTE-020, PUENTE-021, PUENTE-022 |
| Fuentes de competencia | Benchmarks operativos, investigaciones de competidores y referentes nacionales/internacionales | PUENTE-009 a PUENTE-019, INV-023 a INV-040 |
| Fuentes económicas / financieras | Datos o proyecciones sobre activos, inversión, CAPEX/OPEX, precios, ingresos, estructura económica | PUENTE-027, INV-011 |
| Fuentes internas y antecedentes propios del proyecto | Documentación propia vigente o antecedentes internos que requieren reconciliación antes de alimentar el plan | INT-001 a INT-003 |
| Fuentes metodológicas | Guías, plantillas, reglas de trabajo, lecciones aprendidas, gobernanza, fases, gates | PUENTE-001, PUENTE-005 a PUENTE-008, INV-001, INV-003, INV-004, INV-006 |
| Fuentes legacy no reutilizables como contenido | Documentos históricos, casos de otros proyectos o antecedentes que **no pueden copiarse** como respuesta del plan | PUENTE-002, PUENTE-003, PUENTE-004, PUENTE-025, PUENTE-026, INV-015 a INV-017 |

---

## 2. Escala de uso permitido

| Código | Uso permitido | Significado operativo |
|---|---|---|
| `citar` | Citar | Se puede mencionar como referencia, con atribución. No se copia contenido. |
| `resumir` | Resumir | Se puede sintetizar o parafrasear, con atribución. No se transcribe literalmente. |
| `extraer_estructura` | Extraer estructura / preguntas | Se pueden tomar índices, preguntas guía, plantillas o esquemas. No se copian respuestas ni datos de negocio. |
| `referencia_metodologica` | Usar como referencia metodológica | Se usan fases, gates, controles, reglas de calidad o gobernanza. No se usa para contenido de negocio. |
| `usar_parcialmente` | Usar parcialmente | Se pueden tomar partes específicas, verificadas y etiquetadas, con cautela. |
| `no_usar_directo` | No usar directamente como contenido | Se puede consultar para contexto, pero no alimenta respuestas del plan. |

---

## 3. Inventario consolidado por categoría

### 3.1 Fuentes metodológicas

| ID | Nombre | Origen | Contenido real | Uso permitido | Uso prohibido | Riesgo | Estado |
|---|---|---|---|---|---|---|---|
| MET-001 | Guía elaboración Plan de Negocio (Red ARCE 2018) | Externa (`/mnt/data/`) | Sí | `extraer_estructura` | Copiar datos del Taller | Bajo | Activa — pendiente de importación |
| MET-002 | Documento maestro lecciones aprendidas v1.3 | Externa (`/mnt/data/`) | Sí | `referencia_metodologica` | Sustituir decisiones humanas | Bajo | Activa — pendiente de importación |
| MET-003 | Consolidado aprendizajes fuentes Taller Colaborativo | Externa (`/mnt/data/`) | Sí | `referencia_metodologica` | Invertir recomendaciones como verdad | Bajo | Activa — pendiente de importación |
| MET-004 | Chat Análisis documentación | Externa (Google Drive) | Sí | `referencia_metodologica` | Usar como verdad final | Medio | Activa — pendiente de importación |
| MET-005 | Perfil de Marketing Estratégico | Externa (`/mnt/data/`) | Sí | `referencia_metodologica` | Usar como fuente de mercado; solo como criterio de revisión | Medio | Activa — pendiente de importación |
| MET-006 | Reglas del proyecto (repo madre `docs_base/00_`) | Referencia metodológica externa depurada | Sí | `referencia_metodologica` | Imponer arquitectura técnica prematura | Bajo | Activa — diagnosis en repo madre |
| MET-007 | Matriz hipótesis y validación H01–H14 | Referencia metodológica externa depurada | Sí | `extraer_estructura` | Presentar hipótesis como hechos | Medio | Activa — diagnosis en repo madre |
| MET-008 | Matriz preguntas clasificadas | Referencia metodológica externa depurada | Sí | `extraer_estructura` | Copiar respuestas | Bajo | Activa — diagnosis en repo madre |
| MET-009 | Plan de implementación (repo madre `docs_base/04_`) | Referencia metodológica externa depurada | Sí | `referencia_metodologica` | Sustituir las 4 fases oficiales | Medio | Activa — solo referencia, no sustituye fases oficiales |

### 3.2 Fuentes internas y antecedentes propios del proyecto

| ID | Nombre | Origen | Contenido real | Uso permitido | Uso prohibido | Riesgo | Estado |
|---|---|---|---|---|---|---|---|
| INT-001 | Documentación propia del Taller (pendiente de clasificar) | Proyecto actual | Pendiente | `usar_parcialmente` tras clasificación | Usar sin clasificar previo | Bajo | Pendiente de importación y clasificación |
| INT-002 | Decisiones clave D01–D20, P01–P08 | Referencia metodológica externa depurada | Sí | `citar` / `resumir` | Copiar decisiones sin reconciliar | Medio | Requiere reconciliación con decisiones de este repo |
| INT-003 | Matriz verdad 2023 vs 2026 | Referencia metodológica externa depurada | Sí | `extraer_estructura` | Reactivar modelo rural como vigente | Bajo | Activa — clave para separar histórico de vigente |

### 3.3 Fuentes legales / normativas

| ID | Nombre | Origen | Contenido real | Uso permitido | Uso prohibido | Riesgo | Requiere verificación externa | Estado |
|---|---|---|---|---|---|---|---|---|
| LEG-001 | Taller Artesanal: Viabilidad y Marco Legal | Externa (`/mnt/data/`) | Sí | `usar_parcialmente` | Tratar como dictamen legal definitivo | Alto | Sí (Ayuntamiento / asesoría legal / PRL) | Pendiente de importación |
| LEG-002 | Requisitos taller carpintería Zaragoza | Externa (`/mnt/data/`) | Sí | `usar_parcialmente` como checklist | Sustituir verificación profesional | Alto | Sí (normativa vigente) | Pendiente de importación |
| LEG-003 | Taller Artesanal Zaragoza: Guía Completa | Externa (Google Drive) | Sí | `usar_parcialmente` | Copiar sin separar hechos de recomendaciones | Medio-Alto | Sí | Pendiente de importación |

### 3.4 Fuentes de mercado

| ID | Nombre | Origen | Contenido real | Uso permitido | Uso prohibido | Riesgo | Requiere verificación externa | Estado |
|---|---|---|---|---|---|---|---|---|
| MER-001 | Market for Craft full report 2020 (PDF) | Externa (`/mnt/data/`) | Sí | `resumir` tendencias y contexto | Extrapolar cifras UK a Zaragoza | Medio | Sí (datos 2020, no actuales) | Pendiente de importación |
| MER-002 | Estudio de Mercado sobre artesanía (PDF) | Externa (`/mnt/data/`) | Sí | `resumir` metodología y contexto sectorial | Usar datos sin verificar vigencia | Medio | Sí (requiere fecha exacta) | Pendiente de importación |
| MER-003 | Fatiga Digital (TXT) | Externa (`/mnt/data/`) | Sí | `citar` como hipótesis/tendencia | Usar cifras sin comprobar trazabilidad | Alto | Sí (fuentes no trazables) | Pendiente de importación |

### 3.5 Fuentes de competencia

| ID | Nombre | Origen | Contenido real | Uso permitido | Uso prohibido | Riesgo | Requiere verificación externa | Estado |
|---|---|---|---|---|---|---|---|---|
| COMP-001 | Análisis de Competencia (XLSX) | Externa (`/mnt/data/`) | Sí | `usar_parcialmente` tras revisión | Copiar sin verificar hojas/metadatos | Medio | Sí | Pendiente de importación |
| COMP-002 | TMDC — Investigación | Externa (`/mnt/data/`) | Sí | `citar` como referente | Copiar modelo sin validación local | Medio | Sí | Pendiente de importación |
| COMP-003 | The CoMAKING Space — Investigación | Externa (`/mnt/data/`) | Sí | `citar` como referente operativo | Copiar modelo industrial pesado | Medio | Sí | Pendiente de importación |
| COMP-004 | A tu Madera — Investigación | Externa (`/mnt/data/`) | Sí | `citar` como referente prioritario Zaragoza | Tratar tarifas como precios propios | Medio | Sí (tarifas actuales) | Pendiente de importación |
| COMP-005 | T11 Sevilla (Tejares 11) — Investigación | Externa (`/mnt/data/`) | Sí | `citar` como referente estratégico | Copiar sin distinguir interpretación de dato | Medio | Sí | Pendiente de importación |
| COMP-006 | Cara y Canto — Investigación | Externa (`/mnt/data/`) | Sí | `usar_parcialmente` (pricing, servicios) | Copiar tarifas sin verificar vigencia | Medio | Sí | Pendiente de importación |
| COMP-007 | Análisis Competitivo Coworking Madera Aragón | Externa (Google Drive) | Sí | `usar_parcialmente` tras separar hechos/hipótesis | Afirmar ausencia de competencia sin verificación | Medio | Sí | Pendiente de importación |
| COMP-008 | Informe de Inteligencia Competitiva y Alianzas | Externa (`/mnt/data/`) | Sí | `usar_parcialmente` como base preliminar | Afirmaciones absolutas sin verificar | Medio | Sí | Pendiente de importación |
| COMP-009 | Referente Estratégico T11 para Zaragoza | Externa (Google Drive) | Sí | `citar` como análisis secundario | Usar como fuente primaria | Medio-Alto | Sí | Pendiente de importación |
| COMP-010 | T11 Sevilla: Análisis y Comparativa | Externa (Google Drive) | Sí | `citar` como análisis complementario | Posible duplicado con COMP-005/COMP-009 | Medio-Alto | Sí | Pendiente de importación — requiere verificación de duplicados |
| COMP-011–023 | Benchmarks nacionales (repo madre, 13 archivos) | Referencia metodológica externa depurada | No (vacíos) | `citar` cuando tengan contenido | Usar sin contenido verificado | Bajo | Sí (todos vacíos hoy) | Placeholders — sin contenido |
| COMP-024–028 | Benchmarks Europa (repo madre, 5 archivos) | Referencia metodológica externa depurada | No (vacíos) | `citar` cuando tengan contenido | Usar sin contenido verificado | Bajo | Sí (todos vacíos hoy) | Placeholders — sin contenido |

### 3.6 Fuentes económicas / financieras

| ID | Nombre | Origen | Contenido real | Uso permitido | Uso prohibido | Riesgo | Requiere verificación externa | Estado |
|---|---|---|---|---|---|---|---|---|
| ECO-001 | Activos Fijos Coworking (XLSX) | Externa (`/mnt/data/`) | Sí | `usar_parcialmente` tras revisión | Usar precios sin fecha/proveedor | Medio | Sí (precios actuales) | Pendiente de importación |
| ECO-002 | Matriz modelos de ingreso (repo madre) | Referencia metodológica externa depurada | No (vacío) | `extraer_estructura` cuando tenga contenido | Copiar cifras sin validar | Medio | Sí | Placeholder — sin contenido |

### 3.7 Fuentes de ecosistema Zaragoza / Aragón

| ID | Nombre | Origen | Contenido real | Uso permitido | Uso prohibido | Riesgo | Requiere verificación externa | Estado |
|---|---|---|---|---|---|---|---|---|
| ZAR-001 | Ecosistema creativo Zaragoza | Repo madre | No (vacío) | `usar_parcialmente` cuando tenga contenido | Afirmar sin verificar | Bajo | Sí | Placeholder |
| ZAR-002 | Formación y FP | Repo madre | No (vacío) | `usar_parcialmente` cuando tenga contenido | Afirmar sin verificar | Bajo | Sí | Placeholder |
| ZAR-003 | Restauración y tapicería | Repo madre | No (vacío) | `usar_parcialmente` cuando tenga contenido | Afirmar sin verificar | Bajo | Sí | Placeholder |
| ZAR-004 | Movilidad y radio de captación | Repo madre | No (vacío) | `usar_parcialmente` cuando tenga contenido | Afirmar sin verificar | Medio | Sí | Placeholder |
| ZAR-005 | Ubicaciones potenciales | Repo madre | No (vacío) | `no_usar_directo` hasta verificación extrema | Cerrar ubicación sin visita ni validación de precios | Alto | Sí (precios cambian) | Placeholder — alto riesgo de vigencia |

### 3.8 Fuentes legacy — NO reutilizables como contenido

| ID | Nombre | Origen | Contenido real | Uso permitido | Uso prohibido | Riesgo | Estado |
|---|---|---|---|---|---|---|---|
| LEG-LEGACY-001 | Caso legacy no reutilizable como contenido (V2) — Plan empresa | Externa (Google Drive) | Sí | `extraer_estructura` (preguntas guía) | **Copiar respuestas, narrativa, cifras o modelos de negocio** | Alto | Activa — cuarentena |
| LEG-LEGACY-002 | Proyecto taller colaborativo.docx (base rural) | Externa (`/mnt/data/`) | Sí | `citar` como origen fundacional | **Usar supuestos de mercado antiguos; reactivar enfoque rural** | Alto | Pendiente de importación — etiquetar como histórico |
| LEG-LEGACY-003 | Co Working Artesanal 2 pueblos (PDF) | Externa | Sí | `no_usar_directo` | **Copiar cualquier contenido** como base del modelo vigente | Crítico | Activa — cuarentena |
| LEG-LEGACY-004 | Guía de Ayudas para Emprendedores (PDF, 2022) | Externa (`/mnt/data/`) | Sí | `citar` como ejemplo de estructura de búsqueda | **Usar convocatorias caducadas como vigentes** | Alto | Activa — solo referencia histórica |
| LEG-LEGACY-005 | Convocatoria LEADER 2-2021 (PDF) | Externa (`/mnt/data/`) | Sí | `citar` como ejemplo documental de expediente | **Usar como ayuda vigente; es de otra geografía y plazo** | Crítico | Activa — cuarentena |
| LEG-LEGACY-006–008 | Base original 2023 (3 archivos, repo madre) | Referencia metodológica externa depurada | No (vacíos) | `no_usar_directo` | **Alimentar mercado, cliente, operaciones o estrategia vigente** | Alto | Placeholders — en `docs_fuentes/11_legacy_no_usar_directo/` |

---

## 4. Fuentes NO presentes — requieren creación o investigación

| ID | Tema | Carpeta destino | Estado | Prioridad |
|---|---|---|---|---|
| NUEVA-001 | Matriz ODS e impacto | `docs_fuentes/01_base_metodologica/` | Por crear | Media |
| NUEVA-002 | Matriz de riesgos del proyecto | `docs_fuentes/01_base_metodologica/` | Por crear | Alta |
| NUEVA-003 | Matriz de permisos y licencias (verificada) | `docs_fuentes/06_legal_operativo/` | Por crear — requiere verificación profesional | Alta |
| NUEVA-004 | Matriz de seguridad y prevención (PRL) | `docs_fuentes/08_seguridad_responsabilidad_usuarios/` | Por crear — requiere asesor PRL | Alta |
| NUEVA-005 | Matriz de modelos de ingreso (con datos propios) | `docs_fuentes/09_finanzas_activos/` | Por crear | Alta |
| NUEVA-006 | Matriz de ubicaciones y criterios (con visitas) | `docs_fuentes/07_instalaciones_local_producto/` | Por crear — requiere visitas | Alta |
| NUEVA-007 | Glosario del proyecto | `docs_fuentes/01_base_metodologica/` | Por crear | Baja |

---

## 5. Resumen cuantitativo

| Categoría | Fuentes con contenido | Placeholders / vacíos | Total |
|---|---:|---:|---:|
| Fuentes metodológicas | 7 | 2 | 9 |
| Fuentes internas y antecedentes propios del proyecto | 2 | 1 | 3 |
| Fuentes legales / normativas | 3 | 0 | 3 |
| Fuentes de mercado | 3 | 0 | 3 |
| Fuentes de competencia | 10 | 18 | 28 |
| Fuentes económicas / financieras | 1 | 1 | 2 |
| Fuentes ecosistema Zaragoza / Aragón | 0 | 5 | 5 |
| Fuentes legacy no reutilizables | 3 | 3 | 6 |
| Fuentes por crear | — | — | 7 |
| **TOTAL** | **29** | **30** | **66** |

---

## 6. Regla general de uso

```text
1. Ninguna fuente externa se copia literalmente como respuesta del plan.
2. Las fuentes legales requieren verificación profesional antes de alimentar el plan.
3. Las fuentes legacy (LEG-LEGACY-*) NO pueden usarse como contenido del plan, solo como referencia.
4. Los benchmarks (COMP-*) NO son fuentes legales y NO justifican cumplimiento normativo.
5. Las fuentes vacías (placeholders) NO alimentan el plan hasta tener contenido real verificado.
6. Las fuentes metodológicas (MET-*) alimentan gobernanza y estructura, no respuestas de negocio.
7. Las fuentes de mercado (MER-*) se usan para tendencias y contexto; no se extrapolarán cifras geográficas.
8. Tras aprobación humana, este documento será la fuente de verdad del inventario (`01_inventario_fuentes.md`).
```

---

## 7. Relación con documentos complementarios

| Documento | Rol | Relación con este inventario |
|---|---|---|
| Diagnósticos previos absorbidos | Diagnóstico técnico y puente de fuentes | Consolidados aquí |
| `docs_manifest/01_manifest_fuentes_y_uso_permitido.md` | Manifest resumido de políticas de uso | Se mantiene como manifiesto de políticas; este documento lo expande |
| `docs_control/03_gates_documentales.md` | Gates del proyecto | Gate 1B usa este inventario como criterio de cierre |
