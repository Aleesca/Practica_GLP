# Memoria: Selección y Dimensionado del Depósito

## 1. Justificación de la Configuración Aérea Adoptada
Para la estación de almacenamiento de GLP se adopta una configuración de **depósitos aéreos horizontales de superficie**, descartando la alternativa de depósitos enterrados en foso o semienterrados (montículos). Esta decisión se fundamenta en las siguientes ventajas técnicas y económicas:
*   **Inspección y Mantenimiento:** Los tanques aéreos permiten una inspección visual externa directa y continua de las soldaduras, recubrimientos protectores y valvulería, facilitando la detección precoz de cualquier fuga o corrosión sin necesidad de excavaciones.
*   **Obra Civil y Costes:** Requieren únicamente la construcción de soleras y cunas de apoyo de hormigón armado, evitando los elevados costes asociados a la excavación profunda, contención de tierras y gestión de lodos de fosas enterradas.
*   **Inexistencia de Empujes Hidrostáticos (Flotación):** Al estar en superficie, se eliminan por completo los riesgos de flotación de los depósitos ante ascensos del nivel freático, evitando el sobredimensionamiento de los anclajes y losas de lastre.
*   **Innecesariedad de Protección Catódica:** Al no estar en contacto directo con la agresividad del suelo o humedades enterradas, no es obligatorio instalar un sistema de protección catódica activa por corriente impresa o ánodos de sacrificio de magnesio, reduciendo los costes de mantenimiento e inspección periódica de potenciales eléctricos.

## 2. Restricciones Físicas y Evolución de la Solución de Almacenamiento
La parcela catastral disponible presenta limitaciones dimensionales longitudinales estrictas para la ubicación de la estación de almacenamiento, lo cual ha condicionado la selección comercial de los depósitos:

*   **Propuesta Inicial (Descartada):** Se evaluó una batería compuesta por **2 x LPVI 59A-22** (con un volumen total de $118,8\text{ m}^3$). Sin embargo, la longitud física de cada uno de estos tanques es de **$16,39\text{ metros}$**. Tras realizar el replanteo sobre la parcela catastral `8638004TN8183N`, se constató que esta gran longitud impedía cumplir con las distancias de seguridad reglamentarias exigidas por la norma UNE 60250 respecto a los linderos de propiedad colindantes, ya que la proyección horizontal de orificios invadía zonas no permitidas.
*   **Configuración Adoptada (Solución Batería Mixta):** Para reducir la huella longitudinal máxima y dotar al proyecto de la flexibilidad espacial requerida, se ha diseñado una **batería mixta en paralelo** integrada por cuatro depósitos aéreos horizontales del fabricante Lapesa:
    *   **1 x Lapesa LP46A-22 (Depósito Principal):** Volumen geométrico de **$46,60\text{ m}^3$** (capacidad útil de $30.290\text{ litros}$ al $65\%$ operativo).
    *   **3 x Lapesa LP26A-22 (Depósitos de Apoyo):** Volumen geométrico unitario de **$25,90\text{ m}^3$** (capacidad útil unitaria de $16.835\text{ litros}$).

$$ V_{total} = 46,60\text{ m}^3 + 3 \times 25,90\text{ m}^3 = 124,30\text{ m}^3 $$

El volumen total geométrico adoptado de **$124,30\text{ m}^3$** ($124.300\text{ litros}$) es superior al mínimo reglamentario requerido por autonomía de 30 días ($115,34\text{ m}^3$), lo cual proporciona una **autonomía real resultante de $32,5\text{ días}$** a plena carga ($124.300 \times 0,65 / 2.499 = 32,32\text{ días}$).

## 3. Clasificación Reglamentaria de la Estación
Al superar el volumen geométrico total acumulado los $100\text{ m}^3$ de propano líquido sin exceder los $500\text{ m}^3$ ($100\text{ m}^3 < V_{total} \le 500\text{ m}^3$), la estación de almacenamiento queda clasificada oficialmente bajo la norma UNE 60250 y el RD 919/2006 como una **instalación de almacenamiento del Tipo A-500**. Esta clasificación rige con carácter obligatorio el diseño de los vallados de seguridad, los accesos, la instalación eléctrica contra incendios y las distancias mínimas a linderos de propiedad y focos de inflamación.

## 4. Características Físicas y Constructivas de los Depósitos
Los depósitos se proyectan según el código de diseño europeo de recipientes a presión, utilizando aceros de alto límite elástico para soportar las tensiones térmicas y presiones del propano. Sus especificaciones dimensionales y comerciales son:

1.  **Depósito Principal (Lapesa LP46A-22 - Modelo Especial):**
    *   Volumen geométrico nominal: $46,2\text{ m}^3$ ($46.600\text{ l}$ reales).
    *   Diámetro exterior: $2.200\text{ mm}$.
    *   Longitud total del cuerpo: $12.830\text{ mm}$ (longitud reducida que viabiliza el encaje en la parcela).
    *   Peso en vacío: $11.080\text{ kg}$.
    *   Superficie exterior expuesta para intercambio térmico: $\approx 88,58\text{ m}^2$.
    *   **Brida de Servicio DN400 (Modelo Especial):** Debido a que la serie estándar LP46 no dispone de vaporización interna, se ha especificado al fabricante una brida DN400 sobre la boca de hombre para alojar el serpentín de vaporización forzada **VIA 150**.
2.  **Depósitos de Apoyo (Lapesa LP26A-22):**
    *   Volumen geométrico unitario nominal: $26,3\text{ m}^3$ ($25.900\text{ l}$ reales).
    *   Diámetro exterior: $2.200\text{ mm}$.
    *   Longitud total del cuerpo: $7.375\text{ mm}$.
    *   Peso en vacío unitario: $6.920\text{ kg}$.
    *   Superficie exterior expuesta para intercambio unitaria: $\approx 51,00\text{ m}^2$.

Todos los depósitos disponen de apoyos soldados de fábrica (cunas metálicas) que descansan sobre placas de neopreno elástico colocadas sobre cunas de hormigón armado, permitiendo la libre dilatación longitudinal de los recipientes ante fluctuaciones térmicas estacionales.

## Referencias relacionadas
- [Memoria: Autonomía de almacenamiento](autonomia.md)
- [Memoria: Vaporización natural vs. vaporización forzada](vaporizacion.md)
- [Memoria: Implantación y distancias de seguridad](implantacion-seguridad.md)
- [Memoria: Características de los equipos auxiliares del almacenamiento](equipos-auxiliares.md)
- [Selección del depósito](../Anotaciones/seleccion_deposito.md)
- [Cálculo del volumen del depósito](../Anotaciones/calculo_volumen_deposito.md)
- [Implantación y distancias de seguridad](../Anotaciones/distancias_seguridad.md)
- [Vaporización forzada](../Anotaciones/vaporizacion_forzada.md)
