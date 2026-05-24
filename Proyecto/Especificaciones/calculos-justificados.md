# Especificación: Capítulo de Cálculos justificados

## Propósito

Definir el encaje editorial y técnico del capítulo **Cálculos justificados** dentro del cuerpo principal del documento LaTeX del proyecto. Este capítulo no es un anejo independiente: reúne el desarrollo numérico, las hipótesis, la trazabilidad de magnitudes, las tablas de resultados y las comprobaciones que justifican las soluciones resumidas en la Memoria.

## Estructura obligatoria

El capítulo debe mantener la estructura prevista por `Practica_GLPs_LaTeX/plantilla.tex` y completar, como mínimo, los siguientes bloques:

- **Índice de anexos:** debe delimitar anexos reales y dejar claro que los cálculos desarrollados quedan integrados en este capítulo.
- **Consumo y autonomía:** demanda, caudal másico y volumétrico, consumo diario, autonomía de 30 días y volumen útil requerido.
- **Vaporización:** vaporización natural disponible, déficit a temperatura de cálculo y justificación de la vaporización forzada.
- **Válvulas de seguridad:** caudal mínimo de descarga, superficies expuestas y comprobación de capacidad de los equipos seleccionados.
- **Punto máximo de llenado:** cota de llenado del 85 %, longitud del tubo sonda y justificación geométrica.
- **Protección catódica:** justificación de exclusión para instalación aérea y medidas pasivas de protección anticorrosiva.
- **Protección contra incendios:** dotación de refrigeración, caudal de agua, número de boquillas, diámetro de colector y presión requerida.
- **Bibliografía:** cierre del capítulo con las fuentes normativas, catálogos, guías técnicas y datos de cálculo usados en las comprobaciones.

## Reglas de integración editorial

- El contenido técnico debe redactarse como capítulo del cuerpo principal, no como anejo de cálculos.
- Las referencias a la Memoria deben limitarse a contexto, trazabilidad de magnitudes o coherencia con resultados resumidos.
- Las tablas de resultados intermedios deben permanecer dentro del bloque de cálculo al que pertenecen.
- Las fichas comerciales, planos y documentación gráfica auxiliar pueden figurar como anexos reales cuando no formen parte del razonamiento numérico.
- La bibliografía del capítulo debe seguir el mismo criterio funcional que la bibliografía de Memoria: sección propia, entrada en índice y uso de las claves bibliográficas centralizadas en `Practica_GLPs_LaTeX/refs.bib` y `Proyecto/Planificacion/mapa_citas.md`.

## Tabla de dimensionado de tuberías

La tabla de resultados del dimensionado hidráulico de tuberías debe emitirse como una pieza documental única dentro del capítulo **Cálculos justificados**.

Reglas obligatorias:

- se insertará en una hoja aislada **A4 horizontal**;
- conservará el encabezado y pie de página del resto del documento;
- mantendrá la numeración, estilo de tabla y referencias cruzadas compatibles con la plantilla;
- no se convertirá en anejo independiente ni se desplazará al capítulo de Planos;
- deberá incluir, como mínimo, identificación de tramo, longitud real, longitud de cálculo, caudal, diámetro adoptado, pérdida de carga, presión final, velocidad y verificación de límites.

## Criterios de aceptación

- [ ] El capítulo queda definido como parte del cuerpo principal del documento.
- [ ] No se prescribe ningún anejo independiente de cálculos.
- [ ] Cada bloque de cálculo contiene hipótesis, procedimiento, sustitución de valores, resultado y comprobación.
- [ ] La tabla de dimensionado de tuberías queda especificada como hoja A4 horizontal aislada con encabezado y pie de página del documento.
- [ ] El capítulo termina con una bibliografía propia, alineada con el criterio usado en Memoria.

## Referencias relacionadas
- [Cálculos justificados: Índice de anexos e inserción de planos](anejos.md)
- [Cálculos justificados: Cálculos de seguridad y auxiliares](calculos-auxiliares.md)
- [Especificación: Metodología de longitud y cálculo hidráulico](metodologia-longitud-calculo.md)
- [Memoria: Autonomía de almacenamiento](autonomia.md)
- [Memoria: Vaporización natural vs. vaporización forzada](vaporizacion.md)
- [Dimensionado de tuberías GLP](../Anotaciones/dimensionado_tuberias_glp.md)
- [Cálculo del volumen del depósito](../Anotaciones/calculo_volumen_deposito.md)
- [Vaporización forzada](../Anotaciones/vaporizacion_forzada.md)
