# Trazado de red

Esta nota recoge el procedimiento para definir la arquitectura de la red de distribución para el Grupo G1-1.

## Consideraciones
El trazado debe dimensionarse para cubrir la potencia máxima simultánea calculada en [caudales_consumidores.md](caudales_consumidores.md).

El dimensionado por tramos queda desarrollado en [dimensionado_tuberias_glp.md](dimensionado_tuberias_glp.md). Ese documento fija la topología de cálculo, convierte las potencias de los consumidores en caudales de Renouard, incorpora las longitudes normalizadas de `calculos/datos/longitudes_Tramos.csv`, aplica longitud de cálculo iterativa por accesorios y verifica cada tramo mediante Renouard para media presión.

La solución adoptada calcula la red principal como media presión a 1,70 bar relativos, con propano como gas de referencia, caída máxima total del 5% y velocidad límite de 20 m/s. La primera fila del CSV se trata como cuatro derivaciones verticales de depósito agrupadas en el informe.

## Normativa de Referencia
Los diámetros y materiales deben cumplir con los [criterios normativos](criterios_normativos.md) vigentes (UNE 60670 / UNE 60250).

---
**Véase también:**
- [Caudales de consumidores](caudales_consumidores.md)
- [Criterios normativos](criterios_normativos.md)
- [Dimensionado de tuberías GLP](dimensionado_tuberias_glp.md)
- [Valvulería y accesorios](valvuleria_accesorios.md)
