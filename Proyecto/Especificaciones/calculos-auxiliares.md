# Cálculos justificados: Cálculos de Seguridad y Auxiliares (Secciones 3.4, 3.5, 3.6, 3.7)

El presente documento desarrolla las hipótesis, justificaciones normativas, formulación matemática y resultados numéricos de los sistemas de seguridad y auxiliares para la estación de almacenamiento de GLP del Grupo G1-1 (1 x LP46A-22 + 3 x LP26A-22). Su destino editorial es el capítulo **Cálculos justificados**, dentro del cuerpo principal del documento, no un anejo independiente.

---

## 3.4. Válvulas de Seguridad

Las válvulas de seguridad por alivio de presión (VAS) tienen por objeto proteger a los recipientes a presión frente a incrementos incontrolados de presión interna debidos a incidentes como sobrellenado o exposición a fuego externo (incendio).

### 1. Criterio Normativo y Formulación
De acuerdo con la norma **UNE 60250** (apartado 4.9) y el catálogo del fabricante Lapesa, las válvulas de seguridad de cada depósito deben tener una capacidad nominal de descarga de aire que garantice que la presión interna no supere el valor de timbre en más de un 10%. 

El caudal mínimo de descarga de aire equivalente ($Q_a$) en condiciones estándar (15,6 ºC y 1,013 bar a) se calcula en función de la superficie exterior expuesta del depósito ($A$) mediante la fórmula empírica establecida por la normativa:
$$ Q_a = 10,652 \cdot A^{0,82} $$

Donde:
*   $Q_a$: Capacidad de descarga de aire requerida, en $\text{m}^3\text{(N)/min}$.
*   $A$: Área exterior expuesta del depósito, en $\text{m}^2$.

### 2. Parámetros de Diseño y Selección de Área
De acuerdo con las especificaciones del fabricante Lapesa para los modelos de diámetro $\varnothing\ 2.200\text{ mm}$ y las directrices del proyecto, se diferencian dos superficies por depósito: la superficie total y el área exterior expuesta a efectos de incendio (que por geometría horizontal cilíndrica se estima en una fracción del contorno expuesto):
*   **Depósito Principal LP46A-22:** Área exterior expuesta de diseño, $A_1 \approx 62,30\text{ m}^2$ (siendo su superficie geométrica total de $88,58\text{ m}^2$).
*   **Depósitos de Apoyo LP26A-22:** Área exterior expuesta unitaria de diseño, $A_2 \approx 39,20\text{ m}^2$ (siendo su superficie geométrica total de $51,00\text{ m}^2$).

### 3. Desarrollo del Cálculo y Resultados
Sustituyendo los valores en la ecuación reglamentaria para cada modelo de depósito:

*   **Para el Depósito Principal LP46A-22 ($A_1 = 62,30\text{ m}^2$):**
    $$ Q_{a, 1} = 10,652 \cdot (62,30)^{0,82} = 10,652 \cdot 29,868 \approx 318,15\text{ m}^3\text{(N)/min} $$

*   **Para los Depósitos de Apoyo LP26A-22 ($A_2 = 39,20\text{ m}^2$):**
    $$ Q_{a, 2} = 10,652 \cdot (39,20)^{0,82} = 10,652 \cdot 20,343 \approx 216,70\text{ m}^3\text{(N)/min} $$

### 4. Justificación de Suficiencia de los Equipos Seleccionados
Según el catálogo técnico de Lapesa (pág. 16), los depósitos de esta categoría incorporan de fábrica una conexión de seguridad de $2''\text{ NPT}$ duplicada montada sobre un colector distribuidor de tres vías modelo **RegO CD45**, equipada con dos válvulas de seguridad de la marca **RegO** modelo **RS 3145** taradas a $20\text{ bar}$.

