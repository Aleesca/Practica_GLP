# Plan de mejora de `distancias_seguridad.md`

## Estado del documento

- Tipo: plan de implementacion documental
- Estado: activo
- Alcance: mejora tecnica de `Proyecto/Anotaciones/distancias_seguridad.md`

## Objetivo

Definir el plan de trabajo para mejorar la redaccion tecnica, la estructura argumental y la trazabilidad normativa de `Proyecto/Anotaciones/distancias_seguridad.md`, manteniendo su foco en implantacion y distancias de seguridad de la estacion de GLP del Grupo G1-1.

## Fuentes de entrada

- Documento base: `Proyecto/Anotaciones/distancias_seguridad.md`
- Soporte de calculo: `calculos/calculos.ipynb`
- Seleccion de almacenamiento: `Proyecto/Anotaciones/seleccion_deposito.md`
- Criterio normativo general: `Proyecto/Anotaciones/criterios_normativos.md`
- Normativa base: `ZZ_Normativa/UNE_60250-2008_GLP_Depositos_Fijos.pdf`
- Normativa base: `ZZ_Normativa/RD_919-2006_Reglamento_Combustibles_Gaseosos.pdf`
- Encaje metodologico: `Proyecto/Especificaciones/metodologia.md`
- Trazabilidad de memoria: `Proyecto/Planificacion/matriz_fuentes.md`

## Decisiones fijadas

- El documento objetivo sigue siendo `Proyecto/Anotaciones/distancias_seguridad.md`.
- Los marcadores `integrar imagenes ...` e `integrar imagen ...` se conservan sin cambios en esta fase.
- `calculos/calculos.ipynb` se utilizara solo como respaldo cuantitativo para la justificacion de implantacion.
- La comprobacion de redundancias con otras anotaciones no se realiza en este plan; se reserva a otro agente en una fase posterior.
- La ampliacion tecnica del contenido requerira conexion con NotebookLM MCP/CLI.
- La fase de NotebookLM parte de la condicion de que el usuario ya se habra autenticado previamente.
- NotebookLM se utilizara como apoyo de contraste y ampliacion documental, no como sustituto de la normativa base del proyecto.

## Estructura objetivo del documento

Se propone reorganizar `Proyecto/Anotaciones/distancias_seguridad.md` con la siguiente secuencia tecnica:

1. Objeto y alcance del apartado.
2. Normativa y criterio de aplicacion.
3. Configuracion de almacenamiento adoptada.
4. Datos geometricos relevantes de los depositos.
5. Separacion minima entre depositos.
6. Distancias de seguridad respecto al entorno.
7. Verificacion de implantacion en parcela.
8. Incidencia del vaporizador sobre la implantacion.
9. Conclusion tecnica.
10. Referencias cruzadas.

## Fases de trabajo

### F1. Diagnostico tecnico-editorial

- Revisar la redaccion actual para detectar formulaciones poco tecnicas, repeticiones, saltos argumentales y afirmaciones sin soporte explicito.
- Delimitar con claridad que partes del texto pertenecen al ambito de implantacion y distancias de seguridad.
- Identificar que bloques deben pasar a redactarse como dato de partida, criterio normativo, comprobacion o conclusion.

### F2. Reestructuracion del contenido

- Reordenar el documento segun la estructura objetivo definida en este plan.
- Mejorar la continuidad entre seleccion de la configuracion, geometria relevante y verificacion reglamentaria.
- Mantener los marcadores `integrar imagen` como puntos de insercion futura dentro de la secuencia tecnica que mejor corresponda.

### F3. Integracion controlada del cuaderno de calculos

- Incorporar solo los resultados de `calculos/calculos.ipynb` que ayuden a justificar la implantacion.
- Priorizar la incorporacion de volumen geometrico minimo requerido, configuracion final de almacenamiento, capacidad total instalada y datos geometricos utiles para separacion y verificacion espacial.
- Incluir la informacion sobre vaporizacion solo cuando sea necesaria para justificar la solucion implantada o la presencia del vaporizador.
- Evitar trasladar desarrollos completos que ya pertenecen a autonomia, calculo de volumen o temperatura de diseno.

