# 06 — Propuesta de Inventario General de Fuentes

**Estado:** Propuesta — Pendiente de revisión y aprobación humana.  
**Fase:** Fase 1.1 — Inventario y clasificación de fuentes reales.  
**Autor:** Codex (agente técnico-documental).  
**Fecha:** 2026-06-22.

> [!IMPORTANT]
> **Nota de control de gobernanza:** Este documento es una **propuesta**. No se ha movido, copiado, modificado ni eliminado ningún archivo de fuente real. Ninguna decisión de negocio se introduce aquí. La aprobación de esta propuesta por parte de Alex es condición previa para cualquier acción física sobre archivos.

> [!WARNING]
> **Hallazgo crítico de la inspección:** De los ~100 archivos identificados como "fuentes" en el repositorio madre (`taller_colaborativo/`), **solo 6 archivos contienen información real** y todos están dentro de `docs_base/`. El resto (incluidas todas las "fuentes del proyecto" y toda la "investigación externa" de benchmarking y Zaragoza) **son archivos vacíos de 0 bytes** que actúan como **marcadores de localización**. Esto debe confirmarse o corregirse antes de avanzar.

---

## 1. Objetivo de la propuesta

Construir un inventario único, trazable y clasificado de **todas las fuentes reales disponibles** (o previstas) para alimentar el plan de empresa, respetando:

- la cadena documental obligatoria (fuente cruda → clasificación → matriz → consolidado → respuesta → auditoría → final);
- las reglas de anticontaminación;
- el criterio de que el local es parte del producto y la seguridad es estructural;
- la separación entre hechos e hipótesis y entre fuentes vigentes e históricas.

La propuesta **no mueve fuentes**. Solo propone destino, uso permitido, riesgo y verificación.

---

## 2. Alcance de la inspección

Se han inspeccionado dos ubicaciones:

1. **Repositorio actual** (`taller_colaborativo_plan_empresa/`):  
   - `docs_fuentes/` (01–11): **todas las carpetas están vacías**, solo contienen `.gitkeep`. Sin fuentes todavía.
2. **Repositorio madre** (`../taller_colaborativo/`): contiene el esqueleto documental completo del proyecto previo. Se inspeccionaron todas sus carpetas y el respaldo `.zip`.

### 2.1 Recuento físico del repo madre

| Carpeta (repo madre) | Archivos totales | Archivos con contenido | Archivos vacíos (0 B) |
|---|---:|---:|---:|
| `docs_base/` | 14 | 6 | 8 |
| `docs_control/` | 8 | 0 | 8 |
| `docs_fuentes_proyecto/` | 12 | 0 | 12 |
| `docs_investigacion_externa/` | 23 | 0 | 23 |
| `plan_empresa/` | 18 | 0 | 18 |
| `respuestas_plan_empresa/` | 18 | 0 | 18 |
| `anexos/` | 11 | 0 | 11 |
| `_build/` | 4 | 0 | 4 |
| Raíz + `.agents/rules/` | 6 | 6 | 0 |
| **TOTAL** | **114** | **12** | **102** |

El respaldo `taller_colaborativo_2026-06-02_18-00-24.zip` (37 KB) es **idéntico** al estado actual del repo madre: las fuentes vacías ya estaban vacías en el momento del respaldo. **No existe una versión "con contenido" conocida en el repositorio.**

---

## 3. Categorías documentales vigentes de destino (en este repo)

```text
docs_fuentes/01_base_metodologica/
docs_fuentes/02_identidad_y_origen/
docs_fuentes/03_mercado_y_tendencias/
docs_fuentes/04_competencia_benchmarking/
docs_fuentes/05_zaragoza_aragon_ecosistema/
docs_fuentes/06_legal_operativo/
docs_fuentes/07_instalaciones_local_producto/
docs_fuentes/08_seguridad_responsabilidad_usuarios/
docs_fuentes/09_finanzas_activos/
docs_fuentes/10_ayudas_financiacion/
docs_fuentes/11_legacy_no_usar_directo/
```

---

## 4. Clasificaciones de uso permitido

```text
USAR COMO BASE
USAR PARCIALMENTE
USAR SOLO COMO REFERENCIA
PENDIENTE DE VERIFICACIÓN
CUARENTENA / HISTÓRICO
NO USAR EN PLAN FINAL
```

