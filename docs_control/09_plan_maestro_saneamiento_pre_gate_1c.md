# 09 — Plan maestro de saneamiento pre-Gate 1C

## 1. Propósito del documento

Este documento consolida los hallazgos detectados en auditorías previas y los convierte en una hoja de ruta de saneamiento técnico/documental para el repositorio `taller_colaborativo_plan_empresa`.

Su función es ordenar el trabajo pendiente antes de cerrar Gate 1C.

Este documento:

```text
NO ejecuta cambios.
NO mueve archivos.
NO borra archivos.
NO renombra archivos.
NO importa fuentes reales.
NO redacta el plan de empresa.
NO pobla respuestas_plan_empresa/.
NO pobla docs_consolidados/.
NO cierra Gate 1C.
NO abre Gate 1D.
NO aprueba DEC-014.
```

Este documento solo propone paquetes de intervención futuros, pequeños, auditables y aprobables por separado.

---

## 2. Estado real actual del repositorio

Estado vigente:

```text
Fase 1 — Abierta.
Fase 2 — Parcialmente avanzada.
Fase 3 — Bloqueada.
Fase 4 — Bloqueada.
```

Gates actuales:

```text
Gate 1A — Identidad, sede agéntica y anticontaminación: COMPLETADO.
Gate 1B — Inventario real de fuentes: COMPLETADO SOLO COMO INVENTARIO PROVISIONAL OPERATIVO.
Gate 1C — Matriz Red ARCE → fuentes → vacíos: EN CURSO.
Gate 1D — Autorización para poblar respuestas_plan_empresa/: BLOQUEADO.
```

Aclaraciones obligatorias:

```text
Gate 1B no significa fuentes importadas.
docs_fuentes/ sigue sin fuentes reales importadas.
respuestas_plan_empresa/ sigue bloqueado.
docs_consolidados/ sigue bloqueado.
No estamos en redacción.
No estamos en entrega editorial.
```

Estado técnico:

```text
Repositorio válido.
No requiere reinicio.
Harnés parcialmente armado.
Necesita saneamiento controlado antes de cerrar Gate 1C.
```

Estado documental:

```text
ORDENADO_CON_RUIDO.
```

Principal foco de ruido:

```text
docs_organizacion/
```

---

## 3. Restricciones de trabajo

Toda intervención derivada de este plan debe respetar estas reglas:

```text
1. No hacer megatareas.
2. No tocar más archivos de los autorizados para cada paquete.
3. No mover ni borrar archivos sin plan aprobado.
4. No redactar respuestas_plan_empresa/.
5. No poblar docs_consolidados/.
6. No importar fuentes reales sin protocolo específico.
7. No cerrar Gate 1C.
8. No abrir Gate 1D.
9. No aprobar DEC-014 sin confirmación humana.
10. No crear nuevas skills, agentes o scripts si antes no se justifica por necesidad real.
11. No resolver decisiones de marketing o negocio desde Desarrollo.
```

Cuando aparezca una decisión que no corresponda a Desarrollo, debe marcarse como:

```text
REQUIERE_MARKETING
REQUIERE_PROMOTOR
REQUIERE_VALIDACION_EXTERNA
```

---

## 4. Fuentes del diagnóstico

Este plan consolida hallazgos procedentes de:

```text
1. Auditoría 5S / Lean de estructura documental.
2. Auditoría arquitectónica / desarrollo.
3. Auditoría producto / marketing / creación de empresa.
4. Autoauditoría del equipo de desarrollo.
5. Observaciones de continuidad del equipo de desarrollo.
6. Matriz Red ARCE → fuentes → vacíos.
7. Revisión crítica de matriz y vacíos accionables.
8. Matriz de clasificación de preguntas Red ARCE.
9. Registro de decisiones.
10. Mapa de reutilización del repositorio.
```

---

## 5. Hallazgos consolidados por categoría

### A — Gobernanza y estados

Hallazgos:

```text
DEC-002 está desfasada porque habla de tres fases.
El repositorio opera actualmente con cuatro fases oficiales.
DEC-014 sigue pendiente aunque la matriz 08 ya existe.
Gate 1B debe dejar más clara su condición de inventario provisional operativo.
Gate 1B no debe interpretarse como fuentes importadas.
Gate 1C sigue en curso.
Gate 1D sigue bloqueado.
La auditoría 5S puede requerir decisión formal o quedar como reporte técnico vivo.
docs_control/06_fases_oficiales_proyecto.md debe reconciliar el lenguaje de gates antiguos con Gate 1A–1D.
```

