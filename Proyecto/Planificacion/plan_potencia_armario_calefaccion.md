# Plan de calculo y justificacion del armario de calefaccion GLP

## Estado del documento

- Tipo: plan de implementacion documental
- Estado: activo
- Alcance: incorporacion de una justificacion tecnica y un calculo de potencia termica para el armario de calefaccion asociado a la vaporizacion forzada de la instalacion de GLP

## Objetivo

Definir el trabajo necesario para documentar, de forma trazable, la potencia termica en kW que debe tener el armario de calefaccion para garantizar la demanda de la instalacion de GLP, y para justificar tecnicamente por que su instalacion es necesaria.

El resultado final debe quedar reflejado en dos soportes:

- Un nuevo apartado de calculo dentro de `calculos/calculos.ipynb`.
- Un nuevo documento de justificacion tecnica en `Proyecto/Anotaciones/`.

## Fuentes de entrada

- NotebookLM: notebook `GLP`, como apoyo documental y tecnico.
- Cuaderno de calculos: `calculos/calculos.ipynb`.
- Anotaciones del proyecto: `Proyecto/Anotaciones/`.

## Decisiones fijadas

- El notebook `GLP` se usara solo como fuente de consulta documental y no se modifica en esta fase.
- No se incorporaran nuevos calculos en ningun fichero fuera de `calculos/calculos.ipynb` y del nuevo `.md` de `Proyecto/Anotaciones/`.
- La justificacion tecnica debe cubrir tanto la necesidad funcional del armario como el desarrollo numerico de la potencia requerida.
- El calculo debe apoyarse en el caudal ya determinado en `calculos/calculos.ipynb`, no en una estimacion nueva sin trazabilidad.
- La redaccion final debe conservar la coherencia con las anotaciones existentes sobre demanda, vaporizacion natural, vaporizacion forzada, temperatura de diseno y seleccion del deposito.

## Estructura objetivo del trabajo

Se propone que la documentacion final quede organizada en dos piezas:

1. `calculos/calculos.ipynb`
   - Nuevo apartado de calculo de potencia termica.
   - Variables de entrada claramente identificadas.
   - Ecuaciones numericas y resultado final en kW.
   - Comparacion con la potencia del armario seleccionado, si aplica.

2. `Proyecto/Anotaciones/potencia_armario_calefaccion.md`
   - Justificacion tecnica de la necesidad del armario.
   - Desarrollo matematico del calculo.
   - Trazabilidad hacia las anotaciones existentes y hacia el notebook `GLP`.
   - Conclusion tecnica sobre la suficiencia del equipo.

## Fases de trabajo

### F1. Definicion tecnica del criterio de calculo

- Establecer el criterio de dimensionado que se va a seguir para calcular la potencia termica del armario.
- Determinar si el armario se dimensiona por deficit de vaporizacion natural, por capacidad forzada requerida o por otro criterio tecnico que quede claramente justificado.
- Fijar las magnitudes fisicas y las ecuaciones que deben aparecer en la memoria de calculo.

### F2. Justificacion de la necesidad del armario

- Redactar la causa tecnica que hace necesario el armario de calefaccion.
- Explicar que la vaporizacion natural puede no ser suficiente en las condiciones de diseno.
- Justificar que el aporte termico externo es imprescindible para garantizar continuidad de suministro, presion estable y caudal demandado.
- Dejar claro que la instalacion del armario responde a una necesidad funcional y no a una mejora opcional.

### F3. Integracion del calculo en el notebook

- Crear un bloque nuevo en `calculos/calculos.ipynb` para el calculo de potencia termica.
- Introducir los datos de partida de forma ordenada y reutilizable.
- Mostrar el desarrollo con ecuaciones y sustitucion numerica.
- Cerrar el bloque con el valor final requerido en kW y con la comprobacion de suficiencia del armario.

### F4. Redaccion del documento tecnico en Markdown

- Crear el fichero `Proyecto/Anotaciones/potencia_armario_calefaccion.md`.
- Incluir una introduccion, la justificacion tecnica, el desarrollo del calculo y la conclusion.
- Añadir referencias cruzadas a las anotaciones existentes que sustentan la decision.
- Mantener un lenguaje tecnico, explicito y verificable.

### F5. Revision de coherencia documental

- Verificar que la nueva anotacion no duplica contenido que pertenezca a otros apartados del proyecto.
- Comprobar que la secuencia de razonamiento sea compatible con la documentacion ya existente.
- Revisar que las unidades, nomenclatura y simbolos matematicos se mantengan consistentes en ambos soportes.

## Salidas esperadas

- Un nuevo apartado en `calculos/calculos.ipynb` con el calculo completo de la potencia termica del armario de calefaccion.
- Un nuevo fichero Markdown en `Proyecto/Anotaciones/` con la justificacion tecnica completa.
- Una conclusion clara sobre por que el armario es necesario y que potencia debe tener para garantizar la demanda de la instalacion.

## Criterios de aceptacion

- El documento explica de forma explicita por que es necesario instalar un armario de calefaccion.
- El calculo se basa en el caudal ya calculado en el cuaderno existente.
- El resultado final se presenta en kW y queda justificado paso a paso.
- El nuevo apartado del notebook y la anotacion Markdown quedan enlazados conceptualmente con las demas anotaciones del proyecto.
- La documentacion final no introduce datos sin soporte ni rompe la coherencia documental existente.

## Supuestos

- El notebook `GLP` servira como soporte tecnico documental para el criterio de diseno.
- La redaccion del nuevo documento priorizara la trazabilidad sobre la extension.
- Si durante la fase de implementacion aparecieran varios criterios posibles de dimensionado, se dejara explicitado cual se adopta y por que.