---

## 5. Tabla de inventario y clasificación propuesta

Convención de estado físico:  
- `[VACÍO]` = 0 bytes, no usable hasta ser poblado.  
- `[CON CONTENIDO]` = archivo con información real inspeccionada.  
- `[N/A]` = no aplica (documento a crear en fases posteriores).

### 5.1 Bloque base metodológica e identidad (repo madre `docs_base/` con contenido)

| ID | Archivo origen | Ruta actual | Nombre documental | Tipo de fuente | Tema principal | Carpeta destino propuesta | Uso permitido | Riesgo contaminación | Vigencia | Verificación externa | Duplicados / relacionados | Estado del archivo | Observaciones |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INV-001 | `docs_base/00_reglas_del_proyecto.md` | repo madre | Reglas del proyecto (verdad temporal, no invención, clasificación previa, hipótesis vs hechos, foco fase 1, benchmarking, legal estructural, ayudas, foco) | Metodológica interna | Reglas de gobierno del proceso | `docs_fuentes/01_base_metodologica/` | USAR COMO BASE | Bajo — metodología propia | Vigente 2026 | No | Relacionado con `docs_control/02_reglas_anticontaminacion.md` y matriz 2023 vs 2026 | [CON CONTENIDO] | Base rectora del repo madre. Coincide en espíritu con `docs_control/` de este repo. |
| INV-002 | `docs_base/01_matriz_verdad_2023_vs_2026.md` | repo madre | Matriz verdad 2023 vs 2026 | Metodológica interna | Regla de vigencia: 2023 = alma, 2026 = vigente | `docs_fuentes/02_identidad_y_origen/` | USAR COMO BASE | Bajo | Vigente 2026 | No | Vinculada a D16 (decisiones clave) y a `docs_control/01_opcion_activa_taller.md` | [CON CONTENIDO] | Define el pivote rural→Zaragoza. Clave para separar histórico de vigente. |
| INV-003 | `docs_base/02_matriz_hipotesis_y_validacion.md` | repo madre | Matriz de hipótesis y validación (H01–H14) | Metodológica interna | Estado de validación de hipótesis | `docs_fuentes/01_base_metodologica/` | USAR COMO BASE | Medio — riesgo de presentar hipótesis como hechos | Vigente 2026 | Sí (validaciones de mercado, cliente, ubicación) | Relacionada con `docs_organizacion/02_matriz_preguntas_fuentes_vacios.md` | [CON CONTENIDO] | Impone disciplina: nada pasa a "validada" por intuición. |
| INV-004 | `docs_base/03_matriz_preguntas_clasificadas.md` | repo madre | Matriz de preguntas clasificadas `[F]/[U]/[I-SIMPLE]/[I-DEEP]/[M]/[NO-RESPONDER-AÚN]` | Metodológica interna | Clasificación previa a redacción | `docs_fuentes/01_base_metodologica/` | USAR COMO BASE | Bajo | Vigente 2026 | Según clasificación | Vinculada a `plan_empresa_guia/` y a `respuestas_plan_empresa/` | [CON CONTENIDO] | Es el puente con la guía de preguntas del plan actual. |
| INV-005 | `docs_base/05_decisiones_clave.md` | repo madre | Decisiones clave D01–D20 + pendientes P01–P08 | Decisión interna | Decisiones tomadas / provisionales / pendientes | `docs_fuentes/02_identidad_y_origen/` | USAR COMO BASE | Medio — algunas decisiones podrían haber evolucionado | Vigente 2026 | Sí (P01–P08 requieren validación) | Cruzar con `docs_organizacion/04_decisiones_pendientes.md` | [CON CONTENIDO] | **Requiere reconciliación** con DP-001/002/003 de este repo. |
| INV-006 | `docs_base/04_plan_de_implementacion.md` | repo madre | Plan de implementación del proceso (Fases 1–11, sprints) | Metodológica interna | Hoja de ruta del proceso | `docs_fuentes/01_base_metodologica/` | USAR SOLO COMO REFERENCIA | Medio — estructura de fases distinta a las 4 fases oficiales de este repo | Vigente 2026 como referencia | No | Comparar con `docs_control/06_fases_oficiales_proyecto.md` | [CON CONTENIDO] | **No sustituye** a las 4 fases oficiales. Sirve de insumo metodológico. |