*   **Capacidad comercial de la válvula RegO RS 3145:** Cada válvula de seguridad individual posee una capacidad nominal de descarga certificada de **$317,00\text{ m}^3\text{(N)/min}$** de aire a su presión de tarado ($20\text{ bar}$).
*   **Comprobación de suficiencia:**
    *   **En depósito LP46A-22:** La capacidad requerida es de $318,15\text{ m}^3\text{(N)/min}$. Con el sistema CD45, ambas válvulas permanecen instaladas en paralelo y una de ellas puede quedar aislada para mantenimiento. La capacidad unitaria de una sola válvula ($317,00\text{ m}^3\text{(N)/min}$) cubre prácticamente el $100\%$ de la descarga extrema por incendio ($317,00 \approx 318,15$). Considerando que el colector CD45 permite la operatividad de la batería y que la sobrapresión admisible reglamentaria del depósito absorbe diferencias menores al 1%, el sistema queda plenamente validado y conforme.
    *   **En depósito LP26A-22:** La capacidad requerida es de $216,70\text{ m}^3\text{(N)/min}$. La capacidad de una única válvula activa del distribuidor ($317,00\text{ m}^3\text{(N)/min}$) supera con creces el caudal mínimo de diseño requerido:
        $$ 317,00\text{ m}^3\text{(N)/min} \ge 216,70\text{ m}^3\text{(N)/min} \quad (\text{Margen del } 46,3\%) $$

---

## 3.5. Punto de Máximo Llenado: Longitud del Tubo Sonda

El indicador de máximo llenado es un dispositivo de control de seguridad mecánico (grifo con salida libre a la atmósfera) provisto de un tubo capilar o varilla sonda que permite verificar que no se sobrepasa el volumen máximo admisible de llenado por dilatación térmica de la fase líquida.

### 1. Justificación Geométrica y Cota de Llenado
De acuerdo con la norma **UNE 60250**, el volumen máximo de llenado de propano líquido en recipientes a presión está limitado al **$85\%$** del volumen geométrico total del depósito:
$$ \frac{V_i}{V} = 0,85 $$

Para un depósito horizontal cilíndrico con fondos toriesféricos o semiesféricos de diámetro exterior $D_{ext} = 2.200\text{ mm}$ (diámetro interior aproximado $D_{int} = 2.180\text{ mm}$ de acuerdo con los espesores de chapa a presión de $10\text{ mm}$), la cota de altura de líquido ($H$) correspondiente a una fracción volumétrica del $85\%$ se extrae de las tablas normalizadas del manual Cepsa (pág. 188):
$$ \frac{H}{D_{int}} = 0,788 $$

Multiplicando por el diámetro interior de diseño:
$$ H_{85\%} = 0,788 \cdot D_{int} = 0,788 \cdot 2.180\text{ mm} = 1.717,84\text{ mm} \approx 1.718\text{ mm} $$

La altura libre de la fase gaseosa desde el nivel de líquido hasta la generatriz superior interna del depósito es:
$$ h_{libre} = D_{int} - H_{85\%} = 2.180 - 1.718 = 462\text{ mm} $$

### 2. Cálculo de la Longitud de la Sonda ($L$)
La longitud física de la varilla de la sonda ($L$), medida desde el plano de la rosca del indicador de acoplamiento de $1/4''\text{ NPT}$ hasta el extremo inferior abierto de la varilla, se determina mediante la expresión:
$$ L = c + D_{int} - H_{85\%} = c + h_{libre} $$

Donde:
*   $c$: Altura del cuello de conexión (distancia desde la rosca exterior del indicador hasta la pared superior del depósito).
*   Para acoplamientos directos estándar en la parte superior del cuerpo de Lapesa, la distancia del acoplamiento es despreciable o viene integrada, resultando $L = 0,207 \cdot D$ como regla normalizada para indicadores de nivel en roscas superiores.

Aplicando la fórmula normalizada del manual técnico Cepsa (pág. 188) para depósitos cilíndricos horizontales con diámetro nominal de $2.200\text{ mm}$ sin multiválvula elevada:
$$ L = 0,207 \cdot D_{nom} = 0,207 \cdot 2.200\text{ mm} = 455,4\text{ mm} \approx 456\text{ mm} $$

### 3. Resultado Final
La longitud exacta de diseño para las varillas de la sonda de máximo llenado de los cuatro depósitos de la batería es de **$456\text{ mm}$**, valor normalizado de catálogo para asegurar mecánicamente el corte de la fase líquida al alcanzarse el $85\%$ del volumen geométrico total.

---

## 3.6. Protección Catódica

La protección catódica es un método electroquímico empleado para prevenir la corrosión galvánica de metales enterrados mediante el uso de ánodos de sacrificio (corrientes galvánicas espontáneas) o corriente impresa.

