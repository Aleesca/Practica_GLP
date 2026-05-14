# Log de Sesión: Siguientes Pasos del Proyecto GLP

> **Respecto al desarrollo del proyecto de la instalación de GLP ya se han calculado el volumen necesario del depósito, el número de depósitos necesarios y las distancias mínimas de seguridad, cual sería el siguiente paso a realizar e indicame en un breve resumen lo que hay que hacer.**

Una vez que has definido el volumen de almacenamiento, el número de depósitos y has validado que el emplazamiento cumple con las distancias de seguridad reglamentarias (según la **UNE 60250**), el siguiente paso lógico es el **Dimensionado del Sistema de Vaporización y de la Red de Distribución**.

De acuerdo con el esquema de tu memoria y la normativa aplicable, aquí tienes un resumen de lo que debes realizar a continuación:

### 1. Verificación de la Vaporización (Natural vs. Forzada)
Es fundamental comprobar si los depósitos seleccionados son capaces de transformar el GLP líquido a gas al ritmo que exigen tus consumidores.
*   **Qué hacer:** Calcula la capacidad de vaporización natural de tus depósitos considerando la **temperatura exterior de diseño** (normalmente -5 ºC para esta zona) y un nivel de llenado de reserva del **20%**.
*   **Decisión técnica:** Si la vaporización natural es inferior al caudal punta demandado (en tu caso, la demanda es de **187,81 kg/h** y la natural solo llega a **131,3 kg/h**), deberás seleccionar un **vaporizador forzado** (eléctrico o de agua caliente) para cubrir el déficit.

### 2. Dimensionado de la Red de Distribución
Consiste en calcular las tuberías que llevarán el gas desde los depósitos hasta los puntos de consumo.
*   **Qué hacer:** Definir el material (acero, cobre o polietileno), el trazado y el diámetro de cada tramo. 
*   **Cálculo:** Debes verificar que la **pérdida de carga** en la red no sea excesiva, garantizando que el gas llegue con la presión mínima requerida por los quemadores de las calderas o secaderos.

### 3. Selección de la Regulación y Medida
Debes definir cómo vas a reducir la presión del depósito (que es variable) a una presión de red estable.
*   **Qué hacer:** Seleccionar los reguladores de **primera etapa** (en la salida del depósito, normalmente a 1,7 bar o 0,7 bar) y los de **segunda etapa** (antes de los equipos, a 37 mbar o 300 mbar según el quemador).

### 4. Protección contra la Corrosión (Protección Catódica)
Si tus depósitos son enterrados o tienes tuberías de acero enterradas, este paso es obligatorio por seguridad.
*   **Qué hacer:** Justificar el sistema de protección catódica (normalmente mediante **ánodos de sacrificio de magnesio**) para evitar que el terreno degrade el acero de la instalación.

---

> **he generado dos archivos @Proyecto/Anotaciones/vaporizacion_natural.md y @Proyecto/Anotaciones/vaporizacion_forzada.md donde detallo lo que me comentas en el paso 1 con esto es suficiente o que debería hacer**

Lo que has generado en los archivos de **Vaporización Natural** y **Forzada** es excelente. Está muy completo porque no solo incluye los cálculos y la justificación técnica, sino que también define los equipos específicos (VIA 150 y VPC30C) y da pautas para su representación en los planos. 

Para el apartado de vaporización, **es suficiente**. No necesitas añadir más a esos archivos.

### ¿Qué es lo siguiente que deberías hacer?

Ahora debes centrarte en la **Red de Distribución y Regulación**. Para completar esta fase del proyecto, te sugiero los siguientes pasos:

#### 1. Cálculo de la Regulación (Primer y Segundo Salto)
Debes definir los equipos que reducirán la presión desde el depósito hasta los consumidores.
*   **Criterio técnico:** El regulador debe tener una capacidad (Q_r) un **30% superior** a tu demanda máxima (187,81 kg/h).
    *   *Cálculo rápido:* 187,81 * 1,3 = **244,15 kg/h**. Debes buscar un regulador comercial (tipo RegO, Fisher o similar) que garantice este caudal.