### 5.2 Bloque base metodológica (repo madre `docs_base/` vacío — placeholders)

| ID | Archivo origen | Ruta actual | Nombre documental | Tipo de fuente | Tema principal | Carpeta destino propuesta | Uso permitido | Riesgo contaminación | Vigencia | Verificación externa | Duplicados / relacionados | Estado del archivo | Observaciones |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INV-007 | `docs_base/06_matriz_ods_e_impacto.md` | repo madre | Matriz ODS e impacto | Interna base | Impacto social, circularidad, igualdad | `docs_fuentes/01_base_metodologica/` | PENDIENTE DE VERIFICACIÓN | Bajo | Pendiente | No | Vinculada a D15 | [VACÍO] | Solo estructura. Requiere redacción en fase posterior. |
| INV-008 | `docs_base/07_matriz_riesgos_del_proyecto.md` | repo madre | Matriz de riesgos del proyecto | Interna base | Riesgos operativos, legales, financieros | `docs_fuentes/01_base_metodologica/` | PENDIENTE DE VERIFICACIÓN | Medio | Pendiente | Sí (riesgos legales y operativos) | Cruzar con `anexos/A09_...` | [VACÍO] | Estructural para capítulo de viabilidad. |
| INV-009 | `docs_base/08_matriz_permisos_y_licencias.md` | repo madre | Matriz de permisos y licencias | Interna base | Licencias municipales, actividad clasificada | `docs_fuentes/06_legal_operativo/` | PENDIENTE DE VERIFICACIÓN | Bajo | Pendiente | **Sí** (Ayuntamiento / OCA) | Ver `05_propuesta_clasificacion...` fila 2 | [VACÍO] | Ya clasificada en `docs_organizacion/05_...` (fila de `08_matriz_permisos...`). |
| INV-010 | `docs_base/09_matriz_seguridad_y_prevencion.md` | repo madre | Matriz de seguridad y prevención (PRL, EPIs) | Interna base | Prevención de riesgos, EPIs, protocolos | `docs_fuentes/08_seguridad_responsabilidad_usuarios/` | PENDIENTE DE VERIFICACIÓN | Bajo | Pendiente | **Sí** (mutua / asesor prevención) | Ver `05_propuesta_clasificacion...` fila 1 | [VACÍO] | Ya clasificada en `docs_organizacion/05_...`. |
| INV-011 | `docs_base/10_matriz_modelos_de_ingreso.md` | repo madre | Matriz de modelos de ingreso | Interna base | Ingresos principal/complementario/futuro | `docs_fuentes/09_finanzas_activos/` | PENDIENTE DE VERIFICACIÓN | Medio | Pendiente | Sí (validación comercial) | Vinculada a D10/D11 y a P02 | [VACÍO] | Define arquitectura de ingresos. |
| INV-012 | `docs_base/11_matriz_ubicaciones_y_criterios.md` | repo madre | Matriz de ubicaciones y criterios | Interna base | Criterios de layout, zonas limpias/sucias, accesos | `docs_fuentes/07_instalaciones_local_producto/` | PENDIENTE DE VERIFICACIÓN | Bajo | Pendiente | No | Ver `05_propuesta_clasificacion...` fila 3 | [VACÍO] | Trata el local como producto/UX. |
| INV-013 | `docs_base/12_fuentes_maestras_del_proyecto.md` | repo madre | Fuentes maestras del proyecto | Índice interno | Listado maestro de fuentes | `docs_organizacion/01_inventario_fuentes.md` (ya existe) | USAR SOLO COMO REFERENCIA | Bajo | Pendiente | No | Función similar a este documento | [VACÍO] | Posible duplicado funcional con `01_inventario_fuentes.md`. |
| INV-014 | `docs_base/13_glosario_del_proyecto.md` | repo madre | Glosario del proyecto | Interna base | Terminología común | `docs_fuentes/01_base_metodologica/` | PENDIENTE DE VERIFICACIÓN | Bajo | Pendiente | No | — | [VACÍO] | Útil para coherencia terminológica. |

