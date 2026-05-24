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
- **Diagrama del Método Iterativo Elegido:**
  - Integrar en la Memoria un diagrama de flujo equivalente al diagrama Mermaid definido para el método de dimensionado iterativo.
  - El diagrama no debe incorporarse como bloque Mermaid literal en LaTeX. Debe adaptarse a un formato compilable en LaTeX, preferentemente mediante `tikzpicture` con nodos y flechas, o como figura vectorial/PDF generada a partir del Mermaid y referenciada desde LaTeX.
  - La secuencia mínima del diagrama debe ser:
    $$ \text{Datos del tramo} \rightarrow \text{Diámetro inicial} \rightarrow L_c(D) \rightarrow \Delta P \rightarrow \text{Verificación de presión} \rightarrow \text{Verificación de velocidad} \rightarrow \text{Diámetro aceptado o incremento de diámetro} $$
  - Debe quedar ubicado en la Memoria dentro del apartado de red de distribución/canalizaciones, como apoyo metodológico al dimensionado hidráulico, con título, numeración de figura, pie explicativo y referencia cruzada desde el texto.
- **Justificación de Aplicación:**
  - Indicar que para el proyecto G1-1 se adopta el Método 2 (longitudes equivalentes por accesorio e iteración de diámetro) como método de dimensionado elegido para justificar la red de distribución. El Método 1 (factor $1,05$) puede citarse únicamente como contraste simplificado o comprobación preliminar, pero no como criterio final de dimensionado.

## Estilo de redacción
Estilo técnico, formal y riguroso de ingeniería. Uso claro de ecuaciones en formato LaTeX y diagramas lógicos (código/algoritmos). Longitud orientativa: 2 a 3 páginas.

## Figuras, tablas y resultados
- **Tabla de coeficientes adimensionales de pérdida singular ($L_{eq}/D$):** Para codos, tes, reducciones y válvulas.
- **Diagrama de flujo del algoritmo:** Bucle iterativo de cálculo de diámetros, adaptado desde Mermaid a un recurso LaTeX compilable (`tikzpicture` o figura vectorial/PDF), integrado en Memoria con caption y label.
- **Tabla de resultados del dimensionado de tuberías:** Debe consolidar el cálculo tramo a tramo en una hoja aislada **A4 horizontal**, dentro del capítulo **Cálculos justificados**, conservando el encabezado y pie de página del documento. No debe tratarse como anejo independiente de cálculos.

## Conexiones
- **Alcance:** Requisito 5 (Cálculo de la conducción de distribución).
- **Anotaciones:** [Dimensionado de tuberías GLP](../Anotaciones/dimensionado_tuberias_glp.md) (cálculo), [Trazado de red](../Anotaciones/trazado_red.md) (decisión).

## Referencias relacionadas
- [Memoria: Red de distribución y regulación](red-distribucion.md)
- [Especificación: Capítulo de Cálculos justificados](calculos-justificados.md)
- [Especificación: Presupuesto y mediciones](presupuesto.md)
- [Dimensionado de tuberías GLP](../Anotaciones/dimensionado_tuberias_glp.md)
- [Trazado de red](../Anotaciones/trazado_red.md)
- [Valvulería y accesorios comerciales](../Anotaciones/valvuleria_accesorios.md)

## Criterios de aceptación
- [ ] Se detallan las fórmulas de Renouard MPB y límites de validez de Renouard.
- [ ] Se expone el factor de mayoración global del $5\%$ ($1,05$) solo como método simplificado de contraste.
- [ ] Se define la tabla de longitudes equivalentes de accesorios.
- [ ] Se describe el algoritmo de cálculo iterativo de diámetros mediante pseudocódigo o diagrama de flujo.
- [ ] La Memoria integra el diagrama Mermaid del método iterativo elegido adaptado a LaTeX, con título, pie de figura y referencia cruzada.
- [ ] La tabla final de dimensionado de tuberías queda prevista como hoja A4 horizontal aislada con encabezado y pie de página del documento.
