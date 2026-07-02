---
name: validar-coherencia-cliente-propuesta-canales
description: Use when client, value proposition, channels, and communication must be checked together before a block advances.
---

# Validar coherencia cliente, propuesta y canales

> [!NOTE]
> **Estado:** LEGACY / SECUNDARIA.  
> **Uso permitido:** revisión rápida de coherencia cliente → propuesta → canales.  
> **No sustituye a `validar-coherencia-comercial-global`**, que es la skill principal para validar la cadena completa:  
> cliente → propuesta → posicionamiento → canales → acciones → presupuesto/recursos → ventas → KPIs.

## Propósito
Comprobar que cliente, propuesta de valor y canales forman un conjunto coherente antes de pasar a redacción.

## Entradas
- cliente definido;
- propuesta de valor;
- canales;
- comunicación o red prevista.

## Salida esperada
- coherencia / ajuste / bloqueo;
- causa;
- siguiente acción.

## Criterios de bloqueo
- cliente ausente;
- propuesta genérica;
- canal incoherente;
- mezcla de capas.

## Checklist mínimo
- cliente explícito;
- propuesta específica;
- canal justificado;
- comunicación alineada.

## Evidencia requerida
- bloque o capítulo;
- fuente revisada;
- dictamen.

## Formato mínimo de salida
* Veredicto: `APROBADO`, `REQUIERE_AJUSTES` o `BLOQUEADO`.
* Semáforos mínimos:
  * Completitud;
  * Especificidad;
  * Coherencia;
  * Accionabilidad;
  * Realismo.
* Hallazgos críticos.
* Siguiente acción recomendada.

## Límites
- no sustituye auditorías especializadas;
- no redacta contenido final;
- no decide el negocio.
