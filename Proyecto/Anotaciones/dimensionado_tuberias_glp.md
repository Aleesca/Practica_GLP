# Dimensionado de tuberias GLP

El presente documento desarrolla el dimensionado de la red de distribucion de GLP en fase gas, incluyendo criterios de calculo, seleccion de materiales, formulacion hidraulica, optimizacion de diametros y resultados finales por tramo.

## Criterios tecnicos adoptados

El dimensionado de la red de distribucion de GLP se realiza para un regimen de media presion, con presion inicial relativa de `1.70 bar`. La perdida de carga admisible se limita al `5.0%` de dicha presion inicial, lo que fija una presion minima de servicio en el extremo mas desfavorable de `1.615 bar relativos`.

La red se calcula para propano en fase gas. Se adopta densidad corregida Renouard `dc = 1.16` y poder calorifico superior de `13.95 kWh/kg` para transformar la potencia termica instalada en caudal masico. El paso a caudal volumetrico se realiza con densidad de propano gas `1.882 kg/m3`.

La red se proyecta para GLP en fase gas y trazado exterior aereo. Se adopta tuberia metalica de cobre duro estirado sin soldadura conforme a EN 1057, con espesor minimo de 1 mm, por su compatibilidad con instalaciones receptoras de GLP y por permitir ejecucion vista protegida. El polietileno se descarta para estos tramos al tratarse de conduccion aerea expuesta; el acero al carbono se considera alternativa tecnica posible si se justifica proteccion frente a corrosion y autorizacion/criterio especifico aplicable a media presion.

### Criterio de velocidad: limite aereo y limite de proyecto

Para una canalizacion aerea de GLP en fase gas se toma como referencia general el limite maximo de `20 m/s`, asociado a redes generales de distribucion y acometidas aereas. No obstante, el presente proyecto no corresponde a una red general de distribucion de GLP canalizado para distintos abonados, sino a una instalacion receptora alimentada desde almacenamiento propio que suministra a consumidores finales de un unico usuario industrial. De acuerdo con la clasificacion tecnica de instalaciones receptoras, cuando existe un unico usuario la IRG se considera instalacion individual; para instalacion comun o individual el limite de velocidad aplicable es `10 m/s`. Por ello se adopta `10 m/s` como limite de proyecto y `8-10 m/s` como rango operativo preferente. El valor `20 m/s` queda documentado solo como limite maximo de referencia para conducciones aereas generales, pero no gobierna la seleccion de diametros de esta instalacion receptora industrial.

La fuente de calculo empleada establece tres limites de velocidad por tipo de conduccion: `30 m/s` para red general enterrada, `20 m/s` para red general y acometidas aereas, y `10 m/s` para instalacion comun en edificios e instalacion individual. La misma documentacion define que la red de distribucion no existe en GLP a granel y que, si la instalacion receptora suministra a un unico usuario, se considera instalacion individual. En consecuencia, cada tramo se comprueba frente a `v <= 10.0 m/s` como criterio aplicable de proyecto; el valor `v <= 20.0 m/s` se conserva solo como contraste de limite aereo general. La seleccion final prioriza el intervalo `8-10 m/s` cuando el catalogo y la presion disponible lo permiten.

Desde el punto de vista de optimizacion, el diametro seleccionado no se determina unicamente por velocidad. Para cada tramo se comprueba simultaneamente la condicion de aplicacion de Renouard `Q/D < 150`, la presion minima final, la velocidad practica y el catalogo comercial disponible. En tramos terminales de pequeno caudal puede aparecer velocidad baja cuando ya se ha alcanzado el diametro comercial minimo. En ramales de mayor longitud se evalua ademas el equilibrio entre aumentar ligeramente el tramo comun aguas arriba y reducir el diametro del ramal final, usando la masa lineal del tubo como estimador tecnico del coste.

## Material y catalogo de calculo

Material adoptado: **Cobre duro estirado sin soldadura EN 1057, espesor minimo 1 mm, instalacion aerea protegida**.

