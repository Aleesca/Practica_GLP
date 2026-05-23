# Memoria: Red de Distribución y Regulación

## 1. Arquitectura y Trazado de la Red de Canalización
La red de distribución transporta el propano en fase gas desde el colector común de la estación de almacenamiento hasta los puntos de consumo de la planta industrial. 

Se adopta un diseño de **canalización enteramente aérea, vista y fijada en fachada y soportes estructurales metálicos**, discurriendo en el exterior del edificio industrial hasta las derivaciones individuales. 
*   **Justificación del material:** Se selecciona **tubería de cobre desoxidado al fósforo en barra (UNE-EN 1057)**. Este material ofrece una excelente resistencia a la corrosión atmosférica exterior, una baja rugosidad interna que minimiza las pérdidas de carga por fricción y una gran facilidad de ejecución de las uniones soldadas mediante soldadura fuerte (punto de fusión $> 450\text{ ºC}$ con aleaciones de plata/cobre).
*   **Espesores de tubería:** Se adopta un espesor de pared de $\ge 1,0\text{ mm}$ para las tuberías de distribución general, aumentándose a un mínimo de $\ge 1,5\text{ mm}$ en las liras de conexión flexible y derivaciones en la zona de salida de los depósitos para soportar mayores esfuerzos mecánicos de vibración.
*   **Señalización y Acabado:** Toda la tubería exterior de gas de acero y cobre estará pintada de **color amarillo (RAL 1021)** de acuerdo con las especificaciones de seguridad industrial para la identificación inmediata del fluido inflamable transportado.
*   **Dilatación y Soportación:** Debido a la gran longitud de los tramos exteriores expuestos a oscilaciones de temperatura estacional (sol y nieve de León), se dispondrán **liras de dilatación en U** en los tramos rectos de más de 15 metros de longitud y apoyos deslizantes en combinación con soportes rígidos para absorber las tensiones de dilatación térmica. La separación entre abrazaderas de soporte se dimensiona a un máximo de **3,0 metros** para evitar flechas o pandeos.

## 2. Sistema de Regulación de Presión (Doble Salto)
La presión del gas propano en el interior de los depósitos varía sustancialmente en función de la temperatura del líquido ($2\text{ bar}$ a $-5\text{ ºC}$, hasta más de $8\text{ bar}$ en verano). Para garantizar un suministro estable y seguro a los quemadores de los hornos y calderas, se diseña un sistema de regulación de **doble salto**:

1.  **Regulación de Primer Salto (Media Presión B - MPB):**
    *   **Ubicación:** Centralizada en la salida del colector común de los depósitos en la estación de almacenamiento.
    *   **Función:** Reduce la presión variable de fase gas del almacenamiento a una presión de red exterior de **$1,7\text{ bar relativos}$**.
    *   **Equipo:** Se seleccionan reguladores comerciales de alta capacidad con margen de seguridad del $30\%$ sobre la demanda de cálculo máxima ($187,81\text{ kg/h} \times 1,3 = 244,15\text{ kg/h}$), adoptándose el modelo **RegO 1588V** o regulador **Clesse APS** tarado a $1,7\text{ bar}$, el cual incorpora válvula de seguridad por sobrepresión (de escape conducido) y válvula de seguridad por defecto de presión (cierre rápido de seguridad UPS).
2.  **Regulación de Segundo Salto (Baja Presión / Media Presión A - MPA):**
    *   **Ubicación:** Descentralizada, ubicada en armarios metálicos de regulación individuales adosados a la entrada de cada uno de los seis consumidores.
    *   **Función:** Reduce la presión de la red de distribución general ($1,7\text{ bar}$) a la presión nominal que exigen las especificaciones técnicas de los quemadores de cada máquina: **$37\text{ mbar}$** (o $300\text{ mbar}$ según modelo específico del horno).
    *   **Equipo:** Reguladores de segunda etapa de membrana con válvula de seguridad de mínima presión de rearme manual, que bloquean el paso de gas si la presión en la red cae por debajo de la presión mínima admisible del quemador.

## 3. Dispositivos de Medida
Para el control de consumos de la planta fabril y balances de eficiencia térmica de los procesos, se dispondrán **contadores de gas de turbina o de pistones rotativos** con compensación térmica integrados en el interior de los armarios de regulación secundarios de cada consumidor, aguas abajo del segundo salto de regulación y protegidos contra intemperie.
