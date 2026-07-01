# PT-10K — Blueprint completo de Fase 2 con matriz de dependencias empresariales

## 1. Estado actual de Fase 2

- Fase 1 cerrada operativamente.
- Fase 2 activa.
- Gate 1C operativo.
- Gate 1D bloqueado.
- `respuestas_plan_empresa/` congelado.
- Auditor general pendiente por 17 placeholders esperados.
- Cadena de control de skills creada y aprobada.
- Sistema agéntico todavía incompleto.

## Evidencia de estado

- Commit `9633ade` `feat: decide tipo de pieza agentica`.
- Commit `ee68969` `fix: completa criterio de decision de piezas agenticas`.
- Commit `e841005` `feat: controla creacion y auditoria de skills`.

## Lectura operativa

Fase 2 ya no es limpieza documental de base. Ahora debe construir la maquinaria agéntica y de validación que permita entrar en Fase 3 sin improvisación. Gate 1C sigue abierto para diagnóstico y Gate 1D sigue bloqueado porque aún faltan dependencias, validaciones y un sistema agéntico completo.

## 2. Objetivo formal de Fase 2

Fase 2 = construir, ordenar y validar el sistema agéntico completo.

Fase 3 = usar ese sistema para redactar, desarrollar y controlar el Plan de Empresa.

Fase 2 no debe producir el Plan de Empresa final. Su salida correcta es una maquinaria fiable, trazable y auditable que permita pasar a Fase 3 sin mezclar capas ni sobrediseñar.

## 3. Inventario de piezas existentes

Clasificación usada:
`SKILL`, `SCRIPT`, `GATE`, `REGLA`, `WORKFLOW`, `SUBAGENTE`, `MCP`, `DOCUMENTO_CONTROL`, `MATRIZ`, `REPORTE`, `OTRO`.

| Pieza | Ruta | Tipo | Función | Estado | Observación / Riesgo |
| --- | --- | --- | --- | --- | --- |
| `decidir-tipo-pieza-sistema-agentico` | `.agents/skills/decidir-tipo-pieza-sistema-agentico/SKILL.md` | SKILL | Decide si una necesidad debe ser skill, script, gate, regla, workflow, subagente, MCP, ajuste documental o no crear nada | ACTIVA / commit e841005 | Es la puerta de entrada conceptual de toda nueva pieza; no debe saltarse |
| `auditar-skill-antes-de-crear` | `.agents/skills/auditar-skill-antes-de-crear/SKILL.md` | SKILL | Audita si una skill propuesta es nueva, ampliación, duplicado o no skill | ACTIVA / commit e841005 | Debe quedarse subordinada a la skill de decisión |
| `crear-skill-desde-contrato` | `.agents/skills/crear-skill-desde-contrato/SKILL.md` | SKILL | Redacta una skill nueva solo cuando existe contrato aprobado | ACTIVA / commit e841005 | Riesgo de sobrediseño si el contrato no está cerrado |
| `auditar-skill-creada` | `.agents/skills/auditar-skill-creada/SKILL.md` | SKILL | Revisa estructura, función, integración y pruebas funcionales de una skill | ACTIVA / commit e841005 | Debe bloquear si no hay resultado funcional probado |
| `clasificar-pregunta-plan-empresa` | `.agents/skills/clasificar-pregunta-plan-empresa/SKILL.md` | SKILL | Clasifica preguntas del plan por fuente, dependencia y `NO_RESPONDER_AUN` | ACTIVA | Base para convertir preguntas en bloques preparables |
| `preparar-bloque-para-redaccion` | `.agents/skills/preparar-bloque-para-redaccion/SKILL.md` | SKILL | Deja un bloque listo para futura redacción sin escribir el texto final | ACTIVA | Útil para Fase 2/Fase 3; no debe invadir redacción |
| `inventario-clasificacion-fuentes` | `.agents/skills/inventario-clasificacion-fuentes/SKILL.md` | SKILL | Clasifica fuentes por tipo, vigencia, uso permitido y riesgo | ACTIVA | Evita que las fuentes entren sin clasificación previa |
| `control-anticontaminacion-fuentes` | `.agents/skills/control-anticontaminacion-fuentes/SKILL.md` | SKILL | Evalúa contaminación conceptual y vigencia de fuentes | ACTIVA | Guardrail crítico contra fuentes ajenas o desfasadas |
| `auditoria-documental-por-fases` | `.agents/skills/auditoria-documental-por-fases/SKILL.md` | SKILL | Verifica respeto de fase, alcance y criterio de cierre | ACTIVA | Evita que Fase 2 derive en Fase 3 antes de tiempo |
| `auditar-trazabilidad-input-output` | `.agents/skills/auditar-trazabilidad-input-output/SKILL.md` | SKILL | Compara instrucción, alcance, archivos tocados y resultado reportado | ACTIVA | Necesaria para no perder requisitos entre entrada y salida |
| `verificar-evidencia-minima-cierre` | `.agents/skills/verificar-evidencia-minima-cierre/SKILL.md` | SKILL | Comprueba que una tarea tenga evidencia mínima para cerrarse | ACTIVA | Evita cierres prematuros o sin prueba suficiente |
| `verificar-no-mezcla-de-capas` | `.agents/skills/verificar-no-mezcla-de-capas/SKILL.md` | SKILL | Detecta mezcla de gobernanza, negocio, scripts, gates y entrega | ACTIVA | Crucial para separar Fase 2 de Fase 3 |
| `higiene-estructura-documental-5s` | `.agents/skills/higiene-estructura-documental-5s/SKILL.md` | SKILL | Revisa orden, duplicados, basura técnica y coherencia estructural | ACTIVA | Reduce ruido y rutas sobrantes |
| `preparar-paquete-ejecucion-tecnica` | `.agents/skills/preparar-paquete-ejecucion-tecnica/SKILL.md` | SKILL | Convierte una decisión aprobada en paquete técnico cerrado | ACTIVA | Útil para pasos técnicos, pero no sustituye contrato experto |

