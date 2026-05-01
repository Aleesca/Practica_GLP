# Cronograma de trabajo y reparto de responsabilidades

Proyecto: Calculo y diseno de una instalacion de GLP  
Grupo: G1-1  
Fecha limite de entrega: 24 de mayo de 2026  
Formato de entrega: LaTeX, usando `Practica_GLPs_LaTeX/plantilla.tex`

## 1. Criterio de reparto

El reparto se realiza por especialidades, no por capitulos aislados del documento. La razon es que en un proyecto de instalacion industrial los calculos, planos, memoria, presupuesto y anexos no son independientes: los planos proporcionan longitudes y distancias; los calculos fijan capacidades, diametros y necesidades de seguridad; el presupuesto depende de mediciones y equipos; y la memoria debe justificar de forma coherente todas las decisiones.

## 2. Roles principales

| Persona | Rol principal | Responsabilidades |
|---|---|---|
| Alberto | Coordinacion tecnica e integracion LaTeX | Redaccion tecnica, normativa, estructura documental, coherencia de criterios, integracion final en `plantilla.tex` |
| Ruben | Presupuesto y mediciones economicas | Presupuesto con Arquimedes, cuadros de precios, mediciones, apoyo a cantidades de materiales |
| Carlos | CAD - planta y trazado general | Archivo AutoCAD compartido, parcela, implantacion general, trazado de red, distancias generales |
| Juan | CAD - detalles y planos tecnicos | Archivo AutoCAD compartido, detalles, alzados, esquemas tecnicos y planos complementarios |

## 3. Cronograma propuesto

| Fase | Fechas objetivo | Responsable principal | Apoyo | Entregables | Depende de |
|---|---:|---|---|---|---|
| 1. Arranque y criterios comunes | 30 abril - 1 mayo | Alberto | Todos | Lista de datos de partida, alcance cerrado, estructura de carpetas, criterios de nomenclatura | Enunciado, `Datos.md`, `plantilla.tex` |
| 2. Base cartografica y archivo CAD comun | 1 - 3 mayo | Carlos | Juan | Archivo AutoCAD base con parcela, consumidores G1-1, capas y escala de trabajo | Referencia catastral y consumidores del grupo |
| 3. Toma de medidas preliminares | 3 - 5 mayo | Carlos | Juan | Longitudes aproximadas de conducciones, distancias a limites, edificios y elementos relevantes | CAD base correctamente escalado |
| 4. Normativa aplicable y estructura de memoria | 3 - 6 mayo | Alberto | - | Indice tecnico validado, normativa vigente identificada, apartados de memoria preparados | Enunciado y plantilla LaTeX |
| 5. Precalculos de demanda y autonomia | 5 - 7 mayo | Alberto | Ruben | Tabla de potencias, horas de funcionamiento, consumo diario y demanda de calculo | Datos de consumidores de `Datos.md` |
| 6. Primera implantacion de estacion y trazado | 6 - 9 mayo | Carlos | Juan, Alberto | Propuesta de ubicacion en planta y trazado preliminar de red | Medidas preliminares y criterios normativos basicos |
| 7. Calculos principales de instalacion | 8 - 12 mayo | Alberto | Ruben | Dimensionamiento justificado, criterios de calculo y resultados base para memoria | Precalculos, trazado preliminar y longitudes CAD |
| 8. Ajuste CAD tras calculos | 12 - 14 mayo | Juan | Carlos, Alberto | Planta revisada, detalles necesarios, distancias de seguridad y esquemas actualizados | Resultados de calculo y validacion de implantacion |
| 9. Mediciones para presupuesto | 14 - 16 mayo | Ruben | Carlos, Juan | Mediciones de conducciones, equipos principales y partidas auxiliares | Planos CAD revisados y listado de equipos |
| 10. Presupuesto en Arquimedes | 16 - 19 mayo | Ruben | Alberto | Presupuesto, cuadros de precios y resumen economico exportable | Mediciones cerradas y definicion de partidas |
| 11. Pliego, seguridad y salud | 16 - 20 mayo | Alberto | Ruben | Pliego de condiciones, pruebas, certificados, calidad, seguridad y mantenimiento | Normativa aplicable, solucion tecnica y presupuesto preliminar |
| 12. Integracion LaTeX v1 | 19 - 21 mayo | Alberto | Todos | Primera version completa en `plantilla.tex`, con tablas, planos y presupuesto incorporados | Textos, calculos, planos y presupuesto preliminares |
| 13. Revision cruzada | 21 - 22 mayo | Todos | Alberto coordina | Lista de errores, incoherencias, faltantes y ajustes finales | Version LaTeX v1 |
| 14. Cierre tecnico y formal | 22 - 23 mayo | Alberto | Todos | PDF final revisado, indices, referencias, numeracion y anexos | Correcciones de revision cruzada |
| 15. Margen de entrega | 23 - 24 mayo | Alberto | Todos | Version final lista para entregar | PDF final validado |

## 4. Dependencias tecnicas principales