Riesgo:

```text
Gobernanza ambigua.
Falsa sensación de madurez.
Posible avance prematuro a redacción o consolidación.
```

---

### B — Higiene documental y 5S

Hallazgos:

```text
docs_organizacion/ mezcla documentos activos, históricos, propuestas absorbidas y matrices en revisión.
02_matriz_preguntas_fuentes_vacios.md compite con 02_matriz_red_arce_fuentes_vacios.md.
03_mapa_duplicados.md compite funcionalmente con 03_revision_critica_matriz_vacios.md.
04_decisiones_pendientes.md puede contener decisiones obsoletas o absorbidas.
05_propuesta_clasificacion_instalaciones_seguridad.md usa rutas antiguas.
06_propuesta_inventario_general_fuentes.md parece absorbido por 01_inventario_fuentes.md.
07_propuesta_inventario_puente_fuentes_externas.md parece absorbido por 01_inventario_fuentes.md.
08_matriz_clasificacion_preguntas_red_arce.md existe, pero DEC-014 sigue pendiente.
```

Riesgo:

```text
Doble fuente de verdad.
Uso de documentos superados como si fueran activos.
Ruido creciente si se siguen creando documentos sin limpieza previa.
```

---

### C — Rutas, sedes y fuentes

Hallazgos:

```text
docs_fuentes/ sigue físicamente vacío salvo .gitkeep.
Hay rutas históricas o propuestas que no coinciden con la estructura vigente.
Hay sedes documentales que apuntan a documentos antiguos o ambiguos.
```

Rutas inconsistentes detectadas:

```text
docs_fuentes/02_identidad_y_origen/
vs
docs_fuentes/02_identidad_origen/

docs_fuentes/05_zaragoza_aragon_ecosistema/
vs
docs_fuentes/05_zaragoza_aragon/

docs_fuentes/06_legal_normativo/
vs
docs_fuentes/06_legal_operativo/
```

Riesgo:

```text
Creación accidental de carpetas paralelas.
Importación futura de fuentes en rutas incorrectas.
Pérdida de trazabilidad documental.
```

---

### D — Scripts, harnés y SDD

Hallazgos:

```text
auditar_linealidad_plan_empresa.py falla por configuración ausente.
compilar_plan_empresa.py está bloqueado y arrastra rutas legacy.
auditar_formato_markdown_entrega.py falla por placeholders legítimos.
auditar_texto_corrupto_entrega.py puede dar PASS aunque no exista consolidado real.
auditar_contaminacion_conceptual.py detecta hallazgos HIGH en plan_empresa_guia/ pero no los bloquea suficientemente.
Falta modo pre-redacción frente a modo entrega.
Falta auditor baseline de gobernanza.
Falta dry-run de saneamiento.
.agents/workflows/ está vacío o sin flujos operativos suficientes.
Faltan tests deterministas mínimos para scripts críticos.
```

Clasificación inicial de scripts por estado:

| Script                                        | Estado técnico actual               | Lectura operativa                                                                       |
| --------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------- |
| `scripts/auditar_estado_plan_empresa.py`      | Operativo con cautela               | Útil para confirmar que el plan sigue pendiente/bloqueado.                              |
| `scripts/auditar_contaminacion_conceptual.py` | Operativo, requiere endurecimiento  | Debe revisar mejor rutas activas como `plan_empresa_guia/`.                             |
| `scripts/auditar_linealidad_plan_empresa.py`  | Bloqueado por configuración ausente | No debe fallar de forma opaca; debe adaptarse o devolver `NO_APLICA_FASE_ACTUAL`.       |
| `scripts/compilar_plan_empresa.py`            | No aplica en fase actual + legacy   | No debe ejecutarse aún; arrastra dependencias de linealidad y rutas antiguas.           |
| `scripts/auditar_formato_markdown_entrega.py` | Riesgo de falso positivo            | Interpreta placeholders legítimos como fallo de entrega. Necesita modo `pre-redaccion`. |
| `scripts/auditar_texto_corrupto_entrega.py`   | Riesgo de falso PASS                | No debe devolver PASS fuerte si no existe consolidado real auditado.                    |

