# Memoria: Autonomía de Almacenamiento

## 1. Criterio de Diseño y Justificación de la Autonomía
En el diseño de instalaciones industriales de GLP con almacenamiento fijo, los criterios generales de ingeniería y logística suelen establecer una autonomía de suministro recomendada de 15 días, período suficiente para programar las recargas mediante camión cisterna. Sin embargo, para este proyecto, y de acuerdo con los requerimientos específicos de las especificaciones de partida, se dimensionará el almacenamiento para garantizar una autonomía mínima de **$30\text{ días}$** de funcionamiento continuo sin necesidad de reabastecimiento. Esta autonomía extendida proporciona una garantía excepcional de suministro frente a contingencias climáticas (frecuentes en invierno en la provincia de León) o interrupciones en la cadena logística de distribución de combustibles.

## 2. Consumo Diario Equivalente de Propano
A partir de la energía diaria total calculada en la sección de demanda ($17.640\text{ kWh/día}$) y las características físicas del propano comercial, se determina la demanda diaria de combustible:

*   **Consumo másico diario ($C_{mas, diario}$):**
    $$ C_{mas, diario} = \frac{E_{diaria}}{PCS} = \frac{17.640\text{ kWh/día}}{13,95\text{ kWh/kg}} = 1.264,52\text{ kg/día} $$

*   **Consumo volumétrico en fase líquida ($C_{vol, diario}$):**
    El volumen de propano líquido almacenado a la temperatura normal de servicio ($15\text{ ºC}$), con una densidad de líquido de $\rho_{liq} = 506\text{ kg/m}^3$, es:
    $$ C_{vol, diario} = \frac{C_{mas, diario}}{\rho_{liq}} = \frac{1.264,52\text{ kg/día}}{506\text{ kg/m}^3} = 2,499\text{ m}^3/\text{día} $$

## 3. Determinación del Volumen Útil y Geométrico Mínimo
El almacenamiento no puede consumirse por completo ni llenarse al $100\%$ de su volumen geométrico por razones físicas y reglamentarias:
*   **Llenado máximo permitido:** Limitado por el **$85\%$** del volumen geométrico total del depósito (según UNE 60250) para permitir la dilatación térmica de la fase líquida y evitar sobrepresiones peligrosas.
*   **Límitación de nivel mínimo operativo (Reserva):** Fijado en el **$20\%$** del volumen geométrico. Por debajo de este nivel, la superficie mojada de los depósitos disminuye drásticamente, lo cual reduce la capacidad de vaporización natural y expone el serpentín de vaporización interna (VIA 150) a trabajar fuera del líquido, perdiendo eficacia de intercambio.
*   **Fracción útil de almacenamiento:** Por lo tanto, el volumen operativo neto utilizable representa el **$65\%$** ($85\% - 20\%$) del volumen geométrico total:

$$ \text{Fracción útil} = 0,65 $$

A partir de estas hipótesis, se calculan las necesidades físicas de almacenamiento:
1.  **Volumen Útil Requerido ($V_{util}$):**
    $$ V_{util} = C_{vol, diario} \times \text{Autonomía} = 2,499\text{ m}^3/\text{día} \times 30\text{ días} = 74,97\text{ m}^3 $$
2.  **Volumen Geométrico Mínimo de Almacenamiento ($V_{geom}$):**
    $$ V_{geom} = \frac{V_{util}}{\text{Fracción útil}} = \frac{74,97\text{ m}^3}{0,65} = 115,34\text{ m}^3 $$

## 4. Consecuencias en la Configuración del Sistema
Un volumen geométrico mínimo de **$115,34\text{ m}^3$** supera la capacidad unitaria de los tanques comerciales aéreos horizontales estándar de catálogo de gran volumen, cuya longitud para capacidades superiores a $100\text{ m}^3$ excede las limitaciones de implantación física dentro de la parcela catastral. Por consiguiente, resulta obligatoria e indispensable la implantación de una **batería mixta de depósitos acoplados en paralelo**, distribuyendo el volumen necesario en varios tanques de longitudes contenidas para lograr la flexibilidad y el encaje geométrico que exige el emplazamiento industrial.

## Referencias relacionadas
- [Memoria: Demanda y caudales de cálculo](demanda-consumo.md)
- [Memoria: Selección y dimensionado del depósito](deposito.md)
- [Memoria: Vaporización natural vs. vaporización forzada](vaporizacion.md)
- [Autonomía de 30 días](../Anotaciones/autonomia_30_dias.md)
- [Cálculo del volumen del depósito](../Anotaciones/calculo_volumen_deposito.md)
- [Selección del depósito](../Anotaciones/seleccion_deposito.md)
