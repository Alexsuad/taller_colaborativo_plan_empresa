# Mapa maestro de preparación del Plan de Empresa

## 1. Propósito
Este documento establece el mapa maestro y la secuencia ordenada de trabajo para el desarrollo integral del Plan de Empresa del Taller Colaborativo Artesanal en Zaragoza (CCA). Sirve para coordinar las dependencias de información entre las distintas secciones, definir las prioridades estratégicas y evitar la dispersión en la redacción preliminar.

## 2. Reglas de uso
*   **Workflow obligatorio:** Este mapa maestro es organizativo y no sustituye al procedimiento secuencial de resolución definido en `.agents/workflows/resolucion-preguntas-por-capitulo.md`.
*   **No es un contenedor de preguntas:** No recopila ni duplica las preguntas guía literales ni actúa como matriz global de resolución.
*   **No autoriza redacción final:** Su presencia no exime de cumplir los gates y autorizaciones correspondientes para modificar archivos en `respuestas_plan_empresa/`.
*   **Gobernanza de datos:** Prohibido su uso para estimar o inventar asunciones financieras o de mercado sin contraste documental.

## 3. Orden general recomendado
1.  **Fase 1: Identificación y Entorno Competitivo:** Idea de negocio (02), Análisis externo (03_1), Estudio de mercado (03_2) y Benchmarking (03_4).
2.  **Fase 2: Diagnóstico y Estrategia:** Análisis interno (03_3), Naming/Marca (06_0), DAFO / CAME (04) y Objetivos (05).
3.  **Fase 3: Desarrollo de Planes de Área:** Operaciones (06_2), Marketing/Ventas (06_1), Recursos humanos (06_3), Jurídico/Fiscal (06_4) e Implantación (07).
4.  **Fase 4: Evaluación y Resumen:** Plan económico-financiero (06_5 - Fase Especial), Viabilidad (08) y Resumen ejecutivo (00).

---

## 4. Mapa maestro por capítulo

