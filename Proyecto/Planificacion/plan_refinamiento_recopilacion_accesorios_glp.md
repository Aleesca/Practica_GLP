# Plan: Refinamiento de Recopilación de Accesorios y Costes GLP

## Resumen

Refinar `Proyecto/Anotaciones/recopilacion_accesorios_costes_glp.md` para convertirlo en una estimación más cercana a un proyecto real de ingeniería. El refinamiento debe ajustar proveedores, accesorios, válvulas, reguladores, depósitos, válvulas de alivio, armario de calefacción y costes asociados.

La ejecución posterior deberá consultar el notebook GLP para extraer la normativa aplicable y usar exclusivamente los enlaces de `Proyecto/Anotaciones/reporte_accesorios.md` para localizar y valorar todos los productos.

## Cambios Principales

- **Consulta restringida a `reporte_accesorios.md`**: todos los productos con precio deberán buscarse exclusivamente en los enlaces recogidos en `Proyecto/Anotaciones/reporte_accesorios.md`.
- **Proveedor único para tubería de cobre**: procurar seleccionar un mismo proveedor para todos los tubos de cobre, siempre que cubra los diámetros requeridos, tenga precios verificables y productos aptos para gas/GLP.
- **Normativa antes de selección**: consultar primero el notebook GLP para extraer requisitos UNE/EN aplicables a válvulas de corte, reguladores, válvulas de alivio, depósitos, tuberías y accesorios.
- **Válvulas de corte por diámetro**: seleccionar llaves o válvulas de corte según el diámetro y la ubicación, especialmente a la salida de cada depósito.
- **Reguladores por tramo o línea de salida**: añadir reguladores después de la válvula de corte de cada depósito, ajustando el tipo y precio según diámetro, caudal, presión y configuración de cada tramo o línea.
- **Válvulas de alivio**: incluir una válvula de alivio por cada depósito, independiente de los tramos de la instalación.
- **Armario de calefacción**: incluirlo únicamente en el depósito/sistema con vaporizador interno, asociado al caso de mayor caudal.
- **Costes de proyecto real**: añadir costes no materiales como instalación, pruebas, transporte, legalización, ingeniería, seguridad y contingencias.

## Flujo de Refinamiento

1. **Preparar matriz de partidas**
   - Identificar en `recopilacion_accesorios_costes_glp.md` las partidas existentes.
   - Separar por familias: tubería de cobre, accesorios por tramo, válvulas de corte, reguladores, válvulas de alivio, depósitos, armario de calefacción y costes asociados.
   - Marcar para cada partida cantidad, diámetro/capacidad, ubicación, proveedor, precio, fuente y observación normativa.

2. **Consultar normativa GLP**
   - Durante la ejecución, consultar el notebook GLP antes de seleccionar productos.
   - Extraer requisitos UNE/EN aplicables a tuberías de cobre, accesorios, válvulas de corte, reguladores, válvulas de alivio, depósitos y elementos con vaporizador.
   - Registrar para cada familia de producto los requisitos mínimos: material, presión nominal, compatibilidad GLP/gas, rango de caudal, conexiones, accesibilidad y condiciones de instalación.

3. **Usar exclusivamente los enlaces de `reporte_accesorios.md`**
   - Abrir y clasificar todos los enlaces disponibles en `Proyecto/Anotaciones/reporte_accesorios.md`.
   - Asignar cada enlace a una familia de producto: tuberías, accesorios, válvulas, reguladores, depósitos, armarios, seguridad u otros.
   - Buscar precios y fichas técnicas únicamente dentro de esas páginas web.
   - Si una partida no se encuentra en esos enlaces, marcarla como “pendiente por falta de fuente autorizada” y no sustituirla con fuentes externas.

4. **Homogeneizar proveedor de tubos de cobre**
   - Agrupar todos los tramos por diámetro de tubería.
   - Comprobar si un único proveedor de los enlaces autorizados cubre todos los diámetros necesarios.
   - Priorizar un proveedor apto para gas/GLP con precios verificables.
   - Justificar cualquier excepción cuando un diámetro no esté disponible en el proveedor principal.

5. **Seleccionar válvulas de corte**
   - Identificar las válvulas de corte necesarias por depósito, tramo, derivación o punto de aislamiento.
   - Seleccionar cada válvula según diámetro, conexión, presión nominal y compatibilidad GLP.
   - Para las salidas de depósito, colocar la válvula de corte antes del regulador.
   - Registrar precio, proveedor, URL, diámetro, cantidad y criterio normativo.

