---

name: inventario-clasificacion-fuentes
description: Clasifica fuentes del proyecto por tipo, vigencia, uso permitido, riesgo de contaminación y destino documental sugerido. Use when creating or auditing source inventories before drafting business plan content.
---

# Propósito

Usar esta skill para crear, revisar o auditar inventarios de fuentes antes de cualquier redacción del plan de empresa.

Su función es impedir que una fuente entre al sistema sin clasificación previa.

# Cuándo usar esta skill

Usar cuando se necesite:

* inventariar fuentes disponibles;
* clasificar fuentes externas reales;
* revisar si una fuente puede alimentar el plan;
* decidir una carpeta destino propuesta en `docs_fuentes/`;
* detectar placeholders vacíos;
* separar fuentes históricas, legales, financieras, metodológicas, de mercado y de competencia;
* preparar una propuesta de importación controlada, sin ejecutar la importación.

# Entradas esperadas

* Lista de archivos, documentos o fuentes.
* Ruta actual conocida.
* Estado físico de cada fuente: con contenido, vacío, duplicado, histórico o pendiente.
* Fase vigente del proyecto.
* Estructura oficial de `docs_fuentes/`.
* Restricciones activas del proyecto.

# Salidas esperadas

Una tabla de inventario con, como mínimo:

* ID;
* archivo o fuente;
* ubicación actual;
* tipo de fuente;
* tema principal;
* carpeta destino propuesta;
* uso permitido;
* riesgo de contaminación;
* vigencia;
* requiere verificación externa;
* duplicados o relacionados;
* prioridad;
* observaciones.

# Procedimiento

1. Confirmar la fase vigente del proyecto.
2. Confirmar que no se está redactando el plan.
3. Listar las fuentes disponibles.
4. Identificar si cada fuente es real, placeholder, histórica, benchmark, legal, financiera, metodológica, estudio de mercado o ayuda.
5. Asignar carpeta destino propuesta dentro de la estructura oficial.
6. Asignar uso permitido.
7. Asignar riesgo de contaminación.
8. Marcar vigencia.
9. Marcar si requiere verificación externa.
10. Detectar duplicados, solapamientos o fuentes derivadas.
11. Emitir una propuesta, no una acción física.
12. Indicar decisiones humanas requeridas.

# Reglas obligatorias

* Fuente real con contenido no equivale a placeholder vacío.
* Fuente histórica no equivale a fuente vigente.
* Benchmark operativo no equivale a fuente legal.
* Documento IA no equivale a evidencia primaria.
* Ayuda caducada no equivale a financiación disponible.
* Caso ajeno no equivale a contenido del Taller.
* Una fuente no puede alimentar el plan sin clasificación previa.
* Toda fuente legal, normativa, financiera, de precios, ayudas o ubicación requiere verificación externa antes de usarse como afirmación fuerte.

# Límites / No hacer

No hacer:

* mover fuentes reales;
* copiar fuentes reales;
* importar archivos a `docs_fuentes/`;
* rellenar `respuestas_plan_empresa/`;
* crear `docs_consolidados/`;
* redactar el plan;
* declarar una fuente como validada si solo está inventariada;
* decidir estrategia de negocio;
* sustituir aprobación humana.

# Criterio de utilidad para Marketing / Producto

La salida debe ayudar a Marketing a responder:

* qué fuentes puede usar;
* qué fuentes no debe usar;
* qué fuentes requieren verificación;
* qué fuentes contaminan;
* qué fuentes sirven para cliente, competencia, mercado, legal, local, pricing, alianzas o viabilidad;
* qué vacíos siguen abiertos antes de redactar.

# Criterio de cierre

La skill se considera completada cuando existe una propuesta de inventario clara, trazable y revisable, y cuando ninguna acción física sobre fuentes reales queda implícitamente autorizada.

# Evidencia esperada

* Archivo de inventario o propuesta creado/modificado.
* Resumen de fuentes clasificadas.
* Riesgos detectados.
* Decisiones humanas pendientes.
* Confirmación explícita de que no se movieron ni copiaron fuentes reales.