| `docs_control/03_gates_documentales.md` | `docs_control/03_gates_documentales.md` | GATE | Fuente única de gates documentales | ACTIVO | Gate 1C operativo; Gate 1D bloqueado; Fase 2 pendiente |
| `docs_control/04_registro_decisiones.md` | `docs_control/04_registro_decisiones.md` | DOCUMENTO_CONTROL | Registro oficial de decisiones, pivotes y bloqueos | ACTIVO | DEC-017 y DEC-018 sostienen el estado actual |
| `docs_control/06_fases_oficiales_proyecto.md` | `docs_control/06_fases_oficiales_proyecto.md` | DOCUMENTO_CONTROL | Define las fases oficiales del proyecto | ACTIVO | Marca Fase 1 cerrada y Fase 2 parcialmente avanzada |
| `docs_control/reportes/PT-10H_auditoria_skills_base.md` | `docs_control/reportes/PT-10H_auditoria_skills_base.md` | REPORTE | Auditoría de skills base documentales | ACTIVO | Justifica la cadena de skills base y su mínima cobertura |
| `docs_control/reportes/PT-10J_preparacion_gate_1d.md` | `docs_control/reportes/PT-10J_preparacion_gate_1d.md` | REPORTE | Preparación de evidencia mínima para Gate 1D | ACTIVO | Confirma que Gate 1D sigue no listo |
| `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` | `docs_organizacion/08_matriz_clasificacion_preguntas_red_arce.md` | MATRIZ | Matriz activa de clasificación de preguntas | ACTIVA | Es la base de diagnóstico de Gate 1C |
| `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md` | `docs_organizacion/02_matriz_red_arce_fuentes_vacios.md` | MATRIZ | Antecedente de vacíos y fuentes | APOYO_TEMPORAL | No es matriz rectora, pero aún sirve de antecedente |
| `docs_organizacion/03_revision_critica_matriz_vacios.md` | `docs_organizacion/03_revision_critica_matriz_vacios.md` | MATRIZ | Revisión crítica de vacíos accionables | APOYO_TEMPORAL | Útil para depurar vacíos antes de redacción |
| `docs_manifest/01_manifest_fuentes_y_uso_permitido.md` | `docs_manifest/01_manifest_fuentes_y_uso_permitido.md` | DOCUMENTO_CONTROL | Manifiesto de fuentes y uso permitido | ACTIVO | Marca la política de uso de fuentes |
| `docs_manifest/02_clasificacion_zonas_documentales.md` | `docs_manifest/02_clasificacion_zonas_documentales.md` | DOCUMENTO_CONTROL | Clasificación de zonas documentales | ACTIVO | Ayuda a no mezclar repositorio y entrega final |
| `plan_empresa_guia/00_indice_preguntas_guia.md` | `plan_empresa_guia/00_indice_preguntas_guia.md` | OTRO | Índice guía del plan | ACTIVO | Base de la secuencia de preguntas del plan |
| `docs_organizacion/00_organizacion_documental_marketing/` | `docs_organizacion/00_organizacion_documental_marketing/` | OTRO | Material puente de consulta híbrida y calibración competitiva | ACTIVO | No borrarlo por duplicidad aparente; aporta contexto |
| `scripts/auditar_estado_plan_empresa.py` | `scripts/auditar_estado_plan_empresa.py` | SCRIPT | Auditoría de estado general del plan | ACTIVO | Auditor actual de referencia para cierre de tareas |
| `scripts/auditar_contaminacion_conceptual.py` | `scripts/auditar_contaminacion_conceptual.py` | SCRIPT | Detecta contaminación conceptual | ACTIVO | Guardrail crítico de Fase 1/Fase 2 |
| `scripts/auditar_linealidad_plan_empresa.py` | `scripts/auditar_linealidad_plan_empresa.py` | SCRIPT | Auditoría de linealidad | POST-F1 | No operativo como validación actual |
| `scripts/compilar_plan_empresa.py` | `scripts/compilar_plan_empresa.py` | SCRIPT | Compilación del plan | POST-F1 | No usar antes de tiempo |
| `scripts/auditar_formato_markdown_entrega.py` | `scripts/auditar_formato_markdown_entrega.py` | SCRIPT | Auditoría de formato markdown | POST-F1 | No operativo ahora |
| `scripts/auditar_texto_corrupto_entrega.py` | `scripts/auditar_texto_corrupto_entrega.py` | SCRIPT | Auditoría de texto corrupto | POST-F1 | No operativo ahora |