Riesgo:

```text
Scripts con señales falsas.
Ejecución prematura de flujo de entrega.
Confusión entre auditorías de fase inicial y auditorías de entrega final.
```

---

### E — repo_identity + artifact_manifest

Hallazgos:

```text
artifact_manifest.yml es débil para distinguir documento vivo, histórico, absorbido, consolidado o generado.
artifact_manifest.yml no lista con claridad documentos recientes importantes.
repo_identity.yml está incompleto para reflejar la madurez actual del repositorio.
contains_real_data: false es ambiguo si no se separa de fuentes externas identificadas.
```

Campos a considerar en una intervención futura:

```yaml
repo_role: live_project
project_type: business_plan
active_business: taller_colaborativo_artesanal_zaragoza
current_gate: gate_1C_en_curso
gate_1D_status: bloqueado
contains_real_data_in_repo: false
external_sources_identified: true
external_sources_imported: false
contains_project_governance_data: true
allows_artifact_generation_by_phase: false
blocked_operations:
  - redactar_respuestas_plan_empresa
  - poblar_docs_consolidados
  - importar_fuentes_reales
  - cerrar_gate_1C
  - abrir_gate_1D
```

Riesgo:

```text
El repositorio puede parecer menos o más maduro de lo que realmente está.
El manifest no gobierna bien qué documento puede usarse, modificarse, regenerarse o archivarse.
```

---

### F — Producto/negocio pendiente de aterrizar

Estos puntos no deben resolverse desde Desarrollo.

Deben quedar marcados como dependencias de Marketing, Promotor o validación externa:

```text
matriz de segmentos prioritarios.
matriz de local mínimo viable.
modelo unitario de ingresos.
protocolo de onboarding y seguridad.
matriz de alianzas accionable.
mini-GTM de validación.
gate legal/PRL.
taxonomía formal de viabilidad.
mapa de experiencia de usuario del taller.
```

Clasificación:

```text
REQUIERE_MARKETING:
- matriz de segmentos prioritarios.
- modelo unitario de ingresos.
- matriz de alianzas accionable.
- mini-GTM de validación.
- mapa de experiencia de usuario del taller.

REQUIERE_PROMOTOR:
- decisiones sobre alcance inicial real.
- nivel de inversión asumible.
- disponibilidad para validación comercial.
- restricciones personales u operativas.

REQUIERE_VALIDACION_EXTERNA:
- gate legal/PRL.
- compatibilidad de local.
- licencias.
- prevención de riesgos laborales.
- seguros.
```

Riesgo:

```text
Que Desarrollo convierta vacíos de negocio en decisiones técnicas.
Que el plan avance con supuestos no validados.
```

---

### G — Fase 4 futura, anexos y packaging

Hallazgos:

```text
El repositorio aún no está en modo de entrega final.
docs_consolidados/ existe, pero no debe poblarse todavía.
_build/ no debe usarse para generar entrega final.
anexos/ todavía requiere manifest más fuerte en fases posteriores.
El packaging editorial debe esperar a que Gate 1C y Gate 1D estén resueltos.
```

Riesgo:

```text
Activar prematuramente compilación, anexos o documento final.
Confundir placeholders con entregables.
```

---

## 6. Hallazgos duplicados o equivalentes entre auditorías

