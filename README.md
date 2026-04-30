# Proyecto de Instalacion de GLP

Base documental y de coordinacion para el calculo y diseno de una instalacion de almacenamiento y distribucion de GLP del grupo `G1-1`.

## Quick Start

1. Revisa el alcance en `Proyecto/Alcance.md`.
2. Revisa los datos de partida en `Proyecto/Datos.md`.
3. Usa `Proyecto/Planificacion/esquema_memoria.md` y `Proyecto/Especificaciones/metodologia.md` como contrato de trabajo.
4. Desarrolla las notas tecnicas en `Proyecto/Anotaciones/` y la salida final en `Proyecto/Especificaciones/`.
5. Consulta la documentacion tecnica de apoyo en `.agents/skills/doc_tecnica_glp/`.
6. Consolida editorialmente en `Practica_GLPs_LaTeX/` solo cuando el contenido Markdown ya este cerrado.

## Estructura operativa

- `00_Info_proporcionada/`: datos de partida, enunciado y modelo base del proyecto.
- `01_Planos/`: planos de trabajo y archivo CAD base.
- `Proyecto/Planificacion/`: gobierno documental, trazabilidad y planes de trabajo.
- `Proyecto/Especificaciones/`: salida tecnica primaria en Markdown modular.
- `Proyecto/Anotaciones/`: notas tecnicas, criterios y soporte intermedio.
- `.agents/skills/`: skills operativas canonicas del proyecto.
- `Proyecto/skills/`: espejo temporal de skills para apoyo documental.
- `Practica_GLPs_LaTeX/`: consolidacion editorial posterior; no es la fuente de verdad tecnica.
- `ZZ_Normativa/`: normativa de referencia y documentos reglamentarios.

## Decisiones de arquitectura

- El flujo activo se gobierna por `Proyecto/Alcance.md`, `Proyecto/Datos.md`, `Proyecto/Planificacion/esquema_memoria.md` y `Proyecto/Especificaciones/metodologia.md`.
- `Proyecto/Especificaciones/` es la salida primaria del sistema.
- `Practica_GLPs_LaTeX/` se mantiene como capa de consolidacion posterior.
- `.agents/skills/` es la ubicacion operativa de skills.
- `Proyecto/skills/` se conserva como espejo temporal y no debe gobernar el sistema activo.

## Documentacion clave

- `Proyecto/Alcance.md`
- `Proyecto/Datos.md`
- `Proyecto/Planificacion/esquema_memoria.md`
- `Proyecto/Especificaciones/metodologia.md`
- `Proyecto/Planificacion/matriz_fuentes.md`
- `Proyecto/Planificacion/mapa_citas.md`
