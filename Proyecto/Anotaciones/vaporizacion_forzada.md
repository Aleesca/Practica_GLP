# Vaporizacion forzada

Esta nota justifica la selección e integración del sistema de vaporización forzada para cubrir el déficit detectado en la [vaporización natural](vaporizacion_natural.md), consolidando el criterio técnico y de diseño.

## 1. Criterio de Diseño: El Margen del 20% de Llenado
La verificación de vaporización se realiza siempre considerando un **nivel de reserva del 20%**. Este no es un margen arbitrario, sino que responde a una limitación física:
- **Superficie Mojada:** El GLP absorbe calor a través de las paredes en contacto con el líquido. Al vaciarse el depósito, esta superficie disminuye drásticamente, reduciendo la capacidad de gasificación natural.
- **Condición Crítica:** El diseño garantiza el suministro en la peor combinación posible: temperatura exterior mínima (-5ºC) y nivel de llenado mínimo operativo (20%).
- **Seguridad del Vaporizador:** Mantener el cálculo al 20% asegura que el serpentín del vaporizador interno permanezca sumergido en GLP líquido para un intercambio térmico eficiente.

## 2. Selección del Equipo (Modelo Especial)
Dada la limitación de espacio en la parcela, se descarta el modelo estándar LPVI 50A-22 (13,71 m). Se ha optado por una configuración de **Modelo Especial** integrada en la batería mixta.

- **Depósito Base:** LP46A-22 (46,2 m³ - Longitud: 12,82 m).
- **Vaporizador Interno:** VIA 150 (Instalación bajo demanda al fabricante).
- **Capacidad forzada:** **150 kg/h**.
- **Capacidad Natural (Batería mixta):** **131,30 kg/h** (al 20% de llenado y -5ºC).
- **Capacidad Total Garantizada:** **281,30 kg/h**.

## 3. Justificación del Balance de Vaporización
La demanda punta es de **187,81 kg/h**. El sistema ofrece un exceso de capacidad de aproximadamente el 50%.
- **Reserva Operativa:** Este excedente actúa como garantía ante descensos térmicos extremos por debajo de los -5ºC o niveles de llenado excepcionalmente bajos.
- **Estabilidad de Presión:** Evita caídas de presión en la red industrial durante picos de demanda simultánea de todos los consumidores.

## 4. Especificaciones Técnicas del Sistema: Desglose de Componentes
Es fundamental entender que el "sistema de vaporización" no es un único bloque, sino un conjunto de dos equipos interconectados. Esta distinción es crítica para el diseño en CAD y el cálculo de distancias:

### A. Elemento Interno (Intercambiador): Modelo VIA 150
Es un **serpentín de acero inoxidable** que se introduce físicamente en el interior del depósito.
- **Naturaleza física:** Es un componente sumergido. No ocupa espacio exterior ni altera la silueta del depósito en el plano de planta.
- **Acoplamiento:** Se monta sobre una **brida especial de DN400** situada habitualmente en la boca de hombre lateral del depósito (en este caso, el LP46A-22). 
- **Puntos de conexión:** Solo "asoman" por la tapa de la brida dos tomas de agua (ida y retorno) de 1" (DN25).

### B. Elemento Externo (Generador de Calor): Armario VPC30C
Es una **caseta o armario metálico autoportante** que se coloca en el suelo, sobre una pequeña losa de hormigón, junto al depósito.
- **Dimensiones Reales (Espacio en Parcela):** **800 mm (Largo) x 400 mm (Ancho) x 1.200 mm (Alto)**. Este es el objeto que debe dibujarse en el plano de implantación.
- **Contenido:** Aloja una caldera mural de gas (propano), bomba de circulación, vaso de expansión y cuadro eléctrico de control.
- **Conexión con el depósito:** Se une al VIA 150 mediante un circuito cerrado de agua caliente (tuberías aisladas térmicamente).

## 5. Criterios para la Representación en Planos y Seguridad
Para el replanteo en el archivo `01_Planos/instalacion_GLP.dwg`:

1.  **Representación Gráfica:** Se debe dibujar un rectángulo de **0,8 x 0,4 metros** adosado o muy próximo al lateral del depósito LP46A-22, etiquetado como "Armario de Calefacción VPC30C".
2.  **Referencia para Distancias:**
    *   **Desde el depósito:** Las distancias de seguridad (Referencia 4) se miden desde los orificios (válvulas/boca de carga).
    *   **Desde el Armario VPC30C:** Al contener una caldera (foco de ignición), se deben medir las distancias reglamentarias desde las **paredes exteriores de este armario** hacia cualquier otro elemento combustible o límite de propiedad.
3.  **Localización Óptima:** Debe situarse lo más cerca posible de la brida DN400 del depósito para minimizar el recorrido de las tuberías de agua, pero siempre respetando que el armario NO puede estar bajo la proyección de las válvulas de seguridad del depósito.

## 6. Bibliografía y Referencias Técnicas
Para la definición de este sistema se han consultado las siguientes fuentes oficiales y técnicas:

*   **Lapesa Grupo Empresarial:**
    *   [Depósitos y equipos GLP - Catálogo General](https://www.lapesa.es/depositos-y-equipos-glp): Especificaciones de la serie LP y sistemas de vaporización interna.
    *   [Ficha Técnica Módulo VPC30C](https://www.lapesa.es/sites/default/files/cv-gs.pdf): Dimensiones (800x400x1200 mm) y potencias del equipo de apoyo.
    *   [Válvulas, complementos y accesorios](https://www.lapesa.es/sites/default/files/valvulas_complementos_y_accesorios.pdf): Referencias para bridas de servicio DN400 y colectores.
*   **Normativa Vigente:**
    *   [UNE 60250: Seguridad de los depósitos de propano](https://propanogas.com/deposito-granel/seguridad): Resumen de distancias y criterios de implantación.
    *   [RD 919/2006 (ITC-ICG 03)](https://www.boe.es/buscar/pdf/2017/BOE-A-2017-8755-consolidado.pdf): Reglamento de combustibles gaseosos y almacenamientos fijos.
*   **Fuentes de Ingeniería:**
    *   [Teyco Comercial - Vaporizadores GLP](https://www.teyco-comercial.com/vaporizadores-glp/): Criterios de diseño para sistemas mixtos y balance térmico.
    *   [Redexis Gas - Especificación ETRG-Pla-05](https://www.redexis.es/media/1075): Guía técnica para construcción y dimensionamiento de estaciones de GLP.

---
**Véase también:**
- [Vaporización natural](vaporizacion_natural.md)
- [Selección del depósito](seleccion_deposito.md)
- [Caudales de consumidores](caudales_consumidores.md)
- [Recopilación de accesorios y costes](recopilacion_accesorios_costes_glp.md)
- [Pliego de condiciones de equipos](pliego_condiciones_equipos_glp.md)
- [Memoria: Vaporización natural vs. vaporización forzada](../Especificaciones/vaporizacion.md)
- [Memoria: Características de los equipos auxiliares del almacenamiento](../Especificaciones/equipos-auxiliares.md)
- [Memoria: Instalaciones auxiliares y de seguridad de la estación](../Especificaciones/instalaciones-auxiliares.md)
- [Memoria: Selección y dimensionado del depósito](../Especificaciones/deposito.md)
