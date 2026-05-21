# Dimensionado de tuberias GLP por tramos

Documento generado desde `calculos/calculos.ipynb` como salida reproducible del calculo.

## Fuentes y criterios

- Longitudes: `calculos/datos/longitudes_Tramos.csv`.
- Esquema: `esquema_instalacion.pdf`.
- Formulas: `Proyecto/skills/doc_tecnica_glp/references/formulario.md` y `Proyecto/Especificaciones/metodologia-longitud-calculo.md`.
- Consulta NotebookLM: notebook `GLP` (`3bae2f27-6ddf-4f0c-99bf-f37c4e05dea3`) mediante CLI `nlm notebook query`.

Consulta ejecutada con CLI: nlm notebook query 3bae2f27-6ddf-4f0c-99bf-f37c4e05dea3 "Para una instalacion aerea exterior de GLP en media presion, que materiales de tuberia son admisibles/recomendables, que limitaciones aplican a cobre, acero y PE, y que criterio debe usarse para justificar el material seleccionado."

Resultado resumido: para instalacion aerea de GLP en media presion se citan cobre duro estirado sin soldadura y acero como materiales usados en la practica. El PE queda descartado en canalizaciones aereas por degradacion frente a radiacion UV y se reserva a tramos enterrados. El acero requiere proteccion pasiva frente a corrosion y, segun las fuentes consultadas, puede quedar condicionado a autorizacion expresa en redes de media presion. El cobre en instalacion aerea debe garantizar espesor minimo de 1 mm. El criterio resistente se justifica comprobando que la presion maxima de servicio admisible del material sea suficiente frente a la presion de servicio.

## Hipotesis de calculo

- Gas de referencia: propano.
- Densidad corregida Renouard: `dc = 1.16`.
- PCS usado para pasar de potencia a caudal masico: `13.95 kWh/kg`.
- Densidad de propano gas para obtener caudal volumetrico: `1.882 kg/m3`.
- Presion inicial de red: `1.70 bar relativos`.
- Caida maxima admisible total: `5.0%`, equivalente a presion minima `1.615 bar relativos`.
- Velocidad maxima admisible: `20.0 m/s`.
- La fila 1 del CSV se trata como cuatro derivaciones verticales de deposito de 1,90 m y se resume de forma agrupada.
- Los accesorios no confirmados visualmente se incorporan mediante hipotesis conservadora documentada.

## Material seleccionado

Se selecciona cobre duro estirado sin soldadura porque la consulta documental lo identifica como material practico admisible para fase gas en GLP y evita la restriccion indicada para redes de acero en media presion salvo autorizacion. El PE se descarta por ser canalizacion aerea exterior. La alternativa de acero al carbono queda tecnicamente posible solo con proteccion pasiva y autorizacion o documentacion especifica.

Material adoptado: **Cobre duro estirado sin soldadura EN 1057, espesor minimo 1 mm, instalacion aerea protegida**.

### Catalogo de diametros

| material | designacion | D_int_mm | espesor_mm |
| --- | --- | --- | --- |
| cobre_duro_en1057 | 15x1 | 13.000 | 1.000 |
| cobre_duro_en1057 | 18x1 | 16.000 | 1.000 |
| cobre_duro_en1057 | 22x1 | 20.000 | 1.000 |
| cobre_duro_en1057 | 28x1 | 26.000 | 1.000 |
| cobre_duro_en1057 | 35x1.5 | 32.000 | 1.500 |
| cobre_duro_en1057 | 42x1.5 | 39.000 | 1.500 |
| cobre_duro_en1057 | 54x2 | 50.000 | 2.000 |
| cobre_duro_en1057 | 64x2 | 60.000 | 2.000 |
| cobre_duro_en1057 | 76.1x2 | 72.100 | 2.000 |
| cobre_duro_en1057 | 88.9x2 | 84.900 | 2.000 |
| cobre_duro_en1057 | 108x2.5 | 103.000 | 2.500 |

## Formulas empleadas

Conversion de potencia a caudal:

```text
Q_kg/h = P_kW / PCS_propano
Q_m3/h = Q_kg/h / rho_propano_gas
```

Longitud de calculo iterativa por accesorios:

```text
Lc(D) = Lreal + sum(n_i * coef_i * D_mm / 1000)
```

Renouard para media presion:

```text
PA_abs^2 - PB_abs^2 = 51.5 * dc * Lc * Q^1.82 / D^4.82
```

Velocidad del gas:

```text
v = 378.04 * Q / (P_abs * D^2)
```

Condicion de aplicacion y aceptacion:

```text
Q / D < 150
PB_rel >= 1.615 bar
v <= 20.0 m/s
```

## Consumidores y caudales

| nodo | nombre | potencia_kw | q_kg_h | q_m3_h |
| --- | --- | --- | --- | --- |
| C1 | Horno secado 1 | 60 | 4.301 | 2.285 |
| C2 | Horno secado 2 | 60 | 4.301 | 2.285 |
| C3 | Caldera vapor | 500 | 35.842 | 19.045 |
| C4 | Caldera agua caliente | 300 | 21.505 | 11.427 |
| C5 | Horno fusion | 700 | 50.179 | 26.663 |
| C6 | Horno decapado | 1000 | 71.685 | 38.090 |

## Tramos modelizados

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

## Inventario de accesorios

