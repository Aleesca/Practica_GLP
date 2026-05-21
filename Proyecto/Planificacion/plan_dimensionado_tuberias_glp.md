# Plan: Dimensionado de Tuberias GLP por Tramos

> Fuente: solicitud del usuario para preparar el dimensionado de la red a partir de `calculos/datos/longitudes_Tramos.csv`, `esquema_instalacion.pdf`, `Proyecto/Especificaciones/metodologia-longitud-calculo.md` y `formulario.md`.

## Resumen

Preparar en `calculos/calculos.ipynb` el flujo de calculo completo para dimensionar la red de tuberias GLP por tramos, usando la topologia del esquema, las longitudes ya normalizadas en CSV, la metodologia de longitud de calculo y la verificacion de velocidad para depositos aereos.

El resultado final del trabajo debera incluir un fichero Markdown de trazabilidad matematica con las formulas empleadas, los materiales seleccionados, las comprobaciones de velocidad y la justificacion tecnica de cada tramo.

## Decisiones de base

- **Metodo de calculo de longitud**: usar el metodo iterativo por accesorios `Lc(D) = Lreal + sum(ni * coef_i * D/1000)`.
- **Regimen de dimensionado**: tratar la red principal como media presion salvo indicacion explicita contraria en la documentacion del proyecto.
- **Gas de referencia**: propano, con `dc = 1.16`, salvo que la documentacion tecnica del proyecto indique otra cosa.
- **Velocidad maxima**: verificar todos los tramos frente al limite aplicable a instalaciones con depositos aereos; usar `v <= 20 m/s` como criterio base si no se documenta un limite mas restrictivo.
- **NotebookLM**: la consulta a los manuales GLP queda como tarea de implementacion para seleccionar el material mas adecuado, pero en este plan no se realiza conexion ni extraccion de contenido.
- **Material por defecto si falta evidencia documental**: usar una opcion metalica apta para GLP en instalacion aerea exterior, con criterio conservador y justificacion normativa.

---

## Fase 1: Consolidar datos de entrada

**Que se construye**

- Cargar `calculos/datos/longitudes_Tramos.csv` en la libreta.
- Normalizar numero de tramo, descripcion, designacion y longitud real.
- Construir la topologia de la red a partir de las designaciones del CSV:
  `D1-D4`, `D4-A`, `A-C1`, `A-B`, `B-C2`, `B-C`, `C-C3`, `C-D`, `D-C4`, `D-E`, `E-C5`, `E-C6`.
- Vincular cada consumidor final con los datos de `Proyecto/Datos.md`.

**Criterios de aceptacion**

- Los 12 tramos quedan cargados y visibles en una tabla limpia.
- Cada tramo tiene nodo inicial, nodo final y longitud real.
- Cada consumidor final tiene potencia asociada.
- Las filas vacias o anomalias del CSV quedan detectadas y reportadas.

---

## Fase 2: Calcular caudales por consumidor y por tramo

**Que se construye**

- Convertir potencia de cada consumidor a caudal de calculo en las unidades usadas por Renouard.
- Calcular el caudal de cada consumidor y el caudal aguas arriba de cada tramo segun la topologia.
- Documentar si se aplica simultaneidad y dejar trazabilidad de la formula usada.
- Conservar tambien el caudal bruto por consumidor para auditoria.

**Criterios de aceptacion**

- Cada tramo muestra el caudal que transporta.
- Los tramos principales acumulan correctamente los consumos aguas abajo.
- El calculo queda explicado sin ambiguedad de unidades.

---

## Fase 3: Extraer accesorios del esquema

**Que se construye**

- Revisar `esquema_instalacion.pdf` para identificar accesorios por tramo.
- Registrar codos, tes, valvulas, reducciones y equivalentes que afecten a la longitud de calculo.
- Crear una tabla auxiliar de accesorios por tramo para poder recalcular `Lc` en funcion del diametro.
- Marcar como hipotesis cualquier accesorio que no pueda confirmarse visualmente.

**Criterios de aceptacion**

- Cada tramo tiene un inventario de accesorios o una nota de hipotesis.
- El metodo de equivalencias queda vinculado a la tabla de `Proyecto/Especificaciones/metodologia-longitud-calculo.md`.
- La longitud de calculo puede recalcularse para cada diametro candidato.

---

## Fase 4: Seleccionar material y catalogo de diametros

**Que se construye**

- Revisar los manuales GLP del notebook para identificar materiales admisibles en la instalacion.
- Elegir el material que mejor se ajuste a la instalacion aerea y a la metodologia de calculo.
- Definir el catalogo de diametros comerciales con diametro interior real.
- Dejar documentada la decision tecnica y las alternativas descartadas.

**Criterios de aceptacion**

- El material seleccionado queda justificado en texto tecnico.
- El catalogo de diametros es explicito y reutilizable por el calculo.
- Si la documentacion consultada no permite cerrar la seleccion, la incertidumbre queda declarada.

---

## Fase 5: Dimensionar tramo a tramo

**Que se construye**

- Iterar el catalogo de diametros desde el menor al mayor para cada tramo.
- Para cada candidato calcular `Lc(D)`, verificar `Q/D < 150`, aplicar Renouard y obtener la perdida de carga.
- Calcular la presion final del tramo y la velocidad del gas.
- Aceptar el primer diametro que cumpla perdida admisible, presion minima y velocidad.
- Propagar la presion y el caudal aguas arriba hasta cerrar toda la red.

**Criterios de aceptacion**

- Cada tramo termina con un diametro definitivo o con una marca de no conformidad.
- Cada tramo incluye `Lc`, perdida de carga, presion inicial, presion final, `Q/D` y velocidad.
- El criterio de velocidad queda comprobado de forma individual en todos los tramos.

---

## Fase 6: Generar la memoria tecnica en Markdown

**Que se construye**

- Generar un archivo Markdown final, por ejemplo `calculos/dimensionado_tuberias_glp.md`.
- Incluir fuentes, formulas, desarrollo matematico, tabla final de resultados y comprobaciones de velocidad.
- Incorporar el material seleccionado, el catalogo usado y las hipotesis adoptadas.
- Dejar el documento listo para servir como base de la memoria o anexo tecnico.

**Criterios de aceptacion**

- El Markdown permite auditar los calculos sin abrir la libreta.
- Todas las formulas de `formulario.md` empleadas aparecen explicitamente.
- Cada tramo muestra el resultado final y su verificacion de velocidad.
- El documento recoge las limitaciones del esquema y las decisiones adoptadas.

## Pruebas y verificacion

- Ejecutar la libreta desde cero y comprobar que no quedan tramos sin longitud, caudal o diametro.
- Revisar un tramo de control a mano para validar `Lc`, Renouard y velocidad.
- Confirmar que el Markdown generado coincide con las tablas de la libreta.
- Verificar que todos los tramos cumplen el limite de velocidad o quedan claramente marcados como no conformes.

## Supuestos

- Los seis consumidores de `Proyecto/Datos.md` corresponden, en orden, a los seis puntos finales C1-C6 de la red.
- La red se calcula inicialmente en propano.
- La instalacion se considera aerea en los tramos que afectan a la verificacion de velocidad.
- `esquema_instalacion.pdf` es la fuente de referencia para contar accesorios, pero toda interpretacion dudosa se debe documentar como hipotesis.
- La consulta a los manuales GLP del notebook queda como tarea de implementacion y no forma parte de este plan.
