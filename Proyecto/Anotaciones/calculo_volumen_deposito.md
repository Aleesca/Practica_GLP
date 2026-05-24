# Calculo del volumen del deposito

Esta nota detalla el desarrollo matemático para el dimensionamiento del sistema de almacenamiento de GLP del Grupo G1-1.

## 1. Parámetros de Diseño
- **Energía Diaria Total ($E_{dia}$):** $17.640 \text{ kWh/día}$ (Calculado en [caudales_consumidores.md](caudales_consumidores.md)).
- **Poder Calorífico Superior ($PCS$):** $13,95 \text{ kWh/kg}$.
- **Densidad del Propano Líquido ($\rho$):** $506 \text{ kg/m}^3$ (a 20 ºC).
- **Autonomía ($A$):** $30 \text{ días}$ (Justificado en [autonomia_30_dias.md](autonomia_30_dias.md)).
- **Fracción Útil ($f_u$):** $0,65$ ($85\% \text{ llenado máximo} - 20\% \text{ reserva}$).

## 2. Desarrollo de Ecuaciones

### Paso 1: Cálculo del consumo másico diario ($m_{dia}$)
$$m_{dia} = \frac{E_{dia}}{PCS} = \frac{17.640}{13,95} = 1.264,52 \text{ kg/día}$$

### Paso 2: Cálculo del volumen de líquido diario ($V_{liq\_dia}$)
$$V_{liq\_dia} = \frac{m_{dia}}{\rho} = \frac{1.264,52}{506} = 2,499 \text{ m}^3\text{/día}$$

### Paso 3: Cálculo del volumen geométrico mínimo ($V_{geom}$)
$$V_{geom} = \frac{V_{liq\_dia} \cdot A}{f_u} = \frac{2,499 \cdot 30}{0,65} = 115,34 \text{ m}^3 = 115.341 \text{ litros}$$

## 3. Selección Comercial
Se selecciona una configuración de batería ajustada a las dimensiones de la parcela (ver evolución en [seleccion_deposito.md](seleccion_deposito.md)):
- **Modelo:** **1 x LP46A-22 (Modelo Especial)** + **3 x LP26A-22**
- **Capacidad Total:** $125.100 \text{ litros}$

## 4. Conclusión
La instalación garantiza una autonomía real de **32,5 días**, cumpliendo con los 30 días requeridos por la TAREA 3.

---
**Véase también:**
- [Selección del depósito](seleccion_deposito.md)
- [Vaporización natural](vaporizacion_natural.md)
- [Autonomía de 30 días](autonomia_30_dias.md)
- [Caudales de consumidores](caudales_consumidores.md)
- [Memoria: Autonomía de almacenamiento](../Especificaciones/autonomia.md)
- [Memoria: Selección y dimensionado del depósito](../Especificaciones/deposito.md)
- [Memoria: Demanda y caudales de cálculo](../Especificaciones/demanda-consumo.md)