Nota: no existe un reporte PT-10I formal en `docs_control/reportes/`. La secuencia documental visible pasa de PT-10H a PT-10J y ahora este blueprint PT-10K.

## 4. Cadena obligatoria para crear nuevas skills

Cadena aprobada:

`decidir-tipo-pieza-sistema-agentico`
→ `auditar-skill-antes-de-crear`
→ `crear-skill-desde-contrato`
→ `auditar-skill-creada`
→ revisión humana / commit

Regla operativa:

- ninguna skill nueva debe crearse por intuición;
- primero se decide si realmente corresponde skill;
- luego se audita si ya existe algo equivalente;
- luego se crea desde contrato;
- luego se audita estructura, función e integración;
- no se aprueba por Git limpio ni por reporte del agente;
- toda skill nueva debe demostrar que funciona con casos de prueba.

Estado actual:

- la cadena existe, está versionada y funciona como criterio operativo;
- aún requiere uso sistemático en los siguientes PT;
- la cadena evita duplicados, pero aún necesita consolidación operativa y pruebas más sistemáticas;
- la revisión humana sigue siendo obligatoria.

## 5. Matriz de dependencias empresariales del Plan de Empresa

| Bloque / Documento | Depende de | Produce | No puede hacerse si falta | Tipo de pieza necesaria | Gate asociado | Riesgos típicos |
| --- | --- | --- | --- | --- | --- | --- |
| Definición del proyecto (`02_idea_negocio.md`) | Identidad de negocio, opción activa, promotor | Alcance y foco del proyecto | Identidad y alcance base | SKILL + AJUSTE_DOCUMENTAL | Gate 1C / Gate 1D | Inventar alcance o mezclar ideas no vigentes |
| Problema / necesidad / oportunidad | Observación del caso, usuario, contexto | Problema bien formulado | Contexto o promotor | SKILL | Gate 1C | Convertir intuición en oportunidad cerrada |
| Cliente objetivo | Usuario, investigación, propuesta de valor | Segmento inicial | Datos de usuario o mercado | SKILL | Gate 1C / Gate 1D | Segmentar demasiado pronto o sin prueba |
| Segmentación | Cliente objetivo, mercado, competencia | Subsegmentos defendibles | Base de mercado | SKILL + SCRIPT | Gate 1C / Gate 1D | Segmentación ficticia o demasiado amplia |
| Customer persona | Segmentación, motivaciones, fricciones | Perfil de cliente | Segmentación mínima | SKILL | Gate 1D | Persona sin evidencia |
| Propuesta de valor | Cliente, problema, marca, mercado | Propuesta defendible | Problema y cliente claros | SKILL | Gate 1D | Propuesta genérica o vacía |
| Modelo de negocio | Propuesta de valor, cliente, ingresos, costes | Modelo coherente | Inputs de mercado y coste | SKILL + SCRIPT | Gate 1D | Crear un canvas bonito pero incoherente |
| Canvas | Modelo, cliente, propuesta, canales | Lienzo coherente | Bloques previos | SKILL | Gate 1D | Lienzo sin consistencia interna |
| Mercado | Fuentes externas, benchmarking, usuario | Lectura de demanda | Investigación suficiente | SKILL + SCRIPT | Gate 1C / Gate 1D | Sobreestimar demanda o leer mal el sector |
| Entorno | Datos contextuales, normativa, territorio | Factores externos | Evidencia externa | SKILL + SCRIPT | Gate 1C | Omisiones relevantes o datos obsoletos |
| Competencia | Fuentes externas, benchmarking | Mapa competitivo | Fuentes comparables | SKILL + SCRIPT | Gate 1C / Gate 1D | Benchmarking como copia encubierta |
| Benchmarking | Fuentes, inspiradores, usuario | Lecciones útiles | Criterio de comparación | SKILL + MCP | Gate 1C / Gate 1D | Sobredimensionar referentes o importar su modelo |
| DAFO | Mercado, entorno, análisis interno | Diagnóstico estratégico | Base de 3.1, 3.2, 3.3 | SKILL | Gate 1D | DAFO sin evidencia o sin jerarquía |
| CAME | DAFO | Estrategia correctiva | DAFO sólido | SKILL | Gate 1D | Convertir amenazas en promesas |
| Marca | Identidad, tono, usuario | Nombre, tono, estilo | Identidad clara | SKILL + AJUSTE_DOCUMENTAL | Gate 1D | Marca incoherente con el taller |
| Posicionamiento | Marca, mercado, competencia | Posición defendible | Análisis comparado | SKILL | Gate 1D | Posicionamiento aspiracional sin prueba |
| Marketing | Cliente objetivo, propuesta de valor, posicionamiento, canales | Estrategia de captación | Segmento y valor claros | SKILL + SCRIPT | Gate 1D | Mezclar marketing con ventas o RRSS |
| Ventas | Cliente pagador, objeciones, pricing, proceso comercial | Proceso comercial | Pricing y cliente claros | SKILL + SCRIPT | Gate 1D | Vender sin proceso o sin precio real |
| Comunicación | Marca, públicos, objetivos, tono | Plan de comunicación | Marca y audiencias | SKILL | Gate 1D | Confundir comunicación con marketing o RRSS |
| Redes sociales | Comunicación, calendario, objetivos, audiencias | Plan RRSS | Tono y públicos | SKILL | Gate 1D | RRSS sin estrategia o sin objetivo |
| Operaciones | Local, procesos, riesgos, legal | Operación inicial | Local y requisitos | SKILL + SCRIPT | Gate 1D | Operación sobre un local imposible |
| Recursos humanos | Roles, turnos, costes, responsabilidades | Organigrama y costes | Roles definidos | SKILL + SCRIPT | Gate 1D | Costes de personal irreales |
| Legal / fiscal | Actividad, local, normativa, seguros | Requisitos legales | Consulta normativa | SKILL + SCRIPT | Gate 1D | Inventar cumplimiento o mezclar ámbitos |
| Viabilidad económica aportada por usuario | Aporte del usuario, hipótesis, costes, mercado | Hipótesis económicas auditadas | Aporte del usuario | SKILL + SCRIPT | Gate 1D | Construir finanzas desde cero sin base |
| Riesgos | Todos los bloques previos | Lista de riesgos y mitigaciones | Bloques previos | SKILL | Gate 1D | Subestimar riesgos estructurales |
| Go / Pivot / No-Go | Plan auditado completo | Decisión de avance | Cuerpo del plan listo | GATE | Gate de cierre | Aprobar sin evidencia |
| Resumen ejecutivo | Cuerpo del plan auditado | Síntesis ejecutiva | Cuerpo completo | SKILL + GATE | Gate 1D / Fase 3 | Resumen que contradice el cuerpo |
| Anexos | Capítulos respaldatorios | Anexos trazables | Capítulos base | WORKFLOW + SCRIPT | Fase 3 / Fase 4 | Anexos sin respaldo o sin relación |
| Documento final | Todo el plan auditado | Entregable completo | Todo lo anterior | SCRIPT + GATE | Gate Fase 3 / Fase 4 | Compilar antes de validar |

