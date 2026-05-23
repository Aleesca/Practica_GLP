# Mapeo de Markdown a LaTeX

Este documento fija el encaje entre la salida primaria en `Proyecto/Especificaciones/` y la estructura editorial ya existente en `Practica_GLPs_LaTeX/plantilla.tex`.

## Regla general

- `Proyecto/Especificaciones/` sigue siendo la fuente tecnica primaria.
- `Practica_GLPs_LaTeX/plantilla.tex` no se modifica como parte de este mapeo.
- La consolidacion editorial debe rellenar subsecciones ya existentes de la plantilla.
- Si un modulo de Markdown alimenta varias subsecciones, el reparto debe hacerse sin duplicar teoria ni resultados.

## Mapeo principal

| Archivo Markdown | Bloque LaTeX destino | Seccion o subseccion de `plantilla.tex` | Criterio de uso |
| --- | --- | --- | --- |
| `Proyecto/Especificaciones/intro.md` | `Memoria` | `OBJETO.` y `ANTECEDENTES.` | Separar objetivo del proyecto y contexto de partida. |
| `Proyecto/Especificaciones/datos-partida.md` | `Memoria` | `IDENTIFICACIÓN.`, `EMPLAZAMIENTO DE LAS INSTALACIONES.`, `CARACTERÍSTICAS DEL GAS SUMINISTRADO.` | Llevar aqui los datos base, emplazamiento y condiciones del suministro. |
| `Proyecto/Especificaciones/demanda-consumo.md` | `Memoria` + `Calculos justificados` | `RESUMEN DE CARACTERÍSTICAS.` y `CONSUMO Y AUTONOMÍA.` | El resumen ejecutivo va a Memoria; el desarrollo numérico va a Cálculos justificados. |
| `Proyecto/Especificaciones/autonomia.md` | `Memoria` + `Calculos justificados` | `RESUMEN DE CARACTERÍSTICAS.` y `CONSUMO Y AUTONOMÍA.` | La capacidad final alimenta el resumen; el desarrollo va al anexo de cálculos. |
| `Proyecto/Especificaciones/vaporizacion.md` | `Memoria` + `Calculos justificados` | `CARACTERÍSTICAS DE LOS EQUIPOS. -> Equipo de vaporización.` y `VAPORIZACIÓN.` | En Memoria se justifica la solución adoptada; en Cálculos se incorpora la comprobación detallada. |
| `Proyecto/Especificaciones/deposito.md` | `Memoria` | `RESUMEN DE CARACTERÍSTICAS. -> Tipo de instalación`, `Volumen en m3 de almacenamiento. Clasificación.`, `CARACTERÍSTICAS DE LOS EQUIPOS. -> Depósitos.` | Consolidar selección, clasificación y características del almacenamiento. |
| `Proyecto/Especificaciones/red-distribucion.md` | `Memoria` | `DESCRIPCIÓN Y SISTEMA ELEGIDO.` y `CARACTERÍSTICAS DE LOS EQUIPOS. -> Canalizaciones.` | Describir la arquitectura de red y las características de las conducciones. |
| `Proyecto/Especificaciones/implantacion-seguridad.md` | `Memoria` + `Planos` | `CLASIFICACIÓN Y DISTANCIAS DE SEGURIDAD.` y `Planos` (Plano nº 2) | La justificación va en Memoria; la expresión gráfica va en Planos. |
| `Proyecto/Especificaciones/conclusiones-limitaciones.md` | `Memoria` | `DESCRIPCIÓN Y SISTEMA ELEGIDO.` y cierre de apartados tecnicos relacionados | Repartir conclusiones dentro del cierre técnico de Memoria, sin crear una nueva subsección. |
| `Proyecto/Especificaciones/anejos.md` | `Calculos justificados` (3.1) + `Planos` (capítulo) | `ÍNDICE DE ANEXOS.` y `Planos` (Capítulo sin subsecciones) | Funciona como guía de ensamblado de anexos y planos. |
| `Proyecto/Especificaciones/metodologia.md` | Apoyo transversal | No se vuelca de forma literal | Guía la redacción y la trazabilidad; no debe copiarse completa a LaTeX. |

## Mapeo por notas tecnicas

| Nota tecnica | Destino principal en LaTeX | Uso |
| --- | --- | --- |
| `Proyecto/Anotaciones/caudales_consumidores.md` | `CONSUMO Y AUTONOMÍA.` | Soporte de cálculo para demanda y consumo. |
| `Proyecto/Anotaciones/autonomia_30_dias.md` | `CONSUMO Y AUTONOMÍA.` | Soporte de la autonomía y capacidad útil. |
| `Proyecto/Anotaciones/vaporizacion_natural.md` | `VAPORIZACIÓN.` | Soporte del bloque de vaporización. |
| `Proyecto/Anotaciones/seleccion_deposito.md` | `CARACTERÍSTICAS DE LOS EQUIPOS. -> Depósitos.` | Criterio de selección del almacenamiento. |
| `Proyecto/Anotaciones/trazado_red.md` | `DESCRIPCIÓN Y SISTEMA ELEGIDO.` y `Canalizaciones.` | Soporte de trazado y red. |
| `Proyecto/Anotaciones/distancias_seguridad.md` | `CLASIFICACIÓN Y DISTANCIAS DE SEGURIDAD.` | Soporte normativo y geométrico. |
| `Proyecto/Anotaciones/criterios_normativos.md` | `REGLAMENTACIÓN Y NORMAS TÉCNICAS CONSIDERADAS.` | Base normativa del documento. |

## Reglas de consolidacion

- No copiar `metodologia.md` de forma literal a la plantilla.
- No crear subsecciones nuevas en `plantilla.tex` mientras las existentes permitan absorber el contenido.
- Llevar a `Memoria` solo el nivel de detalle justificativo necesario.
- Llevar a `Cálculos justificados` el desarrollo numérico, tablas de comprobación y resultados intermedios.
- Llevar a `Planos` solo la capa gráfica y sus referencias cruzadas.

## Criterios para agentes

- `task-orchestrator` debe usar este documento cuando una tarea pase de Markdown a consolidación editorial.
- `latex-writer` debe tratar este archivo como contrato de encaje, no como fuente técnica primaria.
- `latex-validator` debe usarlo para comprobar que un fragmento LaTeX cae en la subsección correcta.
