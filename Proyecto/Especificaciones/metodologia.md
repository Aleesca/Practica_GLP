# Metodologia

Este documento define, paso a paso, que debe incluirse en cada subapartado de la metodologia de la memoria. La redaccion final debe ser tecnica, ordenada y trazable, de forma que cada calculo pueda seguirse desde los datos de partida hasta los resultados de diseno.

Los apartados se cruzan con `Proyecto/Planificacion/esquema_memoria.md` y con las anotaciones tecnicas de `Proyecto/Anotaciones/`. La trazabilidad debe ser bidireccional: desde la memoria hacia la fuente tecnica y desde cada nota tecnica de vuelta a este documento.

## 2.1 Hipotesis y datos de partida

### Proposito
Reunir en un unico bloque los supuestos, condiciones de diseno y datos base que gobiernan el resto de los calculos del proyecto de GLP.

### Datos de entrada
- Datos del grupo contenidos en `Proyecto/Datos.md`.
- Enunciado y modelo base en `00_Info_proporcionada/`.
- Normativa de referencia en `ZZ_Normativa/`.
- Propiedades fisicas y criterios de calculo recogidos en `.agents/skills/doc_tecnica_glp/references/formulario.md`.

### Secuencia de trabajo
1. Reunir datos de consumidores, emplazamiento y condicionantes de uso.
2. Homogeneizar unidades, parametros y nomenclatura.
3. Registrar hipotesis, simbolos y simplificaciones.
4. Verificar coherencia entre alcance, datos y normativa.

### Salida esperada
- Tabla de datos de partida.
- Resumen de hipotesis de calculo.
- Lista consolidada de simbolos y unidades.

## 2.2 Desarrollo de los calculos

### 2.2.1 Demanda y caudal de calculo

#### Proposito
Obtener la demanda de calculo de la instalacion a partir de los consumidores, su potencia y su regimen de funcionamiento.

#### Datos de entrada
- Potencias y horas de funcionamiento de `Proyecto/Datos.md`.
- Criterios de simultaneidad y conversion definidos en `Proyecto/Anotaciones/caudales_consumidores.md`.

#### Comprobaciones
- La demanda agregada representa el escenario de calculo adoptado.
- Las unidades de consumo y caudal quedan homogeneizadas.

#### Salida esperada
- Tabla de consumidores y demanda individual.
- Tabla de demanda total y caudal de calculo.

### 2.2.2 Autonomia de almacenamiento

#### Proposito
Justificar la capacidad de almacenamiento necesaria para cubrir la autonomia objetivo del proyecto.

#### Datos de entrada
- Demanda de calculo del apartado anterior.
- Criterio de autonomia de 30 dias.
- Notas de `Proyecto/Anotaciones/autonomia_30_dias.md`.

#### Comprobaciones
- La capacidad util cubre el horizonte temporal de diseno.
- El volumen calculado es compatible con alternativas comerciales razonables.

#### Salida esperada
- Tabla de consumos diarios.
- Tabla de autonomia y volumen util requerido.

### 2.2.3 Vaporizacion natural del deposito

#### Proposito
Comprobar que la vaporizacion natural del deposito es suficiente para atender la demanda de calculo en las condiciones mas desfavorables.

#### Datos de entrada
- Demanda de calculo.
- Temperatura exterior de calculo.
- Criterios de `Proyecto/Anotaciones/vaporizacion_natural.md`.

#### Comprobaciones
- La capacidad de vaporizacion disponible cubre la demanda de punta.
- Las condiciones climaticas de referencia quedan explicitadas.

#### Salida esperada
- Tabla de vaporizacion disponible.
- Tabla de verificacion demanda frente a vaporizacion.

### 2.2.4 Seleccion y dimensionado del deposito

#### Proposito
Seleccionar la configuracion de deposito coherente con autonomia, vaporizacion, implantacion y criterios de seguridad.

#### Datos de entrada
- Resultados de autonomia y vaporizacion.
- Catalogos y criterios recogidos en `Proyecto/Anotaciones/seleccion_deposito.md`.

#### Comprobaciones
- La capacidad nominal elegida cubre la necesidad de almacenamiento.
- La configuracion seleccionada es viable desde el punto de vista de implantacion y operacion.

#### Salida esperada
- Tabla de alternativas de deposito.
- Justificacion tecnica de la solucion seleccionada.

### 2.2.5 Red de distribucion

#### Proposito
Describir la arquitectura de la red y verificar diametros, presiones y perdidas de carga hasta los puntos de consumo.

#### Datos de entrada
- Trazado preliminar en `01_Planos/instalacion_GLP.dwg`.
- Medidas y criterios de `Proyecto/Anotaciones/trazado_red.md`.

#### Comprobaciones
- El punto mas desfavorable conserva las condiciones minimas de suministro.
- Las perdidas de carga se mantienen dentro del criterio adoptado.

#### Salida esperada
- Tabla de tramos y caudales.
- Tabla de perdidas de carga y presiones residuales.

### 2.2.6 Implantacion y distancias de seguridad

#### Proposito
Justificar la ubicacion de la estacion de almacenamiento y su compatibilidad con las distancias reglamentarias y los condicionantes del emplazamiento.

#### Datos de entrada
- Parcela y situacion general del proyecto.
- Notas de `Proyecto/Anotaciones/distancias_seguridad.md`.
- Normativa aplicable en `ZZ_Normativa/`.

#### Comprobaciones
- La implantacion propuesta cumple distancias y accesibilidad.
- La solucion es defendible desde el punto de vista de seguridad.

#### Salida esperada
- Tabla de distancias de seguridad verificadas.
- Justificacion de la ubicacion seleccionada.

## 2.3 Criterios comunes de validacion

- Las unidades se mantienen consistentes en todos los apartados.
- Cada tabla de resultados identifica su fuente y criterio de calculo.
- Cada seleccion de equipo se apoya en normativa o catalogo verificable.
- La consolidacion editorial queda fuera del flujo primario mientras el Markdown siga abierto.
