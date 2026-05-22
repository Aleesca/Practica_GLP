# Plan: Recopilación y Coste de Accesorios por Tramo GLP

## Resumen

Generar un archivo Markdown en `Proyecto/Anotaciones/` que recopile, por cada tramo de la instalación GLP ya dimensionada, los accesorios necesarios, sus diámetros, materiales y costes estimados.

El proceso debe conectarse a NotebookLM para consultar el notebook/proyecto GLP y contrastar la normativa UNE aplicable. También debe usar las fuentes internas del repositorio y una consulta externa vía MCP Exa para localizar proveedores europeos de cobre y accesorios aptos para instalaciones GLP.

Fuentes de trabajo:

- `calculos/calculos.ipynb`: cálculos de dimensionado ya realizados.
- `Proyecto/Anotaciones/dimensionado_tuberias_glp.md`: explicación técnica del dimensionado.
- `Proyecto/Anotaciones/reporte_accesorios.md`: referencia inicial de accesorios y precios.
- NotebookLM del proyecto GLP: consulta normativa y validación técnica.
- MCP Exa: búsqueda externa de proveedores europeos y precios.

## Decisiones de Implementación

- **Archivo final**: crear `Proyecto/Anotaciones/recopilacion_accesorios_costes_glp.md`.
- **Unidad de análisis**: cada tramo de tubería tendrá su propio registro con diámetro, longitud, material, accesorios y coste.
- **Material base**: cobre apto para instalaciones GLP.
- **Fuentes externas**: proveedores europeos, priorizando España o la UE.
- **Validación normativa**: consultar NotebookLM para identificar normativa UNE/EN aplicable y contrastarla con las fichas comerciales encontradas.
- **Trazabilidad**: cada precio debe incluir proveedor, URL, país, fecha de consulta y observación normativa.
- **Sin redimensionado**: se usan los diámetros y longitudes ya calculados; no se recalcula la instalación.

## Fases de Implementación

### Fase 1: Preparar la Estructura del Informe

Crear la plantilla del Markdown final con estas secciones:

- Introducción y alcance.
- Fuentes internas consultadas.
- Consulta a NotebookLM y criterios normativos UNE/EN.
- Tabla resumen por tramo.
- Tabla de accesorios por tramo.
- Tabla de precios unitarios por diámetro/material.
- Coste estimado por tramo.
- Fuentes externas.
- Limitaciones y datos pendientes.

Criterios de aceptación:

- El informe tiene una estructura clara antes de incorporar datos.
- Las tablas contemplan tramo, diámetro, longitud, accesorio, cantidad, precio unitario, subtotal y fuente.
- Existe una sección específica para normativa consultada en NotebookLM.

### Fase 2: Consultar NotebookLM y Fuentes Internas

Conectar con NotebookLM para consultar el notebook/proyecto GLP y extraer criterios normativos relevantes para accesorios, tuberías de cobre, diámetros y compatibilidad con GLP.

Consultar también:

- `calculos/calculos.ipynb`
- `Proyecto/Anotaciones/dimensionado_tuberias_glp.md`
- `Proyecto/Anotaciones/reporte_accesorios.md`

Criterios de aceptación:

- Se identifican los tramos dimensionados, sus longitudes y diámetros.
- Se recoge la normativa UNE/EN aplicable desde NotebookLM.
- Todo dato técnico queda asociado a su fuente.
- Los datos ausentes se marcan como “pendiente de confirmar”.

### Fase 3: Asociar Accesorios por Tramo

Para cada tramo, listar los accesorios necesarios:

- Codos.
- Tes o derivaciones.
- Manguitos/uniones.
- Reducciones.
- Llaves o válvulas asociadas al tramo.
- Racores, adaptadores u otros accesorios de cobre compatibles con GLP.
- Elementos especiales citados en `reporte_accesorios.md`.

Criterios de aceptación:

- Cada accesorio queda vinculado a un tramo concreto.
- Cada accesorio incluye diámetro nominal compatible.
- Las cantidades se justifican por trazado, derivaciones o documentación existente.
- Los elementos generales no atribuibles a un tramo se separan en una sección propia.

### Fase 4: Buscar Precios con MCP Exa

Usar MCP Exa para localizar proveedores europeos especializados en cobre y accesorios para instalaciones de gas/GLP.

Para cada diámetro y accesorio relevante, registrar:

- Producto.
- Diámetro.
- Material.
- Compatibilidad con gas/GLP.
- Proveedor.
- País.
- Precio unitario.
- Moneda e IVA si se indica.
- URL.
- Fecha de consulta.
- Referencia normativa declarada por el proveedor.

Criterios de aceptación:

- Cada diámetro usado tiene al menos una referencia de precio.
- Cada precio externo tiene fuente trazable.
- Las fuentes son europeas.
- No se usan productos sin indicación razonable de compatibilidad con gas/GLP.
- Si falta precio fiable, se marca como “sin precio verificado”.

### Fase 5: Calcular Coste por Tramo

Construir las tablas económicas:

- Coste de tubería: longitud x precio por metro según diámetro.
- Coste de accesorios: cantidad x precio unitario.
- Subtotal por tramo.
- Total general.
- Columna separada para importes pendientes o estimados sin verificación completa.

Criterios de aceptación:

- Cada tramo tiene subtotal independiente.
- El total general se puede recalcular desde las tablas.
- Las unidades son consistentes: metros, unidades, euros y diámetro nominal.
- Los precios pendientes quedan claramente diferenciados de los verificados.

### Fase 6: Revisión Técnica y Normativa

Revisar el documento final:

- Confirmar que los diámetros coinciden con el dimensionado.
- Verificar que accesorios y tubería son de cobre apto para GLP.
- Comprobar que las fuentes externas son europeas.
- Contrastar compatibilidad normativa con lo consultado en NotebookLM.
- Añadir advertencias donde el proveedor no declare explícitamente cumplimiento UNE/EN.

Criterios de aceptación:

- No quedan tramos sin revisar.
- Todas las fuentes están citadas.
- Las limitaciones están explícitas.
- El archivo final queda guardado en `Proyecto/Anotaciones/`.

## Contenido Esperado del Markdown Final

El documento incluirá estas tablas:

1. **Tabla de tramos**
   - Tramo
   - Descripción
   - Longitud
   - Diámetro
   - Material
   - Fuente interna

2. **Tabla de accesorios**
   - Tramo
   - Accesorio
   - Diámetro
   - Cantidad
   - Justificación
   - Fuente

3. **Tabla normativa**
   - Norma UNE/EN
   - Aplicación
   - Requisito relevante
   - Fuente NotebookLM
   - Observaciones

4. **Tabla de precios**
   - Producto
   - Diámetro
   - Material
   - Proveedor
   - País
   - Precio unitario
   - URL
   - Fecha de consulta
   - Observación normativa

5. **Tabla de coste por tramo**
   - Tramo
   - Coste tubería
   - Coste accesorios
   - Subtotal
   - Datos pendientes

## Supuestos

- El dimensionado está cerrado y no se modifica.
- El cobre es el material principal de la instalación.
- NotebookLM contiene o referencia la normativa GLP/UNE relevante del proyecto.
- La consulta externa se realizará con MCP Exa.
- El resultado será un documento técnico-económico de recopilación de accesorios y costes, no una memoria de redimensionado.
