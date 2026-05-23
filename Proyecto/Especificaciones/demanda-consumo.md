# Memoria: Demanda y Caudales de Cálculo

## 1. Metodología de Conversión Térmico-Masiva y Volumétrica
El caudal de gas demandado por cada punto de consumo se determina a partir de su potencia nominal y las características termodinámicas del propano comercial. 

El **caudal másico nominal ($Q_{mas}$)** de cada consumidor en kilogramos por hora se calcula mediante la relación entre la potencia nominal ($P$) y el Poder Calorífico Superior (PCS) del propano comercial:
$$ Q_{mas} \left[\text{kg/h}\right] = \frac{P \left[\text{kW}\right]}{PCS \left[\text{kWh/kg}\right]} = \frac{P \left[\text{kW}\right]}{13,95 \left[\text{kWh/kg}\right]} $$

Posteriormente, el **caudal volumétrico nominal ($Q_{vol}$)** en metros cúbicos normales por hora se obtiene a partir del caudal másico utilizando la densidad del gas propano en condiciones de diseño ($\rho_{gas} = 1,882\text{ kg/m}^3$):
$$ Q_{vol} \left[\text{m}^3/\text{h}\right] = \frac{Q_{mas} \left[\text{kg/h}\right]}{\rho_{gas} \left[\text{kg/m}^3\right]} = \frac{Q_{mas} \left[\text{kg/h}\right]}{1,882 \left[\text{kg/m}^3\right]} $$

## 2. Resultados de Demanda Individual por Consumidor
Aplicando las fórmulas de conversión descritas a los datos nominales del Grupo G1-1, se obtienen las necesidades operativas individuales para cada receptor:

*   **Horno de secado 1 (C1) y Horno de secado 2 (C2):**
    *   Potencia: $60\text{ kW}$
    *   Caudal másico: $Q_{mas} = 60 / 13,95 = 4,30\text{ kg/h}$
    *   Caudal volumétrico: $Q_{vol} = 4,30 / 1,882 = 2,29\text{ m}^3/\text{h}$
    *   Energía diaria: $60\text{ kW} \times 12\text{ h/d} = 720\text{ kWh/día}$

*   **Caldera de vapor (C3):**
    *   Potencia: $500\text{ kW}$
    *   Caudal másico: $Q_{mas} = 500 / 13,95 = 35,84\text{ kg/h}$
    *   Caudal volumétrico: $Q_{vol} = 35,84 / 1,882 = 19,04\text{ m}^3/\text{h}$
    *   Energía diaria: $500\text{ kW} \times 10\text{ h/d} = 5.000\text{ kWh/día}$

*   **Caldera de agua caliente (C4):**
    *   Potencia: $300\text{ kW}$
    *   Caudal másico: $Q_{mas} = 300 / 13,95 = 21,51\text{ kg/h}$
    *   Caudal volumétrico: $Q_{vol} = 21,51 / 1,882 = 11,43\text{ m}^3/\text{h}$
    *   Energía diaria: $300\text{ kW} \times 8\text{ h/d} = 2.400\text{ kWh/día}$

*   **Horno de fusión (C5):**
    *   Potencia: $700\text{ kW}$
    *   Caudal másico: $Q_{mas} = 700 / 13,95 = 50,18\text{ kg/h}$
    *   Caudal volumétrico: $Q_{vol} = 50,18 / 1,882 = 26,66\text{ m}^3/\text{h}$
    *   Energía diaria: $700\text{ kW} \times 4\text{ h/d} = 2.800\text{ kWh/día}$

*   **Horno de decapado (C6):**
    *   Potencia: $1.000\text{ kW}$
    *   Caudal másico: $Q_{mas} = 1000 / 13,95 = 71,68\text{ kg/h}$
    *   Caudal volumétrico: $Q_{vol} = 71,68 / 1,882 = 38,09\text{ m}^3/\text{h}$
    *   Energía diaria: $1.000\text{ kW} \times 6\text{ h/d} = 6.000\text{ kWh/día}$

## 3. Demanda Agregada y Caudal de Cálculo de la Instalación
Para el dimensionado de las partes comunes de la instalación (colector de la estación de almacenamiento, vaporizador forzado y regulador de primera etapa), se adopta un **coeficiente de simultaneidad $f_s = 1$**. Esta decisión se justifica por la naturaleza del proceso productivo continuo de la planta, donde no se puede descartar la operación simultánea a plena carga de todos los equipos durante picos de producción.

Los valores de cálculo globales para el conjunto del sistema resultan:
*   **Potencia térmica agregada de diseño ($P_{total}$):** $2.620\text{ kW}$
*   **Caudal másico de cálculo global ($Q_{mas, total}$):** **$187,81\text{ kg/h}$** (suma exacta de consumos individuales, $4,30 + 4,30 + 35,84 + 21,51 + 50,18 + 71,68 = 187,81\text{ kg/h}$).
*   **Caudal volumétrico de cálculo global ($Q_{vol, total}$):** **$99,79\text{ m}^3/\text{h}$** (equivalente a $187,81\text{ kg/h} / 1,882\text{ kg/m}^3$).
*   **Energía diaria demandada acumulada ($E_{diaria}$):** **$17.640\text{ kWh/día}$** (equivalente a un consumo de **$1.264,52\text{ kg/día}$** de propano comercial).