| Hallazgo repetido                          | Aparece en                                                 | Lectura unificada                                                               | Riesgo                                 |
| ------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------- |
| Doble sede funcional para matriz de vacíos | Auditoría 5S, auditoría arquitectura, auditoría desarrollo | Hay una matriz antigua/simple y una matriz Red ARCE más completa que compiten   | Confusión de fuente de verdad          |
| Propuestas absorbidas visibles             | Auditoría 5S, inventarios, autoauditoría desarrollo        | `06` y `07` parecen absorbidas por `01`, pero siguen visibles como piezas vivas | Ruido documental                       |
| DEC-014 pendiente                          | Arquitectura, Marketing, Desarrollo                        | La matriz 08 existe, pero su decisión de aprobación sigue pendiente             | Uso operativo de artefacto no aprobado |
| Gate 1B ambiguo                            | Arquitectura, Marketing, Desarrollo                        | Está completado como inventario provisional, no como fuentes importadas         | Falsa madurez                          |
| Scripts no listos para entrega             | Arquitectura, Desarrollo                                   | Algunos scripts fallan, otros dan falsos positivos o falsos PASS                | Flujos prematuros                      |
| `artifact_manifest.yml` débil              | Arquitectura, Marketing, Desarrollo                        | No gobierna bien artefactos vivos, históricos, absorbidos o generados           | Pérdida de trazabilidad                |
| `repo_identity.yml` incompleto             | Arquitectura, Marketing, Desarrollo                        | No expresa con precisión estado real, gates y fuentes externas identificadas    | Estado ambiguo                         |

---

## 7. Paquetes de intervención propuestos

Este plan solo propone paquetes.

La existencia de estos paquetes no autoriza su ejecución.

Cada paquete deberá solicitarse, aprobarse y ejecutarse como una tarea separada, con alcance propio, archivos permitidos, archivos prohibidos, comandos de validación y reporte final.

---

### PT-10A — Reconciliar gobernanza y estados

Objetivo:

```text
Alinear estados, notas y decisiones para que gates, decisiones, fases y repo_identity no se contradigan.
```

Problemas que resuelve:

```text
DEC-002 desfasada.
DEC-014 pendiente.
Gate 1B ambiguo.
Gate 1C en curso.
Gate 1D bloqueado.
Lenguaje antiguo de fases/gates.
```

Archivos probablemente afectados en una tarea futura:

```text
docs_control/03_gates_documentales.md
docs_control/04_registro_decisiones.md
docs_control/06_fases_oficiales_proyecto.md
repo_identity.yml
```

Archivos prohibidos para este paquete:

```text
respuestas_plan_empresa/
docs_consolidados/
docs_fuentes/
docs_organizacion/
_build/
```

Salida esperada:

```text
Propuesta o cambio controlado que deje consistente el estado del repositorio:
Gate 1B provisional,
Gate 1C en curso,
Gate 1D bloqueado,
DEC-014 pendiente o aprobada solo si existe autorización humana explícita.
```

Criterio de aceptación:

```text
Todos los documentos de gobernanza explican el mismo estado.
No se cierra Gate 1C.
No se abre Gate 1D.
No se aprueba DEC-014 sin autorización humana.
```

Validaciones futuras recomendadas:

```bash
git status --short
git diff --stat
python3 scripts/auditar_estado_plan_empresa.py
```

---

### PT-10B — docs_organizacion: activos, históricos y duplicados

Objetivo:

```text
Definir qué documentos de docs_organizacion/ quedan activos, cuáles son históricos, cuáles están absorbidos y cuáles requieren revisión.
```

Problemas que resuelve:

```text
Duplicidad de matrices.
Propuestas absorbidas aún visibles.
Documentos obsoletos o compitiendo semánticamente.
Numeración con ruido.
```

Archivos probablemente afectados en una tarea futura:

```text
docs_organizacion/02_matriz_preguntas_fuentes_vacios.md
docs_organizacion/03_mapa_duplicados.md
docs_organizacion/04_decisiones_pendientes.md
docs_organizacion/05_propuesta_clasificacion_instalaciones_seguridad.md
docs_organizacion/06_propuesta_inventario_general_fuentes.md
docs_organizacion/07_propuesta_inventario_puente_fuentes_externas.md
```

Archivos que no deben modificarse sin autorización específica:

```text
docs_organizacion/01_inventario_fuentes.md
docs_organizacion/02_matriz_red_arce_fuentes_vacios.md
docs_organizacion/03_revision_critica_matriz_vacios.md
docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md
```

Salida esperada:

```text
Mapa de documentos activos, históricos, absorbidos y pendientes.
Propuesta de renombre, archivo o cabecera de estado.
No necesariamente ejecución de movimientos.
```

Criterio de aceptación:

```text
Cada concepto tiene una sede activa clara.
Los documentos históricos o absorbidos quedan identificados.
No se pierde trazabilidad.
No se mueven ni borran archivos sin dry-run y aprobación humana.
```

Validaciones futuras recomendadas:

