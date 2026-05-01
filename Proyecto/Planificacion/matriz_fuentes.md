# Matriz de Fuentes Tecnicas y Trazabilidad

Este documento fija el contrato de fuentes activo para la memoria tecnica. La salida primaria sigue siendo `Proyecto/Especificaciones/`; `Practica_GLPs_LaTeX/` solo consolida editorialmente.

## Matriz operativa

| Seccion | Fuente primaria | Fuente secundaria | Calculo | Figura | Estado | Observacion operativa |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `1. Introduccion` | `Proyecto/Especificaciones/intro.md` | `Proyecto/Alcance.md` | - | - | `base creada` | El bloque define contexto, objetivos y alcance. |
| `2. Metodologia` | `Proyecto/Especificaciones/metodologia.md` | `Proyecto/Planificacion/esquema_memoria.md` | Contrato metodologico | - | `base creada` | Estructura prescriptiva activa del proyecto. |
| `2.1 Hipotesis y datos de partida` | `Proyecto/Especificaciones/datos-partida.md` | `Proyecto/Datos.md` | Tabla maestra futura | - | `base creada` | Debe consolidar datos del grupo y supuestos de calculo. |
| `2.2.1 Demanda y caudal de calculo` | `Proyecto/Especificaciones/demanda-consumo.md` | `Proyecto/Anotaciones/caudales_consumidores.md` | Hoja o tabla de demanda | Plano base si procede | `pendiente desarrollo tecnico` | Debe cerrar la demanda comun del sistema. |
| `2.2.2 Autonomia de almacenamiento` | `Proyecto/Especificaciones/autonomia.md` | `Proyecto/Anotaciones/autonomia_30_dias.md` | Tabla de autonomia | - | `pendiente desarrollo tecnico` | Debe justificar el horizonte de 30 dias. |
| `2.2.3 Vaporizacion natural del deposito` | `Proyecto/Especificaciones/vaporizacion.md` | `Proyecto/Anotaciones/vaporizacion_natural.md` | Tabla de vaporizacion | - | `pendiente desarrollo tecnico` | Debe comprobar la suficiencia en condiciones desfavorables. |
| `2.2.4 Seleccion y dimensionado del deposito` | `Proyecto/Especificaciones/deposito.md` | `Proyecto/Anotaciones/seleccion_deposito.md` | Comparativa de alternativas | Catalogos tecnicos | `pendiente desarrollo tecnico` | Debe cruzar autonomia, vaporizacion e implantacion. |
| `2.2.5 Red de distribucion` | `Proyecto/Especificaciones/red-distribucion.md` | `Proyecto/Anotaciones/trazado_red.md` | Tabla de tramos y perdidas | `01_Planos/instalacion_GLP.dwg` | `pendiente desarrollo tecnico` | Debe cerrar longitudes, diametros y presiones. |
| `2.2.6 Implantacion y distancias de seguridad` | `Proyecto/Especificaciones/implantacion-seguridad.md` | `Proyecto/Anotaciones/distancias_seguridad.md` | Cuadro de distancias | Plano general | `pendiente desarrollo tecnico` | Debe justificar la ubicacion de la estacion. |
| `3. Conclusiones` | `Proyecto/Especificaciones/conclusiones-limitaciones.md` | `Proyecto/Alcance.md` | - | - | `base creada` | Debe sintetizar la solucion adoptada. |
| `4. Limitaciones` | `Proyecto/Especificaciones/conclusiones-limitaciones.md` | `Proyecto/Especificaciones/metodologia.md` | - | - | `base creada` | Debe recoger limites y simplificaciones reales. |
| `5. Bibliografia` | `Proyecto/Planificacion/mapa_citas.md` | `.agents/skills/doc_tecnica_glp/references/` | - | - | `base creada` | Debe cerrar la trazabilidad de citas del proyecto. |
| `6. Anejos` | `Proyecto/Especificaciones/anejos.md` | `Proyecto/Planificacion/manifiesto_figuras_memoria.md` | Tablas auxiliares y anexos | Planos y cuadros | `base creada` | La estructura editorial queda preparada sin tocar LaTeX. |