Dependencias explícitas:

- Marketing depende de cliente objetivo, propuesta de valor, competencia, posicionamiento y canales.
- Ventas depende de cliente pagador, objeciones, proceso comercial, pricing y activos comerciales.
- RRSS depende de comunicación, audiencias, tono, objetivos y calendario.
- Plan de comunicación depende de marca, públicos, propuesta de valor y canales.
- DAFO/CAME depende de mercado, entorno, competencia y análisis interno.
- Finanzas/viabilidad no se crea desde cero si debe aportarla el usuario; se analiza críticamente.
- Resumen ejecutivo depende del cuerpo del plan auditado.
- Anexos dependen de los capítulos que respaldan.

## 6. Contrato experto por tipo de skill futura

No crear skills todavía; esta tabla define el contrato mínimo que deberían cumplir cuando toque.

| Skill candidata | Rol experto | Entrada requerida | Salida estructurada | Errores que debe detectar | Cuándo bloquea | Gate asociado | Prioridad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `analizar-definicion-proyecto` | Definir alcance y límites | Identidad, opción activa, promotor | Definición breve y acotada | Mezcla de fases, alcance inventado | Si el alcance no está claro | Gate 1C / 1D | Alta |
| `analizar-problema-necesidad-oportunidad` | Formular el problema real | Contexto, usuario, mercado | Problema con causa y efecto | Problema genérico o vacío | Si no hay base suficiente | Gate 1C | Alta |
| `analizar-cliente-segmentacion-persona` | Segmentar y perfilar cliente | Mercado, observaciones, evidencias | Segmento + persona defendibles | Segmentos inventados | Si se mezclan segmentos incompatibles | Gate 1D | Alta |
| `analizar-propuesta-valor` | Sintetizar valor | Cliente, problema, recursos | Propuesta de valor clara | Promesa exagerada | Si no cuadra con mercado | Gate 1D | Alta |
| `analizar-modelo-negocio-canvas` | Ordenar el modelo | Propuesta, cliente, ingresos, costes | Canvas coherente | Lienzo bonito pero inconsistente | Si un bloque invalida otro | Gate 1D | Alta |
| `analizar-mercado-entorno` | Lectura externa | Fuentes, contexto, territorio | Diagnóstico externo | Fuentes débiles o viejas | Si la evidencia es insuficiente | Gate 1C / 1D | Alta |
| `analizar-competencia-benchmarking` | Comparar mercado y referentes | Competidores, inspiradores | Comparativa y lecciones | Copia encubierta | Si se confunde inspiración con copia | Gate 1C / 1D | Alta |
| `analizar-dafo-came` | Convertir diagnóstico en estrategia | Mercado, entorno, interno | DAFO y CAME | DAFO arbitrario | Si faltan capítulos previos | Gate 1D | Alta |
| `analizar-marca-posicionamiento` | Definir marca y posición | Identidad, mercado, tono | Marca y posicionamiento | Incoherencia de tono | Si la marca contradice el negocio | Gate 1D | Media-Alta |
| `analizar-marketing` | Diseñar captación | Cliente, valor, canales | Estrategia marketing | Mezcla con ventas/RRSS | Si el pricing o cliente faltan | Gate 1D | Alta |
| `analizar-ventas` | Diseñar proceso comercial | Cliente pagador, pricing | Flujo de ventas | Vender sin proceso | Si no hay precio o proceso | Gate 1D | Alta |
| `analizar-comunicacion` | Diseñar comunicación | Marca, públicos, objetivos | Plan de comunicación | Confundir comunicación con campaña | Si no hay marca o audiencia | Gate 1D | Media |
| `analizar-redes-sociales` | Diseñar RRSS | Audiencias, tono, calendario | Plan RRSS | RRSS sin objetivos | Si RRSS se usa como sustituto de marketing | Gate 1D | Media |
| `analizar-operaciones` | Diseñar operación | Local, procesos, riesgos | Operación inicial | Operación imposible | Si local o licencias faltan | Gate 1D | Alta |
| `analizar-recursos-humanos` | Definir roles y costes | Roles, turnos, costes | Organigrama mínimo | Costes irreales | Si no hay base laboral | Gate 1D | Media-Alta |
| `analizar-legal-fiscal` | Verificar requisitos | Normativa, local, actividad | Requisitos y riesgos | Legalidad inventada | Si no hay fuente oficial | Gate 1D | Alta |
| `analizar-viabilidad-economica-aportada` | Criticar la parte financiera | Aporte del usuario, hipótesis | Viabilidad auditada | Finanzas creadas de cero | Si no hay aporte del usuario | Gate 1D | Alta |
| `validar-coherencia-mercado-ventas-finanzas` | Cruzar coherencia global | Mercado, ventas, finanzas | Diagnóstico de coherencia | Supuestos incompatibles | Si hay contradicciones entre bloques | Gate 1D | Muy alta |
| `analizar-riesgos-go-pivot-no-go` | Decidir avance o pivote | Plan auditado | Go / Pivot / No-Go | Aprobación sin evidencia | Si faltan bloques críticos | Gate de cierre | Muy alta |
| `redactar-bloque-plan-empresa` | Redactar bloque final | Bloque preparado | Texto final del bloque | Redacción prematura | Si la evidencia no está cerrada | Gate 1D | Posterior |
| `auditar-bloque-plan-empresa` | Auditar bloque final | Bloque redactado | Dictamen del bloque | Bloque sin respaldo | Si faltan pruebas o citas | Gate 1D | Posterior |
| `auditar-coherencia-global-plan` | Auditar todo el plan | Cuerpo completo | Veredicto global | Contradicciones globales | Si un bloque rompe el conjunto | Gate Fase 3 | Muy alta |
| `preparar-anexos-plan-empresa` | Preparar anexos | Capítulos fuente | Anexos trazables | Anexos sin respaldo | Si los capítulos base no existen | Gate Fase 4 | Posterior |