### 5.3 Bloque identidad y origen (repo madre `docs_fuentes_proyecto/2023_base_original/`)

| ID | Archivo origen | Ruta actual | Nombre documental | Tipo de fuente | Tema principal | Carpeta destino propuesta | Uso permitido | Riesgo contaminación | Vigencia | Verificación externa | Duplicados / relacionados | Estado del archivo | Observaciones |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INV-015 | `docs_fuentes_proyecto/2023_base_original/proyecto_taller_colaborativo_2023.md` | repo madre | Proyecto Taller Colaborativo 2023 (base rural) | Interna histórica | Espíritu fundacional, contexto rural | `docs_fuentes/11_legacy_no_usar_directo/` | CUARENTENA / HISTÓRICO | **Alto** — contexto rural no vigente | Histórica 2023 | No | Vinculado a INV-002 (matriz verdad) | [VACÍO] | **Solo como alma fundacional.** No usar para decisiones operativas. |
| INV-016 | `docs_fuentes_proyecto/2023_base_original/presentacion_rural_2023.md` | repo madre | Presentación rural 2023 | Interna histórica | Pitch en contexto rural | `docs_fuentes/11_legacy_no_usar_directo/` | CUARENTENA / HISTÓRICO | Alto | Histórica 2023 | No | — | [VACÍO] | Mismo criterio que INV-015. |
| INV-017 | `docs_fuentes_proyecto/2023_base_original/notas_resumen_2023.md` | repo madre | Notas resumen 2023 | Interna histórica | Resumen del proyecto original | `docs_fuentes/11_legacy_no_usar_directo/` | CUARENTENA / HISTÓRICO | Medio | Histórica 2023 | No | — | [VACÍO] | Rescatar solo ideas fundacionales vigentes. |

### 5.4 Bloque mercado y tendencias (repo madre `docs_fuentes_proyecto/2026_actualizacion/`)

| ID | Archivo origen | Ruta actual | Nombre documental | Tipo de fuente | Tema principal | Carpeta destino propuesta | Uso permitido | Riesgo contaminación | Vigencia | Verificación externa | Duplicados / relacionados | Estado del archivo | Observaciones |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INV-018 | `2026_actualizacion/guia_zaragoza_2026.md` | repo madre | Guía Zaragoza 2026 | Investigación externa | Contexto Zaragoza, ecosistema | `docs_fuentes/05_zaragoza_aragon_ecosistema/` | PENDIENTE DE VERIFICACIÓN | Bajo | 2026 | Sí (datos cambian) | Vinculada a `zaragoza/01_ecosistema_creativo.md` | [VACÍO] | Requiere contenido y validación. |
| INV-019 | `2026_actualizacion/notas_resumen_2026.md` | repo madre | Notas resumen 2026 | Investigación externa | Síntesis actualización 2026 | `docs_fuentes/03_mercado_y_tendencias/` | PENDIENTE DE VERIFICACIÓN | Medio | 2026 | Sí | — | [VACÍO] | — |
| INV-020 | `2026_actualizacion/fatiga_digital_2026.md` | repo madre | Fatiga digital 2026 | Investigación externa | Tendencia bienestar/trabajo manual | `docs_fuentes/03_mercado_y_tendencias/` | PENDIENTE DE VERIFICACIÓN | Bajo | 2026 | Sí (tendencia) | Vinculada a H08, H05 | [VACÍO] | Apoya posicionamiento. |
| INV-021 | `2026_actualizacion/competencia_espana_2026.md` | repo madre | Competencia España 2026 | Investigación externa | Competencia nacional | `docs_fuentes/04_competencia_benchmarking/` | PENDIENTE DE VERIFICACIÓN | Bajo | 2026 | Sí | Vinculada a `benchmarking_espana/*` (13 archivos) | [VACÍO] | Síntesis del benchmarking España. |
| INV-022 | `2026_actualizacion/competencia_zaragoza_2026.md` | repo madre | Competencia Zaragoza 2026 | Investigación externa | Competencia local | `docs_fuentes/04_competencia_benchmarking/` | PENDIENTE DE VERIFICACIÓN | Medio | 2026 | **Sí** (mercado local cambiante) | Vinculada a H01, H02 | [VACÍO] | **Crítica para viabilidad local.** |

