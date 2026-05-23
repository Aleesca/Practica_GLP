# Especificación: Demanda y Caudal de Cálculo (Sección 2.2.1)

## Propósito
Justificar y desarrollar el cálculo de la demanda de GLP de la instalación para el Grupo G1-1, determinando los caudales de cálculo individuales de cada punto de consumo y el caudal de diseño conjunto del sistema.

## Contenido obligatorio
- **Metodología de Conversión y Fórmulas:**
  - Explicar la obtención del caudal másico nominal ($Q_{kg/h} = P / PCS$) usando el poder calorífico superior del propano ($PCS = 13,95 \text{ kWh/kg}$).
  - Explicar la obtención del caudal volumétrico ($Q_{m^3/h} = Q_{kg/h} / \rho_{gas}$) con la densidad de diseño ($\rho_{gas} = 1,882 \text{ kg/m}^3$).
- **Resultados de Demanda Individual por Consumidor:**
  - Tabla de consumidores C1 a C6, indicando para cada uno: Potencia nominal ($P$), Caudal másico ($Q_{kg/h}$), Caudal volumétrico ($Q_{m^3/h}$), Horas de uso y energía diaria demandada.
- **Demanda Agregada y Caudal de Cálculo:**
  - Explicar y justificar el coeficiente de simultaneidad $f_s = 1$ para las puntas de consumo industrial.
  - Resultados agregados: Potencia de $2.620 \text{ kW}$, Caudal másico acumulado de $187,81 \text{ kg/h}$, Caudal volumétrico acumulado de $99,79 \text{ m}^3\text{/h}$ y Energía diaria demandada acumulada de $17.640 \text{ kWh/día}$.

## Estilo de redacción
Tono de ingeniería preciso, formal y descriptivo. Uso de notación LaTeX para fórmulas. Longitud orientativa: 1,5 páginas.

## Figuras, tablas y resultados
- **Tabla de caudales individuales:** Consumidores C1 a C6 con potencias, caudales y energía diaria.
- **Resultado final:** Caudal de cálculo global de $187,81 \text{ kg/h}$ ($99,79 \text{ m}^3\text{/h}$).

## Conexiones
- **Alcance:** Requisito 1 (Caudal individual y total de cálculo).
- **Anotaciones:** [caudales_consumidores.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/caudales_consumidores.md) (Cálculo).

## Criterios de aceptación
- [ ] La potencia de diseño agregada es exactamente $2.620 \text{ kW}$.
- [ ] El caudal de cálculo másico total de la batería es igual a $187,81 \text{ kg/h}$ (redondeo correcto).
- [ ] Se detalla un ejemplo de cálculo de conversión para uno de los consumidores.
- [ ] Se justifica el uso de coeficiente de simultaneidad de 1.