Separación que no debe romperse:

- `marketing` ≠ `ventas` ≠ `comunicación` ≠ `RRSS`.

## 7. Scripts deterministas necesarios

No crear scripts ahora; esta tabla solo define el backlog técnico mínimo.

| Script candidato | Función | Qué valida | Cuándo se ejecuta | Prioridad | Justificación |
| --- | --- | --- | --- | --- | --- |
| `validar_skills_frontmatter.py` | Valida frontmatter de skills | Nombre, descripción, estructura mínima | Cada vez que se crea o modifica una skill | Imprescindible | Evita skills mal formadas |
| `validar_no_rutas_prohibidas.py` | Comprueba rutas prohibidas | Que no se toque lo vetado | Antes de commit o cierre | Imprescindible | Reduce riesgo de contaminación documental |
| `validar_gate_1d.py` | Verifica condiciones de Gate 1D | Bloqueos, dependencias y evidencia | Antes de cualquier apertura de Gate 1D | Imprescindible | Gate 1D no debe abrirse por intuición |
| `validar_placeholders_respuestas.py` | Detecta placeholders pendientes | `[PENDIENTE]`, `Pendiente de completar` | Antes de cerrar fases | Imprescindible | Evita cerrar con huecos visibles |
| `validar_estructura_respuestas.py` | Valida estructura de respuestas | Secciones mínimas y orden | Antes de redacción o cierre | Imprescindible | Evita respuestas mal estructuradas |
| `validar_fuentes_referencias.py` | Valida fuentes y referencias | Citas, rutas, vigencia | Antes de usar fuentes fuertes | Imprescindible | Protege la trazabilidad |
| `validar_anexos.py` | Comprueba anexos | Correspondencia entre anexos y capítulos | Antes de Fase 4 | Conveniente | Evita anexos huérfanos |
| `validar_canvas.py` | Valida el canvas | Coherencia interna del canvas | Antes de redacción definitiva | Conveniente | Útil, pero no bloquea el sistema entero |
| `validar_presupuesto_documental.py` | Valida presupuesto y soportes | Hipótesis económicas y soportes | Antes de conclusiones de viabilidad | Imprescindible | Sin esto, la viabilidad queda débil |
| `validar_coherencia_mercado_ventas_finanzas.py` | Cruza coherencia de bloques críticos | Mercado, ventas, finanzas | Antes de cierre del plan | Imprescindible | Es una de las comprobaciones más críticas |
| `generar_reporte_estado_plan.py` | Genera reporte de estado | Estado global del plan y bloqueos | En hitos y cierres | Conveniente | Acelera reportes, pero no sustituye validación |

