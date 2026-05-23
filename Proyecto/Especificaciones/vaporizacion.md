# Especificación: Vaporización Natural y Forzada (Sección 2.2.3)

## Propósito
Comprobar la suficiencia de la capacidad de vaporización natural de la batería de depósitos en las condiciones climáticas de diseño y dimensionar el sistema de vaporización forzada de apoyo requerido para abastecer la demanda punta.

## Contenido obligatorio
- **Cálculo de Vaporización Natural del Depósito:**
  - Desarrollar la fórmula de gasificación natural para depósitos cilíndricos horizontales de superficie:
    $$ Q_{\text{nat}} = \frac{P \cdot S \cdot K \cdot (T_e - T_g)}{CLV} $$
    donde:
    - $P$: factor de superficie mojada en el nivel de llenado del $20\%$ ($P = 0,336$).
    - $S$: superficie expuesta del depósito en $\text{m}^2$.
    - $K$: coeficiente de transmisión de calor para tanques aéreos ($0,0116\text{ kW/m}^2\cdot\text{ºC}$).
    - $T_e$: temperatura mínima exterior de diseño de León ($-5\text{ ºC}$).
    - $T_g$: temperatura de equilibrio del propano comercial ($-15\text{ ºC}$).
    - $CLV$: calor latente de vaporización del propano ($0,11 \text{ kWh/kg}$).
  - Calcular la capacidad unitaria de gasificación a $-5\text{ ºC}$ y $20\%$ de llenado para cada depósito:
    - LP46A ($S = 88,58 \text{ m}^2$): $Q_{\text{nat}} \approx 35,46 \text{ kg/h}$.
    - LP26A ($S = 51,00 \text{ m}^2$): $Q_{\text{nat}} \approx 20,42 \text{ kg/h}$ por tanque.
  - Sumar la gasificación natural total de la batería de 4 depósitos:
    $$ Q_{\text{nat, total}} = 35,46 + 3 \cdot 20,42 = 96,72 \text{ kg/h} $$
- **Balance Térmico y Determinación de Déficit:**
  - Comparar la capacidad natural agregada de gasificación ($96,72 \text{ kg/h}$) frente a la demanda punta agregada de la instalación ($187,81 \text{ kg/h}$).
  - Identificar y cuantificar el déficit térmico resultante:
    $$ Q_{\text{deficit}} = 187,81 - 96,72 = 91,09 \text{ kg/h} $$
- **Selección y Dimensionamiento del Vaporizador Forzado:**
  - Justificar técnicamente la necesidad de un vaporizador eléctrico/calefacción forzado debido al déficit.
  - Seleccionar el intercambiador de serpentín VIA 150 montado sobre brida DN400 del depósito LP46A, alojado en armario metálico VPC30C.
  - Dimensionar la potencia de calefacción requerida del armario (caldera de agua caliente):
    $$ P_{\text{cal}} = Q_{\text{evap}} \cdot CLV = 91,09 \text{ kg/h} \cdot 0,11 \text{ kWh/kg} \approx 10,02 \text{ kW} $$
  - Justificar la adopción comercial de una caldera de calefacción de agua caliente de $45 \text{ kW}$ para asegurar un margen amplio y cubrir pérdidas térmicas.

## Estilo de redacción
Tono de ingeniería formal y riguroso. Uso de ecuaciones matemáticas LaTeX. Longitud orientativa: 2 páginas.

## Figuras, tablas y resultados
- **Figuras a integrar:**
  - [armario_calefaccion.png](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/armario_calefaccion.png): Imagen y esquema del armario de calefacción (modelo VPC30C) de 45 kW que da soporte al intercambiador de calor de serpentín VIA 150.
- **Tablas obligatorias:**
  - **Tabla de balance de vaporización:** Vaporización de cada depósito de la batería, suma, demanda y déficit resultante.
- **Resultado final de diseño:** Capacidad natural total de $96,72 \text{ kg/h}$, déficit de $91,09 \text{ kg/h}$ y potencia del vaporizador adoptado de $45 \text{ kW}$.

## Conexiones
- **Alcance:** Requisito 3 (Vaporización natural y forzada).
- **Anotaciones:** [vaporizacion_natural.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/vaporizacion_natural.md) (Cálculo), [vaporizacion_forzada.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/vaporizacion_forzada.md) (Decisión), [potencia_armario_calefaccion.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/potencia_armario_calefaccion.md) (Cálculo).

## Criterios de aceptación
- [ ] La ecuación de vaporización natural se aplica correctamente a depósitos aéreos horizontales.
- [ ] La gasificación natural agregada calculada para la batería es de $96,72 \text{ kg/h}$ (al $20\%$ de llenado).
- [ ] Se cuantifica el déficit de gasificación de $91,09 \text{ kg/h}$.
- [ ] Se justifica la elección del intercambiador VIA 150 en armario VPC30C y la potencia de $45 \text{ kW}$.