```bash
git status --short
git diff --stat
find docs_organizacion -maxdepth 1 -type f | sort
```

---

### PT-10C — Rutas, sedes y docs_fuentes

Objetivo:

```text
Estabilizar rutas oficiales, sedes documentales y nomenclatura de docs_fuentes/.
```

Problemas que resuelve:

```text
Rutas antiguas.
Sedes confusas.
Variantes incompatibles de nombres.
docs_fuentes/ vacío pero con fuentes externas identificadas.
```

Rutas a reconciliar:

```text
docs_fuentes/02_identidad_y_origen/
docs_fuentes/02_identidad_origen/

docs_fuentes/05_zaragoza_aragon_ecosistema/
docs_fuentes/05_zaragoza_aragon/

docs_fuentes/06_legal_normativo/
docs_fuentes/06_legal_operativo/
```

Archivos probablemente afectados en una tarea futura:

```text
docs_control/05_sedes_informacion_plan_empresa.yml
docs_manifest/01_manifest_fuentes_y_uso_permitido.md
docs_manifest/02_clasificacion_zonas_documentales.md
artifact_manifest.yml
```

Archivos prohibidos para este paquete:

```text
docs_fuentes/
docs_consolidados/
respuestas_plan_empresa/
```

Salida esperada:

```text
Listado único de rutas oficiales.
Listado de rutas obsoletas.
Regla de no crear carpetas paralelas.
Sedes documentales alineadas con rutas reales.
```

Criterio de aceptación:

```text
Las sedes quedan inequívocas.
No se importan fuentes.
No se crean carpetas nuevas sin aprobación.
No se duplican rutas por diferencia de nombre.
```

Validaciones futuras recomendadas:

```bash
git status --short
git diff --stat
find docs_fuentes -maxdepth 2 -type d | sort
grep -R "legal_normativo\|legal_operativo\|zaragoza_aragon_ecosistema\|zaragoza_aragon\|identidad_y_origen\|identidad_origen" -n docs_control docs_organizacion docs_manifest
```

---

### PT-10D — Scripts y modo pre-redacción/entrega

Objetivo:

```text
Clasificar y adaptar scripts para distinguir fase actual, pre-redacción, saneamiento, entrega final y compilación.
```

Problemas que resuelve:

```text
Auditores con límites difusos.
Compilador bloqueado.
Rutas legacy.
Falsos positivos por placeholders.
Falsos PASS cuando no existe documento real auditado.
Falta de modo pre-redacción vs modo entrega.
```

Archivos probablemente afectados en una tarea futura:

```text
scripts/auditar_estado_plan_empresa.py
scripts/auditar_linealidad_plan_empresa.py
scripts/compilar_plan_empresa.py
scripts/auditar_texto_corrupto_entrega.py
scripts/auditar_formato_markdown_entrega.py
scripts/auditar_contaminacion_conceptual.py
```

Archivos que no deben modificarse salvo que la tarea lo autorice expresamente:

```text
config/
docs_fuentes/
docs_consolidados/
respuestas_plan_empresa/
_build/plan_empresa*
_build/test/
```

Salida esperada:

```text
Inventario de scripts por estado.
Definición de modo pre-redacción.
Definición de modo entrega.
Propuesta de adaptación de scripts.
Scripts que no aplican en fase actual deben devolver estado controlado, no fallos opacos.
```

Criterio de aceptación:

```text
Cada script tiene un uso claro por fase.
Ningún script sugiere falsamente que el plan está listo.
Ningún script empuja compilación final.
Los placeholders legítimos no bloquean fases previas.
```

Validaciones futuras recomendadas:

```bash
git status --short
git diff --stat
python3 scripts/auditar_estado_plan_empresa.py
python3 scripts/auditar_contaminacion_conceptual.py --verbose
```

No ejecutar en esta fase:

```bash
python3 scripts/compilar_plan_empresa.py
```

---

### PT-10E — repo_identity + artifact_manifest

Objetivo:

```text
Fortalecer la identidad del repositorio y el manifiesto de artefactos.
```

Problemas que resuelve:

```text
manifest débil.
identidad incompleta.
estado ambiguo.
contains_real_data: false insuficiente.
documentos vivos, históricos, absorbidos y generados sin clasificación fuerte.
```

