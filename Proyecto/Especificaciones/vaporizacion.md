# Memoria: Vaporización Natural vs. Vaporización Forzada

## 1. Verificación del Balance Térmico en Condiciones Críticas
La capacidad de un depósito aéreo de GLP para auto-vaporizar el gas propano líquido a fase vapor depende de la transferencia de calor del aire exterior a través de la chapa mojada por el fluido líquido. Esta capacidad es menor en invierno debido a las bajas temperaturas y al vaciado progresivo del tanque (menor área de transferencia mojada).

El balance de vaporización natural se verifica bajo las siguientes condiciones de diseño de León:
*   **Temperatura exterior mínima de cálculo ($T_e$):** $-5\text{ ºC}$.
*   **Nivel de llenado del depósito (reserva operativa de seguridad):** **$20\%$**.
*   **Temperatura de equilibrio líquido-gas del propano ($T_g$):** $-15\text{ ºC}$.
*   **Coeficiente de transmisión de calor global ($K$):** $0,0116\text{ kW/m}^2\cdot\text{ºC}$ (para depósitos aéreos expuestos al viento).
*   **Calor latente de vaporización del propano ($CLV$):** $0,11\text{ kWh/kg}$.

## 2. Capacidad de Vaporización Natural de la Batería
Aplicando las fórmulas de transferencia térmica a la geometría de la batería mixta adoptada a un nivel del $20\%$ de llenado, se obtienen los siguientes caudales de evaporación natural individuales:
*   **Depósito Principal Lapesa LP46A-22:**
    *   Superficie exterior total: $88,58\text{ m}^2$.
    *   Caudal de vaporización natural a $-5\text{ ºC}$ ($Q_{nat, 1}$): **$47,00\text{ kg/h}$**.
*   **Depósitos de Apoyo Lapesa LP26A-22 (3 unidades):**
    *   Superficie exterior unitaria: $51,00\text{ m}^2$.
    *   Caudal de vaporización natural unitario a $-5\text{ ºC}$ ($Q_{nat, 2}$): **$28,10\text{ kg/h}$** por depósito.
    *   Caudal conjunto de las 3 unidades de apoyo: $3 \times 28,10 = 84,30\text{ kg/h}$.

*   **Capacidad de Vaporización Natural Total de la Batería ($Q_{nat, total}$):**
    $$ Q_{nat, total} = 47,00\text{ kg/h} + 84,30\text{ kg/h} = 131,30\text{ kg/h} $$

## 3. Justificación del Déficit y Elección de la Vaporización Forzada
La demanda punta agregada de los seis consumidores industriales de la planta asciende a **$187,81\text{ kg/h}$** ($99,79\text{ m}^3/\text{h}$). Al comparar esta demanda con la vaporización natural límite disponible en condiciones de diseño, se constata un déficit significativo:

$$ \text{Déficit} = Q_{\text{demanda}} - Q_{nat, total} = 187,81\text{ kg/h} - 131,30\text{ kg/h} = 56,51\text{ kg/h} $$

Bajo estas condiciones desfavorables, la batería mixta es físicamente incapaz de suministrar gas propano en fase de vapor al caudal requerido por los quemadores, lo que provocaría un enfriamiento excesivo del líquido, caída de presión en la instalación, formación de escarcha exterior y el apagado imprevisto de los hornos. Se justifica, por tanto, la necesidad técnica indispensable de instalar un **sistema de vaporización forzada**.

## 4. Selección del Sistema de Vaporización y Especificaciones de Equipos
El sistema de vaporización forzada adoptado no constituye un equipo independiente de gas directo, sino un **sistema mixto de agua caliente de circuito cerrado** compuesto por dos componentes diferenciados:

1.  **Elemento Interno (Intercambiador sumergido) - Modelo Lapesa VIA 150:**
    *   **Naturaleza:** Es un haz tubular en serpentín fabricado en acero inoxidable, que se introduce de forma estanca en el interior del depósito principal LP46A-22, quedando permanentemente sumergido en el propano líquido.
    *   **Acoplamiento:** Se monta sobre una brida especial de servicio **DN400** en la boca de hombre del depósito, lo que evita ocupar espacio adicional en la parcela y protege el intercambiador del exterior.
    *   **Capacidad Nominal de Vaporización:** **$150\text{ kg/h}$**.
2.  **Elemento Externo (Generador de agua caliente) - Armario Lapesa VPC30C:**
    *   **Naturaleza:** Armario metálico exterior autoportante, con dimensiones de **$800\text{ mm}$ (Largo) x $400\text{ mm}$ (Ancho) x $1.200\text{ mm}$ (Alto)**. Se implanta sobre una solera de hormigón adosada al lateral del depósito LP46A-22.
    *   **Equipamiento:** Aloja una caldera mural de gas propano de circuito estanco, bomba de circulación, vaso de expansión y cuadro de control con seguridades térmicas. El circuito cerrado de agua caliente de la caldera circula por el interior del serpentín VIA 150 a una temperatura de consigna regulada.
    *   **Potencia de la caldera:** De cálculo mínimo se requiere una potencia útil de $17,5\text{ kW}$ ($56,51\text{ kg/h} \times 0,11\text{ kWh/kg} \approx 6,2\text{ kW}$ netos, aplicando rendimientos e inercias térmicas). Se adopta la caldera estándar integrada en el armario VPC30C de **$45\text{ kW}$** de potencia térmica, ofreciendo un amplio margen de calentamiento y rapidez de respuesta frente a demandas transitorias.

## 5. Balance Global con Vaporización Forzada y Margen de Seguridad
Con la entrada en servicio del intercambiador VIA 150 acoplado al depósito principal, la capacidad térmica conjunta del almacenamiento es:

$$ Q_{\text{total, disponible}} = Q_{nat, total} + Q_{\text{forzada}} = 131,30\text{ kg/h} + 150,00\text{ kg/h} = 281,30\text{ kg/h} $$

Este valor total disponible ($281,30\text{ kg/h}$) supera con un **margen de seguridad del $49,8\%$** la demanda punta máxima de la instalación ($187,81\text{ kg/h}$). Este excedente garantiza:
*   La estabilidad absoluta de la presión de regulación MPB a $1,7\text{ bar}$ en el colector común, eliminando oscilaciones en los quemadores.
*   Capacidad de respuesta ante eventuales descensos térmicos transitorios por debajo de los $-5\text{ ºC}$ de diseño.
*   Seguridad de funcionamiento incluso con niveles de almacenamiento residuales inferiores al $20\%$.

## Referencias relacionadas
- [Memoria: Hipótesis y datos de partida](datos-partida.md)
- [Memoria: Demanda y caudales de cálculo](demanda-consumo.md)
- [Memoria: Selección y dimensionado del depósito](deposito.md)
- [Memoria: Instalaciones auxiliares y de seguridad de la estación](instalaciones-auxiliares.md)
- [Vaporización natural](../Anotaciones/vaporizacion_natural.md)
- [Vaporización forzada](../Anotaciones/vaporizacion_forzada.md)
- [Temperatura exterior de cálculo](../Anotaciones/temperatura_diseno.md)
- [Potencia del armario de calefacción](../Anotaciones/potencia_armario_calefaccion.md)
