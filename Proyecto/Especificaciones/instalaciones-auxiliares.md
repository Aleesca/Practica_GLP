# Memoria: Instalaciones Auxiliares y de Seguridad de la Estación

## 1. Instalación Eléctrica y Clasificación de Áreas (ATEX)
Debido a la presencia de propano comercial, gas inflamable de categoría 1 que en mezclas con el aire puede formar atmósferas explosivas, el diseño eléctrico de la estación de almacenamiento cumple estrictamente con el **Real Decreto 144/2016** (Directiva ATEX 2014/34/UE) y la instrucción técnica **ITC-BT-29** del Reglamento Electrotécnico de Baja Tensión (REBT):

*   **Clasificación de Zonas ATEX:**
    *   **Zona 1 (Peligro Ocasional):** Se define un volumen esférico de $1,5\text{ metros}$ de radio alrededor de las válvulas de seguridad, boca de carga y purgas de los depósitos. En este espacio, todos los equipos eléctricos instalados (sensores de nivel, presostatos) contarán con certificación de seguridad intrínseca `Ex i` o envolventes antideflagrantes `Ex d` para el Grupo IIA y clase de temperatura T3.
    *   **Zona 2 (Peligro Poco Probable o Corto Duración):** Se define un volumen cilíndrico de $3,0\text{ metros}$ de radio alrededor de los depósitos de almacenamiento y del colector de regulación. En esta zona se restringe el uso de motores o interruptores normales, exigiéndose equipos de seguridad aumentada `Ex e`.
*   **Acometida Eléctrica y Cuadro de Control:**
    La acometida eléctrica para alimentar la bomba del circuito de agua caliente, el encendido electrónico y el cuadro de control del armario de calefacción **VPC30C** se realiza mediante conductores de cobre con aislamiento de tensión nominal de $0,6/1\text{ kV}$ tipo **RV-K**, entubados en conductos metálicos rígidos de acero galvanizado conectados a tierra. El cuadro eléctrico general de maniobra de la estación se ubicará en zona segura (fuera de la Zona 2), en el interior de la nave industrial contigua.

## 2. Instalaciones de Protección contra Incendios
La estación de almacenamiento Tipo A-500 cuenta con sistemas de protección activa y pasiva diseñados según la norma UNE 60250 y el CTE DB-SI:

*   **Extintores Portátiles:**
    En las proximidades del recinto de almacenamiento, a una distancia no superior a 15 metros de las bocas de carga y depósitos, se dispondrán **dos extintores portátiles de polvo químico seco (polvo ABC)** de eficacia mínima **21A-113B** y una carga de $9\text{ kg}$. Estarán protegidos de la intemperie mediante armarios de plástico de color rojo y serán fácilmente accesibles desde las puertas de salida peatonal.
*   **Red de Rociadores de Agua Fría para Refrigeración (PCI):**
    Para proteger la estructura metálica de los depósitos del calor radiante ante un posible incendio exterior o en un depósito adyacente, se diseña un sistema de refrigeración por agua de pulverización:
    *   **Caudal de Diseño:** Según la norma UNE 60250, el sistema debe ser capaz de suministrar un caudal mínimo de pulverización de **$3\text{ l/min}\cdot\text{m}^2$** sobre la totalidad de la superficie exterior expuesta de los depósitos.
    *   **Rociadores (Pulverizadores):** Se instala una línea aérea de tuberías de acero galvanizado con boquillas pulverizadoras distribuidas longitudinalmente sobre la parte superior de cada uno de los cuatro depósitos, de forma que el agua forme una película protectora continua que cubra toda la chapa de los recipientes. El sistema se alimentará de la red de protección contra incendios de la planta mediante válvula de accionamiento manual exterior de fácil acceso y protegida del fuego.

## 3. Instalación de Puesta a Tierra y Conexiones Equipotenciales
Para evitar riesgos de ignición por acumulación de electricidad estática generada por la fricción del propano líquido durante las descargas o flujos rápidos, así como para la protección eléctrica del personal frente a derivaciones accidentales:

*   **Red de Tierras de la Estación:**
    Se proyecta un anillo perimetral subterráneo formado por un conductor de cobre desnudo de **$35\text{ mm}^2$** de sección, enterrado a una profundidad mínima de $0,8\text{ metros}$ en el contorno del recinto de almacenamiento. A este conductor se conectarán mecánicamente **cuatro picas de puesta a tierra** de acero cobreado de $2,0\text{ metros}$ de longitud introducidas verticalmente en el suelo en las esquinas de la estación.
*   **Conexiones de Equipotencialidad:**
    Se conectarán directamente a este anillo de tierras:
    *   Las cunas metálicas de soporte de los cuatro depósitos mediante pletinas de cobre.
    *   La brida del serpentín VIA 150 y la carcasa metálica del armario VPC30C.
    *   Las tuberías generales de distribución de gas de cobre a la salida de la estación y en la entrada de los consumidores, intercalando **puentes de cobre flexibles** para asegurar la continuidad eléctrica en las uniones roscadas o bridas.
*   **Resistencia Máxima de Tierra:**
    La resistencia de la red de tierras de la estación se verificará mediante telurómetro en fase de puesta en servicio, garantizando un valor de resistencia óhmica inferior a **$20\ \Omega$** en las peores condiciones de sequedad del terreno.
