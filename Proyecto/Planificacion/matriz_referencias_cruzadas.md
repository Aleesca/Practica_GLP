# Matriz de referencias cruzadas entre Anotaciones y Especificaciones

Este documento resume las conexiones documentales implantadas entre `Proyecto/Anotaciones/` y `Proyecto/Especificaciones/`. Su función es servir como guía de revisión, control de trazabilidad y punto de mantenimiento para futuras ampliaciones.

## Anotaciones

| Archivo | Tema principal | Especificaciones vinculadas |
| --- | --- | --- |
| `autonomia_30_dias.md` | criterio de autonomía | `autonomia.md`, `demanda-consumo.md`, `deposito.md` |
| `calculo_volumen_deposito.md` | volumen geométrico mínimo | `autonomia.md`, `demanda-consumo.md`, `deposito.md` |
| `caudales_consumidores.md` | demanda térmica y conversión a caudal | `datos-partida.md`, `demanda-consumo.md`, `red-distribucion.md`, `autonomia.md` |
| `criterios_normativos.md` | marco reglamentario | `datos-partida.md`, `implantacion-seguridad.md`, `instalaciones-auxiliares.md`, `calculos-auxiliares.md` |
| `dimensionado_tuberias_glp.md` | cálculo hidráulico y selección de diámetros | `datos-partida.md`, `red-distribucion.md`, `metodologia-longitud-calculo.md`, `calculos-justificados.md`, `presupuesto.md` |
| `distancias_seguridad.md` | implantación y seguridad | `implantacion-seguridad.md`, `deposito.md`, `instalaciones-auxiliares.md`, `promotor-plazo-accesos.md` |
| `pliego_condiciones_equipos_glp.md` | requisitos de suministro | `deposito.md`, `vaporizacion.md`, `equipos-auxiliares.md`, `presupuesto.md` |
| `potencia_armario_calefaccion.md` | potencia mínima del armario VPC30C | `vaporizacion.md`, `equipos-auxiliares.md`, `instalaciones-auxiliares.md` |
| `recopilacion_accesorios_costes_glp.md` | coste consolidado | `presupuesto.md`, `equipos-auxiliares.md`, `instalaciones-auxiliares.md`, `red-distribucion.md` |
| `reporte_accesorios.md` | contraste comercial y normativo | `presupuesto.md`, `equipos-auxiliares.md`, `calculos-auxiliares.md` |
| `seleccion_deposito.md` | configuración final de la batería | `deposito.md`, `autonomia.md`, `implantacion-seguridad.md`, `presupuesto.md` |
| `temperatura_diseno.md` | temperatura exterior de cálculo | `datos-partida.md`, `vaporizacion.md`, `conclusiones-limitaciones.md` |
| `trazado_red.md` | arquitectura de red | `red-distribucion.md`, `metodologia-longitud-calculo.md`, `demanda-consumo.md`, `presupuesto.md` |
| `valvuleria_accesorios.md` | selección de accesorios y regulación | `equipos-auxiliares.md`, `red-distribucion.md`, `presupuesto.md` |
| `vaporizacion_forzada.md` | sistema mixto de vaporización | `vaporizacion.md`, `equipos-auxiliares.md`, `instalaciones-auxiliares.md`, `deposito.md` |
| `vaporizacion_natural.md` | balance térmico de depósitos | `vaporizacion.md`, `demanda-consumo.md`, `deposito.md` |

## Especificaciones

| Archivo | Tema principal | Anotaciones vinculadas |
| --- | --- | --- |
| `anejos.md` | delimitación de anexos y planos | `pliego_condiciones_equipos_glp.md`, `distancias_seguridad.md` |
| `autonomia.md` | autonomía de almacenamiento | `autonomia_30_dias.md`, `calculo_volumen_deposito.md`, `seleccion_deposito.md` |
| `calculos-auxiliares.md` | válvulas, sonda, PCI y protección catódica | `distancias_seguridad.md`, `valvuleria_accesorios.md`, `pliego_condiciones_equipos_glp.md`, `vaporizacion_forzada.md` |
| `calculos-justificados.md` | encaje editorial del capítulo de cálculo | `dimensionado_tuberias_glp.md`, `calculo_volumen_deposito.md`, `vaporizacion_forzada.md` |
| `conclusiones-limitaciones.md` | síntesis técnica y límites del proyecto | `seleccion_deposito.md`, `dimensionado_tuberias_glp.md`, `distancias_seguridad.md` |
| `datos-partida.md` | hipótesis base | `temperatura_diseno.md`, `criterios_normativos.md`, `caudales_consumidores.md` |
| `demanda-consumo.md` | demanda y caudales | `caudales_consumidores.md`, `dimensionado_tuberias_glp.md` |
| `deposito.md` | selección y características de depósitos | `seleccion_deposito.md`, `calculo_volumen_deposito.md`, `distancias_seguridad.md`, `vaporizacion_forzada.md` |
| `equipos-auxiliares.md` | regulación, corte y seguridad | `valvuleria_accesorios.md`, `pliego_condiciones_equipos_glp.md`, `vaporizacion_forzada.md` |
| `implantacion-seguridad.md` | encaje geométrico y distancias | `distancias_seguridad.md`, `criterios_normativos.md`, `seleccion_deposito.md` |
| `instalaciones-auxiliares.md` | ATEX, PCI y puesta a tierra | `vaporizacion_forzada.md`, `distancias_seguridad.md`, `potencia_armario_calefaccion.md`, `criterios_normativos.md` |
| `intro.md` | contexto y objeto del proyecto | `criterios_normativos.md`, `caudales_consumidores.md` |
| `metodologia-longitud-calculo.md` | método de cálculo hidráulico | `dimensionado_tuberias_glp.md`, `trazado_red.md`, `valvuleria_accesorios.md` |
| `metodologia.md` | directriz metodológica global | `caudales_consumidores.md`, `dimensionado_tuberias_glp.md`, `distancias_seguridad.md` |
| `presupuesto.md` | mediciones y costes | `recopilacion_accesorios_costes_glp.md`, `reporte_accesorios.md`, `pliego_condiciones_equipos_glp.md`, `dimensionado_tuberias_glp.md` |
| `promotor-plazo-accesos.md` | promotor, plazo y accesibilidad | `distancias_seguridad.md`, `seleccion_deposito.md` |
| `red-distribucion.md` | red exterior y regulación | `trazado_red.md`, `dimensionado_tuberias_glp.md`, `valvuleria_accesorios.md` |
| `vaporizacion.md` | justificación del sistema de vaporización | `vaporizacion_natural.md`, `vaporizacion_forzada.md`, `temperatura_diseno.md`, `potencia_armario_calefaccion.md` |

## Criterios de mantenimiento

- Mantener enlaces relativos entre carpetas, evitando rutas absolutas o `file:///`.
- Priorizar referencias justificativas: cálculo, normativa, selección de equipo, implantación o coste.
- Actualizar esta matriz cuando se cree, renombre o elimine un archivo en cualquiera de las dos carpetas.
