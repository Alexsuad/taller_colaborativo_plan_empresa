---

name: higiene-estructura-documental-5s
description: Revisa orden, nombres, rutas, duplicados, placeholders, basura técnica y coherencia estructural del repositorio documental sin decidir contenido de negocio. Use when maintaining repository hygiene before importing sources or running document pipelines.
---

# Propósito

Usar esta skill para mantener limpia la estructura documental del repositorio.

Su función no es decidir contenido, sino evitar que el sistema se rompa por rutas duplicadas, carpetas paralelas, basura técnica, placeholders mal usados o nombres inconsistentes.

# Cuándo usar esta skill

Usar cuando:

* se detecten rutas divergentes;
* haya carpetas con nombres antiguos;
* aparezcan archivos `*Zone.Identifier*`;
* existan carpetas vacías o solo `.gitkeep`;
* haya duplicados funcionales;
* se preparen importaciones;
* se creen nuevas estructuras;
* se revise el estado antes de una auditoría.

# Entradas esperadas

* Estructura esperada del repo.
* Listado de carpetas existentes.
* Listado de archivos detectados.
* Fase vigente.
* Carpetas autorizadas y prohibidas.
* Resultado de `git status`, si aplica.

# Salidas esperadas

Informe de higiene con:

* rutas correctas;
* rutas inconsistentes;
* carpetas vacías;
* placeholders;
* duplicados;
* basura técnica;
* acciones recomendadas;
* acciones bloqueadas;
* decisiones humanas requeridas.

# Procedimiento

1. Confirmar estructura oficial.
2. Listar carpetas relevantes.
3. Comparar rutas físicas contra rutas aprobadas.
4. Detectar carpetas paralelas o nombres antiguos.
5. Detectar placeholders.
6. Detectar archivos `*Zone.Identifier*`.
7. Detectar duplicados funcionales.
8. Separar limpieza segura de limpieza que requiere aprobación.
9. Emitir propuesta de acción.
10. No ejecutar eliminación si no está autorizada.

# Reglas obligatorias

* No borrar sin listar antes.
* No renombrar carpetas con archivos reales sin aprobación.
* No crear carpetas paralelas.
* No tocar `docs_fuentes/` si la tarea no lo autoriza.
* No modificar contenido de negocio.
* No resolver conflictos semánticos como si fueran simples errores de ruta.
* No confundir limpieza técnica con decisión documental.

# Límites / No hacer

No hacer:

* mover fuentes reales;
* borrar fuentes reales;
* editar contenido estratégico;
* reclasificar fuentes;
* modificar plan de empresa;
* decidir sedes documentales nuevas sin aprobación;
* limpiar por intuición.

# Criterio de utilidad para Marketing / Producto

La skill debe reducir errores que afecten el plan, especialmente:

* rutas incorrectas;
* duplicación de fuentes;
* pérdida de trazabilidad;
* creación de carpetas no aprobadas;
* contaminación por archivos técnicos;
* fricción al importar fuentes reales.

# Criterio de cierre

La skill se considera completada cuando queda claro qué está limpio, qué está desalineado y qué requiere decisión humana antes de corregirse.

# Evidencia esperada

* Listado de rutas revisadas.
* Listado de inconsistencias.
* Listado de basura técnica.
* Recomendación de limpieza.
* Confirmación de que no se borró ni movió contenido real sin autorización.