### 5.5 Bloque benchmarking España (repo madre `docs_investigacion_externa/benchmarking_espana/`)

> Los 13 archivos de benchmarking español son **fuentes externas de referencia operativa**, no fuentes legales. Su uso es para aprender mejores prácticas, no para justificar cumplimiento normativo.

| ID | Archivo origen | Tema | Carpeta destino propuesta | Uso permitido | Estado |
|---|---|---|---|---|---|
| INV-023 | `benchmarking_espana/01_cara_y_canto.md` | Referente operativo España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-024 | `benchmarking_espana/02_tmdc.md` | Taller compartido carpintería | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-025 | `benchmarking_espana/03_a_tu_madera.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-026 | `benchmarking_espana/04_comaking.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-027 | `benchmarking_espana/05_t11_sevilla.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-028 | `benchmarking_espana/06_made_de_madera.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-029 | `benchmarking_espana/07_transfolab_bcn.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-030 | `benchmarking_espana/08_the_workshop_madrid.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-031 | `benchmarking_espana/09_la_fabrica_de_hobbies.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-032 | `benchmarking_espana/10_artisano_cat.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-033 | `benchmarking_espana/11_el_secadero_reviverdes.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-034 | `benchmarking_espana/12_talleres_twm.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-035 | `benchmarking_espana/13_la_termita.md` | Referente España | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |

### 5.6 Bloque benchmarking Europa (repo madre `docs_investigacion_externa/benchmarking_europa/`)

| ID | Archivo origen | Tema | Carpeta destino propuesta | Uso permitido | Estado |
|---|---|---|---|---|---|
| INV-036 | `benchmarking_europa/01_ici_nantes.md` | Referente Europa | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-037 | `benchmarking_europa/02_knock_on_wood.md` | Referente Europa | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-038 | `benchmarking_europa/03_la_planche.md` | Reglas comunidad y EPIs (FR) | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-039 | `benchmarking_europa/04_xylolab.md` | Referente Europa | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |
| INV-040 | `benchmarking_europa/05_otros_referentes.md` | Otros referentes | `docs_fuentes/04_competencia_benchmarking/` | USAR SOLO COMO REFERENCIA | [VACÍO] |

### 5.7 Bloque Zaragoza / Aragón / ecosistema (repo madre `docs_investigacion_externa/zaragoza/`)

| ID | Archivo origen | Tema | Carpeta destino propuesta | Uso permitido | Riesgo | Verificación externa | Estado |
|---|---|---|---|---|---|---|---|
| INV-041 | `zaragoza/01_ecosistema_creativo.md` | Ecosistema creativo Zaragoza | `docs_fuentes/05_zaragoza_aragon_ecosistema/` | PENDIENTE DE VERIFICACIÓN | Bajo | Sí | [VACÍO] |
| INV-042 | `zaragoza/02_formacion_y_fp.md` | Formación y FP | `docs_fuentes/05_zaragoza_aragon_ecosistema/` | PENDIENTE DE VERIFICACIÓN | Bajo | Sí | [VACÍO] |
| INV-043 | `zaragoza/03_restauracion_y_tapiceria.md` | Restauración y tapicería | `docs_fuentes/05_zaragoza_aragon_ecosistema/` | PENDIENTE DE VERIFICACIÓN | Bajo | Sí | [VACÍO] |
| INV-044 | `zaragoza/04_movilidad_y_radio_de_captacion.md` | Movilidad y radio de captación | `docs_fuentes/05_zaragoza_aragon_ecosistema/` | PENDIENTE DE VERIFICACIÓN | Medio | Sí | [VACÍO] |
| INV-045 | `zaragoza/05_ubicaciones_potenciales.md` | Ubicaciones potenciales | `docs_fuentes/07_instalaciones_local_producto/` | PENDIENTE DE VERIFICACIÓN | **Alto** (precios/disponibilidad cambian) | **Sí** | [VACÍO] |

### 5.8 Bloque legal, ayudas y estudios (repo madre `docs_fuentes_proyecto/legales_ayudas_estudios/`)

