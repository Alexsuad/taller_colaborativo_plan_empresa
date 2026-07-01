---
name: auditar-skill-creada
description: Usar para auditar una skill ya creada o modificada, verificando estructura, propósito, formato de salida, ejemplos, límites, evidencia mínima, solapes y utilidad funcional antes de aprobarla.
---

# Auditar skill creada

## Propósito

Auditar una skill ya creada o modificada antes de aprobarla, commitearla o usarla como parte de Fase 2.

## Cuándo usarla

Usarla cuando exista una skill nueva o modificada que deba revisarse antes de su uso real.

## Cuándo NO usarla

No usarla para decidir si una skill debe existir.
No usarla para redactar negocio.
No usarla para abrir Gates.

## Entradas

- skill auditada;
- ruta;
- contrato de origen;
- dictámenes previos;
- skills relacionadas;
- restricciones activas;
- casos de prueba.

## Salidas

- veredicto;
- hallazgos estructurales;
- hallazgos funcionales;
- hallazgos de integración;
- casos de prueba;
- resultado funcional;
- pruebas funcionales ejecutadas;
- resultado esperado vs resultado obtenido;
- ajustes requeridos;
- riesgo si se aprueba;
- decisión humana requerida.

## Niveles de auditoría

### 1. Estructura

- frontmatter;
- name;
- description;
- secciones obligatorias;
- formato de respuesta;
- valores cerrados;
- ejemplos;
- evidencia mínima;
- prohibiciones;
- criterio de cierre.

### 2. Calidad funcional

- si resuelve la necesidad real;
- si no duplica otra skill;
- si no invade scripts, gates, reglas, workflows o subagentes;
- si puede ejecutarse repetidamente;
- si genera salida auditable;
- si bloquea cuando falta información;
- si evita ambigüedad;
- si respeta Fase 2 / Fase 3;
- si no maquilla resultados;
- si no convierte hipótesis en hechos;
- si el resultado funcional realmente sirve para la tarea prevista.

### 3. Integración

- si puede usarse con `decidir-tipo-pieza-sistema-agentico`;
- si puede usarse con `auditar-skill-antes-de-crear`;
- si puede usarse con `crear-skill-desde-contrato`;
- si necesita script complementario;
- si debe quedar pendiente de revisión humana.

## Checklist estructural

- frontmatter válido;
- propósito claro;
- uso y no uso claros;
- entradas y salidas claras;
- formato cerrado;
- ejemplos útiles;
- criterio de cierre;
- evidencia mínima;
- prohibiciones.

## Checklist funcional

- la skill hace una sola cosa principal;
- la salida es accionable;
- el alcance es acotado;
- no mezcla capas;
- no crea falsos positivos de aprobación;
- no simula completitud;
- no elimina necesidad de revisión humana cuando el impacto es alto;
- el resultado funcional realmente sirve para la tarea prevista.

## Checklist de integración

- encaja con la cadena `decidir-tipo-pieza-sistema-agentico` → `auditar-skill-antes-de-crear` → `crear-skill-desde-contrato` → `auditar-skill-creada`;
- no rompe la sede de skills;
- no depende de una pieza no aprobada;
- no sustituye validaciones exactas por lenguaje ambiguo.

## Pruebas con casos

- caso normal;
- caso incompleto;
- caso que debería bloquear;
- caso de solape con otra skill;
- caso que realmente debería ser script, gate, regla o workflow.

Cada prueba debe indicar:

```text
CASO:
ENTRADA_RESUMIDA:
RESULTADO_ESPERADO:
RESULTADO_OBTENIDO:
DICTAMEN_DE_LA_PRUEBA:
```

## Casos de prueba obligatorios

La skill auditada debe probarse, como mínimo, con:

1. caso normal;
2. caso incompleto;
3. caso que debe bloquear;
4. caso de solape con otra pieza;
5. caso que no corresponde a esa skill.

## Formato de respuesta

```text
SKILL_AUDITADA:
RUTA:
VEREDICTO:
HALLAZGOS_ESTRUCTURALES:
HALLAZGOS_FUNCIONALES:
HALLAZGOS_INTEGRACION:
CASOS_DE_PRUEBA:
PRUEBAS_FUNCIONALES_EJECUTADAS:
RESULTADO_FUNCIONAL:
AJUSTES_REQUERIDOS:
RIESGO_SI_SE_APRUEBA:
DECISION_HUMANA_REQUERIDA: SI/NO
DICTAMEN:
```

## Dictámenes permitidos

- `APROBADA`
- `APROBADA_CON_AJUSTES_MENORES`
- `REQUIERE_AJUSTES`
- `BLOQUEADA`
- `REQUIERE_DECISION_HUMANA`

## Valores permitidos para `RESULTADO_FUNCIONAL`

- `FUNCIONA`
- `FUNCIONA_CON_AJUSTES`
- `NO_FUNCIONA`
- `NO_PROBADA`

## Regla obligatoria

Si no se ejecutan pruebas funcionales, `RESULTADO_FUNCIONAL` debe ser `NO_PROBADA`.
No se puede emitir `DICTAMEN: APROBADA` si `RESULTADO_FUNCIONAL` es `NO_PROBADA`, `NO_FUNCIONA` o `FUNCIONA_CON_AJUSTES`.

## Criterio de cierre

La skill queda cerrada cuando la auditoría deja claro si puede aprobarse, corregirse o bloquearse, y también si funciona realmente en los casos probados.

## Evidencia mínima

- skill auditada;
- checklist completado;
- casos de prueba;
- pruebas funcionales ejecutadas;
- resultado funcional;
- dictamen;
- decisión humana requerida, si aplica.

## Prohibiciones

- No aprobar una skill solo porque existe.
- No aprobar una skill solo porque Git está limpio.
- No aprobar una skill sin leer contenido.
- No aprobar una skill sin casos de prueba.
- No hacer commit sin revisión humana cuando el cambio sea de alto impacto.
- No tocar `respuestas_plan_empresa/`.
- No abrir Gate 1D.

## Criterio operativo del proyecto

Una skill no se crea por ocurrencia. Se planifica, se conecta con negocio, se define con entradas y salidas, se usa para que la IA siga pasos constantes, se audita con checklist y se somete a revisión humana cuando afecta decisiones importantes.
