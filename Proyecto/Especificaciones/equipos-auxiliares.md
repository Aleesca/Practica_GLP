# Especificación: Equipos Auxiliares de la Estación (Secciones 2.13.3, 2.13.5, 2.13.6, 2.13.7)

## Propósito
Describir detalladamente los componentes mecánicos, de control y de seguridad del almacenamiento de GLP, garantizando su adecuación comercial y normativa.

## Contenido obligatorio

### Sección 2.13.3 Boca de carga.
- Definir la boca de carga rápida (acoplamiento tipo RegO de 3" o equivalente).
- Describir la configuración de doble válvula de retención y la purga intermedia para evitar emisiones fugitivas durante el desacoplamiento.
- Especificar el limitador de llenado automático de seguridad al $85\%$.

### Sección 2.13.5 Equipos de regulación y medida.
- Describir la regulación de primera etapa instalada en la salida de fase gas de los depósitos (Regulador RegO 1588V o Clesse APS) que reduce la presión del depósito a la presión de la red de distribución ($1,7 \text{ bar}$).
- Detallar las llaves de corte general en la salida de cada tanque y las transiciones cobre-acero.
- Indicar que la medida de consumo individual en los hornos no forma parte de la red de distribución general regulada de primera etapa (o en su caso, justificar la ausencia de contadores generales en la estación de almacenamiento).

### Sección 2.13.6 Equipo de trasvase.
- Justificar técnicamente la exclusión de bombas o compresores de trasvase activo en esta instalación.
- Explicar que la descarga del camión cisterna se realiza por diferencia de presión o gravedad, y que el consumo se abastece por la presión del propio gas (apoyado por el vaporizador).

### Sección 2.13.7 Válvulas de seguridad.
- Describir las válvulas de seguridad instaladas en la fase gas de cada depósito (RegO RS 3145 o similar).
- Especificar que se montan por duplicado sobre un acoplamiento distribuidor de tres vías (CD45) para posibilitar el mantenimiento de una de ellas sin dejar el depósito desprotegido.
- Indicar la presión nominal de tarado de las válvulas ($20 \text{ bar}$).

## Estilo de redacción
Tercera persona del singular, impersonal y tono formal técnico. Longitud orientativa: 1,5 a 2 páginas.

## Figuras, tablas y resultados
- **Figuras/Planos a integrar (como referencia de equipos):**
  - [deposito_seleccionado.png](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/deposito_seleccionado.png): Vista del depósito y sus accesorios (boca de carga, válvulas, manómetro y limitador de llenado) sobre la brida superior.
  - [plano_Esquema_instalacion.pdf](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/plano_Esquema_instalacion.pdf): Esquema de principio hidráulico (P&ID) que muestra la interconexión de todos los equipos y valvulería de la estación.
- **Tablas obligatorias:**
  - **Tabla de componentes comerciales:** Recuento de reguladores, acoplamientos, válvulas de corte y seguridad indicando modelo comercial, fabricante, diámetro nominal ($DN$) y presión nominal ($PN$).
- **Resultados de catálogo:** Tarados de presión del regulador general ($1,7 \text{ bar}$) y válvulas de seguridad ($20 \text{ bar}$).

## Conexiones
- **Alcance:** Requisito 4 (Características principales del depósito y equipos) y Requisito 5 (Conducción - regulación).
- **Anotaciones:** [valvuleria_accesorios.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/valvuleria_accesorios.md) (Decisión), [reporte_accesorios.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/reporte_accesorios.md) (Evidencia), [pliego_condiciones_equipos_glp.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/pliego_condiciones_equipos_glp.md) (Criterio Normativo).

## Criterios de aceptación
- [ ] Se detalla el modelo de boca de carga rápida comercial.
- [ ] Queda justificada la presión de regulación de salida a $1,7 \text{ bar}$.
- [ ] Se justifica formalmente el descarte del equipo de trasvase activo.
- [ ] Se describe el acoplamiento de tres vías (CD45) y tarado a 20 bar de las válvulas de seguridad.