*   **Configuración:** Lo habitual es un primer salto de regulación a la salida del depósito (de presión de depósito a **MPB 1,7 bar**) y un segundo salto en el armario de regulación del edificio o equipo (de 1,7 bar a la presión de uso, ej. **37 mbar**).

#### 2. Dimensionado de Tuberías (Cálculo de Diámetros)
Necesitas calcular los diámetros de los tramos de tubería para asegurar que la caída de presión no supere el **5%** (según UNE 60670).
*   **Fórmulas:** Se deben usar las **fórmulas de Renouard** para gas.
*   **Materiales sugeridos:** 
    *   **Acero al carbono** (estirado sin soldadura) para los tramos principales o exteriores vistos.
    *   **Polietileno (PE 80/100)** para tramos enterrados.
    *   **Cobre** para tramos interiores o de pequeño diámetro.

#### 3. Protección contra la Corrosión
Dado que has diseñado una batería de depósitos (que suelen estar enterrados o apoyados sobre bancadas), es obligatorio justificar la protección.
*   **Qué hacer:** Redacta una breve nota sobre la **protección catódica** mediante ánodos de sacrificio de magnesio y el uso de **manguitos dieléctricos** para aislar eléctricamente la red de los depósitos.

#### 4. Esquema de Principio (Diagrama de Flujo)
Este es un dibujo técnico (en CAD o esquema) que muestra:
1.  Los depósitos.
2.  El vaporizador forzado.
3.  Los reguladores.
4.  Las válvulas de corte y seguridad.
5.  Los puntos de consumo con su presión y caudal.

---

> **No se van a utilizar tramos enterrados**

Perfecto, al no haber tramos enterrados, el diseño se simplifica en unos aspectos pero se vuelve más exigente en otros (materiales y soportes). 

Aquí tienes cómo queda el planteamiento técnico para esta fase:

### 1. Materiales de la Red (Instalación Aérea)
Al ser todo aéreo, descartamos el Polietileno (PE). Los materiales permitidos son:
*   **Acero al Carbono (Principal):** Tubo de acero estirado sin soldadura (calidad **ASTM A-106 Gr B**). Es el material obligatorio para la fase líquida y el más recomendado para la fase gas a la intemperie por su resistencia mecánica.
*   **Cobre:** Solo podrías usarlo en tramos finales de pequeño diámetro o interiores, siempre que sea **cobre duro estirado** (UNE-EN 1057) y vaya debidamente protegido.

### 2. Protección contra la Corrosión y Acabado
Como los depósitos son **aéreos horizontales**, la protección ya no es mediante ánodos de magnesio (protección catódica), sino mediante **recubrimientos pasivos**:
*   **Pintura:** Los depósitos y las tuberías de acero deben llevar un tratamiento antioxidante y un acabado final. Según normativa, las tuberías de gas deben estar pintadas de **color amarillo (RAL 1021)** para su rápida identificación.
*   **Aislamiento Térmico:** Si el tramo de agua caliente que va del armario de calefacción VPC30C al depósito es largo, esas tuberías de agua deben ir aisladas (calorifugadas) para no perder potencia de vaporización.

### 3. Trazado y Soportación
*   **Dilatación:** Al estar expuestas a cambios de temperatura (sol/nieve), las tuberías de acero largas deben tener "liras de dilatación" o puntos fijos y móviles para absorber los movimientos térmicos.
*   **Soportes:** Debes definir la distancia entre soportes (abrazaderas) para evitar flechas en la tubería. Por ejemplo, para una tubería de acero de 2", los soportes suelen ir cada **3-4 metros**.

### 4. Regulación (Cálculo del 30% de Margen)
Para tu demanda de **187,81 kg/h**, el regulador principal debe ser capaz de suministrar:
$$Q_{reg} = 187,81 \times 1,3 = 244,15 \text{ kg/h}$$