Archivos probablemente afectados en una tarea futura:

```text
repo_identity.yml
artifact_manifest.yml
```

Archivos prohibidos para este paquete salvo autorización explícita:

```text
docs_control/03_gates_documentales.md
docs_control/04_registro_decisiones.md
docs_organizacion/
respuestas_plan_empresa/
docs_consolidados/
docs_fuentes/
```

Salida esperada:

```text
repo_identity.yml más preciso.
artifact_manifest.yml más útil para gobernanza.
Campos para distinguir:
- documento vivo
- histórico
- absorbido
- consolidado
- generado
- fuente metodológica
- fuente externa identificada
- salida futura
```

Criterio de aceptación:

```text
El repo expresa su estado real sin ambigüedad.
El manifest no se limita a listar archivos.
El manifest ayuda a decidir qué se puede tocar, regenerar, auditar o bloquear.
```

Validaciones futuras recomendadas:

```bash
git status --short
git diff --stat
python3 - <<'PY'
import yaml
for path in ["repo_identity.yml", "artifact_manifest.yml"]:
    with open(path, "r", encoding="utf-8") as f:
        yaml.safe_load(f)
    print(f"OK YAML: {path}")
PY
```

---

### PT-10F — Matrices de negocio bloqueantes

Objetivo:

```text
Identificar qué matrices de negocio bloquean Gate 1C o Gate 1D, sin resolver su contenido desde Desarrollo.
```

Problemas que resuelve:

```text
Dependencias entre matrices.
Clasificación pendiente.
Preguntas sin resolver.
Riesgo de usar matrices como respuestas.
```

Archivos probablemente afectados en una tarea futura:

```text
docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md
docs_organizacion/02_matriz_red_arce_fuentes_vacios.md
docs_organizacion/03_revision_critica_matriz_vacios.md
```

Archivos prohibidos para este paquete:

```text
respuestas_plan_empresa/
docs_consolidados/
docs_fuentes/
```

Límite de Desarrollo:

```text
Desarrollo NO decide segmentos.
Desarrollo NO decide precios.
Desarrollo NO decide local viable.
Desarrollo NO decide modelo de ingresos.
Desarrollo NO decide alianzas.
Desarrollo NO decide viabilidad.
```

Desarrollo solo puede:

```text
marcar dependencias.
marcar estados.
marcar bloqueos.
marcar rutas.
marcar qué requiere Marketing.
marcar qué requiere Promotor.
marcar qué requiere validación externa.
```

Salida esperada:

```text
Lista de matrices bloqueantes.
Lista de vacíos por resolver.
Marcadores REQUIERE_MARKETING, REQUIERE_PROMOTOR y REQUIERE_VALIDACION_EXTERNA.
No redacción de respuestas.
```

Criterio de aceptación:

```text
Las matrices indican claramente qué bloquea, pero no inventan respuestas.
No se convierte una hipótesis en decisión.
No se avanza a respuestas_plan_empresa/.
```

Validaciones futuras recomendadas:

```bash
git status --short
git diff --stat
grep -R "REQUIERE_MARKETING\|REQUIERE_PROMOTOR\|REQUIERE_VALIDACION_EXTERNA" -n docs_organizacion
```

---

### PT-10G — Protocolo futuro de pivotes y revalidación

Objetivo:

```text
Definir cómo registrar cambios de rumbo, reaperturas de hipótesis o revalidaciones futuras sin perder trazabilidad.
```

Problemas que resuelve:

```text
Cambios de alcance.
Pivotajes del modelo.
Revalidación de hipótesis.
Actualización futura del plan como documento vivo.
```

Archivos probablemente afectados en una tarea futura:

```text
docs_control/04_registro_decisiones.md
docs_control/09_plan_maestro_saneamiento_pre_gate_1c.md
posible nuevo documento docs_control/XX_protocolo_cambios_pivotes_revalidacion.md
```

Archivos prohibidos para este paquete:

```text
respuestas_plan_empresa/
docs_consolidados/
docs_fuentes/
_build/
```

Salida esperada:

```text
Propuesta de protocolo de pivotes.
No ejecución de pivotes.
No cambio de modelo de negocio.
No reapertura de fases sin aprobación.
```

