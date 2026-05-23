# Plan de revision del apartado 7: Dimensionado de tuberia GLP

## Objetivo

Revisar y compactar el apartado 7 de `calculos/calculos.ipynb` para que conserve el calculo tecnico del dimensionado de tuberia GLP, pero con una presentacion mas limpia y menos redundante.

La revision se centra en tres frentes:

- reducir descripciones textuales innecesariamente largas;
- simplificar o fusionar `DataFrames` que repiten informacion;
- eliminar columnas de instancia, auxiliares o redundantes que no aportan valor en la salida final.

## Alcance

Queda dentro de este plan:

- el apartado 7 del notebook;
- los textos explicativos asociados a ese apartado;
- las tablas y `DataFrames` generados para mostrar el dimensionado;
- las columnas visibles en la salida final del apartado.

Queda fuera de este plan:

- cualquier cambio de formula, criterio tecnico o hipotesis de calculo;
- la reestructuracion de otros apartados del notebook;
- la validacion normativa de fondo salvo que aparezca una incoherencia evidente al revisar la presentacion.

## Criterios de revision

### 1. Texto

Las descripciones del apartado deben quedar en un nivel de detalle suficiente para guiar la lectura, pero sin párrafos largos que repitan lo que ya se ve en el propio calculo.

Reglas de compactacion:

- sustituir bloques narrativos por frases breves o encabezados cortos;
- conservar solo las notas que aporten contexto tecnico real;
- eliminar explicaciones que no cambien la interpretacion del resultado;
- evitar redundancias entre texto, comentarios y tablas.

### 2. DataFrames

Los `DataFrames` del apartado deben representar una vista clara y no una sucesion de tablas con la misma informacion repetida.

Reglas de consolidacion:

- identificar tablas de entrada, intermedias y finales;
- fusionar tablas que muestren los mismos datos con distinto formato;
- conservar solo los `DataFrames` que ayuden a verificar el dimensionado;
- dejar una salida final principal que resuma el resultado tecnico.

### 3. Columnas

Las tablas visibles deben contener solo columnas utiles para interpretar el dimensionado.

Reglas de simplificacion:

- eliminar columnas de instancia que existan solo por construccion interna;
- ocultar columnas auxiliares que no se usen en la lectura tecnica;
- mantener columnas de apoyo solo si son necesarias para el calculo posterior;
- priorizar nombres de columna comprensibles y directos.

## Fases de revision

### Fase 1. Inventario del apartado

Identificar las celdas, textos, `DataFrames` y columnas que forman parte del apartado 7.

Salida esperada:

- lista de elementos a conservar;
- lista de elementos a compactar;
- lista de elementos a eliminar o fusionar.

### Fase 2. Compactacion textual

Reducir las descripciones largas del apartado a una version mas breve y util.

Salida esperada:

- narracion tecnica mas corta;
- menos repeticion entre celdas;
- mejor separacion entre explicacion y resultado.

### Fase 3. Limpieza de tablas

Revisar los `DataFrames` para reducir duplicidad y dejar una estructura de salida mas limpia.

Salida esperada:

- tablas fusionadas cuando aporten lo mismo;
- tablas intermedias solo si son realmente utiles;
- una tabla final de dimensionado clara.

### Fase 4. Depuracion de columnas

Revisar las columnas visibles para eliminar las que no aportan interpretacion tecnica.

Salida esperada:

- menos columnas auxiliares;
- menos ruido visual;
- misma capacidad de verificacion tecnica.

### Fase 5. Validacion de consistencia

Comprobar que la revision no altera el resultado tecnico ni introduce inconsistencias en el apartado.

Salida esperada:

- el apartado sigue ejecutando correctamente;
- los resultados principales se mantienen;
- la version final es mas concisa y mantenible.

## Criterios de aceptacion

La revision se considera correcta cuando:

- el apartado 7 mantiene su objetivo tecnico sin cambiar formulas ni criterios;
- las descripciones largas quedan reducidas a lo necesario;
- los `DataFrames` redundantes se han fusionado o eliminado;
- las columnas sin valor tecnico visible ya no aparecen en la salida final;
- la lectura del apartado es mas rapida y clara sin perder trazabilidad.

## Resultado esperado

Al terminar este plan, el apartado 7 de `calculos/calculos.ipynb` debe quedar preparado para una lectura tecnica mas limpia, con menos ruido textual y menos tablas o columnas sobrantes, manteniendo intacto el contenido de calculo.