### F4. Mejora de redaccion tecnica

- Sustituir formulaciones narrativas o informales por lenguaje tecnico justificativo.
- Unificar unidades, nomenclatura y convenciones de redaccion.
- Separar de forma explicita los datos de partida, el criterio normativo, la comprobacion realizada y el resultado de implantacion.

### F5. Refuerzo del nucleo tecnico de seguridad

- Desarrollar con mayor precision el criterio de separacion minima entre depositos.
- Explicitar la referencia normativa aplicable al grupo de la instalacion y al tipo de distancia verificada.
- Mejorar la justificacion de las distancias respecto a muros, limites, focos de ignicion y otros elementos del entorno que correspondan.
- Preparar el contenido para una tabla de distancias verificadas como salida tecnica del apartado.

### F6. Conservacion de marcadores editoriales

- Mantener literalmente los textos `integrar imagenes ...` e `integrar imagen ...`.
- Considerar estos marcadores como referencias de trabajo para futuras fases de maquetacion, figuras y anexos.
- No convertir todavia esos marcadores en referencias editoriales cerradas ni en integracion LaTeX definitiva.

### F7. Revision posterior de redundancias por otro agente

- Encargar a otro agente una verificacion especifica de solapes con `Proyecto/Anotaciones/autonomia_30_dias.md`.
- Encargar a otro agente una verificacion especifica de solapes con `Proyecto/Anotaciones/calculo_volumen_deposito.md`.
- Encargar a otro agente una verificacion especifica de solapes con `Proyecto/Anotaciones/seleccion_deposito.md`.
- Encargar a otro agente una verificacion especifica de solapes con `Proyecto/Anotaciones/temperatura_diseno.md`.
- Solicitar a ese agente que determine que contenido debe permanecer en `distancias_seguridad.md`, que contenido debe resumirse mediante referencia cruzada y que contenido pertenece de forma exclusiva al apartado de implantacion y seguridad.

### F8. Conexion necesaria con NotebookLM para ampliacion tecnica

- Conectar con NotebookLM MCP/CLI una vez que el usuario ya se haya autenticado previamente.
- Incorporar a NotebookLM la documentacion tecnica y normativa que resulte util para contrastar y ampliar la nota de distancias de seguridad.
- Consultar criterios complementarios sobre implantacion, distancias, seguridad, entorno de instalacion y referencias tecnicas de apoyo.
- Extraer referencias adicionales que permitan reforzar la trazabilidad tecnica de `Proyecto/Anotaciones/distancias_seguridad.md`.
- Incorporar al documento las referencias o apoyos tecnicos utiles que mejoren la solidez de la justificacion final.

## Salidas esperadas

- Un documento `Proyecto/Anotaciones/distancias_seguridad.md` con estructura tecnica mas clara y lenguaje profesional.
- Un apartado centrado en implantacion y distancias de seguridad, con apoyo cuantitativo suficiente y sin invadir otros modulos del proyecto.
- Conservacion integra de los marcadores `integrar imagen` para su tratamiento en fases posteriores.
- Preparacion de una tabla de distancias verificadas y de una conclusion tecnica defendible.
- Refuerzo posterior de referencias mediante conexion planificada con NotebookLM.

## Criterios de aceptacion

- El plan deja fijado que la mejora del documento no elimina los marcadores editoriales existentes.
- El plan deja fijado que la verificacion de redundancias corresponde a otro agente y a una fase posterior.
- El plan deja fijado que sera necesario conectarse a NotebookLM MCP/CLI para asegurar y ampliar la informacion tecnica.
- El plan deja fijado que esa conexion se realizara sobre la base de que el usuario ya se habra logeado previamente.
- El plan mantiene como eje del documento la implantacion y las distancias de seguridad de la instalacion de GLP.
