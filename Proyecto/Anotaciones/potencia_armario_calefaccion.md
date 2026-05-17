# Potencia del armario de calefaccion

Esta nota documenta el criterio de calculo de la potencia termica minima del armario de calefaccion asociado al sistema de [vaporizacion forzada](vaporizacion_forzada.md).

## 1. Necesidad tecnica del armario

La [vaporizacion natural](vaporizacion_natural.md) de la bateria de depositos no cubre la demanda punta de la instalacion en la condicion critica de diseno. La comprobacion se realiza con:

- Temperatura exterior de calculo: **-5 ºC**, definida en [temperatura_diseno.md](temperatura_diseno.md).
- Nivel minimo operativo: **20%** de llenado.
- Presion de comprobacion: **2 bar**.

En estas condiciones, la demanda punta obtenida a partir de los [caudales de consumidores](caudales_consumidores.md) es **187,81 kg/h**, mientras que la vaporizacion natural total de la bateria seleccionada es **131,30 kg/h**. Por tanto, aparece un deficit de:

$$
Q_{def} = 187,81 - 131,30 = 56,51\ \text{kg/h}
$$

Este deficit hace necesario un aporte termico externo. El armario de calefaccion no se incorpora como mejora opcional, sino como equipo funcional imprescindible para alimentar el circuito cerrado de agua caliente que transfiere calor al serpentín interno del vaporizador.

## 2. Criterio de dimensionado

El sistema adoptado en [seleccion_deposito.md](seleccion_deposito.md) es un deposito **LP46A-22** como modelo especial con vaporizador interno **VIA 150**. El criterio de dimensionado del armario se fija por la potencia minima de caldera requerida por el vaporizador seleccionado, no solo por el deficit instantaneo de vaporizacion natural.

Segun la tabla tecnica utilizada en `calculos/calculos.ipynb`, el **VIA 150** tiene:

- Capacidad de vaporizacion forzada: **150 kg/h**.
- Potencia minima de caldera: **17,5 kW**.

La capacidad total garantizada con el sistema mixto queda:

$$
Q_{total} = Q_{natural} + Q_{forzada} = 131,30 + 150 = 281,30\ \text{kg/h}
$$

El margen frente a la demanda punta es:

$$
Q_{margen} = 281,30 - 187,81 = 93,49\ \text{kg/h}
$$

## 3. Resultado

La potencia termica minima exigida para el generador del armario de calefaccion asociado al **VIA 150** es:

$$
P_{armario,min} = 17,5\ \text{kW}
$$

El armario seleccionado, identificado en la documentacion del proyecto como **VPC30C**, debe acreditar una potencia termica igual o superior a **17,5 kW** para ser coherente con el vaporizador interno adoptado. Al no quedar confirmada en esta implementacion una potencia nominal adicional desde NotebookLM o ficha tecnica accesible, no se introduce un valor nominal distinto del requisito minimo documentado.

## 4. Conclusion

La instalacion del armario de calefaccion es necesaria porque la vaporizacion natural disponible en las condiciones criticas de diseno no garantiza el caudal requerido por la instalacion. Con el vaporizador interno **VIA 150** y una potencia minima de caldera de **17,5 kW**, el sistema mixto alcanza **281,30 kg/h**, suficiente para cubrir la demanda punta de **187,81 kg/h**.

---
**Vease tambien:**
- [Caudales de consumidores](caudales_consumidores.md)
- [Vaporizacion natural](vaporizacion_natural.md)
- [Vaporizacion forzada](vaporizacion_forzada.md)
- [Seleccion del deposito](seleccion_deposito.md)
- [Temperatura exterior de calculo](temperatura_diseno.md)