Resumen:

- Imprescindibles: frontmatter, rutas prohibidas, Gate 1D, placeholders, estructura de respuestas, fuentes, presupuesto documental, coherencia mercado-ventas-finanzas.
- Convenientes: anexos, canvas, reporte de estado.

## 8. Gates necesarios

No crear gates ahora; esta tabla define lo que debería existir si Fase 2 madura correctamente.

| Gate candidato | Qué bloquea | Entradas | Condición de aprobación | Condición de bloqueo | Evidencia mínima | Prioridad |
| --- | --- | --- | --- | --- | --- | --- |
| `gate_no_maquillaje_viabilidad` | Cierres de viabilidad sin base | Bloques 3, 4, 5, 6, 7, 8 | Evidencia suficiente y coherencia global | Datos inventados o insuficientes | Auditoría de coherencia y fuentes | Imprescindible |
| `gate_secuencia_documental_plan_empresa` | Saltos de secuencia | Matriz, bloques y dependencias | Orden correcto de ejecución | Bloque posterior antes del previo | Mapa de dependencias | Imprescindible |
| `gate_coherencia_mercado_ventas_finanzas` | Contradicciones críticas | Mercado, ventas, finanzas | Bloques alineados | Supuestos incompatibles | Validación cruzada | Imprescindible |
| `gate_payload_listo_para_redaccion` | Payload antes de redactar | Bloque preparado, fuentes y pruebas | Bloque estable y trazable | Falta evidencia o hay vacíos | Bloque preparado auditado | Imprescindible |
| `gate_bloque_auditable` | Bloques no auditables | Bloque, pruebas y referencias | Bloque auditable | Bloque opaco o ambiguo | Evidencia mínima completa | Conveniente |
| `gate_sistema_agentico_listo_fase_3` | Entrada a Fase 3 | Skills, scripts, gates, workflows | Sistema completo y probado | Cualquier pieza crítica falla | Checklist de Fase 2 completo | Imprescindible |
| `gate_no_respuestas_sin_fuente` | Respuestas sin fuente | Respuestas plan + fuente | Fuente clara y trazable | Respuesta sin base | Citación o referencia | Conveniente |

## 9. Workflows candidatos

No crear workflows ahora; esta tabla define secuencias repetibles deseables.

| Workflow candidato | Objetivo | Pasos | Piezas que usa | Gate de cierre | Prioridad |
| --- | --- | --- | --- | --- | --- |
| `entrada_diagnostico_clasificacion` | Convertir una duda en acción | Entrar pregunta -> diagnosticar -> clasificar | `clasificar-pregunta-plan-empresa`, `decidir-tipo-pieza-sistema-agentico` | Gate 1C | Imprescindible |
| `repo_primero_notebooklm_despues` | Evitar autoridad externa prematura | Buscar en repo -> detectar hueco -> consultar NotebookLM -> validar -> integrar | `buscar-primero-en-repositorio`, `preparar-consulta-notebooklm-controlada`, `validar-salida-notebooklm`, `integrar-hallazgo-notebooklm-en-matriz` | Gate 1C / Gate payload | Imprescindible |
| `preparar-consulta-notebooklm-controlada` | SKILL | Hacer la consulta externa controlada | Solo si el hueco no está en el repo |