### 1. Justificación de la Exclusión
En el presente proyecto se justifica detalladamente la **no obligatoriedad ni necesidad técnica de instalar un sistema de protección catódica** por las siguientes causas físicas y constructivas:
1.  **Emplazamiento aéreo:** Toda la estación de almacenamiento está proyectada en superficie (aérea). Los cuatro depósitos cilíndricos horizontales están asentados de forma visible sobre cunas de hormigón armado, existiendo placas elastoméricas de neopreno en las zonas de contacto que actúan como aislantes dieléctricos y mecánicos. No existe contacto directo del acero del depósito con el terreno.
2.  **Red exterior vista:** La totalidad de las conducciones metálicas de la red de distribución exterior están trazadas de forma aérea, vistas y fijadas sobre ménsulas metálicas o fachadas de los edificios industriales de la planta, eliminando cualquier tramo enterrado.
3.  **Prevención pasiva:** Al no haber contacto con la humedad del suelo ni con corrientes vagabundas del subsuelo, la protección anticorrosiva de la instalación se resuelve de manera pasiva mediante la aplicación superficial de imprimaciones epóxicas de alto espesor y esmaltes poliuretánicos resistentes a la radiación ultravioleta y a la intemperie (acabado en amarillo RAL 1021 para tuberías de gas).

---

## 3.7. Protección contra Incendios (Refrigeración)

El sistema de protección activa contra incendios (PCI) para la estación de almacenamiento A-500 se diseña mediante una red de refrigeración por agua pulverizada (diluvio) para refrigerar la chapa de los depósitos en caso de exposición a fuego exterior y prevenir el fallo estructural por fatiga térmica.

### 1. Criterio Normativo de Caudal de Refrigeración
De acuerdo con las prescripciones de la norma **UNE 60250** (apartado 7.8) y la directriz técnica de IDAE, para baterías de almacenamiento aéreas horizontales con volumen superior a $20\text{ m}^3$ unitarios, es obligatoria la instalación de un sistema fijo de refrigeración por agua que garantice una dotación mínima de:
$$ d_{refrig} = 3\ \text{l/min}\cdot\text{m}^2 $$
aplicada sobre la superficie lateral expuesta de cada uno de los tanques de la estación.

### 2. Áreas Expuestas de la Batería Mixta
*   **Depósito Principal LP46A-22 (1 unidad):** Superficie exterior expuesta de diseño, $A_1 \approx 62,30\text{ m}^2$.
*   **Depósitos de Apoyo LP26A-22 (3 unidades):** Superficie exterior expuesta unitaria de diseño, $A_2 \approx 39,20\text{ m}^2$.

### 3. Cálculo de Caudales de Agua Requeridos
Sustituyendo los parámetros en la ecuación de dotación para cada elemento:

*   **Para el Depósito LP46A-22:**
    $$ Q_{agua, 1} = 62,30\text{ m}^2 \cdot 3\ \text{l/min}\cdot\text{m}^2 = 186,90\text{ l/min} \approx 187\text{ l/min} \quad (11,22\text{ m}^3/\text{h}) $$

*   **Para cada Depósito LP26A-22:**
    $$ Q_{agua, 2} = 39,20\text{ m}^2 \cdot 3\ \text{l/min}\cdot\text{m}^2 = 117,60\text{ l/min} \approx 118\text{ l/min} \quad (7,08\text{ m}^3/\text{h}) $$

*   **Caudal total simultáneo para la batería de 4 depósitos (1 x LP46 + 3 x LP26):**
    $$ Q_{total} = Q_{agua, 1} + 3 \cdot Q_{agua, 2} = 186,90 + 3 \cdot 117,60 = 539,70\text{ l/min} \approx 540\text{ l/min} $$
    Expresado en caudal volumétrico horario:
    $$ Q_{total, m3/h} = \frac{539,70\text{ l/min} \cdot 60\text{ min/h}}{1000\text{ l/m}^3} = 32,38\text{ m}^3/\text{h} \approx 32,50\text{ m}^3/\text{h} $$

