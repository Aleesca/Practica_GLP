# Plan de revision de calculos justificados y bibliografia

## Resumen

Este plan define dos ajustes editoriales sobre `Practica_GLPs_LaTeX/plantilla.tex`:

- reducir las redundancias en las referencias a `deposito principal` y `depositos de apoyo` dentro de los apartados de calculos justificados;
- reorganizar la bibliografia para que deje de estar dispersa en los calculos y pase a un capitulo propio con todas las referencias citadas.

El objetivo es mejorar la legibilidad y la estructura documental sin cambiar formulas, resultados ni contenido tecnico.

## Cambios clave

- Introducir una convencion breve de identificacion, por ejemplo `DP` para el deposito principal y `DA` para los depositos de apoyo.
- Reescribir los apartados repetitivos para que el tipo de deposito quede claro por el encabezado, la etiqueta del bloque o la primera menciona, sin repetir innecesariamente la misma expresion.
- Mantener la trazabilidad tecnica de cada calculo, pero con una redaccion mas compacta y menos redundante.
- Crear un capitulo especifico de bibliografia donde confluyan todas las referencias citadas en el documento.
- Retirar las citas bibliograficas incrustadas en los calculos justificados y dejar que la bibliografia quede centralizada al final o en el capitulo propio que se determine.

## Fases

### Fase 1. Localizacion de redundancias y citas

Identificar los pasajes donde se repiten de forma excesiva las menciones al deposito principal y a los depositos de apoyo, asi como las referencias bibliograficas insertadas dentro de los calculos.

Salida esperada:

- quedan localizados los bloques con redundancia terminologica;
- quedan localizadas las citas dispersas dentro de los calculos;
- no se modifica todavia el contenido tecnico.

### Fase 2. Convencion terminologica

Definir una forma estable de nombrar el deposito principal y los depositos de apoyo para poder usarla en los calculos sin perdida de claridad.

Salida esperada:

- la convencion aparece antes de que se use;
- cada bloque queda asociado de forma inequvoca a `DP` o `DA`;
- la redaccion deja de depender de repetir continuamente el nombre completo.

### Fase 3. Reescritura de calculos justificados

Reformular los apartados mas repetitivos para compactar la redaccion y conservar la identificacion tecnica de cada calculo.

Salida esperada:

- se reducen las repeticiones innecesarias;
- no se alteran formulas, resultados ni unidades;
- sigue siendo evidente si un calculo corresponde al deposito principal o a los depositos de apoyo.

### Fase 4. Capitulo propio de bibliografia

Reorganizar el tratamiento de las referencias para que la bibliografia quede concentrada en un capitulo propio, en lugar de aparecer integrada en los calculos justificados.

Salida esperada:

- la bibliografia deja de estar repartida por el cuerpo de calculos;
- todas las referencias citadas quedan reunidas en el capitulo especifico;
- las citas del texto siguen siendo coherentes y rastreables.

### Fase 5. Revision final de coherencia

Comprobar que la nueva redaccion y la nueva estructura bibliografica no introducen ambiguedades ni rompen la continuidad del documento.

Salida esperada:

- cada bloque de calculo sigue siendo identificable;
- la bibliografia queda centralizada y completa;
- el documento mantiene coherencia formal y tecnica.

## Criterios de aceptacion

La revision se considera correcta cuando:

- las menciones a `deposito principal` y `depositos de apoyo` ya no se repiten de forma innecesaria;
- cada calculo sigue pudiendo atribuirse sin dudas al deposito principal o a los depositos de apoyo;
- la bibliografia pasa a estar organizada en un capitulo propio;
- no se pierden referencias citadas durante la reorganizacion;
- no cambia el contenido tecnico de los calculos.

## Supuestos

- No se implementan cambios en esta fase; el documento solo queda planificado.
- El ajuste es editorial y estructural, no tecnico.
- La bibliografia se centralizara sin alterar el sentido de las citas.
- La implementacion posterior se hara sobre `Practica_GLPs_LaTeX/plantilla.tex` cuando se pase a ejecucion.
