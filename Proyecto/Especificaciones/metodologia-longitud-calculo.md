# Especificación: Metodología de Longitud y Cálculo Hidráulico (Sección de Cálculo Auxiliar Transversal)

## Propósito
Describir y justificar las bases metodológicas, algoritmos y ecuaciones matemáticas empleados para calcular la longitud de cálculo ($L_c$) de las tuberías y realizar el dimensionamiento hidráulico de los diámetros comerciales mediante las fórmulas de Renouard.

## Contenido obligatorio
- **Criterios y Fórmulas Base de Pérdida de Carga:**
  - Ecuación de Renouard para Media Presión B ($0,05\text{ bar} < P < 5\text{ bar}$):
    $$ P_A^2 - P_B^2 = 51,5 \cdot d_c \cdot L_c \cdot \frac{Q^{1,82}}{D^{4,82}} $$
  - Límite de validez del modelo hidráulico:
    $$ \frac{Q}{D} < 150 $$
  - Densidad corregida del propano ($d_c = 1,16$).
- **Métodos para Obtención de la Longitud de Cálculo ($L_c$):**
  - **Método 1: Coeficiente de Mayoración Global (Simplificado):**
    - Aplicación del factor de incremento del $5\%$ para Media Presión B: $L_c = 1,05 \cdot L_{\text{real}}$. Justificar su idoneidad en anteproyectos.
  - **Método 2: Longitudes Equivalentes por Accesorio (Iterativo):**
    - Expresar la longitud de cálculo como:
      $$ L_c = L_{\text{real}} + \sum L_{eq}(D) $$
    - Tabular los coeficientes de fricción equivalente en función del diámetro ($L_{eq}/D$) para codos de $90^\circ$ ($30\cdot D$), codos de $45^\circ$ ($15\cdot D$), ramales de te ($60\cdot D$), paso en te ($20\cdot D$) y llaves de corte ($10\cdot D$).
  - **Algoritmo de Selección de Diámetro:**
    - Explicar el bucle iterativo (Selección de diámetro inicial $\rightarrow$ cálculo de $L_c(D)$ $\rightarrow$ cálculo de pérdidas de carga $\rightarrow$ verificación frente al límite del $5\%$ $\rightarrow$ comprobación de velocidad de gas $< 10 \text{ m/s}$ $\rightarrow$ incremento de diámetro si falla).
- **Justificación de Aplicación:**
  - Indicar que para el proyecto G1-1 se adopta el Método 1 (factor $1,05$) como base para la memoria de tramos general de distribución, y el Método 2 se reserva para verificaciones detalladas en el colector de la estación.

## Estilo de redacción
Estilo técnico, formal y riguroso de ingeniería. Uso claro de ecuaciones en formato LaTeX y diagramas lógicos (código/algoritmos). Longitud orientativa: 2 a 3 páginas.

## Figuras, tablas y resultados
- **Tabla de coeficientes adimensionales de pérdida singular ($L_{eq}/D$):** Para codos, tes, reducciones y válvulas.
- **Diagrama de flujo del algoritmo:** Bucle iterativo de cálculo de diámetros.

## Conexiones
- **Alcance:** Requisito 5 (Cálculo de la conducción de distribución).
- **Anotaciones:** [dimensionado_tuberias_glp.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/dimensionado_tuberias_glp.md) (Cálculo), [trazado_red.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/trazado_red.md) (Decisión).

## Criterios de aceptación
- [ ] Se detallan las fórmulas de Renouard MPB y límites de validez de Renouard.
- [ ] Se expone el factor de mayoración global del $5\%$ ($1,05$) para MPB.
- [ ] Se define la tabla de longitudes equivalentes de accesorios.
- [ ] Se describe el algoritmo de cálculo iterativo de diámetros mediante pseudocódigo o diagrama de flujo.
