# Especificación: Cálculos de Seguridad y Auxiliares (Secciones 3.4, 3.5, 3.6, 3.7)

## Propósito
Describir detalladamente el desarrollo matemático, fórmulas e hipótesis de cálculo empleadas para justificar el dimensionado de las válvulas de alivio, la longitud del tubo sonda, la protección catódica (si procede) y el caudal de refrigeración frente a incendios.

## Contenido obligatorio

### Sección 3.4 VÁLVULAS DE SEGURIDAD (Cálculo).
- Desarrollar la fórmula de descarga de aire equivalente ($Q_a$) exigida por la norma UNE 60250 para incendios externos:
  $$ Q_a = 10,652 \cdot A^{0,82} $$
  donde $A$ es el área total exterior expuesta del depósito en $\text{m}^2$.
- Calcular el área exterior expuesta de los depósitos LP46A ($A \approx 62,3 \text{ m}^2$) y LP26A ($A \approx 39,2 \text{ m}^2$).
- Obtener el caudal mínimo de descarga requerido y justificar que la capacidad nominal de descarga de las válvulas RegO RS 3145 a la presión de tarado supera este mínimo.

### Sección 3.5 PUNTO MÁXIMO LLENADO: LONGITUD TUBO SONDA.
- Describir las ecuaciones geométricas para determinar la cota física de la sonda que corta el llenado al $85\%$ del volumen geométrico total del depósito horizontal cilíndrico con fondos semiesféricos o toriesféricos.
- Exponer el porcentaje de altura del líquido correspondiente a la capacidad del $85\%$.
- Calcular el valor de la longitud del tubo sonda ($L_{sonda}$) medido desde la brida de acoplamiento del depósito.

### Sección 3.6 PROTECCIÓN CATÓDICA.
- Justificar detalladamente por qué no se requiere realizar un cálculo ni instalar un sistema de protección catódica activa o pasiva (ánodos de sacrificio / corriente impresa).
- Citar que el descarte se basa en que los depósitos de la estación son enteramente aéreos de superficie, asentados sobre cunas de hormigón mediante apoyos aislantes de neopreno y con canalizaciones viales aéreas soportadas en ménsulas o postes elevados.

### Sección 3.7 PROTECCIÓN CONTRA INCENDIOS (Cálculo).
- Desarrollar el cálculo del caudal de agua fría de enfriamiento exigido por la norma UNE 60250 para proteger los depósitos horizontales en caso de fuego.
- Aplicar la dotación de refrigeración de $3\ \text{l/min}\cdot\text{m}^2$ sobre la superficie lateral expuesta de todos los tanques de la batería:
  - Depósito LP46A: Superficie lateral $\approx 62,3 \text{ m}^2 \rightarrow Q_{agua} \approx 187 \text{ l/min}$.
  - Depósitos LP26A (3 unidades): Superficie lateral unitaria $\approx 39,2 \text{ m}^2 \rightarrow Q_{agua} \approx 118 \text{ l/min}$ por depósito.
  - Caudal total para la batería mixta: $Q_{total} = 187 + 3 \cdot 118 = 541 \text{ l/min}$ ($32,5 \text{ m}^3/\text{h}$).
- Dimensionar el número de boquillas de pulverización de agua fría, el diámetro del colector de alimentación y la presión mínima requerida en boquillas ($1,5 - 2,0 \text{ bar}$).

## Estilo de redacción
Estilo científico-técnico riguroso, formal y preciso. Inclusión clara de ecuaciones en formato LaTeX. Longitud orientativa: 2 a 3 páginas.

## Figuras, tablas y resultados
- **Ecuaciones detalladas:** Expresiones matemáticas de descarga, cota de llenado y caudal de agua.
- **Tabla de resultados de seguridad:** Para cada depósito, indicar el área expuesta, el caudal de aire exigido, la longitud calculada del tubo sonda y el caudal de agua de refrigeración requerido.

## Conexiones
- **Alcance:** Requisito 4 (Características principales depósito y equipos) y Requisito 6 (Esquema de distribución y distancias).
- **Anotaciones:** [calculo_volumen_deposito.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/calculo_volumen_deposito.md) (Cálculo), [distancias_seguridad.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/distancias_seguridad.md) (Criterio Normativo), [valvuleria_accesorios.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/valvuleria_accesorios.md) (Decisión).

## Criterios de aceptación
- [ ] Se detalla la ecuación de descarga $Q_a = 10,652 \cdot A^{0,82}$ para válvulas de seguridad.
- [ ] Se justifica formalmente la cota de llenado del $85\%$.
- [ ] Queda justificada la exclusión de la protección catódica.
- [ ] Se detalla el caudal total de agua de refrigeración para toda la batería ($541 \text{ l/min}$).