| ID | Archivo origen | Tema | Carpeta destino propuesta | Uso permitido | Riesgo | Verificación externa | Estado |
|---|---|---|---|---|---|---|---|
| INV-046 | `legales_ayudas_estudios/resumen_aspectos_legales.md` | Aspectos legales | `docs_fuentes/06_legal_operativo/` | PENDIENTE DE VERIFICACIÓN | Medio | **Sí** | [VACÍO] |
| INV-047 | `legales_ayudas_estudios/resumen_ayudas.md` | Ayudas y financiación | `docs_fuentes/10_ayudas_financiacion/` | PENDIENTE DE VERIFICACIÓN | Medio (convocatorias cambian) | **Sí** | [VACÍO] |
| INV-048 | `legales_ayudas_estudios/resumen_estudio_artesania.md` | Estudio artesanía | `docs_fuentes/03_mercado_y_tendencias/` | USAR SOLO COMO REFERENCIA | Bajo | Sí | [VACÍO] |
| INV-049 | `legales_ayudas_estudios/resumen_market_for_craft.md` | Estudio "Market for Craft" | `docs_fuentes/03_mercado_y_tendencias/` | USAR SOLO COMO REFERENCIA | Bajo | Sí | [VACÍO] |

### 5.9 Bloque ZIP de respaldo (repo madre)

| ID | Archivo origen | Nombre | Tipo | Carpeta destino propuesta | Uso permitido | Estado |
|---|---|---|---|---|---|---|
| INV-050 | `taller_colaborativo_2026-06-02_18-00-24.zip` | Respaldo del repo madre (2026-06-02) | Respaldo histórico | No mover (permanece en repo madre) | NO USAR EN PLAN FINAL | [CON CONTENIDO, pero solo espejo del repo] |

### 5.10 Bloque ZIP extraviado en repo actual (riesgo de higiene)

| ID | Archivo/carpeta | Nombre | Tipo | Carpeta destino propuesta | Uso permitido | Estado |
|---|---|---|---|---|---|---|
| INV-051 | `C:Mis Documentosarchivos_zip/` (en **este** repo) | Carpeta con nombre malformado (path Windows mal escapado) | Higiene / basura | Eliminar o mover a `.gitignore` tras aprobación | NO USAR EN PLAN FINAL | [A revisar] |

---

## 6. Resumen agregado de la propuesta

| Métrica | Valor |
|---|---:|
| Total de fuentes identificadas | 51 entradas |
| Fuentes con contenido real utilizable | **6** (INV-001 a INV-006, todas en `docs_base/`) |
| Fuentes vacías (placeholders de localización) | 43 |
| Respaldo zip (no fuente) | 1 |
| Elemento de higiene a revisar | 1 |
| Destinos `docs_fuentes/` cubiertos por la propuesta | 9 de 11 |
| Destinos sin fuentes propuestas: `09_finanzas_activos/` (parcial, solo INV-011), `08_seguridad_responsabilidad_usuarios/` (parcial, solo INV-010) | — |

### Distribución por uso permitido propuesto

| Uso permitido | Nº de fuentes |
|---|---:|
| USAR COMO BASE | 5 |
| USAR SOLO COMO REFERENCIA | 19 |
| PENDIENTE DE VERIFICACIÓN | 22 |
| CUARENTENA / HISTÓRICO | 3 |
| NO USAR EN PLAN FINAL | 2 |

---

## 7. Riesgos detectados (priorizados)

1. **R1 — Crítico: las fuentes "reales" están vacías.**  
   La cadena documental obligatoria (fuente cruda → clasificación → …) **no puede arrancar** porque no hay fuente cruda con contenido. **Bloquea el avance de la Fase 1.1 hacia la Fase 2.** Requiere decisión humana sobre de dónde provendrá el contenido real (¿se poblarán estos placeholders? ¿existen fuentes en otra ubicación no inspeccionada? ¿se generarán nuevas?).

2. **R2 — Contaminación histórica 2023 vs 2026.**  
   Los 3 archivos de `2023_base_original/` (INV-015 a INV-017) se proponen a `11_legacy_no_usar_directo/` con uso CUARENTENA/HISTÓRICO para evitar arrastrar el contexto rural no vigente. Coherente con D16 e INV-002.

