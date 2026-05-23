# Especificación: Hipótesis y Datos de Partida (Sección 2.1)

## Propósito
Consolidar las hipótesis de cálculo, los datos base del grupo de trabajo y las propiedades físicas y normativas que gobiernan el desarrollo del proyecto de GLP para el Grupo G1-1.

## Contenido obligatorio
- **Datos de Emplazamiento y Referencias:**
  - Ubicación de la parcela catastral `8638004TN8183N` en León.
  - Temperatura exterior de cálculo de $-5 \text{ ºC}$ justificada por percentil $99,6\%$ del IDAE para León (Virgen del Camino).
  - Citar normas de referencia: UNE 60250:2008 para almacenamiento y red de estación, UNE 60670:2014 para red receptora general y RD 919/2006.
- **Consumidores del Proyecto (Grupo G1-1):**
  - Tabla de consumidores (C1 a C6) con potencias nominales (desde 60 kW hasta 1000 kW), horas de uso diario y potencia agregada total de $2.620 \text{ kW}$.
- **Propiedades Físicas del Propano y Criterios:**
  - Tabla de propiedades del propano comercial (PCS $13,95\text{ kWh/kg}$, densidades en fase líquida $506\text{ kg/m}^3$ y gas $1,882\text{ kg/m}^3$, CLV $0,11\text{ kWh/kg}$, coeficiente $K$ para tanques aéreos $0,0116\text{ kW/m}^2\cdot\text{ºC}$ y $T_g = -15 \text{ ºC}$).
- **Hipótesis Operativas y de Diseño:**
  - Red aérea en su totalidad, de tuberías de cobre UNE-EN 1057 en barra (espesor $\ge 1,0 \text{ mm}$ en general y $\ge 1,5 \text{ mm}$ en derivaciones de tanques).
  - Presión de diseño de red MPB: presión inicial de regulación $1,7 \text{ bar relativos}$, pérdida de carga admisible del $5\%$ ($0,085 \text{ bar}$ max).
  - Límite de velocidad de gas: $10 \text{ m/s}$ máximo para red general y $20 \text{ m/s}$ para la estación de almacenamiento.
  - Coeficiente de simultaneidad igual a $1$ (escenario punta).
- **Nomenclatura y Símbolos:**
  - Tabla de símbolos, variables y unidades empleadas en los cálculos.

## Estilo de redacción
Tono formal, impersonal y técnico de ingeniería. Uso claro de tablas y ecuaciones en formato LaTeX. Longitud orientativa: 2 a 3 páginas.

## Figuras, tablas y resultados
- **Tabla de Emplazamiento:** Parámetros base y referencia de León.
- **Tabla de Consumidores:** Datos nominales del Grupo G1-1.
- **Tabla de Propiedades del Gas:** Valores del propano comercial adoptados.
- **Tabla de Nomenclatura:** Lista consolidada de variables.

## Conexiones
- **Alcance:** Sección 2 (Datos de partida) e hipótesis generales de cálculo.
- **Anotaciones:** [temperatura_diseno.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/temperatura_diseno.md) (Evidencia), [criterios_normativos.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/criterios_normativos.md) (Criterio Normativo).

## Criterios de aceptación
- [ ] La temperatura mínima exterior de diseño de León está justificada a $-5 \text{ ºC}$.
- [ ] La potencia térmica conjunta de los hornos y calderas de G1-1 suma exactamente $2.620 \text{ kW}$.
- [ ] Se adopta cobre UNE-EN 1057 y velocidad máxima del gas de $10 \text{ m/s}$ para la red.
- [ ] La presión de regulación de salida inicial es de $1,7 \text{ bar}$.
