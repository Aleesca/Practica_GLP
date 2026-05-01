# Plan de revision del sistema de agentes

## Estado del documento

- Tipo: plan de integracion
- Estado: activo
- Alcance: documentacion activa y skills del proyecto GLP

## Objetivo

Definir el contrato de trabajo del sistema de agentes para que el flujo documental del proyecto se gobierne por `Proyecto/Alcance.md`, `Proyecto/Datos.md`, `Proyecto/Planificacion/esquema_memoria.md`, `Proyecto/Especificaciones/metodologia.md` y `.agents/skills/`.

## Fuentes canonicas

- Alcance: `Proyecto/Alcance.md`
- Datos de partida: `Proyecto/Datos.md`
- Estructura de memoria: `Proyecto/Planificacion/esquema_memoria.md`
- Mapeo editorial: `Proyecto/Planificacion/mapeo_markdown_a_latex.md`
- Guia prescriptiva: `Proyecto/Especificaciones/metodologia.md`
- Skills operativas: `.agents/skills/`
- Skills espejo: `Proyecto/skills/`
- Salida primaria: `Proyecto/Especificaciones/`
- Consolidacion editorial posterior: `Practica_GLPs_LaTeX/`

## Decisiones fijadas

- `.agents/skills/` es la ubicacion operativa unica.
- `Proyecto/skills/` se conserva como espejo temporal.
- La salida primaria del sistema es `Proyecto/Especificaciones/`.
- La consolidacion en `Practica_GLPs_LaTeX/` queda fuera del flujo activo mientras el Markdown no este cerrado.
- El encaje del Markdown sobre la plantilla existente se gobierna por `Proyecto/Planificacion/mapeo_markdown_a_latex.md`.

## Fases de trabajo

### F1. Contrato canonico
- Validar rutas, entradas, salidas y artefactos.

### F2. Desarrollo documental
- Producir y revisar modulos de `Proyecto/Especificaciones/`.

### F3. Trazabilidad tecnica
- Mantener al dia `matriz_fuentes.md`, `mapa_citas.md` y los manifiestos.

### F4. Integracion editorial posterior
- Transferir al LaTeX propio del proyecto solo contenido ya cerrado.

## Criterio de aceptacion

El sistema queda alineado con GLP, sin dependencias del dominio anterior y con una separacion clara entre notas tecnicas, memoria modular y consolidacion editorial.