| ID | Capítulo | Propósito | Preguntas madre a resolver | Fuentes prioritarias | Dependencias | Estado inicial | Prioridad | Observaciones |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **00** | Resumen ejecutivo | Sintetizar los hitos y viabilidad global del proyecto. | Hitos clave, cifras de inversión y propuesta de valor condensada. | Secciones consolidadas del Plan de Empresa. | Todos los capítulos | `NO_RESPONDER_AUN` | `POSTERIOR` | Se redacta al finalizar todo el plan. |
| **01** | Equipo promotor | Presentar la capacidad del equipo de ejecutar el taller. | Competencias de carpintería, gestión de taller y vacíos formativos. | Datos de promotores locales (`docs_control/`). | Ninguna | `LISTO_PARA_RESOLUCION` | `MEDIA` | Información de base de la persona física. |
| **02** | Idea de negocio | Definir el modelo híbrido del taller y la propuesta de valor. | Estructura de servicios del MVP, exclusión de CNC y modelo de acceso. | `docs_preparacion/02_base_competencia_e_inspiradores.md` | `01` | `PARCIALMENTE_LISTO` | `ALTA` | Base estratégica del plan de operaciones. |
| **03_1** | Análisis externo | Evaluar los factores macro (PESTEL) aplicados a Zaragoza. | Trámites municipales, subvenciones activas y normativas de ruidos. | Ordenanzas locales y diarios oficiales de Aragón. | Ninguna | `LISTO_PARA_RESOLUCION` | `ALTA` | Crítico para licencias y subvenciones. |
| **03_2** | Estudio de mercado | Validar la existencia de demanda de ocio artesanal y talleres. | Demografía de aficionados, artesanos locales y canales de captación. | Datos censales y `docs_organizacion/`. | Ninguna | `LISTO_PARA_RESOLUCION` | `ALTA` | Determina el tamaño del local y cuotas. |
| **03_3** | Análisis interno | Evaluar activos y recursos del equipo inicial. | Herramientas disponibles y capacidad de tutoría de carpintería. | Inventario de activos iniciales del promotor. | Ninguna | `LISTO_PARA_RESOLUCION` | `MEDIA` | Aporta datos para el plan de maquinaria. |
| **03_4** | Benchmarking | Extraer aprendizajes y evitar sobredimensionamiento. | Criterios operativos, tarifas base y políticas de almacenamiento modular. | Fichas `COMP-F003` y `COMP-F005`. | Ninguna | `LISTO_PARA_RESOLUCION` | `ALTA` | Se resolverá estrictamente mediante su workflow. |
| **04** | DAFO / CAME | Diagnosticar debilidades y cruzar acciones de respuesta. | Fortalezas operativas frente a riesgos de accidentes y aforo. | Análisis internos y de mercado precedentes. | `03_1`, `03_2`, `03_3` | `BLOQUEADO_POR_DEPENDENCIAS` | `MEDIA` | Exige cerrar la fase de análisis del entorno. |
| **05** | Objetivos | Fijar los objetivos estratégicos cuantitativos y cualitativos. | Volumen de usuarios, retención y número de cursos anuales. | Resultados del DAFO / CAME. | `04` | `BLOQUEADO_POR_DEPENDENCIAS` | `MEDIA` | Subordinado a la viabilidad estratégica. |
| **06_0** | Naming y marca | Definir la marca comercial y el relato de comunicación. | Nombre provisional, dominio web y registro de marca comercial. | Manuales de identidad y registros del promotor. | Ninguna | `LISTO_PARA_RESOLUCION` | `MEDIA` | Requisito previo para el plan de marketing. |
| **06_1** | Marketing y ventas | Estructurar los bonos de acceso y canales de ventas. | Canales de captación (experienciales) y escalera de valor comercial. | `03_4`, `03_2`, `06_0` | `02`, `03_2` | `BLOQUEADO_POR_DEPENDENCIAS` | `MEDIA` | Depende de la validación del cliente objetivo. |
| **06_2** | Operaciones | Diseñar el layout, seguridad y maquinaria del taller. | Layout del local, plan de EPIs, inducción técnica y CAPEX. | `03_4`, ordenanzas industriales locales. | `02`, `03_4` | `BLOQUEADO_POR_DEPENDENCIAS` | `MEDIA` | Crucial para dimensionar los costes fijos. |
| **06_3** | Recursos humanos | Definir las funciones del operario de taller y su contratación. | Perfil del operario de taller, convenio de madera y salarios. | Convenio colectivo siderometalúrgico/madera Aragón. | `06_2` | `BLOQUEADO_POR_DEPENDENCIAS` | `MEDIA` | Aporta los costes de personal. |
| **06_4** | Jurídico y fiscal | Determinar la forma societaria y los requisitos de apertura. | Forma jurídica (Autónomo vs S.L.) y trámites de registro. | Estatutos y reglamentos del promotor. | `06_2`, `06_3` | `BLOQUEADO_POR_DEPENDENCIAS` | `MEDIA` | Define las tasas de constitución y seguros. |
| **06_5** | Económico-financiero | Estructurar supuestos, flujos de caja y punto de equilibrio. | Costes, CAPEX de maquinaria, ingresos previstos y tesorería. | Insumos de tarifas y CAPEX previos de operaciones. | Todos los anteriores | `ESPECIAL_FINANCIERO` | `POSTERIOR` | **No desarrollar ahora**. Reservar para fase especial. |
| **07** | Implantación | Planificar el cronograma de puesta en marcha del taller. | Hitos desde la firma del alquiler del local hasta la apertura. | Diagrama de flujos y secuenciación del proyecto. | `06_2`, `06_4` | `BLOQUEADO_POR_DEPENDENCIAS` | `MEDIA` | Requiere licencias y local cerrado. |
| **08** | Viabilidad | Emitir conclusiones sobre la sostenibilidad del taller. | Nivel de certidumbre comercial, operativa y social del CCA. | Cifras del plan económico-financiero. | `06_5` | `NO_RESPONDER_AUN` | `POSTERIOR` | Depende del análisis financiero final. |

---

## 5. Capítulos listos para iniciar resolución
Los siguientes apartados no presentan bloqueos por dependencias de información precedente y disponen de bases sólidas en el repositorio:
*   **01 Equipo promotor:** Información biográfica e inicial disponible.
*   **02 Idea de negocio:** Soportado por la base de competencia consolidada y la exclusión de CNC.
*   **03_1 Análisis externo:** Basado en datos macro y regulatorios locales.
*   **03_2 Estudio de mercado:** Trazable con estudios de demanda preliminares.
*   **03_4 Benchmarking:** Listo para preparación secuencial bajo su respectivo workflow.
*   **06_0 Naming y marca:** Basado en el registro y opciones preliminares.

## 6. Capítulos bloqueados o posteriores
*   **06_5 Económico-financiero:** Clasificado como **Especial Financiero**. No se realizarán estimaciones ni proyecciones de números en esta fase; su desarrollo queda diferido a una sesión experta dedicada.
*   **Capítulos de Planes de Área (06_1, 06_2, 06_3, 06_4, 07, 04, 05):** Bloqueados hasta que se resuelvan y validen los capítulos previos de mercado y el benchmarking operativo.
*   **00 Resumen ejecutivo / 08 Viabilidad:** Posteriores (se elaborarán en el cierre del Plan de Empresa).

## 7. Regla de avance
Para iniciar la resolución de cualquiera de los capítulos declarados como listos, es obligatorio aplicar previamente la guía procedimental de:
[workflow de resolución de preguntas por capítulo](file:///.agents/workflows/resolucion-preguntas-por-capitulo.md)
