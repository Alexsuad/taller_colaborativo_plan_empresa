---

name: preparar-paquete-ejecucion-tecnica
description: Convierte una decisión aprobada en un paquete técnico cerrado para Codex, Antigravity o terminal, con contenido exacto, rutas, comandos permitidos, restricciones, validación y criterio de cierre. Use when execution must happen without strategic interpretation.
---

# Propósito

Usar esta skill para preparar instrucciones técnicas cerradas que un agente o una persona pueda ejecutar sin interpretar el negocio.

La función central es reducir iteraciones, errores y cambios no autorizados.

# Cuándo usar esta skill

Usar cuando:

* el contenido sustantivo ya está decidido;
* se necesita crear o reemplazar un archivo con texto exacto;
* se necesita crear carpetas aprobadas;
* se necesita ejecutar comandos de validación;
* se quiere evitar que Codex o Antigravity redacten;
* se prepara una tarea de terminal;
* se empaqueta una intervención técnica limitada.

# Entradas esperadas

* Objetivo técnico.
* Ruta exacta de archivos.
* Contenido exacto si aplica.
* Comandos permitidos.
* Comandos prohibidos.
* Restricciones de carpetas.
* Validación esperada.
* Criterio de cierre.
* Evidencia esperada.

# Salidas esperadas

Un paquete técnico con:

* nombre de tarea;
* objetivo;
* alcance autorizado;
* alcance prohibido;
* pasos exactos;
* contenido exacto a pegar;
* comandos;
* validaciones;
* reporte esperado.

# Procedimiento

1. Confirmar que la tarea es técnica, no estratégica.
2. Identificar archivos y carpetas autorizadas.
3. Redactar instrucciones sin ambigüedad.
4. Incluir contenido exacto cuando se cree o reemplace un archivo.
5. Incluir comandos seguros.
6. Incluir restricciones explícitas.
7. Incluir validación esperada.
8. Incluir formato de reporte.
9. Prohibir interpretación de negocio.
10. Prohibir cambios fuera del alcance.

# Reglas obligatorias

* El agente técnico no inventa contenido estratégico.
* El agente técnico no decide negocio.
* El agente técnico no reclasifica fuentes salvo instrucción expresa.
* El agente técnico no mueve fuentes reales sin tabla aprobada.
* El agente técnico debe reportar si encuentra divergencias.
* Si encuentra archivos no esperados, se detiene y pregunta.
* Si una carpeta contiene archivos reales cuando se esperaba solo `.gitkeep`, se detiene.

# Límites / No hacer

No hacer:

* redactar plan de empresa;
* ajustar narrativa comercial;
* modificar contenido sustantivo no aprobado;
* tocar carpetas prohibidas;
* ejecutar comandos destructivos sin autorización;
* limpiar archivos sin listar antes;
* asumir intención del usuario.

# Criterio de utilidad para Marketing / Producto

La skill debe ayudar a que Marketing entregue necesidades claras a Desarrollo sin ambigüedad, y a que Desarrollo ejecute sin desplazar decisiones de negocio.

Debe responder:

* qué problema reduce;
* qué error evita;
* qué entregable mejora;
* qué decisión humana conserva.

# Criterio de cierre

La skill se considera completada cuando el paquete técnico puede ejecutarse de forma mecánica, verificable y sin interpretación estratégica.

# Evidencia esperada

* Paquete de ejecución.
* Comandos ejecutados.
* Archivos creados/modificados.
* Archivos no tocados.
* Resultado de auditoría.
* Divergencias encontradas.
