# Especificación: Red de Distribución (Sección 2.2.5)

## Propósito
Describir y justificar la arquitectura geométrica y el dimensionamiento hidráulico de la red de tuberías aéreas de propano comercial que alimenta a los 6 consumidores del Grupo G1-1.

## Contenido obligatorio
- **Descripción de la Arquitectura de Red:**
  - Definir la topología de la red aérea (trazado visto en fachadas y soportes elevados).
  - Justificar el descarte de canalización enterrada (evitando obra en zanjas, tuberías de polietileno, problemas de inundaciones y la instalación de protección catódica).
  - Especificar el material de conducción: cobre en barra estirado sin soldadura (UNE-EN 1057) para todos los tramos.
- **Criterios e Ecuaciones de Dimensionamiento Hidráulico:**
  - Desarrollar la fórmula de Renouard para Media Presión B ($0,05\text{ bar} < P < 5\text{ bar}$):
    $$ P_A^2 - P_B^2 = 51,5 \cdot d_c \cdot L_c \cdot \frac{Q^{1,82}}{D^{4,82}} $$
    donde:
    - $P_A, P_B$: presiones absolutas inicial y final en el tramo [bar a] ($P_{\text{relativa}} + 1,01325 \text{ bar}$).
    - $d_c$: densidad corregida del propano ($d_c = 1,16$).
    - $Q$: caudal volumétrico de diseño [$m^3/h$].
    - $D$: diámetro interior de la tubería [mm].
    - $L_c$: longitud de cálculo del tramo en metros. Para MPB se aplica la longitud mayorada por singularidades de accesorios: $L_c = 1,05 \cdot L_{\text{real}}$.
  - Ecuación de velocidad de gas para consistencia dimensional:
    $$ v = 378,04 \cdot \frac{Q}{P_{\text{media\_abs}} \cdot D^2} $$
    donde $P_{\text{media\_abs}}$ es la presión absoluta media en el tramo.
- **Resumen de Resultados por Tramo:**
  - Detallar los resultados de diseño de la red:
    - Presión de entrada inicial a la salida de los depósitos: $1,70 \text{ bar relativos}$ ($2,713 \text{ bar absolutos}$).
    - Pérdida de carga máxima admisible del $5\%$ ($0,085 \text{ bar}$), exigiendo presión mínima en consumidores de $1,615 \text{ bar relativos}$.
    - Límite máximo de velocidad de gas en tramos generales: $10 \text{ m/s}$.
    - Diámetros nominales de cobre comercial propuestos por tramo ($\phi 54$, $\phi 42$, $\phi 35$, $\phi 28$, $\phi 22$) y sus espesores.

## Estilo de redacción
Tono de ingeniería formal y descriptivo. Uso de expresiones matemáticas LaTeX. Longitud orientativa: 2 páginas.

## Figuras, tablas y resultados
- **Figuras/Planos a integrar:**
  - [plano_Esquema_instalacion.pdf](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/plano_Esquema_instalacion.pdf): Plano y esquema de principio (P&ID) de la red de tuberías aéreas de propano comercial y acometidas de consumo de la instalación.
- **Tablas obligatorias:**
  - **Tabla resumen de tramos de la red:** Código del tramo (ej. Tramo A-B, B-C, etc.), longitud real, longitud de cálculo, caudal, diámetro exterior/interior adoptado, velocidad de flujo y presión final del tramo.
- **Resultado final:** Presión final del consumidor más desfavorable ($1,623 \text{ bar relativos}$, cumpliendo con el límite mínimo de $1,615 \text{ bar}$).

## Conexiones
- **Alcance:** Requisito 5 (Cálculo de la conducción de distribución: diámetros, presiones y pérdidas de carga) y Requisito 6 (Esquema de distribución).
- **Anotaciones:** [dimensionado_tuberias_glp.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/dimensionado_tuberias_glp.md) (Cálculo), [trazado_red.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/trazado_red.md) (Decisión), [metodologia-longitud-calculo.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/metodologia-longitud-calculo.md) (Cálculo).
- **Planos:** Esquema de instalación general (`plano_Esquema_instalacion.pdf`).

## Criterios de aceptación
- [ ] Se describe formalmente el trazado aéreo de cobre UNE-EN 1057.
- [ ] Se detalla la ecuación de pérdidas de carga de Renouard MPB y de velocidad.
- [ ] La presión final en el punto más desfavorable calculada supera los $1,615 \text{ bar}$.
- [ ] La velocidad del fluido en todas las conducciones de distribución es inferior a $10 \text{ m/s}$.
- [ ] Se incluye la longitud equivalente con el factor de mayoración de $1,05$.
