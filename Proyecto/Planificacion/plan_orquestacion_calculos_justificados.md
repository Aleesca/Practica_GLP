# Plan de orquestacion para Calculos justificados

## Objetivo

Este plan define como invocar el orquestador existente para elaborar o revisar el bloque de **Calculos justificados** del proyecto de GLP.

La invocacion es independiente y no debe ejecutarse en paralelo con la invocacion del bloque de **Memoria**. No se crean orquestadores especializados: se usa siempre `.agents/agents/task-orchestrator.md` con el alcance acotado por la orden de entrada.

## Orden de invocacion

```markdown
Orquesta la elaboracion del bloque Calculos justificados. Limita el trabajo al desarrollo numerico, comprobaciones, hipotesis de calculo, tablas, resultados intermedios y trazabilidad de magnitudes. No reescribas la Memoria descriptiva salvo referencias breves necesarias para contextualizar los calculos.
```

## Alcance

El orquestador debe coordinar la elaboracion documental de los Calculos justificados a partir de las fuentes canonicas del proyecto:

- `Proyecto/Alcance.md`
- `Proyecto/Datos.md`
- `Proyecto/Planificacion/esquema_memoria.md`
- `Proyecto/Planificacion/mapeo_markdown_a_latex.md`
- `Proyecto/Especificaciones/metodologia.md`
- `Proyecto/Especificaciones/`
- `Proyecto/Anotaciones/`

La salida primaria sigue siendo Markdown modular en `Proyecto/Especificaciones/`. La consolidacion LaTeX queda fuera de esta invocacion salvo peticion explicita posterior.

## Fuera de alcance

- No crear `task-orchestrator-calculos.md`.
- No crear ningun nuevo orquestador especializado.
- No ejecutar en paralelo esta tarea con el bloque de Memoria.
- No reescribir la Memoria descriptiva, salvo referencias breves necesarias para contextualizar un calculo.
- No modificar `Practica_GLPs_LaTeX/plantilla.tex` salvo peticion explicita.

## Fases de implementacion

### Fase 1. Apertura y delimitacion

El orquestador debe:

- Identificar los calculos requeridos: demanda, autonomia, vaporizacion, volumen de deposito, red de distribucion, perdidas de carga y anejos.
- Declarar entradas, salida esperada y huecos de informacion.
- Separar explicitamente que contenido queda reservado para Memoria.
- Confirmar que la salida primaria sera Markdown en `Proyecto/Especificaciones/`.

Criterios de aceptacion:

- [ ] El alcance queda limitado a Calculos justificados.
- [ ] Las magnitudes base quedan fijadas antes de desarrollar formulas.
- [ ] La reescritura narrativa de Memoria queda excluida de esta invocacion.

### Fase 2. Investigacion tecnica y trazabilidad numerica

El orquestador debe invocar a `glp-researcher` solo cuando necesite soporte tecnico para:

- Formulas de calculo.
- Coeficientes y parametros adoptados.
- Criterios normativos aplicables.
- Unidades y conversiones.
- Tablas, comprobaciones y trazabilidad de resultados.

Criterios de aceptacion:

- [ ] Cada calculo tiene fuente o criterio tecnico asociado.
- [ ] Las unidades se mantienen coherentes con el Sistema Internacional o con unidades tecnicas justificadas.
- [ ] Los parametros transversales no se contradicen entre demanda, autonomia, vaporizacion, deposito y red.

### Fase 3. Produccion o revision de Markdown

El orquestador debe coordinar la redaccion o revision de los modulos de Calculos justificados en `Proyecto/Especificaciones/`.

Cada bloque de calculo debe quedar estructurado con hipotesis, procedimiento, sustitucion de valores, resultado y comprobacion. Las referencias a Memoria deben limitarse a contexto o trazabilidad.

Criterios de aceptacion:

- [ ] Los calculos son reproducibles y auditables.
- [ ] Las tablas y resultados intermedios quedan incluidos donde correspondan.
- [ ] El bloque contiene justificacion suficiente para defender la solucion tecnica.

### Fase 4. Validacion dimensional y cierre

El orquestador debe:

- Validar coherencia dimensional, continuidad de magnitudes y correspondencia con `metodologia.md`.
- Comprobar que los resultados finales coinciden con los valores resumidos en Memoria.
- Cerrar la tarea con calculos trabajados, fuentes usadas, salida generada o pendiente, bloqueos reales y siguiente paso.

Criterios de aceptacion:

- [ ] No hay saltos de calculo sin explicacion.
- [ ] Los resultados finales pueden alimentar la Memoria sin duplicacion.
- [ ] La tarea queda preparada para una consolidacion editorial posterior, si se solicita.

## Verificacion del plan

- [ ] Este plan remite al orquestador existente `.agents/agents/task-orchestrator.md`.
- [ ] Este plan indica que la invocacion no es paralela a Memoria.
- [ ] Este plan no recomienda crear dos orquestadores.
- [ ] Este plan mantiene la salida primaria en `Proyecto/Especificaciones/`.