| designacion | accesorio | cantidad | coef_leq_D | criterio |
| --- | --- | --- | --- | --- |
| D1-D4 | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D1-D4 | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D2-D4 | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D2-D4 | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D3-D4 | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D3-D4 | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4 vertical | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4 vertical | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4-A | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4-A | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D4-A | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-C1 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-C1 | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-C1 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-B | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| A-B | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C2 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C2 | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C2 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| B-C | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-C3 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-C3 | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-C3 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-D | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| C-D | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-C4 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-C4 | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-C4 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-E | codo_90 | 1 | 30 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| D-E | te_linea | 1 | 20 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C5 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C5 | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C5 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C6 | te_desviada | 1 | 60 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C6 | valvula_bola | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |
| E-C6 | reduccion | 1 | 10 | visible/hipotesis conservadora segun esquema_instalacion.pdf |

## Resumen de derivaciones verticales de deposito

| designacion | unidades | longitud_m_por_unidad | q_m3_h_por_unidad | designacion_tubo | D_int_mm | Lc_m_por_unidad | P_fin_rel_bar_min | velocidad_ms_max | estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1/D2/D3/D4 verticales | 4 | 1.900 | 24.949 | 18x1 | 16.000 | 2.540 | 1.685 | 13.656 | Conforme |

## Resultados de dimensionado

| designacion | tipo_tramo | longitud_m | q_m3_h | designacion_tubo | D_int_mm | Lc_m | Q_D | P_ini_rel_bar | P_fin_rel_bar | delta_p_bar | velocidad_ms | estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-D4 | derivacion_deposito | 1.900 | 24.949 | 18x1 | 16.000 | 2.540 | 1.559 | 1.700 | 1.685 | 0.015 | 13.656 | Conforme |
| D2-D4 | derivacion_deposito | 1.900 | 24.949 | 18x1 | 16.000 | 2.540 | 1.559 | 1.700 | 1.685 | 0.015 | 13.656 | Conforme |
| D3-D4 | derivacion_deposito | 1.900 | 24.949 | 18x1 | 16.000 | 2.540 | 1.559 | 1.700 | 1.685 | 0.015 | 13.656 | Conforme |
| D4 vertical | derivacion_deposito | 1.900 | 24.949 | 18x1 | 16.000 | 2.540 | 1.559 | 1.700 | 1.685 | 0.015 | 13.656 | Conforme |
| D4-A | red_principal | 15.120 | 99.795 | 35x1.5 | 32.000 | 17.040 | 3.119 | 1.700 | 1.654 | 0.046 | 13.812 | Conforme |
| A-C1 | red_principal | 1.810 | 2.285 | 15x1 | 13.000 | 2.850 | 0.176 | 1.654 | 1.654 | 0.001 | 1.917 | Conforme |
| A-B | red_principal | 4.970 | 97.509 | 35x1.5 | 32.000 | 6.570 | 3.047 | 1.654 | 1.637 | 0.017 | 13.582 | Conforme |
| B-C2 | red_principal | 21.790 | 2.285 | 15x1 | 13.000 | 22.830 | 0.176 | 1.637 | 1.632 | 0.005 | 1.932 | Conforme |
| B-C | red_principal | 17.320 | 95.224 | 42x1.5 | 39.000 | 19.270 | 2.442 | 1.637 | 1.618 | 0.019 | 8.993 | Conforme |
| C-C3 | red_principal | 1.750 | 19.045 | 28x1 | 26.000 | 3.830 | 0.732 | 1.618 | 1.617 | 0.001 | 4.049 | Conforme |
| C-D | red_principal | 10.770 | 76.179 | 54x2 | 50.000 | 13.270 | 1.524 | 1.618 | 1.616 | 0.003 | 4.381 | Conforme |
| D-C4 | red_principal | 1.680 | 11.427 | 28x1 | 26.000 | 3.760 | 0.439 | 1.616 | 1.615 | 0.001 | 2.431 | Conforme |
| D-E | red_principal | 13.060 | 64.752 | 76.1x2 | 72.100 | 16.665 | 0.898 | 1.616 | 1.615 | 0.000 | 1.791 | Conforme |
| E-C5 | red_principal | 1.690 | 26.663 | 42x1.5 | 39.000 | 4.810 | 0.684 | 1.615 | 1.615 | 0.000 | 2.521 | Conforme |
| E-C6 | red_principal | 14.460 | 38.090 | 64x2 | 60.000 | 19.260 | 0.635 | 1.615 | 1.615 | 0.000 | 1.522 | Conforme |

## No conformidades

No se detectan no conformidades.

## Control manual de trazabilidad

Tramo de control: `D4-A`.

- `Lc` recalculada: `17.040 m`.
- `Q/D` recalculado: `3.119`.
- Velocidad recalculada: `13.812 m/s`.

## Limitaciones

- El inventario de accesorios se basa en el esquema y en hipotesis conservadoras para los elementos no distinguibles con certeza en el PDF.
- El catalogo de diametros se fija como catalogo de calculo para este proyecto; debe contrastarse con proveedor antes de mediciones o presupuesto definitivo.
- Si se sustituye el cobre por acero, debe documentarse autorizacion o criterio equivalente para media presion y proteccion pasiva frente a corrosion.

## Conclusion tecnica

Con las hipotesis adoptadas, la red queda dimensionada para el caudal punta simultaneo de `187.81 kg/h` (`99.79 m3/h`). Todos los tramos modelizados cumplen la condicion de Renouard `Q/D < 150`, la velocidad maxima de `20.0 m/s` y la presion minima relativa de `1.615 bar`. La solucion queda condicionada a validar en fase de detalle el inventario definitivo de accesorios y el catalogo comercial exacto del tubo seleccionado.
