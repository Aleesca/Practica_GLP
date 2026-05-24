# Plan de revision de plantilla LaTeX y limpieza editorial

## Resumen

Este plan define los ajustes editoriales necesarios en `Practica_GLPs_LaTeX/plantilla.tex` para cerrar las ausencias detectadas en la memoria:

- integracion coherente de figuras disponibles segun la redaccion de cada apartado;
- eliminacion o reencuadre del apartado de indice de anexos, que actualmente referencia anexos inexistentes;
- correccion del criterio bibliografico para incluir solo referencias citadas;
- ajuste de formato de tablas para mejorar uniformidad y legibilidad;
- limpieza del estilo de bullets para eliminar negritas innecesarias y reservar el subrayado para elementos realmente destacados;
- sustitucion de las menciones a `Grupo G1-1` por una denominacion profesional generica, preferentemente `planta industrial`.

## Cambios clave

- Revisar los apartados del documento y decidir en cuales conviene incorporar las figuras disponibles en `Figuras/`, siempre con correspondencia directa con el contenido tecnico.
- Suprimir el apartado de `Indice de anexos` si no se van a definir anexos reales, o reescribirlo para que no cite anexos inexistentes.
- Eliminar el uso de `\nocite{*}` para que la bibliografia final contenga solo obras citadas en el documento.
- Homogeneizar el formato de tablas, especialmente las de mayor anchura, para evitar desbordes y mejorar la lectura.
- Sustituir el patron de `\textbf{...}` en bullets por una version mas sobria, usando `\underline{...}` solo en los puntos que deban resaltarse de forma expresa.
- Reemplazar todas las menciones a `Grupo G1-1` por `planta industrial` o una formula equivalente de caracter profesional.

## Fases

### Fase 1. Figuras y coherencia de apartados

Identificar en que secciones de la plantilla las figuras disponibles aportan valor real y añadirlas solo donde refuercen la redaccion.

Salida esperada:

- cada figura incorporada queda vinculada a un apartado concreto;
- el texto remite a la figura con referencias consistentes;
- no se introducen imagenes sin justificacion tecnica.

### Fase 2. Reordenacion del apartado de anexos

Eliminar el apartado de indice de anexos si no existe un bloque de anexos al final del documento, o reescribirlo para que no enumere contenido inexistente.

Salida esperada:

- desaparecen las referencias a anexos no presentes;
- el capitulo de calculos queda coherente con la estructura real del documento;
- no se rompe la numeracion ni la navegacion del indice general.

### Fase 3. Bibliografia citada

Retirar `\nocite{*}` y dejar que la bibliografia se alimente solo de las citas efectivamente usadas en el texto.

Salida esperada:

- la lista bibliografica final refleja solo referencias citadas;
- no aparecen entradas huérfanas por inclusion global;
- el criterio bibliografico queda alineado con el uso academico esperado.

### Fase 4. Formato de tablas y estilo de bullets

Aplicar una limpieza visual en tablas y listas para que el documento mantenga un estilo uniforme.

Salida esperada:

- las tablas presentan un formato consistente;
- los bullets usan subrayado solo en elementos relevantes;
- se eliminan negritas innecesarias en los puntos de lista.

### Fase 5. Normalizacion terminologica

Sustituir todas las referencias a `Grupo G1-1` por `planta industrial`, manteniendo el mismo tono profesional ya usado en la memoria.

Salida esperada:

- no quedan menciones a `Grupo G1-1` en el documento;
- la terminologia queda unificada con el resto del proyecto;
- no se introducen denominaciones informales ni dependientes del grupo de trabajo.

## Criterios de aceptacion

La revision se considera correcta cuando:

- las figuras estan integradas solo donde corresponden y con referencias validas;
- el apartado de anexos deja de citar material inexistente;
- la bibliografia incluye unicamente fuentes citadas;
- las tablas muestran un formato coherente y legible;
- los bullets han perdido la negrita sistematica y reservan el subrayado para lo esencial;
- no aparece `Grupo G1-1` en el texto final.

## Supuestos

- No se implementan cambios en esta fase; el documento solo queda planificado.
- Se prioriza la coherencia editorial sobre la incorporacion de figuras no justificadas.
- `planta industrial` es la denominacion generica preferente para sustituir `Grupo G1-1`.
