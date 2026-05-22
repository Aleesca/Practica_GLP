# Plan de revision del sistema de agentes GLP

## Resumen

El plan fija el contrato operativo del sistema de agentes para que la documentacion del proyecto se gobierne por `Proyecto/Alcance.md`, `Proyecto/Datos.md`, `Proyecto/Planificacion/esquema_memoria.md`, `Proyecto/Especificaciones/metodologia.md` y `.agents/skills/`.

La revision no introduce desarrollo tecnico nuevo del proyecto. Solo consolida el marco documental y la separacion entre la produccion Markdown y la consolidacion editorial posterior.

## Cambios clave

- Confirmar `.agents/skills/` como ubicacion operativa unica de skills.
- Mantener `Proyecto/skills/` como espejo temporal, sin autoridad operativa.
- Reforzar `Proyecto/Especificaciones/` como salida documental primaria.
- Mantener `Practica_GLPs_LaTeX/` como capa editorial posterior, fuera del flujo activo hasta cerrar Markdown.
- Alinear el orquestador y los agentes auxiliares con el contrato canonico y el mapeo editorial existente.

## Verificacion

- Comprobar que `Proyecto/Alcance.md`, `Proyecto/Datos.md`, `Proyecto/Planificacion/esquema_memoria.md`, `Proyecto/Planificacion/mapeo_markdown_a_latex.md`, `Proyecto/Especificaciones/metodologia.md` y `.agents/skills/doc_tecnica_glp/` existen y siguen siendo la referencia activa.
- Revisar que `task-orchestrator`, `glp-researcher`, `latex-writer` y `latex-validator` solo delegan dentro del flujo previsto.
- Confirmar que no queda ninguna dependencia operativa del dominio anterior.
- Verificar con `rg` que `Proyecto/skills/` aparece solo como espejo temporal o referencia documental.

## Supuestos

- No se modifica `Practica_GLPs_LaTeX/plantilla.tex`.
- No se produce contenido tecnico nuevo de GLP.
- No se eliminan los espejos documentales existentes; solo se excluyen de la autoridad operativa.

## Criterio de aceptacion

El sistema queda alineado con GLP, sin dependencias del dominio anterior y con una separacion clara entre notas tecnicas, memoria modular y consolidacion editorial.