MCP queda como opción posterior solo si existe integración externa viva, recurrente, segura y necesaria. No se clasifica como MCP por defecto.
| `investigacion_digestivo_payload` | Convertir investigación en bloque usable | Investigación -> digestión -> payload | Skills analíticas, scripts de validación | Gate payload listo para redacción | Imprescindible |
| `payload_redaccion_auditoria` | Redactar con control | Payload -> redacción -> auditoría | `preparar-bloque-para-redaccion`, `redactar-bloque-plan-empresa`, `auditar-bloque-plan-empresa` | Gate 1D | Imprescindible |
| `anexos_referencias_documento_fisico` | Mantener trazabilidad editorial | Anexos -> referencias -> documento físico | `preparar-anexos-plan-empresa`, validadores de anexos, compilar | Gate Fase 4 | Posterior |
| `auditoria_global_gate_fase_3` | Cerrar Fase 2 | Auditoría global -> gate Fase 3 | `auditar-coherencia-global-plan`, scripts de validación | Gate sistema agéntico listo Fase 3 | Imprescindible |

## 10. Subagentes candidatos justificados o descartados

No crear subagentes ahora.

| Subagente candidato | Responsabilidad | Por qué no basta una skill | Skills que usaría | Capacidad de veto | Prioridad | Dictamen |
| --- | --- | --- | --- | --- | --- | --- |
| `coordinador_fase2_sistema_agentico` | Coordinar la fase completa | Porque cruza skills, scripts, gates y reportes de forma persistente | Decisión, auditorías, validadores, reportes | Sí | Posible solo si la coordinación se vuelve recurrente y autónoma | Aplazar |
| `integrador_notebooklm_controlado` | Coordinar consultas externas recurrentes | Porque la consulta externa podría convertirse en patrón persistente | MCP/consulta, validación, matriz | Limitada | Posible, pero primero debe bastar un workflow/MCP | Aplazar |
| `auditor_global_fase3` | Veto final sobre el paso a Fase 3 | Porque necesitaría contexto y salida persistentes | Auditoría global, scripts, gates | Sí | Posible si Fase 2 crece mucho | Aplazar |
| `gestor_anexos_y_exportacion` | Orquestar anexos y entrega final | Porque podría ser workflow/script | Preparación de anexos, compilación | No | Descargable a workflow + script | Descartado por ahora |
| `subagente_por_skill` | Uno por cada skill | Porque duplica estructura y no aporta valor | Todas las skills | No | Nunca como estrategia base | Descartado |

Regla:

- no crear subagente por skill;
- solo justificar subagente si tiene criterio propio, contexto propio, salida propia, capacidad de veto o coordinación recurrente.

## 11. Protocolo repo primero / NotebookLM después

Protocolo:

- Repositorio primero.
- NotebookLM después.
- NotebookLM solo para huecos concretos.
- NotebookLM no decide.
- NotebookLM no actualiza el repo automáticamente.
- La salida de NotebookLM se valida antes de integrarse.

Piezas candidatas:

| Pieza candidata | Tipo | Función | Observación |
| --- | --- | --- | --- |
| `buscar-primero-en-repositorio` | SKILL | Detectar si el hueco ya está resuelto en el repo | Debe actuar antes de abrir NotebookLM |
| `preparar-consulta-notebooklm-controlada` | SKILL | Hacer la consulta externa controlada | Solo si el hueco no está en el repo |
| `validar-salida-notebooklm` | SKILL + SCRIPT | Comprobar que la salida es utilizable | No debe asumir que NotebookLM tiene razón |
| `integrar-hallazgo-notebooklm-en-matriz` | AJUSTE_DOCUMENTAL | Volcar hallazgo validado en la matriz o reporte | Debe pasar por validación humana si afecta contenido de negocio |

MCP queda como opción posterior solo si existe integración externa viva, recurrente, segura y necesaria. No se clasifica como MCP por defecto.

## 12. Backlog priorizado de Fase 2

Clasificación:

- `IMPRESCINDIBLE PARA ABRIR FASE 3`
- `CONVENIENTE ANTES DE FASE 3`
- `POSTERIOR / NO BLOQUEANTE`
- `DESCARTADO POR AHORA`

| Pieza candidata | Tipo | Prioridad | Razón | Dependencias | Riesgo si se omite |
| --- | --- | --- | --- | --- | --- |
| `validar_skills_frontmatter.py` | SCRIPT | Imprescindible para abrir Fase 3 | Sin eso, la sede de skills no queda cerrada | Skills creadas y modificadas | Skills mal formadas |
| `validar_no_rutas_prohibidas.py` | SCRIPT | Imprescindible para abrir Fase 3 | Protege carpetas prohibidas | Reglas de gobernanza | Contaminación de rutas |
| `validar_placeholders_respuestas.py` | SCRIPT | Imprescindible para abrir Fase 3 | Evita cerrar con huecos visibles | `respuestas_plan_empresa/` | Respuestas prematuras |
| `validar_estructura_respuestas.py` | SCRIPT | Imprescindible para abrir Fase 3 | Sin estructura no hay redacción controlable | Bloques y plantillas | Respuestas inconsistentes |
| `validar_coherencia_mercado_ventas_finanzas.py` | SCRIPT | Imprescindible para abrir Fase 3 | Es la validación crítica del negocio | Mercado, ventas, finanzas | Viabilidad maquillada |