Criterio de aceptación:

```text
El repositorio sabe cómo registrar cambios sin reescribir la historia.
Cada pivote futuro exige decisión, motivo, impacto y validación.
```

Validaciones futuras recomendadas:

```bash
git status --short
git diff --stat
```

---

## 8. Prioridades P0 / P1 / P2 / P3

### P0 — Bloqueante inmediato

Debe resolverse antes de seguir creando más piezas:

```text
Desalineación entre estados y notas de gobernanza.
Doble sede funcional para matrices de vacíos.
Propuestas absorbidas aún compitiendo con documentos activos.
Contradicción entre fuentes identificadas y fuentes importadas.
```

Paquetes asociados:

```text
PT-10A
PT-10B
```

---

### P1 — Antes de cerrar Gate 1C

Debe resolverse antes de declarar Gate 1C como completado:

```text
Separar históricos, absorbidos y activos en docs_organizacion/.
Alinear DEC-014 con la existencia real de la matriz 08.
Clarificar el sentido operativo de Gate 1B.
Estabilizar rutas y sedes principales.
```

Paquetes asociados:

```text
PT-10A
PT-10B
PT-10C
PT-10F
```

---

### P2 — Antes de autorizar respuestas_plan_empresa/

Debe resolverse antes de Gate 1D:

```text
Asegurar que las matrices bloqueantes estén claras y clasificadas.
Definir qué requiere Marketing, Promotor o validación externa.
Estabilizar sedes documentales y reglas de uso.
Definir modo pre-redacción frente a modo entrega.
```

Paquetes asociados:

```text
PT-10C
PT-10D
PT-10F
```

---

### P3 — Antes de Fase 3 / Fase 4 / entrega final

Debe resolverse antes de implementación técnica avanzada o packaging:

```text
Fortalecer artifact_manifest.yml.
Fortalecer repo_identity.yml.
Ajustar scripts de entrega y compilación.
Definir packaging, anexos y auditorías finales.
Definir protocolo de pivotes y revalidación.
```

Paquetes asociados:

```text
PT-10D
PT-10E
PT-10G
```

---

## 9. Política de archivos permitidos y prohibidos

Este plan maestro no autoriza editar ningún archivo salvo este mismo documento.

Para paquetes futuros, los archivos listados como “probablemente afectados” solo podrán tocarse si:

```text
1. El paquete se aprueba explícitamente.
2. El alcance del paquete enumera los archivos permitidos.
3. Se ejecuta git status --short antes.
4. Se reporta git diff --stat después.
5. No se tocan rutas prohibidas.
```

Regla general:

```text
Un archivo puede estar permitido dentro de un paquete aprobado,
pero sigue prohibido fuera de ese paquete.
```

Rutas siempre protegidas salvo autorización explícita:

```text
respuestas_plan_empresa/
docs_consolidados/
docs_fuentes/
_build/plan_empresa*
_build/test/
```

Rutas sensibles que solo pueden tocarse dentro de un paquete aprobado:

```text
plan_empresa_guia/
scripts/
config/
artifact_manifest.yml
repo_identity.yml
docs_control/
docs_organizacion/
docs_manifest/
anexos/
.agents/
```

---

## 10. Criterios de aceptación generales

Todo paquete futuro debe cumplir:

```text
1. Ser pequeño y aprobable.
2. Tener objetivo claro.
3. Tener archivos permitidos explícitos.
4. Tener archivos prohibidos explícitos.
5. Reportar comandos ejecutados.
6. Reportar git status --short.
7. Reportar git diff --stat.
8. No mezclar saneamiento técnico con redacción de negocio.
9. No cerrar Gate 1C accidentalmente.
10. No abrir Gate 1D accidentalmente.
11. No aprobar DEC-014 sin confirmación humana.
12. No importar fuentes reales sin protocolo.
13. No mover/borrar documentos sin dry-run y aprobación.
```

---

## 11. Validaciones recomendadas por tipo de paquete

### Gobernanza

```bash
git status --short
git diff --stat
python3 scripts/auditar_estado_plan_empresa.py
```

Revisión manual:

```text
docs_control/03_gates_documentales.md
docs_control/04_registro_decisiones.md
docs_control/06_fases_oficiales_proyecto.md
repo_identity.yml
```

