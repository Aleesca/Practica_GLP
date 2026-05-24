# Plan de revision de especificaciones para Calculos justificados

## Resumen

Este plan define la revision documental necesaria para alinear el bloque de **Calculos justificados** con la plantilla LaTeX del proyecto, evitando tratarlo como un anejo independiente cuando el contenido debe vivir dentro del capitulo correspondiente.

Tambien fija dos requisitos de formato y contenido que deben quedar reflejados en las especificaciones antes de ejecutar cualquier cambio de orquestacion:

- la tabla de resultados del dimensionado de tuberias debe ir en una hoja aislada **A4 horizontal**, conservando encabezado y pie de pagina del resto del documento;
- el capitulo de **Calculos justificados** debe incluir un apartado de **Bibliografia** siguiendo el criterio ya usado en el capitulo de Memoria.

## Cambios clave

- Revisar `Proyecto/Especificaciones/anejos.md` para eliminar o reencuadrar cualquier instruccion que presuponga un anejo de calculos separado.
- Alinear las especificaciones del bloque de calculos con `Practica_GLPs_LaTeX/plantilla.tex`, de forma que el contenido tecnico resida en el capitulo **Calculos justificados**.
- Incorporar en `Proyecto/Especificaciones/` la regla de salida para el dimensionado de tuberias: una unica hoja A4 horizontal, aislada, con los estilos de encabezado y pie de pagina del documento.
- Añadir en las especificaciones del capitulo un apartado de **Bibliografia** equivalente al del capitulo de Memoria.

## Fases

### Fase 1. Revision de anejos

Identificar las instrucciones de `Proyecto/Especificaciones/anejos.md` que asuman un anejo de calculos y reexpresarlas para que encajen en el capitulo de **Calculos justificados**.

Salida esperada:

- referencias a anejo de calculos sustituidas por referencias al capitulo correspondiente;
- delimitacion clara entre anejos reales y calculos integrados en el cuerpo del documento;
- no se altera la plantilla LaTeX en esta fase.

### Fase 2. Ajuste de la estructura del capitulo

Actualizar las especificaciones del bloque de calculos para que el contenido tecnico, las tablas y los resultados formen parte del capitulo **Calculos justificados**.

Salida esperada:

- el bloque de calculos queda definido como parte del cuerpo principal;
- la orquestacion posterior ya no depende de un anejo de calculos;
- el contenido sigue siendo compatible con la estructura existente del documento.

### Fase 3. Formato de la tabla de dimensionado

Establecer en las especificaciones que la tabla de resultados del dimensionado de tuberias debe emitirse en una hoja aislada **A4 horizontal**.

Reglas obligatorias:

- conservar los estilos de encabezado y pie de pagina del resto del documento;
- mantener la tabla separada como pieza documental unica;
- evitar cualquier formato que la convierta en anejo independiente de calculos.

Salida esperada:

- requisito de formato documentado de forma inequívoca;
- salida preparada para integracion editorial posterior sin cambios de estilo estructural.

### Fase 4. Bibliografia del capitulo

Incluir en las especificaciones del capitulo de **Calculos justificados** un apartado de **Bibliografia** con el mismo criterio funcional que el capitulo de Memoria.

Salida esperada:

- el capitulo de calculos queda cerrado con su propia bibliografia;
- el criterio bibliografico queda alineado entre Memoria y Calculos justificados;
- no se crean referencias bibliograficas aisladas fuera de la estructura del capitulo.

### Fase 5. Preparacion de la orquestacion posterior

Actualizar posteriormente el plan de orquestacion de calculos para reflejar las especificaciones ya revisadas.

Salida esperada:

- el plan de orquestacion hereda la nueva definicion del capitulo;
- la tabla A4 horizontal queda contemplada como salida obligatoria;
- la bibliografia del capitulo queda incluida en el flujo de trabajo;
- no se ejecuta todavia la implementacion.

## Criterios de aceptacion

La revision se considera correcta cuando:

- `anejos.md` ya no fuerza un tratamiento de calculos como anejo separado si la plantilla no lo contempla;
- el bloque de **Calculos justificados** queda definido como capitulo propio dentro de la estructura documental;
- la tabla de dimensionado de tuberias queda especificada como hoja aislada A4 horizontal, con encabezado y pie de pagina coherentes con el resto del documento;
- el capitulo de calculos incluye un apartado de **Bibliografia** equivalente al de Memoria;
- el plan de orquestacion posterior puede actualizarse sin contradicciones.

## Supuestos

- No se modifica `Proyecto/Planificacion/plan_orquestacion_calculos_justificados.md` en esta fase.
- No se implementan cambios en el contenido del proyecto; solo se deja preparado el plan de revision.
- `Practica_GLPs_LaTeX/plantilla.tex` es la referencia estructural para decidir si algo va en capitulo o en anejo.
