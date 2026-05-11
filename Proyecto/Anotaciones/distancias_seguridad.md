# Implantación y Distancias de Seguridad

## 1. Objeto y alcance
El objeto de este apartado es la definición, justificación y verificación técnica de la implantación de la estación de almacenamiento de GLP para el Grupo G1-1. Se pretende asegurar que la disposición de los equipos y las distancias de seguridad respecto a los elementos internos y externos del entorno cumplen estrictamente con la normativa de seguridad industrial vigente, minimizando los riesgos operacionales y de incendio.

## 2. Normativa y criterio de aplicación
La justificación técnica de la instalación se fundamenta en el marco normativo español para el almacenamiento de GLP en depósitos fijos:
- **Real Decreto 919/2006**: Reglamento técnico de distribución y utilización de combustibles gaseosos e Instrucción Técnica Complementaria **ITC-ICG 03**.
- **Norma UNE 60250:2008**: "Instalaciones de almacenamiento de GLP en depósitos fijos para su consumo en instalaciones receptoras".

De acuerdo con el volumen total de almacenamiento previsto (125.100 L), la instalación se clasifica bajo la categoría **A-500** (volumen total $V$ tal que $120\text{ m}^3 < V \le 500\text{ m}^3$), según el Anexo B de la norma UNE 60250:2008.

## 3. Configuración de almacenamiento adoptada
Basándose en el cálculo de autonomía de 30 días ([autonomia_30_dias.md](autonomia_30_dias.md)), se ha proyectado una batería mixta de 4 depósitos aéreos con una **capacidad total instalada de 125,10 m³**.

**Clasificación de la instalación:** Según la capacidad total (120 < V ≤ 500 m³), la planta se clasifica como **Categoría A-500**.

Para el detalle de la composición de la batería (modelos Lapesa LP46A-22 y LP26A-22) y la lógica de selección, consúltese [seleccion_deposito.md](seleccion_deposito.md).

## 4. Datos geométricos relevantes de los depósitos
Para la verificación de la implantación física, se consideran las siguientes dimensiones exteriores (según catálogo):
- **Depósitos LP46A-22:** Diámetro $D = 2.200 \text{ mm}$, Longitud $L = 12.820 \text{ mm}$.
- **Depósitos LP26A-22:** Diámetro $D = 2.200 \text{ mm}$, Longitud $L = 7.480 \text{ mm}$.

integrar imagenes `Practica_GLPs_LaTeX\Figuras\deposito_seleccionado.png`
`Practica_GLPs_LaTeX\Figuras\tabla_de_caracteristicas.png`

## 5. Separación mínima entre depósitos
Según el apartado 5.1.4 de la norma UNE 60250:2008, la distancia mínima de separación ($d$) entre las paredes de depósitos aéreos adyacentes dispuestos en paralelo debe ser:
$$d \ge \frac{D_1 + D_2}{4}$$
Dado que todos los depósitos tienen un diámetro de $2,2 \text{ m}$:
$$d \ge \frac{2,2 + 2,2}{4} = 1,1 \text{ m}$$
Se adopta una separación de **1,1 metros**, cumpliendo estrictamente con el requisito normativo de $d \ge 1\text{ m}$.

integrar imagen `Practica_GLPs_LaTeX\Figuras\distancias_seguridad.png`

## 6. Distancias de seguridad respecto al entorno (Categoría A-500)
Las distancias de seguridad se verifican según el Cuadro de Distancias del Anexo B de la norma UNE 60250:2008. Se distinguen dos tipos de mediciones:
- **$D_o$ (Distancia desde orificios):** Medida desde aberturas (válvulas de seguridad, bocas de carga).
- **$D_p$ (Distancia desde paredes/perímetro):** Medida desde la superficie exterior del depósito.

