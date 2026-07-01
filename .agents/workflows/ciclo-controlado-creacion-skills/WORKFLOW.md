# Ciclo controlado de creación de skills

## Propósito
Encadenar de forma controlada la decisión, auditoría, creación, revisión y validación de skills para evitar duplicados, solapes y piezas incompletas.

## Cuándo usarlo
Usar este workflow cuando exista un contrato o necesidad concreta que pueda convertirse en una skill y se quiera cerrar el ciclo con evidencia mínima antes de revisión humana.

## Cuándo NO usarlo
No usarlo cuando:
- la necesidad no esté todavía formulada;
- se quiera crear contenido de negocio;
- se pretenda saltar auditoría previa;
- falte autorización humana para crear la pieza;
- la salida esperada sea un cambio en `respuestas_plan_empresa/`.

## Entradas
- contrato o necesidad concreta;
- skill o pieza candidata;
- restricciones vigentes;
- evidencia documental disponible;
- criterio de cierre esperado.

## Salidas
- dictamen de tipo de pieza;
- dictamen de auditoría previa;
- SKILL.md creado o rechazado;
- auditoría posterior de la skill creada;
- paquete listo para revisión humana.

## Pasos obligatorios
1. Recibir el contrato o necesidad.
2. Ejecutar `decidir-tipo-pieza-sistema-agentico`.
3. Si el dictamen admite skill, ejecutar `auditar-skill-antes-de-crear`.
4. Si corresponde, crear o completar la skill desde el contrato.
5. Ejecutar `auditar-skill-creada`.
6. Si hay ajustes, corregir la skill y volver a auditar.
7. Ejecutar los validadores deterministas aplicables.
8. Preparar el resultado para revisión humana y, si procede, commit.

## Criterio operativo del proyecto
Una skill no se crea por ocurrencia. Se planifica, se conecta con el negocio, se define con entradas y salidas, se usa para que la IA siga pasos constantes, se audita con checklist y se somete a revisión humana cuando afecta decisiones importantes.

## Criterio de cierre
El workflow queda cerrado cuando:
- la pieza está clasificada;
- la auditoría previa está resuelta;
- la skill, si existe, está funcionalmente auditable;
- la validación mínima pasa;
- la revisión humana puede decidir sin ambigüedad.

## Evidencia mínima
- contrato o necesidad de partida;
- dictamen de tipo de pieza;
- dictamen de auditoría previa;
- skill creada o descartada;
- auditoría de la skill creada;
- salida de validadores.

## Prohibiciones
- no crear skills por defecto;
- no saltar auditoría previa;
- no crear scripts, gates, workflows o subagentes sin dictamen previo;
- no tocar `respuestas_plan_empresa/`;
- no convertir la revisión humana en un trámite automático;
- no mezclar creación de skill con redacción final del plan.
