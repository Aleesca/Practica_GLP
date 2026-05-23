# Plan de revision y limpieza de `Proyecto/Planificacion/`

## Objetivo

Reducir el contexto documental necesario para construir el entregable final, identificando los archivos de `Proyecto/Planificacion/` que ya no aportan decisiones activas, trazabilidad o contenido que deba mantenerse como fuente de verdad.

La limpieza debe ser reversible hasta que el documento final este consolidado en LaTeX. Por tanto, la primera pasada no debe borrar archivos directamente: debe clasificarlos, extraer cualquier decision pendiente y mover a archivo historico solo lo que quede cubierto por documentos canonicos.

## Estado de aplicacion

Aplicado el 2026-05-23 con politica conservadora de archivo, no de borrado.

Los siguientes documentos fueron movidos a `Proyecto/Planificacion/_archivo/`:

- `inventario_y_estructura_canonica.md`
- `plan_especificaciones_documentacion.md`
- `plan_implementacion_especificaciones_documentacion.md`
- `plan_potencia_armario_calefaccion.md`
- `plan_recopilacion_accesorios_glp.md`
- `plan_refinamiento_recopilacion_accesorios_glp.md`

El `README.md` de este directorio fue actualizado para separar documentos activos y archivo historico.

## Fuente de verdad activa

Para decidir si un archivo de planificacion sigue siendo necesario, se toma como flujo activo:

- `Proyecto/Alcance.md`
- `Proyecto/Datos.md`
- `Proyecto/Planificacion/esquema_memoria.md`
- `Proyecto/Planificacion/matriz_fuentes.md`
- `Proyecto/Planificacion/mapeo_markdown_a_latex.md`
- `Proyecto/Planificacion/mapa_citas.md`
- `Proyecto/Especificaciones/`
- `Proyecto/Anotaciones/`
- `.agents/skills/`
- `Practica_GLPs_LaTeX/` solo como capa de consolidacion editorial, no como origen tecnico primario.

## Criterios de clasificacion

Cada archivo debe recibir una de estas etiquetas:

- `mantener-activo`: se consulta para redactar, validar o integrar el documento final.
- `mantener-referencia`: no gobierna el trabajo diario, pero conserva decisiones utiles o trazabilidad historica de alto valor.
- `archivar`: su contenido ya esta absorbido por especificaciones, anotaciones o matrices activas; puede moverse fuera del contexto principal.
- `eliminar-candidato`: duplicado, obsoleto o superado por otro documento, sin decisiones unicas pendientes.
- `fusionar-y-archivar`: contiene una decision puntual util que debe copiarse primero a un documento activo antes de archivarlo.

## Revision archivo por archivo

| Archivo | Clasificacion inicial | Motivo | Accion propuesta |
| --- | --- | --- | --- |
| `README.md` | `mantener-activo` | Define reglas del directorio y documentos clave. | Actualizar despues de la limpieza para que refleje solo archivos activos y archivo historico. |
| `esquema_memoria.md` | `mantener-activo` | Es contrato de estructura de la memoria y aparece en el `README` raiz como referencia activa. | Mantener. Revisar si la estructura canonica extraida en `inventario_y_estructura_canonica.md` debe sustituir o complementar este esquema. |
| `matriz_fuentes.md` | `mantener-activo` | Centraliza trazabilidad entre LaTeX, especificaciones, anotaciones y estado documental. | Mantener como matriz principal de cobertura. |
| `mapeo_markdown_a_latex.md` | `mantener-activo` | Define reglas de consolidacion editorial hacia LaTeX. | Mantener mientras exista conversion Markdown-LaTeX pendiente. |
| `mapa_citas.md` | `mantener-activo` | Centraliza claves bibliograficas y normativa a citar. | Mantener hasta cerrar bibliografia final. |
| `manifiesto_figuras_memoria.md` | `mantener-activo` | Inventario breve de figuras y planos esperados. | Mantener si no esta incorporado en `matriz_fuentes.md`; si la matriz ya cubre todo, fusionar y archivar. |
| `manifiesto_tablas_metodologia.md` | `mantener-activo` | Inventario breve de tablas tecnicas esperadas. | Mantener si no esta incorporado en `matriz_fuentes.md`; si la matriz ya cubre todo, fusionar y archivar. |
| `Cronograma_responsables_dependencias.md` | `mantener-referencia` | Contiene RACI, autores, dependencias e hitos; puede apoyar portada/plazo, pero no gobierna la redaccion tecnica. | Extraer solo datos de autores/responsabilidades necesarios. Luego mover a historico si no se usa para entrega final. |
| `inventario_y_estructura_canonica.md` | `fusionar-y-archivar` | Documenta fases ya ejecutadas y brechas ya resueltas en `Proyecto/Especificaciones/`; conserva informacion util sobre estructura canonica. | Comparar contra `matriz_fuentes.md`. Si no hay brechas nuevas, conservar solo la estructura canonica o integrarla en `mapeo_markdown_a_latex.md`; despues archivar. |
| `plan_especificaciones_documentacion.md` | `eliminar-candidato` | Plan inicial de fases para crear especificaciones; su salida ya existe en `Proyecto/Especificaciones/` y en la matriz completada. | Confirmar que todas sus fases estan cubiertas. Si lo estan, archivar o eliminar. |
| `plan_implementacion_especificaciones_documentacion.md` | `eliminar-candidato` | Plan de implementacion ya ejecutado; sus resultados aparecen en `inventario_y_estructura_canonica.md`, `matriz_fuentes.md` y especificaciones creadas. | Mantener solo si se necesita auditoria historica. En caso contrario, archivar o eliminar. |
| `plan_potencia_armario_calefaccion.md` | `eliminar-candidato` | Plan especifico ya absorbido por `Proyecto/Anotaciones/potencia_armario_calefaccion.md`, `vaporizacion_forzada.md` y especificaciones de vaporizacion. | Verificar que no contiene supuestos exclusivos. Si no, archivar o eliminar. |
| `plan_recopilacion_accesorios_glp.md` | `eliminar-candidato` | Plan operativo de recopilacion ya cubierto por anotaciones de accesorios, costes, reporte y presupuesto. | Verificar que precios/fuentes estan en anotaciones. Si lo estan, archivar o eliminar. |
| `plan_refinamiento_recopilacion_accesorios_glp.md` | `eliminar-candidato` | Refinamiento posterior del plan de accesorios; probablemente duplicado por resultados ya consolidados. | Comparar contra `recopilacion_accesorios_costes_glp.md`, `reporte_accesorios.md` y `presupuesto.md`; despues archivar o eliminar. |
| `plan_revision_orquestador_agentes.md` | `mantener-referencia` | Describe contrato operativo de agentes y ubicacion canonica de skills. | Mantener mientras el sistema de agentes siga en uso. Archivar al final si `.agents/skills/` queda estable y documentado en `README.md`. |