3. **R3 — Riesgo de duplicación funcional.**  
   `docs_base/12_fuentes_maestras_del_proyecto.md` (INV-013) cumple la misma función que `docs_organizacion/01_inventario_fuentes.md` y que este documento. Requiere decidir sede única para evitar divergencia.

4. **R4 — Decisiones potencialmente desincronizadas.**  
   `docs_base/05_decisiones_clave.md` (INV-005) contiene D01–D20 y P01–P08. Este repo contiene `docs_organizacion/04_decisiones_pendientes.md` con DP-001/002/003 y DC-001. **Requieren reconciliación** antes de consolidar.

5. **R5 — Benchmarks no son fuentes legales.**  
   Los 18 archivos de benchmarking (INV-023 a INV-040) se proponen como USAR SOLO COMO REFERENCIA. No pueden justificar cumplimiento normativo ni cuantificar demanda local.

6. **R6 — Ubicaciones potenciales con vigencia muy frágil.**  
   `zaragoza/05_ubicaciones_potenciales.md` (INV-045) tiene riesgo Alto: precios, disponibilidad y normativa municipal cambian. Requiere verificación externa continua.

7. **R7 — Higiene del repositorio: carpeta malformada.**  
   `C:Mis Documentosarchivos_zip/` aparece **en ambos repos** (madre y actual). En este repo está sin trackear. Requiere decisión de limpieza.

8. **R8 — Fases del repo madre vs fases oficiales de este repo.**  
   El `04_plan_de_implementacion.md` (INV-006) define 11 fases; este repo define 4 fases oficiales. No se deben mezclar. Se propone uso solo como referencia.

---

## 8. Verificación de la cadena documental

Comprobación contra la cadena obligatoria del proyecto:

```text
Fuente cruda → clasificación → matriz pregunta/fuente/vacío/decisión
            → documento consolidado → respuesta del plan → auditoría → documento final
```

- **Fuente cruda:** la mayoría de orígenes están vacíos. Solo los 6 archivos de `docs_base/` están listos.
- **Clasificación:** este documento la propone; falta aprobación humana.
- **Matriz pregunta/fuente/vacío:** existe (`docs_organizacion/02_matriz_preguntas_fuentes_vacios.md`) pero está casi vacía.
- **Consolidado / respuesta / auditoría / final:** fuera del alcance de la Fase 1.1.

**Conclusión de proceso:** la propuesta **no salta** la cadena. Identifica con honestidad que el primer eslabón (fuente cruda) es el cuello de botella actual.

---

## 9. Acciones requeridas tras aprobación (NO ejecutadas)

Estas acciones **no se ejecutan** hasta aprobación explícita de Alex:

1. Confirmar o corregir el hallazgo R1: ¿existen fuentes con contenido en otra ubicación?
2. Reconciliar INV-005 con `docs_organizacion/04_decisiones_pendientes.md`.
3. Decidir sede única para el inventario de fuentes (R3).
4. Ejecutar los movimientos propuestos de fuentes reales (cuando tengan contenido).
5. Decidir qué hacer con la carpeta malformada `C:Mis Documentosarchivos_zip/` (R7).
6. Poblar `docs_organizacion/03_mapa_duplicados.md` con los duplicados funcionales detectados (R3, R4).

---

## 10. Criterio de éxito de la Fase 1.1 (autoevaluación)

| Criterio requerido | Estado |
|---|---|
| Inventario general de fuentes | ✅ Propuesta creada (este documento) |
| Clasificación propuesta | ✅ Incluida (secciones 5 y 6) |
| Mapa de duplicados | ⚠️ Detectados (R3), pendiente de volcar en `03_mapa_duplicados.md` |
| Riesgos de contaminación identificados | ✅ R1–R8 |
| Fuentes legales separadas de benchmarks | ✅ (bloques 5.5/5.6 vs 5.8) |
| Fuentes históricas separadas de vigentes | ✅ (bloque 5.3 vs 5.4) |
| Propuesta revisada por humano | ⏳ Pendiente |
| Aprobación explícita antes de mover fuentes reales | ⏳ Pendiente |

**La Fase 1.1 aún NO está preparada para avanzar** hasta que se resuelva R1 y se obtenga aprobación humana.