### 6.1. Verificación de Referencias Normativas
| Referencia | Elemento del entorno | $D_o$ (m) | $D_p$ (m) | Verificación |
| :--- | :--- | :---: | :---: | :--- |
| Ref. 2 | Cerramientos de recinto (no colindantes) | 0 | 5,0 | Cumple |
| Ref. 3 | Muros o paredes ciegas (RF-120) | - | 5,0 | Cumple |
| Ref. 4 | Límites de propiedad / Focos ignición | 15,0 | 10,0 | Cumple |
### 6.2. Otras Distancias Específicas
| Elemento | $D_o$ (m) | $D_p$ (m) | Observaciones |
| :--- | :---: | :---: | :--- |
| Proyección líneas eléctricas (AT/BT) | 15,0 | 10,0 | **No reducible** mediante muros. |
| Almacenamiento inflamables/combustibles | - | 5,0 | Prohibido dentro del recinto (Ref. 2). |

*Nota: La Referencia 4 y 5 pueden reducirse hasta un 50% mediante la interposición de muros cortafuegos (RF-120) según UNE 60250.*

## 7. Verificación de implantación en parcela
La ubicación seleccionada permite inscribir las distancias de seguridad reglamentarias sin colisionar con edificaciones ajenas ni elementos críticos. El perímetro de seguridad queda íntegramente dentro de la parcela de servicio. Se ha verificado que no existen líneas eléctricas aéreas en la vertical de la estación.

Integrar imagen `Practica_GLPs_LaTeX\Figuras\cerramiento.jpeg`

## 8. Incidencia del vaporizador sobre la implantación
Para compensar el déficit de vaporización natural, se instala un sistema de vaporización forzada. A efectos de distancias de seguridad, el vaporizador se asimila a un depósito **Categoría A-1** (V < 5 m³):
- **Intercambiador interno:** Modelo VIA 150, sin incremento de la huella física.
- **Armario de calefacción:** Modelo VPC30C (0,8 x 0,4 m). Sus áreas de seguridad pueden solaparse con las de los depósitos principales.

Para el detalle del balance térmico y dimensionado técnico, consúltese [vaporizacion_forzada.md](vaporizacion_forzada.md).

## 9. Protección contra incendios y ventilación
Dada la clasificación **A-500** y el volumen unitario de los depósitos (> 60 m³ no aplica aquí pero sí el total de la estación), se establecen los siguientes requisitos:

### 9.1. Sistema de refrigeración
Es obligatoria la instalación de un **sistema automático de enfriamiento por agua pulverizada** que garantice:
- Caudal mínimo: $3 \text{ l/min}$ por $\text{m}^2$ de superficie de los depósitos.
- Presión dinámica mínima: $1 \text{ bar}$ en la boquilla más desfavorable.

### 9.2. Dotación de extintores
Para una capacidad de 125,1 m³, la dotación mínima de polvo químico seco (PQS) es de **101 kg** (100 kg base + 1 kg por cada 10 m³ que excedan los 120 m³), distribuidos en:
- Al menos dos extintores de eficacia **34A-183B-C**.

### 9.3. Ventilación y Cerramiento
- **Cerramiento:** Perimetral de al menos $2 \text{ m}$ de altura, realizado en malla metálica o sistema análogo que garantice ventilación natural cruzada.
- **Zócalo:** Máximo $30 \text{ cm}$ de altura para no obstruir la dispersión de posibles fugas (el GLP es más denso que el aire).

## 10. Conclusión técnica
La implantación propuesta para la batería de depósitos (125,1 m³) cumple íntegramente con los requisitos de la norma UNE 60250:2008. La disposición geométrica, las distancias de seguridad adoptadas y los sistemas de protección contra incendios previstos garantizan la viabilidad técnica y reglamentaria de la instalación.

## 11. Referencias cruzadas
- [Selección del depósito](seleccion_deposito.md)
- [Criterios normativos](criterios_normativos.md)
- [Cálculo de volumen del depósito](calculo_volumen_deposito.md)
- [Autonomía 30 días](autonomia_30_dias.md)
- [Vaporización forzada](vaporizacion_forzada.md)
