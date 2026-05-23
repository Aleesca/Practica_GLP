# Especificación: Selección y Dimensionado del Depósito (Sección 2.2.4)

## Propósito
Seleccionar y justificar la configuración y dimensiones de la batería de almacenamiento de GLP a partir de la autonomía requerida, el volumen de diseño y las restricciones físicas de la parcela.

## Contenido obligatorio
- **Justificación de la Configuración Adoptada:**
  - Argumentar la elección de depósitos aéreos sobre depósitos enterrados (facilidad de inspección visual, menor coste de obra civil, descarte de problemas de flotación y protección catódica).
  - Justificar el descarte de tanques horizontales comerciales de gran capacidad (como 1xLPVI 59A o superior) debido a la limitación longitudinal de la parcela en la zona de implantación.
- **Selección Comercial de Depósitos:**
  - Definir la batería mixta adoptada: 1 depósito Lapesa LP46A-22 (volumen geométrico $46,60 \text{ m}^3$) y 3 depósitos Lapesa LP26A-22 (volumen unitario $25,90 \text{ m}^3$):
    $$ V_{total} = 46,60 + 3 \cdot 25,90 = 124,30 \text{ m}^3 $$
  - Comprobar que el volumen total ($124,30 \text{ m}^3$) cubre con margen de seguridad el volumen mínimo geométrico calculado para la autonomía ($88,20 \text{ m}^3$).
  - Clasificar la batería bajo la categoría A-500 al superar los $100 \text{ m}^3$ acumulados de almacenamiento de propano.
- **Detalle de Características de los Depósitos:**
  - Describir las especificaciones físicas de los depósitos Lapesa seleccionados:
    - LP46A: Diámetro $\phi = 2.200 \text{ mm}$, Longitud total $L = 12.830 \text{ mm}$, Peso vacío $11.080 \text{ kg}$, Superficie exterior $\approx 88,58 \text{ m}^2$.
    - LP26A: Diámetro $\phi = 2.200 \text{ mm}$, Longitud total $L = 7.375 \text{ mm}$, Peso vacío $6.920 \text{ kg}$, Superficie exterior $\approx 51,00 \text{ m}^2$.
    - Chapa de acero para recipientes a presión, presión de prueba de $25 \text{ bar}$, brida de inspección DN400 (Modelo Especial).

## Estilo de redacción
Tono de ingeniería formal, preciso e impersonal. Uso de tablas y unidades técnicas en sistema internacional. Longitud orientativa: 1,5 a 2 páginas.

## Figuras, tablas y resultados
- **Figuras a integrar:**
  - [deposito_seleccionado.png](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/deposito_seleccionado.png): Croquis/imagen en 3D del modelo de depósito aéreo de almacenamiento de GLP Lapesa.
  - [tabla_de_caracteristicas.png](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/tabla_de_caracteristicas.png): Ficha técnica comercial que detalla las dimensiones, volumen y características constructivas de los depósitos del fabricante.
- **Tablas obligatorias:**
  - **Tabla comparativa de alternativas comerciales:** Modelos analizados y motivos de descarte.
  - **Tabla de características de los depósitos seleccionados:** Modelo, volumen, dimensiones, peso y área exterior.

## Conexiones
- **Alcance:** Requisito 4 (Cálculo del volumen del depósito y de sus características principales).
- **Anotaciones:** [seleccion_deposito.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/seleccion_deposito.md) (Decisión), [calculo_volumen_deposito.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/calculo_volumen_deposito.md) (Cálculo), [pliego_condiciones_equipos_glp.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/pliego_condiciones_equipos_glp.md) (Criterio Normativo).

## Criterios de aceptación
- [ ] Se justifica formalmente la configuración aérea frente a enterrada.
- [ ] La capacidad agregada de la batería mixta es exactamente $124,30 \text{ m}^3$ (LP46A + 3xLP26A).
- [ ] Se demuestra que el volumen de la batería cubre la autonomía exigida ($124,30 \text{ m}^3 > 88,20 \text{ m}^3$).
- [ ] Se enumeran las características comerciales (diámetro, longitud, peso y áreas expuestas) de los modelos de Lapesa.