6. **Seleccionar reguladores**
   - Añadir reguladores después de la válvula de corte que sale de cada depósito.
   - Determinar el tipo de regulador según el tramo o línea: diámetro, caudal, presión de entrada, presión de salida y configuración del sistema.
   - No asumir un único regulador para toda la instalación: seleccionar el modelo adecuado para cada caso.
   - Buscar modelos y precios solo en los enlaces de `reporte_accesorios.md`.
   - Registrar para cada regulador: ubicación, caudal nominal, rango de presión, diámetro/conexión, compatibilidad GLP, precio y fuente.

7. **Incluir válvulas de alivio por depósito**
   - Identificar los depósitos seleccionados.
   - Añadir una válvula de alivio por cada depósito, independiente de los tramos.
   - Verificar presión de tarado, compatibilidad y normativa aplicable.
   - Buscar precio y ficha únicamente en los enlaces autorizados.
   - Asociar cada válvula de alivio al depósito correspondiente.

8. **Incluir armario de calefacción y depósitos**
   - Incorporar cada depósito seleccionado como partida independiente.
   - Incluir el armario de calefacción únicamente en el depósito/sistema con vaporizador interno y mayor caudal.
   - Registrar capacidad, cantidad, configuración, fuente técnica y coste.
   - Mantener depósitos, armario, válvulas de alivio y reguladores de salida como elementos generales del sistema, no como accesorios ordinarios de tramo salvo que el documento lo necesite para trazabilidad.

9. **Añadir costes asociados de proyecto real**
   - Incorporar una sección de costes no materiales.
   - Incluir mano de obra de instalación, soportación/fijaciones, transporte, medios auxiliares, pruebas de presión/estanqueidad, puesta en marcha, legalización, inspección, gestión documental, seguridad y salud, dirección técnica o ingeniería, imprevistos y contingencia.
   - Diferenciar costes medidos, estimados y porcentuales.
   - Documentar la hipótesis usada para cada coste sin precio directo.

10. **Actualizar estructura económica**
   - Recalcular subtotales por tramo para tubería, accesorios, válvulas de corte y reguladores cuando correspondan.
   - Añadir tabla de elementos generales para depósitos, válvulas de alivio, armario de calefacción y reguladores de salida.
   - Añadir tabla de costes asociados de proyecto.
   - Calcular subtotal de materiales, subtotal de equipos, subtotal de costes asociados y total general.
   - Mantener una columna de precios pendientes o no verificados.

## Criterios de Aceptación

- `recopilacion_accesorios_costes_glp.md` queda refinado como estimación técnico-económica de proyecto real.
- Todos los productos con precio se buscan exclusivamente en los enlaces de `reporte_accesorios.md`.
- La tubería de cobre usa un proveedor único cuando sea viable; las excepciones quedan justificadas.
- La selección de válvulas, reguladores, accesorios y depósitos se filtra primero con normativa del notebook GLP.
- Las válvulas de corte se dimensionan según diámetro y ubicación.
- Cada salida de depósito incluye válvula de corte y, después, su regulador correspondiente.
- Los reguladores se seleccionan por caudal, presión, diámetro y configuración; no se usa un único modelo para todos si no corresponde.
- Se incluye una válvula de alivio independiente por cada depósito.
- El armario de calefacción solo aparece en el sistema con vaporizador interno y mayor caudal.
- Los depósitos seleccionados aparecen como partidas independientes.
- Se incluyen costes asociados no materiales y se diferencian de materiales/equipos.
- Los totales distinguen importes verificados, estimados y pendientes.
- No se modifica el dimensionado de diámetros, longitudes ni caudales.

## Supuestos

- `recopilacion_accesorios_costes_glp.md` ya existe y contiene una primera estimación de tramos, accesorios y costes.
- `reporte_accesorios.md` contiene los enlaces autorizados para buscar todos los productos y precios.
- El notebook GLP contiene la normativa necesaria para validar tuberías, accesorios, válvulas de corte, reguladores, válvulas de alivio, depósitos y sistema con vaporizador.
- Las válvulas de alivio pertenecen a los depósitos, no a los tramos de instalación.
- El armario de calefacción solo aplica al sistema con vaporizador interno y mayor caudal.
- El refinamiento no redimensiona la instalación; solo mejora selección, trazabilidad y estimación económica.