## Procedimiento de revision

1. Crear una carpeta de retencion temporal:
   - `Proyecto/Planificacion/_archivo/`
   - No usarla como fuente activa; solo como deposito historico durante la limpieza.

2. Revisar los candidatos por grupos:
   - Grupo A, planes ya ejecutados: `plan_especificaciones_documentacion.md`, `plan_implementacion_especificaciones_documentacion.md`, `plan_potencia_armario_calefaccion.md`, `plan_recopilacion_accesorios_glp.md`, `plan_refinamiento_recopilacion_accesorios_glp.md`.
   - Grupo B, documentos de trazabilidad activos: `matriz_fuentes.md`, `mapeo_markdown_a_latex.md`, `mapa_citas.md`, `esquema_memoria.md`.
   - Grupo C, manifiestos compactos: `manifiesto_figuras_memoria.md`, `manifiesto_tablas_metodologia.md`.
   - Grupo D, gobierno operativo: `Cronograma_responsables_dependencias.md`, `plan_revision_orquestador_agentes.md`, `README.md`.

3. Para cada archivo candidato:
   - Buscar referencias con `rg "<nombre_archivo>" .`.
   - Comprobar si contiene decisiones no repetidas en `Proyecto/Especificaciones/` o `Proyecto/Anotaciones/`.
   - Si contiene una decision unica, copiarla al documento activo correspondiente.
   - Si no contiene informacion unica, moverlo a `_archivo/`.

4. Actualizar `README.md`:
   - Separar "Documentos activos" de "Archivo historico".
   - Indicar que `_archivo/` no debe cargarse en contexto salvo auditoria.

5. Validar que la limpieza no rompe el flujo activo:
   - `rg --files Proyecto/Planificacion`
   - `rg "Proyecto/Planificacion/(plan_|inventario_y_estructura_canonica)" README.md Proyecto .agents`
   - Revisar que `matriz_fuentes.md` sigue cubriendo todos los apartados LaTeX necesarios.

## Orden recomendado de limpieza

1. Archivar primero los planes especificos ya ejecutados:
   - `plan_potencia_armario_calefaccion.md`
   - `plan_recopilacion_accesorios_glp.md`
   - `plan_refinamiento_recopilacion_accesorios_glp.md`

2. Revisar y archivar los planes de especificaciones:
   - `plan_especificaciones_documentacion.md`
   - `plan_implementacion_especificaciones_documentacion.md`

3. Fusionar informacion util de `inventario_y_estructura_canonica.md`:
   - Mantener en activo solo si aporta una estructura canonica mas precisa que `esquema_memoria.md` y `matriz_fuentes.md`.
   - Si su contenido esta duplicado, archivar.

4. Compactar manifiestos:
   - Si `matriz_fuentes.md` ya lista figuras y tablas finales, fusionar `manifiesto_figuras_memoria.md` y `manifiesto_tablas_metodologia.md` en una seccion breve de la matriz.

5. Dejar para el final los documentos de coordinacion:
   - `Cronograma_responsables_dependencias.md`
   - `plan_revision_orquestador_agentes.md`
   - `README.md`

## Resultado esperado

Tras la limpieza, `Proyecto/Planificacion/` deberia quedar con un conjunto reducido de documentos activos:

- `README.md`
- `esquema_memoria.md`
- `matriz_fuentes.md`
- `mapeo_markdown_a_latex.md`
- `mapa_citas.md`
- `manifiesto_figuras_memoria.md` si no se fusiona.
- `manifiesto_tablas_metodologia.md` si no se fusiona.
- `Cronograma_responsables_dependencias.md` solo si sigue siendo necesario para reparto o portada.
- `plan_revision_orquestador_agentes.md` solo si se sigue usando el sistema de agentes.

Los planes ejecutados y documentos de auditoria deberian quedar fuera del contexto activo, preferiblemente en `_archivo/` hasta que el entregable final este cerrado.

## Criterio de aceptacion

La limpieza se considera correcta cuando:

- Ningun archivo activo de `Proyecto/Planificacion/` es solo un plan ya ejecutado.
- Las decisiones tecnicas siguen localizables en `Proyecto/Especificaciones/`, `Proyecto/Anotaciones/` o `matriz_fuentes.md`.
- El `README.md` explica que cargar para trabajar y que omitir para ahorrar contexto.
- Los archivos archivados no son referenciados como fuente activa por el `README.md` raiz ni por documentos canonicos.
- Se puede reconstruir la trazabilidad del proyecto sin abrir planes historicos.