---

### Higiene documental / 5S

```bash
git status --short
git diff --stat
find docs_organizacion -maxdepth 1 -type f | sort
```

Revisión manual:

```text
documentos activos
documentos históricos
documentos absorbidos
documentos pendientes
```

---

### Rutas y sedes

```bash
git status --short
git diff --stat
find docs_fuentes -maxdepth 2 -type d | sort
grep -R "legal_normativo\|legal_operativo\|zaragoza_aragon_ecosistema\|zaragoza_aragon\|identidad_y_origen\|identidad_origen" -n docs_control docs_organizacion docs_manifest
```

---

### Scripts

```bash
git status --short
git diff --stat
python3 scripts/auditar_estado_plan_empresa.py
python3 scripts/auditar_contaminacion_conceptual.py --verbose
```

No ejecutar salvo autorización explícita:

```bash
python3 scripts/compilar_plan_empresa.py
```

---

### YAML / manifiestos

```bash
git status --short
git diff --stat
python3 - <<'PY'
import yaml
for path in ["repo_identity.yml", "artifact_manifest.yml"]:
    with open(path, "r", encoding="utf-8") as f:
        yaml.safe_load(f)
    print(f"OK YAML: {path}")
PY
```

---

### Matrices de negocio

```bash
git status --short
git diff --stat
grep -R "REQUIERE_MARKETING\|REQUIERE_PROMOTOR\|REQUIERE_VALIDACION_EXTERNA" -n docs_organizacion
```

---

## 12. Riesgos pendientes

Riesgos activos:

```text
Convertir saneamiento en reestructuración grande.
Mezclar limpieza técnica con decisión de negocio.
Repetir la misma corrección en varios documentos sin una sede clara.
Mover archivos absorbidos sin antes fijar su rol histórico.
Usar el plan maestro como excusa para redactar contenido del plan.
Confundir fuentes identificadas con fuentes importadas.
Confundir matriz de clasificación con respuesta redactada.
Confundir docs_consolidados/ con documentos listos para poblar.
Activar Fase 4 por presencia de carpetas de anexos o _build/.
```

---

## 13. Orden recomendado de ejecución

Orden recomendado:

```text
1. PT-10A — Reconciliar gobernanza y estados.
2. PT-10B — docs_organizacion: activos, históricos y duplicados.
3. PT-10C — Rutas, sedes y docs_fuentes.
4. PT-10E — repo_identity + artifact_manifest.
5. PT-10D — Scripts y modo pre-redacción/entrega.
6. PT-10F — Matrices de negocio bloqueantes.
7. PT-10G — Protocolo futuro de pivotes y revalidación.
```

Nota:

```text
PT-10E puede adelantarse parcialmente si PT-10A y PT-10C necesitan reflejo inmediato en repo_identity.yml o artifact_manifest.yml.
PT-10D debe evitar tocar compilación final hasta que Gate 1D esté resuelto.
PT-10F debe ejecutarse con participación o revisión de Marketing/Promotor.
```

---

## 14. Qué NO autoriza este documento

Este documento no autoriza:

```text
Redactar el plan de empresa.
Mover archivos.
Borrar archivos.
Renombrar archivos.
Importar fuentes reales.
Poblar respuestas_plan_empresa/.
Poblar docs_consolidados/.
Cerrar Gate 1C.
Abrir Gate 1D.
Aprobar DEC-014.
Ejecutar saneamiento real.
Crear nuevos scripts.
Crear nuevas skills.
Crear nuevos agentes.
Modificar contenido de negocio.
Compilar DOCX/PDF.
Generar _build/plan_empresa*.
```

---

## 15. Dictamen de trabajo

Dictamen actual:

```text
Repo válido.
No reiniciar.
No redactar.
No consolidar.
No importar fuentes todavía.
No cerrar Gate 1C.
No abrir Gate 1D.
```

Acción recomendada:

```text
Aprobar este plan maestro como documento rector de saneamiento pre-Gate 1C.
Después ejecutar paquetes pequeños, empezando por PT-10A o PT-10B, según decisión humana.
```

Estado esperado tras este documento:

```text
El repositorio no queda saneado todavía.
Queda ordenada la hoja de ruta para sanearlo sin amplificar ruido.
```