| Elemento que se necesita | Lo produce | Lo usa | Motivo de dependencia |
|---|---|---|---|
| Datos de consumidores | Alberto | Alberto, Ruben | Son la base para caudales, consumos, autonomia y presupuesto |
| Plano CAD base escalado | Carlos y Juan | Alberto, Ruben | Sin escala fiable no hay longitudes, distancias ni mediciones defendibles |
| Longitudes de red | Carlos y Juan | Alberto, Ruben | Condicionan calculo de conducciones, perdidas de carga y mediciones |
| Ubicacion preliminar de estacion | Carlos | Alberto, Juan | Permite comprobar distancias, justificar seguridad y dibujar detalles |
| Criterios normativos | Alberto | Carlos, Juan, Ruben | Fijan restricciones de implantacion, seguridad, documentacion y partidas |
| Calculos principales | Alberto | Carlos, Juan, Ruben | Determinan elementos que deben aparecer en planos y presupuesto |
| Planos revisados | Carlos y Juan | Ruben, Alberto | Son necesarios para mediciones, anexos y coherencia de memoria |
| Mediciones | Ruben | Ruben, Alberto | Alimentan presupuesto y resumen economico de la memoria |
| Presupuesto | Ruben | Alberto | Debe incorporarse al documento final y al resumen de caracteristicas |
| Version LaTeX integrada | Alberto | Todos | Es la base de la revision cruzada y cierre final |

## 5. Matriz RACI simplificada

Leyenda: R = responsable de ejecutar, A = responsable final, C = consultado, I = informado.

| Tarea | Alberto | Ruben | Carlos | Juan |
|---|---|---|---|---|
| Coordinacion general | A/R | I | I | I |
| Integracion en LaTeX | A/R | C | C | C |
| Normativa y memoria tecnica | A/R | C | C | C |
| Calculos de demanda y autonomia | A/R | C | I | I |
| Calculos de conducciones y resultados tecnicos | A/R | C | C | C |
| Archivo AutoCAD compartido | C | I | A/R | R |
| Planta, trazado y distancias | C | I | A/R | R |
| Alzados, detalles y esquemas | C | I | R | A/R |
| Mediciones | C | A/R | C | C |
| Presupuesto en Arquimedes | C | A/R | I | I |
| Pliego de condiciones | A/R | C | I | I |
| Seguridad y salud | A/R | C | C | C |
| Revision final | A/R | R | R | R |

## 6. Entregables por persona

### Alberto

- Documento LaTeX integrado.
- Memoria tecnica redactada.
- Normativa aplicable y justificacion general.
- Calculos justificados principales.
- Pliego de condiciones.
- Estudio de seguridad y salud.
- Control de coherencia entre memoria, calculos, planos y presupuesto.

### Ruben

- Presupuesto en Arquimedes.
- Cuadro de precios numero 1.
- Cuadro de precios numero 2.
- Mediciones.
- Resumen de presupuesto para incorporar a memoria.
- Exportacion o tablas finales para LaTeX.

### Carlos

- Archivo AutoCAD compartido con base de parcela.
- Planta general de estacion y red.
- Trazado de conducciones.
- Medicion grafica de distancias principales.
- Plano de situacion y emplazamiento.

### Juan

- Planos de detalle.
- Alzados necesarios.
- Esquemas tecnicos complementarios.
- Zonas clasificadas, si procede en el desarrollo documental.
- Apoyo a la revision grafica del archivo AutoCAD compartido.

## 7. Reglas de coordinacion

1. El archivo AutoCAD compartido debe tener una unica version vigente. Carlos y Juan deben acordar capas, escala, unidades y convencion de nombres antes de empezar a dibujar en detalle.
2. Alberto no debe cerrar los calculos definitivos hasta recibir longitudes y distancias medidas desde CAD.
3. Ruben no debe cerrar presupuesto hasta recibir planos revisados y listado de elementos principales.
4. Ningun plano debe considerarse final hasta que Alberto confirme que no contradice la memoria ni la normativa aplicada.
5. La version LaTeX integrada debe cerrarse al menos un dia antes de la entrega para reservar margen a compilacion, indices, referencias, tablas y planos.
6. Toda modificacion tecnica que afecte a planos, calculos o presupuesto debe comunicarse al resto del grupo, porque puede obligar a actualizar varios entregables.

## 8. Hitos de control

| Hito | Fecha objetivo | Criterio de aceptacion |
|---|---:|---|
| H1 - Datos y CAD base listos | 3 mayo | Parcela y consumidores colocados en AutoCAD con escala fiable |
| H2 - Medidas preliminares cerradas | 5 mayo | Longitudes y distancias principales disponibles |
| H3 - Calculos base disponibles | 12 mayo | Resultados suficientes para alimentar planos, memoria y presupuesto |
| H4 - Planos revisados | 14 mayo | Planta, trazado y detalles listos para mediciones |
| H5 - Presupuesto preliminar | 19 mayo | Arquimedes exportado o resumido para LaTeX |
| H6 - Documento completo v1 | 21 mayo | `plantilla.tex` compila con todos los apartados principales |
| H7 - PDF final | 23 mayo | Documento revisado, coherente y listo para entregar |