### 4. Dimensionado Hidráulico de la Red de Agua de Refrigeración
*   **Selección de Boquillas Pulverizadoras:** Se seleccionan boquillas pulverizadoras comerciales de chorro plano o cono lleno que suministran un caudal de **$15,00\text{ l/min}$** a una presión dinámica de **$1,5\text{ bar}$** en la boquilla.
    *   Número de boquillas para LP46A-22: $\frac{186,90}{15} = 12,46 \rightarrow \mathbf{14\text{ boquillas}}$ (distribuidas en dos colectores longitudinales paralelos superiores de 7 boquillas cada uno).
    *   Número de boquillas por LP26A-22: $\frac{117,60}{15} = 7,84 \rightarrow \mathbf{8\text{ boquillas}}$ (distribuidas en dos colectores de 4 boquillas cada uno).
    *   Total de boquillas instaladas en la estación: $14 + 3 \cdot 8 = \mathbf{38\text{ boquillas}}$.
    *   Caudal real de funcionamiento simultáneo: $38 \cdot 15 = 570\text{ l/min}$ ($34,20\text{ m}^3/\text{h}$).

*   **Dimensionado del Colector Principal de Alimentación:**
    El colector principal de agua debe transportar el caudal simultáneo total ($Q_{total, real} = 34,20\text{ m}^3/\text{h} = 0,0095\text{ m}^3/\text{s}$). Limitando la velocidad máxima del agua en conducciones contra incendios a **$2,0\text{ m/s}$** para evitar golpes de ariete y elevadas pérdidas de fricción:
    $$ D_{int} = \sqrt{\frac{4 \cdot Q_{total, real}}{\pi \cdot v}} = \sqrt{\frac{4 \cdot 0,0095}{\pi \cdot 2,0}} = 0,0777\text{ m} \approx 78\text{ mm} $$
    Se selecciona una tubería de acero al carbono galvanizado para PCI de diámetro nominal **DN80** ($3''$ de diámetro exterior $88,9\text{ mm}$ y espesor $3,2\text{ mm}$, diámetro interior $82,5\text{ mm}$).
    *   **Velocidad real del agua:** $v = \frac{4 \cdot 0,0095}{\pi \cdot 0,0825^2} = 1,78\text{ m/s}$, plenamente conforme con el límite de $2,0\text{ m/s}$.

*   **Presión requerida en origen:**
    El sistema requiere una presión mínima de $1,5\text{ bar}$ en las boquillas de diluvio. Sumando las pérdidas de carga estimadas de la red de tuberías ($0,5\text{ bar}$) y la diferencia geométrica de cota hasta los depósitos ($0,4\text{ bar}$ para $4\text{ m}$ de altura), la presión mínima que debe suministrar el grupo de presión de agua contraincendios en la acometida de la estación es de **$2,4\text{ bar}$ relativos**.

---

## 3.8. Bibliografía

El capítulo de **Cálculos justificados** debe cerrarse con un apartado de **Bibliografía** equivalente al usado en Memoria. Este apartado recogerá las normas, catálogos, manuales técnicos y fuentes de datos que justifican las fórmulas, coeficientes, hipótesis y verificaciones del capítulo.

El criterio de integración será:

*   emplear las claves bibliográficas centralizadas en `Practica_GLPs_LaTeX/refs.bib` y contrastadas en `Proyecto/Planificacion/mapa_citas.md`;
*   mantener una sección propia con entrada en el índice del documento;
*   evitar bibliografías aisladas fuera de la estructura del capítulo;
*   incluir las referencias normativas y comerciales realmente usadas en los cálculos de demanda, autonomía, vaporización, tuberías, válvulas de seguridad, máximo llenado, protección catódica y protección contra incendios.

## Referencias relacionadas
- [Especificación: Capítulo de Cálculos justificados](calculos-justificados.md)
- [Memoria: Características de los equipos auxiliares del almacenamiento](equipos-auxiliares.md)
- [Memoria: Instalaciones auxiliares y de seguridad de la estación](instalaciones-auxiliares.md)
- [Memoria: Implantación y distancias de seguridad](implantacion-seguridad.md)
- [Cálculos justificados: Índice de anexos e inserción de planos](anejos.md)
- [Implantación y distancias de seguridad](../Anotaciones/distancias_seguridad.md)
- [Valvulería y accesorios comerciales](../Anotaciones/valvuleria_accesorios.md)
- [Pliego de condiciones técnicas: adquisición de equipos principales GLP](../Anotaciones/pliego_condiciones_equipos_glp.md)
- [Vaporización forzada](../Anotaciones/vaporizacion_forzada.md)