- Skill: analiza coherencia empresarial y semántica.
- Script: valida estructura, presencia de datos y campos verificables.
- Gate: bloquea avance si hay contradicciones graves.
| `gate_sistema_agentico_listo_fase_3` | GATE | Imprescindible para abrir Fase 3 | Declara si la maquinaria ya sirve | Skills, scripts, workflows | Entrar en Fase 3 demasiado pronto |
| `validar_gate_1d.py` | SCRIPT | Conveniente antes de Fase 3 | Ordena la apertura de Gate 1D | Gate 1C, evidencia | Abrir Gate 1D sin base |
| `validar_fuentes_referencias.py` | SCRIPT | Conveniente antes de Fase 3 | Protege referencias y vigencia | Inventario de fuentes | Citas débiles |
| `buscar-primero-en-repositorio` | SKILL | Conveniente antes de Fase 3 | Evita dependencias externas innecesarias | Repo y matriz | Usar NotebookLM como primera fuente |
| `preparar-consulta-notebooklm-controlada` | MCP | Conveniente antes de Fase 3 | Consulta externa controlada | Huecos concretos | Sobrecargar el sistema |
| `integrar-hallazgo-notebooklm-en-matriz` | AJUSTE_DOCUMENTAL | Conveniente antes de Fase 3 | Mantiene trazabilidad de hallazgos | Consulta validada | Integrar ruido o sesgo |
| `validar_anexos.py` | SCRIPT | Posterior / no bloqueante | Ayuda a la Fase 4 | Capítulos cerrados | Anexos huérfanos |
| `validar_canvas.py` | SCRIPT | Posterior / no bloqueante | Útil para consistencia visual/documental | Canvas completo | Se puede validar manualmente al principio |
| `auditar-coherencia-global-plan` | SKILL | Posterior / no bloqueante | Útil cuando el plan ya esté casi completo | Bloques completos | Auditoría demasiado pronto |
| `preparar-anexos-plan-empresa` | WORKFLOW | Posterior / no bloqueante | Orquesta el cierre editorial | Capítulos previos | Cerrar sin respaldo |
| `subagente_por_skill` | SUBAGENTE | Descartado por ahora | Sobredimensiona sin aportar control | Ninguna | Complejidad inútil |

## 13. Riesgos de sobrediseño y mitigación

| Riesgo | Señal de alarma | Mitigación |
| --- | --- | --- |
| Crear demasiadas skills | Se fragmenta una tarea simple en muchas piezas | Usar la cadena de decisión y exigir contrato previo |
| Crear scripts que deberían ser skills | Se fuerza automatización donde hace falta criterio | Separar juicio experto de validación determinista |
| Crear skills que deberían ser scripts | Se deja una verificación exacta en manos subjetivas | Exigir formato, conteo, rutas y pruebas |
| Crear subagentes innecesarios | Cada skill acaba con su propio agente | No crear subagente por skill |
| Usar NotebookLM como autoridad | Se integra sin validar | Repositorio primero, NotebookLM después |
| Mezclar Fase 2 con Fase 3 | Se redacta antes de cerrar maquinaria | Gatear la transición y mantener Fase 2 técnica |
| Crear documentos largos innecesarios | El blueprint se vuelve un manual inmanejable | Mantener secciones cortas y listas accionables |
| Duplicar piezas existentes | Misma función con otro nombre | Pasar por `auditar-skill-antes-de-crear` |
| Abrir Gate 1D sin evidencia | Se intenta poblar respuestas sin base | Auditoría, trazabilidad y evidencia mínima |
| Tocar `respuestas_plan_empresa/` antes de tiempo | Se escribe contenido final prematuro | Mantener congelación hasta Gate 1D |

## 14. Definition of Done de Fase 2

Fase 2 queda cerrada cuando:

- las skills críticas están creadas, auditadas y probadas funcionalmente;
- los scripts críticos están creados y ejecutables;
- los gates críticos están definidos;
- los workflows mínimos están definidos;
- los subagentes están justificados o descartados;
- NotebookLM queda integrado solo como consulta controlada;
- la matriz de dependencias empresariales está lista;
- el gate del sistema agéntico está listo para Fase 3;
- Alex aprueba el paso a Fase 3.

## 15. Dictamen final del blueprint

Dictamen:

- `FASE_2_BLUEPRINT_INCOMPLETO`

Motivo:

- la arquitectura conceptual ya está bastante clara;
- pero la Fase 2 aún no está cerrada de forma operativa porque faltan validadores deterministas, el gate de paso a Fase 3 y la consolidación funcional completa;
- Gate 1D sigue bloqueado y `respuestas_plan_empresa/` sigue congelado;
- el sistema agéntico todavía necesita consolidación antes de usarlo como maquinaria de Fase 3.

Siguiente PT recomendado:

- `PT-10L — Contrato operativo de Fase 2`

La capa determinista mínima debe quedar como PT-10M.

Estado final del blueprint:

- listo como mapa de trabajo;
- no listo como autorización para Fase 3;
- pendiente de decisión humana de Alex para la siguiente prioridad técnica.

