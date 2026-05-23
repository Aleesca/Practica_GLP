# Plan de orquestacion para la Memoria

## Objetivo

Este plan define como invocar el orquestador existente para elaborar o revisar el bloque de **Memoria** del proyecto de GLP.

La invocacion es independiente y no debe ejecutarse en paralelo con la invocacion del bloque de **Calculos justificados**. No se crean orquestadores especializados: se usa siempre `.agents/agents/task-orchestrator.md` con el alcance acotado por la orden de entrada.

## Orden de invocacion

```markdown
Orquesta la elaboracion del bloque Memoria. Limita el trabajo a la redaccion descriptiva, justificacion tecnica, normativa, seleccion de solucion, equipos, red, implantacion, seguridad, conclusiones y limitaciones. No desarrolles el cuerpo completo de los Calculos justificados ni tablas numericas extensas.
```

## Alcance

El orquestador debe coordinar la elaboracion documental de la Memoria a partir de las fuentes canonicas del proyecto:

- `Proyecto/Alcance.md`
- `Proyecto/Datos.md`
- `Proyecto/Planificacion/esquema_memoria.md`
- `Proyecto/Planificacion/mapeo_markdown_a_latex.md`
- `Proyecto/Especificaciones/metodologia.md`
- `Proyecto/Especificaciones/`
- `Proyecto/Anotaciones/`

La salida primaria sigue siendo Markdown modular en `Proyecto/Especificaciones/`. La consolidacion LaTeX queda fuera de esta invocacion salvo peticion explicita posterior.

## Fuera de alcance

- No crear `task-orchestrator-memoria.md`.
- No crear ningun nuevo orquestador especializado.
- No ejecutar en paralelo esta tarea con el bloque de Calculos justificados.
- No redactar el desarrollo completo de calculos, tablas numericas extensas ni resultados intermedios propios del bloque de Calculos justificados.
- No modificar `Practica_GLPs_LaTeX/plantilla.tex` salvo peticion explicita.

## Fases de implementacion

### Fase 1. Apertura y delimitacion

El orquestador debe:

- Identificar las secciones de Memoria afectadas segun `esquema_memoria.md`.
- Declarar entradas, salida esperada y huecos de informacion.
- Separar explicitamente que contenido queda reservado para Calculos justificados.
- Confirmar que la salida primaria sera Markdown en `Proyecto/Especificaciones/`.

Criterios de aceptacion:

- [ ] El alcance queda limitado a Memoria.
- [ ] Las fuentes canonicas quedan listadas.
- [ ] Los desarrollos numericos completos quedan excluidos de esta invocacion.

### Fase 2. Investigacion tecnica acotada

El orquestador debe invocar a `glp-researcher` solo cuando necesite soporte documental para:

- Normativa y criterios tecnicos aplicables.
- Seleccion y justificacion de la solucion adoptada.
- Caracteristicas de equipos.
- Red de distribucion desde el punto de vista descriptivo.
- Implantacion, seguridad, accesos y distancias reglamentarias.

Criterios de aceptacion:

- [ ] La investigacion produce soporte trazable para la Memoria.
- [ ] No duplica el desarrollo numerico propio de Calculos justificados.
- [ ] Las magnitudes criticas quedan referenciadas para mantener coherencia con los calculos.

### Fase 3. Produccion o revision de Markdown

El orquestador debe coordinar la redaccion o revision de los modulos de Memoria en `Proyecto/Especificaciones/`, manteniendo un tono tecnico, descriptivo y justificativo.

El contenido puede incluir resultados finales necesarios para entender la solucion, pero no debe sustituir al desarrollo numerico justificativo.

Criterios de aceptacion:

- [ ] La Memoria explica objeto, datos de partida, solucion adoptada, equipos, red, implantacion, seguridad, conclusiones y limitaciones.
- [ ] Los calculos aparecen solo como resultados resumidos o referencias.
- [ ] La redaccion es compatible con una consolidacion editorial posterior en LaTeX.

### Fase 4. Validacion y cierre

El orquestador debe:

- Validar la coherencia contra `Proyecto/Alcance.md`, `esquema_memoria.md`, `metodologia.md` y `mapeo_markdown_a_latex.md`.
- Comprobar que no se ha invadido el bloque de Calculos justificados.
- Cerrar la tarea con secciones trabajadas, fuentes usadas, salida generada o pendiente, bloqueos reales y siguiente paso.

Criterios de aceptacion:

- [ ] La validacion es semantica y documental, no de compilacion LaTeX salvo peticion explicita.
- [ ] El cierre identifica pendientes reales.
- [ ] La tarea queda preparada para que, en una invocacion separada, se aborde Calculos justificados.

## Verificacion del plan

- [ ] Este plan remite al orquestador existente `.agents/agents/task-orchestrator.md`.
- [ ] Este plan indica que la invocacion no es paralela a Calculos justificados.
- [ ] Este plan no recomienda crear dos orquestadores.
- [ ] Este plan mantiene la salida primaria en `Proyecto/Especificaciones/`.
