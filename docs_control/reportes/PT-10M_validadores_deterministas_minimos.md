# PT-10M — Validadores deterministas mínimos de Fase 2

## 1. Objetivo

Crear la capa determinista mínima de Fase 2 para que las comprobaciones exactas, repetibles y verificables no dependan de criterio de IA.

## 2. Scripts creados

- `scripts/validar_skills_frontmatter.py`
- `scripts/validar_no_rutas_prohibidas.py`
- `scripts/validar_placeholders_respuestas.py`

## 3. Qué valida cada script

### `validar_skills_frontmatter.py`

Valida que cada `SKILL.md`:

- existe;
- tiene frontmatter YAML;
- tiene `name`;
- tiene `description`;
- usa un `name` que coincide con la carpeta;
- no deja `description` vacía;
- devuelve `0` si todo está bien;
- devuelve `1` si hay errores.

### `validar_no_rutas_prohibidas.py`

Valida con `git status --short` que no haya cambios pendientes en:

- `respuestas_plan_empresa/`
- `_build/`
- `docs_consolidados/`

No bloquea por archivos nuevos fuera de esas rutas.

### `validar_placeholders_respuestas.py`

Valida `respuestas_plan_empresa/` buscando placeholders pendientes:

- `[PENDIENTE]`
- `Pendiente de completar`
- `TODO`
- `TBD`

El estado `PENDIENTE` no es un error técnico.

## 4. Qué no valida cada script

### `validar_skills_frontmatter.py`

- no audita contenido de negocio;
- no decide si una skill es útil;
- no verifica solapes semánticos;
- no aprueba la skill por sí sola.

### `validar_no_rutas_prohibidas.py`

- no revisa el contenido de los archivos;
- no valida `respuestas_plan_empresa/` por dentro;
- no comprueba coherencia de negocio;
- no impide cambios fuera de las rutas prohibidas.

### `validar_placeholders_respuestas.py`

- no rellena placeholders;
- no decide Gate 1D;
- no redacta respuestas;
- no considera error técnico encontrar placeholders esperados.

## 5. Comandos de ejecución

```bash
python3 scripts/validar_skills_frontmatter.py
python3 scripts/validar_no_rutas_prohibidas.py
python3 scripts/validar_placeholders_respuestas.py
python3 scripts/auditar_estado_plan_empresa.py
git status --short
git diff --stat
```

## 6. Resultado de ejecución

- `validar_skills_frontmatter.py`: OK.
- `validar_no_rutas_prohibidas.py`: OK.
- `validar_placeholders_respuestas.py`: `VERDICT: PENDIENTE` por los `17` placeholders esperados.
- `auditar_estado_plan_empresa.py`: `VERDICT: PENDIENTE` por los `17` placeholders esperados.

## 7. Limitaciones

- Los validadores son mínimos y de propósito acotado.
- No sustituyen la auditoría de Fase 2 completa.
- No abren Gate 1D.
- No sustituyen skills especialistas, gates ni workflows.

## 8. Siguiente PT recomendado

- `PT-10N — Gate mínimo de sistema agéntico listo para Fase 3`

## 9. Dictamen final

- `PT_10M_COMPLETO`

Estado final:

- la capa determinista mínima queda creada;
- la Fase 2 sigue incompleta por los placeholders de `respuestas_plan_empresa/`;
- el siguiente paso lógico es crear el gate mínimo de sistema agéntico para Fase 3.
