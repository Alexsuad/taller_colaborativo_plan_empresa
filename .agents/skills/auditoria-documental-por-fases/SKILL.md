---

name: auditoria-documental-por-fases
description: Audita si una intervención documental respeta la fase vigente del proyecto, sus límites, sus carpetas autorizadas y su criterio de cierre. Use after any agent, script, human or automation modifies repository documents.
---

# Propósito

Usar esta skill para revisar si una entrega respeta la fase actual del proyecto y no avanza artificialmente hacia fases posteriores.

Su función es emitir un veredicto claro: aprobado, aprobado con ajustes, bloqueado o fuera de fase.

# Cuándo usar esta skill

Usar después de:

* crear una propuesta documental;
* modificar documentos de organización;
* crear skills;
* crear plantillas;
* ejecutar cambios por terminal;
* recibir entregas de Codex o Antigravity;
* recibir entregas de Marketing o Desarrollo;
* antes de cerrar una sub-tarea.

# Entradas esperadas

* Descripción de la intervención.
* Lista de archivos creados.
* Lista de archivos modificados.
* Lista de archivos no tocados.
* Fase vigente del proyecto.
* Resultado de auditoría técnica, si existe.
* Restricciones activas.
* Riesgos reportados.

# Salidas esperadas

Informe de auditoría con:

* fase evaluada;
* alcance real;
* archivos tocados;
* cumplimiento de restricciones;
* hallazgos;
* riesgos;
* veredicto;
* decisiones humanas requeridas.

# Procedimiento

1. Confirmar fase vigente.
2. Comparar intervención contra alcance autorizado.
3. Revisar si se tocaron carpetas prohibidas.
4. Revisar si se redactó contenido fuera de fase.
5. Revisar si se movieron o importaron fuentes reales sin autorización.
6. Revisar si se crearon estructuras no autorizadas.
7. Revisar si el resultado de auditoría técnica coincide con lo esperado.
8. Evaluar utilidad real para el plan de empresa.
9. Emitir veredicto.
10. Listar próximos pasos permitidos.

# Veredictos posibles

* APROBADO
* APROBADO CON AJUSTES
* BLOQUEADO
* FUERA DE FASE
* REQUIERE DECISIÓN HUMANA

# Reglas obligatorias

* En Fase 1.1, `VERDICT: PENDIENTE` puede ser correcto.
* No confundir auditoría correcta con proyecto terminado.
* No pasar a Fase 1.2 sin aprobación explícita.
* No considerar una propuesta como acción física autorizada.
* No validar contenido de negocio solo porque el formato sea correcto.

# Límites / No hacer

No hacer:

* redactar contenido nuevo del plan;
* decidir negocio;
* corregir archivos por cuenta propia;
* crear nuevas tareas fuera del alcance;
* aprobar importaciones no autorizadas;
* cerrar fases sin decisión humana.

# Criterio de utilidad para Marketing / Producto

La auditoría debe responder:

* si la entrega ayuda a construir un plan más claro, honesto y trazable;
* si evita convertir hipótesis en afirmaciones;
* si produce una salida útil para decidir;
* si evita retrabajo;
* si respeta que Marketing decide contenido de negocio y Desarrollo implementa técnica.

# Criterio de cierre

La skill se considera completada cuando el veredicto es explícito y deja claro qué puede hacerse después y qué sigue bloqueado.

# Evidencia esperada

* Informe de auditoría.
* Veredicto.
* Lista de archivos afectados.
* Resultado de comando de auditoría, si aplica.
* Próxima decisión humana requerida.
