# Especificación: Autonomía de Almacenamiento (Sección 2.2.2)

## Propósito
Justificar la capacidad de almacenamiento útil necesaria para garantizar la autonomía de proyecto durante 30 días de funcionamiento continuado del Grupo G1-1.

## Contenido obligatorio
- **Criterios de Autonomía de Almacenamiento:**
  - Definir la ecuación de la autonomía:
    $$ \text{Gas acumulado} = C_{\text{diario}} \cdot N_{\text{días}} $$
    donde $C_{\text{diario}}$ es el consumo en masa diario en $\text{kg/día}$ y $N_{\text{días}}$ es la autonomía requerida ($30 \text{ días}$).
  - Calcular el consumo diario combinado a partir de la suma de consumos diarios individuales de los hornos y calderas:
    $$ C_{\text{diario}} = \sum (Q_{\text{kg/h}} \cdot t_{\text{uso}}) = 1.264,52 \text{ kg/día} $$
  - Determinar la masa útil acumulada requerida para 30 días:
    $$ M_{\text{util}} = 1.264,52 \text{ kg/día} \cdot 30 \text{ días} = 37.935,63 \text{ kg} $$
  - Convertir la masa útil en volumen líquido de diseño empleando la densidad del propano líquido ($\rho_{liq} = 506 \text{ kg/m}^3$):
    $$ V_{\text{util}} = \frac{M_{\text{util}}}{\rho_{liq}} = \frac{37.935,63 \text{ kg}}{506 \text{ kg/m}^3} = 74,97 \text{ m}^3 $$
- **Consideración de Factor de Llenado de Seguridad:**
  - Especificar el coeficiente de llenado máximo del depósito establecido por seguridad en el $85\%$ (ITC-ICG 03):
    $$ V_{\text{geom}} = \frac{V_{\text{util}}}{0,85} = 88,20 \text{ m}^3 $$
  - Justificar que cualquier volumen de almacenamiento comercial adoptado debe superar este valor geométrico mínimo ($88,20 \text{ m}^3$).

## Estilo de redacción
Tono de ingeniería preciso, formal y descriptivo. Uso de notación LaTeX para fórmulas. Longitud orientativa: 1,5 páginas.

## Figuras, tablas y resultados
- **Tabla resumen de consumo diario:** Potencias, consumos horarios y consumos diarios por equipo.
- **Resultado final:** Masa útil de diseño de $37.935,63 \text{ kg}$, Volumen útil de $74,97 \text{ m}^3$ y Volumen geométrico mínimo necesario de $88,20 \text{ m}^3$.

## Conexiones
- **Alcance:** Requisito 2 (Autonomía de almacenamiento para 30 días) y Requisito 4 (Cálculo del volumen del depósito).
- **Anotaciones:** [autonomia_30_dias.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/autonomia_30_dias.md) (Cálculo), [calculo_volumen_deposito.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/calculo_volumen_deposito.md) (Cálculo).

## Criterios de aceptación
- [ ] El consumo de propano diario agregado calculado es igual a $1.264,52 \text{ kg/día}$.
- [ ] La masa requerida acumulada para 30 días es de $37.935,63 \text{ kg}$.
- [ ] El volumen geométrico mínimo de diseño considerando el factor de llenado del $85\%$ es exactamente $88,20 \text{ m}^3$.