Se selecciona cobre duro estirado sin soldadura como material metalico apto para la red exterior en fase gas de GLP. Esta solucion evita recurrir a PE en tramos aereos y simplifica la proteccion frente a corrosion respecto al acero al carbono. El PE se descarta por ser canalizacion aerea exterior. La alternativa de acero al carbono queda tecnicamente posible solo con proteccion pasiva y autorizacion o documentacion especifica. La seleccion queda supeditada a que el material mantenga presion maxima admisible suficiente frente a la presion de servicio y a las condiciones de montaje exterior.

El catalogo utilizado incorpora diametro interior, espesor, diametro exterior y masa lineal estimada a partir de la seccion metalica y densidad del cobre `8960 kg/m3`. Esta masa lineal se emplea solo como criterio comparativo interno para seleccionar alternativas equivalentes desde el punto de vista hidraulico.

Las dimensiones comerciales y masas lineales empleadas se han contrastado con tablas de tuberia de cobre conforme a EN 1057 para aplicaciones de agua/gas y con tablas tecnicas de instalaciones de GLP. Como referencias externas de material se consideran: [EN 1057:2006+A1:2010 - seamless copper tubes for water and gas](https://standards.iteh.ai/catalog/standards/cen/472e132f-b218-4e1e-9158-a3974034b500/en-1057-2006a1-2010), [Manual de instalaciones de GLP - Cepsa](https://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com/04422d24271abec52042f58a558069bf/1_09_glp_cepsa.pdf), [COPTECH - tubos de cobre duro R290 EN 1057](https://www.copper.rs/hard.html) y [ALSIMET - tabla de tubo sanitario EN 1057](https://alsimet.es/en/copper/copper-tubes/sanitary-copper). Estas referencias se usan para justificar el tipo de tubo, la nomenclatura `diametro exterior x espesor`, el uso de cobre duro y la estimacion de masa lineal; el catalogo definitivo debera validarse con el proveedor antes de presupuesto.

| material | designacion | D_int_mm | espesor_mm | D_ext_mm | area_metal_mm2 | masa_lineal_kg_m |
| --- | --- | --- | --- | --- | --- | --- |
| cobre_duro_en1057 | 15x1 | 13.000 | 1.000 | 15.000 | 43.982 | 0.394 |
| cobre_duro_en1057 | 18x1 | 16.000 | 1.000 | 18.000 | 53.407 | 0.479 |
| cobre_duro_en1057 | 22x1 | 20.000 | 1.000 | 22.000 | 65.973 | 0.591 |
| cobre_duro_en1057 | 28x1 | 26.000 | 1.000 | 28.000 | 84.823 | 0.760 |
| cobre_duro_en1057 | 35x1.5 | 32.000 | 1.500 | 35.000 | 157.865 | 1.414 |
| cobre_duro_en1057 | 42x1.5 | 39.000 | 1.500 | 42.000 | 190.852 | 1.710 |
| cobre_duro_en1057 | 54x2 | 50.000 | 2.000 | 54.000 | 326.726 | 2.927 |
| cobre_duro_en1057 | 64x2 | 60.000 | 2.000 | 64.000 | 389.557 | 3.490 |
| cobre_duro_en1057 | 76.1x2 | 72.100 | 2.000 | 76.100 | 465.584 | 4.172 |
| cobre_duro_en1057 | 88.9x2 | 84.900 | 2.000 | 88.900 | 546.009 | 4.892 |
| cobre_duro_en1057 | 108x2.5 | 103.000 | 2.500 | 108.000 | 828.595 | 7.424 |

## Conexiones con otros documentos del proyecto

- [Datos de partida](../Datos.md): potencias nominales de consumidores y documentacion base del encargo.
- [Caudales de consumidores](caudales_consumidores.md): potencia maxima simultanea y base de demanda de la red.
- [Trazado de red](trazado_red.md): topologia de la red, longitudes y enlace con el plano de implantacion.
- [Valvuleria y accesorios](valvuleria_accesorios.md): criterio de valvulas de corte, tes, reducciones y elementos singulares.
- [Criterios normativos](criterios_normativos.md): marco normativo general de almacenamiento e instalacion de GLP.
- [Metodologia de longitud de calculo](../Especificaciones/metodologia-longitud-calculo.md): desarrollo metodologico de `Lc`, Renouard y comprobacion de velocidad.

## Formulacion empleada

La potencia de cada consumidor se transforma a caudal masico y volumetrico mediante:

```text
Q_kg/h = P_kW / PCS_propano
Q_m3/h = Q_kg/h / rho_propano_gas
```

Para el consumidor `C6`, de `1000 kW`, resulta:

```text
Q_kg/h = 1000 / 13.95 = 71.68 kg/h
Q_m3/h = 71.68 / 1.882 = 38.09 m3/h
```

La longitud de calculo se obtiene sumando a la longitud geometrica la longitud equivalente de accesorios:

```text
Lc(D) = Lreal + sum(n_i * K_i * D_mm / 1000)
```

Para el tramo `E-C6`, con `Lreal = 14.46 m`, diametro interior `26 mm` y accesorios equivalentes `te_desviada + valvula_corte + reduccion`, se obtiene `Lc = 16.540 m`.

La perdida de carga en media presion se calcula con Renouard:

```text
PA_abs^2 - PB_abs^2 = 51.5 * dc * Lc * Q^1.82 / D^4.82
```

Para `E-C6`, con `PA_rel = 1.641 bar`, `Q = 38.090 m3/h`, `D = 26 mm` y `Lc = 16.540 m`, la presion final calculada es `PB_rel = 1.620 bar`, con perdida de carga `0.021 bar`.

La velocidad del gas se comprueba mediante:

```text
v = 378.04 * Q / (P_abs * D^2)
```

En el mismo tramo `E-C6`, el resultado es `v = 8.089 m/s`, dentro del rango operativo de `8-10 m/s`.

## Consumidores y caudales

| nodo | nombre | potencia_kw | q_kg_h | q_m3_h |
| --- | --- | --- | --- | --- |
| C1 | Horno secado 1 | 60 | 4.301 | 2.285 |
| C2 | Horno secado 2 | 60 | 4.301 | 2.285 |
| C3 | Caldera vapor | 500 | 35.842 | 19.045 |
| C4 | Caldera agua caliente | 300 | 21.505 | 11.427 |
| C5 | Horno fusion | 700 | 50.179 | 26.663 |
| C6 | Horno decapado | 1000 | 71.685 | 38.090 |

## Topologia y caudales por tramo

Los caudales aguas arriba se obtienen por suma de los consumidores descendentes, sin simultaneidad adicional. La fila inicial de derivaciones verticales de deposito se trata como cuatro subtramos equivalentes de `1,90 m` y se resume agrupada en la tabla posterior.

| designacion | tipo_tramo | nodo_ini | nodo_fin | longitud_m | q_m3_h | q_kg_h |
| --- | --- | --- | --- | --- | --- | --- |
| D1-D4 | derivacion_deposito | D1 | D4 | 1.900 | 24.949 | 46.953 |
| D2-D4 | derivacion_deposito | D2 | D4 | 1.900 | 24.949 | 46.953 |
| D3-D4 | derivacion_deposito | D3 | D4 | 1.900 | 24.949 | 46.953 |
| D4 vertical | derivacion_deposito | D4_dep | D4 | 1.900 | 24.949 | 46.953 |
| D4-A | red_principal | D4 | A | 15.120 | 99.795 | 187.814 |
| A-C1 | red_principal | A | C1 | 1.810 | 2.285 | 4.301 |
| A-B | red_principal | A | B | 4.970 | 97.509 | 183.513 |
| B-C2 | red_principal | B | C2 | 21.790 | 2.285 | 4.301 |
| B-C | red_principal | B | C | 17.320 | 95.224 | 179.211 |
| C-C3 | red_principal | C | C3 | 1.750 | 19.045 | 35.842 |
| C-D | red_principal | C | D | 10.770 | 76.179 | 143.369 |
| D-C4 | red_principal | D | C4 | 1.680 | 11.427 | 21.505 |
| D-E | red_principal | D | E | 13.060 | 64.752 | 121.864 |
| E-C5 | red_principal | E | C5 | 1.690 | 26.663 | 50.179 |
| E-C6 | red_principal | E | C6 | 14.460 | 38.090 | 71.685 |

## Accesorios considerados

El inventario de accesorios se introduce como longitud equivalente proporcional al diametro. Se consideran codos por cambios de direccion, tes en derivaciones, valvulas de corte por consumidor y por salida de deposito, y reducciones cuando el ramal deriva hacia un diametro inferior.

En el tramo `B-C2` se conserva la longitud real `21,79 m`, ya que corresponde a la suma de `0,53 m` a nivel de suelo, `8,00 m` de subida, `5,26 m` de tramo horizontal aereo y `8,00 m` de bajada. La revision no altera dicha longitud geometrica, pero si incorpora cuatro codos de 90 grados asociados a los cambios de direccion suelo-subida, subida-horizontal, horizontal-bajada y conexion final al consumidor. El desnivel no se corrige mediante termino hidrostatico porque el ramal sube y baja hasta una cota final equivalente y la comprobacion se realiza para GLP en fase gas.

| designacion | accesorio | cantidad | coef_leq_D | criterio |
| --- | --- | --- | --- | --- |
| D1-D4 | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D1-D4 | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D2-D4 | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D2-D4 | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D3-D4 | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D3-D4 | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4 vertical | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4 vertical | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4-A | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4-A | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4-A | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-C1 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-C1 | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-C1 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-B | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-B | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C2 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C2 | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C2 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C2 | codo_90 | 4 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-C3 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-C3 | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-C3 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-D | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-D | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-C4 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-C4 | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-C4 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-E | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-E | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C5 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C5 | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C5 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C6 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C6 | valvula_corte | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C6 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |

### Sensibilidad del tramo B-C2

| subtramo | descripcion | longitud_m | tipo |
| --- | --- | --- | --- |
| B-C2.1 | tramo inicial a nivel de suelo | 0.530 | horizontal_suelo |
| B-C2.2 | subida vertical hasta tramo aereo | 8.000 | vertical_subida |
| B-C2.3 | tramo horizontal aereo | 5.260 | horizontal_aereo |
| B-C2.4 | bajada vertical hasta consumidor C2 | 8.000 | vertical_bajada |

La comparacion siguiente muestra el efecto de incorporar los codos del trazado vertical-aereo. El diametro se mantiene en `15x1`, por ser el minimo del catalogo adoptado y porque la presion final sigue por encima del minimo admisible.

| escenario | designacion_tubo | D_int_mm | Lc_m | P_ini_rel_bar | P_fin_rel_bar | delta_p_bar | velocidad_ms | incremento_Lc_m | incremento_delta_p_bar |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anterior: sin codos vertical-aereo adicionales | 15x1 | 13.000 | 22.830 | 1.675 | 1.670 | 0.005 | 1.905 | 0.000 | 0.000 |
| revisado: con 4 codos 90 por subida/bajada | 15x1 | 13.000 | 24.390 | 1.675 | 1.670 | 0.005 | 1.905 | 1.560 | 0.000 |

Como condicion constructiva, el tramo aereo debe resolverse con soportes que no carguen sobre uniones, separacion respecto a paramentos, proteccion anticorrosiva, identificacion de fase gas y previsiones de dilatacion si la longitud expuesta queda sometida a variaciones termicas relevantes.

## Derivaciones verticales de deposito

| designacion | unidades | longitud_m_por_unidad | q_m3_h_por_unidad | designacion_tubo | D_int_mm | Lc_m_por_unidad | P_fin_rel_bar_min | velocidad_ms_max | estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1/D2/D3/D4 verticales | 4 | 1.900 | 24.949 | 22x1 | 20.000 | 2.700 | 1.694 | 8.708 | Conforme |

## Optimizacion hidraulica y economica del subarbol E

El tramo `E-C6` es un ramal largo con caudal relevante. El dimensionado secuencial inicial mantenia `D-E` en `35x1.5` y obligaba a seleccionar `E-C6` en `35x1.5` para cumplir presion, lo que dejaba una velocidad baja en el ramal final. Para evitar esta solucion local, se evalua de forma combinada el conjunto `D-E`, `E-C5` y `E-C6`.

La seleccion se realiza sobre combinaciones comerciales que cumplen `Q/D`, presion minima y `v <= 10.0 m/s`, ordenadas por masa equivalente total de cobre. La alternativa adoptada incrementa `D-E` a `42x1.5`, reduciendo su perdida de carga a `0.007 bar` y elevando la presion disponible en el nodo `E` hasta `1.641 bar`. Con esa presion disponible, `E-C6` puede reducirse a `28x1` y queda con velocidad `8.089 m/s`, dentro del rango objetivo.

| D-E_tubo | E-C5_tubo | E-C6_tubo | D-E_velocidad_ms | E-C5_velocidad_ms | E-C6_velocidad_ms | D-E_P_fin_rel_bar | E-C5_P_fin_rel_bar | E-C6_P_fin_rel_bar | masa_total_kg | desviacion_total_ms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 42x1.5 | 22x1 | 28x1 | 6.062 | 9.520 | 8.089 | 1.641 | 1.634 | 1.620 | 34.322 | 4.869 |
| 42x1.5 | 28x1 | 28x1 | 6.062 | 5.622 | 8.089 | 1.641 | 1.639 | 1.620 | 34.607 | 8.727 |
| 42x1.5 | 35x1.5 | 28x1 | 6.062 | 3.709 | 8.089 | 1.641 | 1.640 | 1.620 | 35.713 | 10.640 |
| 42x1.5 | 42x1.5 | 28x1 | 6.062 | 2.497 | 8.089 | 1.641 | 1.641 | 1.620 | 36.213 | 11.852 |
| 42x1.5 | 54x2 | 28x1 | 6.062 | 1.519 | 8.089 | 1.641 | 1.641 | 1.620 | 38.270 | 12.830 |

La velocidad de `D-E` queda en `6.062 m/s`, por debajo del rango preferente, pero se considera justificada porque el tramo comun conserva margen de presion y permite reducir material en el ramal largo `E-C6`. El tramo `E-C5` mantiene `22x1` con velocidad `9.520 m/s`.

## Justificacion de velocidades bajas

Determinados tramos presentan velocidades inferiores al rango preferente `8-10 m/s`. Estos casos no se clasifican automaticamente como sobredimensionado, ya que el criterio principal es garantizar simultaneamente presion minima, condicion `Q/D < 150`, diametro comercial disponible y velocidad maxima admisible. La velocidad baja se acepta solo cuando existe una causa tecnica identificable.

- `A-C1` y `B-C2`: ambos alimentan consumidores de `60 kW`, con caudal `2.285 m3/h`. El diametro seleccionado es `15x1`, con diametro interior `13 mm`, que es el minimo del catalogo adoptado. En `B-C2`, la revision del trazado vertical-aereo aumenta la longitud de calculo por los cuatro codos adicionales, pero el diametro no cambia y la presion final permanece conforme. La velocidad resultante queda en torno a `1.9 m/s`; reducir el diametro para aproximarse a `8-10 m/s` exigiria introducir un tubo no contemplado en el catalogo de calculo y con menor robustez mecanica. Por tanto, la baja velocidad se justifica por caudal reducido, diametro comercial minimo y margen de presion suficiente aun incorporando los cambios de direccion.

- `C-C3`: alimenta el consumidor de `500 kW`, con caudal `19.045 m3/h`. El tubo `22x1` proporciona `6.752 m/s`, por debajo del rango preferente pero cumpliendo presion y `Q/D`. El diametro inmediatamente inferior elevaria la velocidad, pero penalizaria la perdida de carga y reduciria el margen de presion disponible en un ramal conectado a la red principal. Se mantiene `22x1` como equilibrio entre margen hidraulico y dimension comercial.

- `C-D`: transporta el caudal remanente hacia los consumidores `C4`, `C5` y `C6`. La seleccion `42x1.5` da `7.113 m/s`, ligeramente inferior al objetivo, pero mantiene margen de presion para el subarbol final y evita trasladar una perdida excesiva a los ramales aguas abajo. La velocidad baja se considera admisible por equilibrio hidraulico de conjunto.

- `D-E`: tras la optimizacion combinada del subarbol `E`, se adopta `42x1.5`, con `6.062 m/s`. Esta reduccion de velocidad en el tramo comun permite elevar la presion en el nodo `E` y reducir `E-C6` a `28x1`, donde la velocidad pasa a `8.089 m/s`. El criterio no minimiza la velocidad de cada tramo de forma aislada, sino la solucion conjunta de presion, perdida de carga y masa equivalente de tubo.

## Resultados de dimensionado

| designacion | tipo_tramo | longitud_m | q_m3_h | designacion_tubo | D_int_mm | Lc_m | Q_D | P_ini_rel_bar | P_fin_rel_bar | delta_p_bar | velocidad_ms | velocidad_objetivo | desviacion_velocidad_ms | criterio_seleccion | estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-D4 | derivacion_deposito | 1.900 | 24.949 | 22x1 | 20.000 | 2.700 | 1.247 | 1.700 | 1.694 | 0.006 | 8.708 | 8-10 m/s | 0.792 | diametro con velocidad dentro de 8-10 m/s mas cercana a 9.5 m/s | Conforme - velocidad objetivo |
| D2-D4 | derivacion_deposito | 1.900 | 24.949 | 22x1 | 20.000 | 2.700 | 1.247 | 1.700 | 1.694 | 0.006 | 8.708 | 8-10 m/s | 0.792 | diametro con velocidad dentro de 8-10 m/s mas cercana a 9.5 m/s | Conforme - velocidad objetivo |
| D3-D4 | derivacion_deposito | 1.900 | 24.949 | 22x1 | 20.000 | 2.700 | 1.247 | 1.700 | 1.694 | 0.006 | 8.708 | 8-10 m/s | 0.792 | diametro con velocidad dentro de 8-10 m/s mas cercana a 9.5 m/s | Conforme - velocidad objetivo |
| D4 vertical | derivacion_deposito | 1.900 | 24.949 | 22x1 | 20.000 | 2.700 | 1.247 | 1.700 | 1.694 | 0.006 | 8.708 | 8-10 m/s | 0.792 | diametro con velocidad dentro de 8-10 m/s mas cercana a 9.5 m/s | Conforme - velocidad objetivo |
| D4-A | red_principal | 15.120 | 99.795 | 42x1.5 | 39.000 | 17.460 | 2.559 | 1.700 | 1.682 | 0.018 | 9.203 | 8-10 m/s | 0.297 | diametro con velocidad dentro de 8-10 m/s mas cercana a 9.5 m/s | Conforme - velocidad objetivo |
| A-C1 | red_principal | 1.810 | 2.285 | 15x1 | 13.000 | 2.850 | 0.176 | 1.682 | 1.681 | 0.001 | 1.897 | 8-10 m/s | 7.603 | diametro mas cercano al rango objetivo sin superar el limite practico de 10 m/s | Conforme - velocidad baja justificada |
| A-B | red_principal | 4.970 | 97.509 | 42x1.5 | 39.000 | 6.920 | 2.500 | 1.682 | 1.675 | 0.007 | 9.015 | 8-10 m/s | 0.485 | diametro con velocidad dentro de 8-10 m/s mas cercana a 9.5 m/s | Conforme - velocidad objetivo |
| B-C2 | red_principal | 21.790 | 2.285 | 15x1 | 13.000 | 24.390 | 0.176 | 1.675 | 1.670 | 0.005 | 1.905 | 8-10 m/s | 7.595 | diametro mas cercano al rango objetivo sin superar el limite practico de 10 m/s | Conforme - velocidad baja justificada |
| B-C | red_principal | 17.320 | 95.224 | 42x1.5 | 39.000 | 19.270 | 2.442 | 1.675 | 1.657 | 0.018 | 8.864 | 8-10 m/s | 0.636 | diametro con velocidad dentro de 8-10 m/s mas cercana a 9.5 m/s | Conforme - velocidad objetivo |
| C-C3 | red_principal | 1.750 | 19.045 | 22x1 | 20.000 | 3.350 | 0.952 | 1.657 | 1.652 | 0.004 | 6.752 | 8-10 m/s | 2.748 | diametro mas cercano al rango objetivo sin superar el limite practico de 10 m/s | Conforme - velocidad baja justificada |
| C-D | red_principal | 10.770 | 76.179 | 42x1.5 | 39.000 | 12.720 | 1.953 | 1.657 | 1.649 | 0.008 | 7.113 | 8-10 m/s | 2.387 | diametro mas cercano al rango objetivo sin superar el limite practico de 10 m/s | Conforme - velocidad baja justificada |
| D-C4 | red_principal | 1.680 | 11.427 | 15x1 | 13.000 | 2.720 | 0.879 | 1.649 | 1.638 | 0.011 | 9.642 | 8-10 m/s | 0.142 | diametro con velocidad dentro de 8-10 m/s mas cercana a 9.5 m/s | Conforme - velocidad objetivo |
| D-E | red_principal | 13.060 | 64.752 | 42x1.5 | 39.000 | 15.010 | 1.660 | 1.649 | 1.641 | 0.007 | 6.062 | 8-10 m/s | 3.438 | optimizacion economica del subarbol E: aumenta D-E para reducir masa total en E-C6 | Conforme - velocidad baja justificada |
| E-C5 | red_principal | 1.690 | 26.663 | 22x1 | 20.000 | 3.290 | 1.333 | 1.641 | 1.634 | 0.008 | 9.520 | 8-10 m/s | 0.020 | seleccionado por optimizacion economica del subarbol E con presion aguas arriba recalculada | Conforme - velocidad objetivo |
| E-C6 | red_principal | 14.460 | 38.090 | 28x1 | 26.000 | 16.540 | 1.465 | 1.641 | 1.620 | 0.021 | 8.089 | 8-10 m/s | 1.411 | seleccionado por optimizacion economica del subarbol E con presion aguas arriba recalculada | Conforme - velocidad objetivo |

## No conformidades

No se detectan no conformidades.

## Control manual de trazabilidad

Como control independiente se recalcula el tramo `D4-A`:

```text
Lc = 17.460 m
Q/D = 2.559
v = 9.203 m/s
```

El resultado confirma la coherencia entre longitud de calculo, caudal, diametro y velocidad final del tramo principal de alimentacion.

## Conclusion tecnica

Con las hipotesis adoptadas, la red queda dimensionada para un caudal punta simultaneo de `187.81 kg/h`, equivalente a `99.79 m3/h`. Todos los tramos cumplen la condicion de aplicacion `Q/D < 150`, la presion minima relativa de `1.615 bar` y el limite practico de velocidad adoptado. Las velocidades bajas que permanecen en ramales concretos responden al diametro comercial minimo o a una decision de equilibrio hidraulico-economico, y quedan justificadas de forma expresa en la tabla de resultados.
