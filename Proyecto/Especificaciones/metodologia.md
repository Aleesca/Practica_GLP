# Especificación: Metodología General del Proyecto (Sección 2)

## Propósito
Definir la estructura procedimental, los estándares de validación técnica, la coherencia de magnitudes físicas y el flujo de cálculo transversal que rige la redacción de la sección de Metodología de la memoria.

## Contenido obligatorio
- **Guía de Apartados de Metodología:**
  - Estructurar y gobernar la redacción de:
    - 2.1 Hipótesis y datos de partida.
    - 2.2.1 Demanda y caudal de cálculo.
    - 2.2.2 Autonomía de almacenamiento.
    - 2.2.3 Vaporización natural del depósito.
    - 2.2.4 Selección y dimensionado del depósito.
    - 2.2.5 Red de distribución.
    - 2.2.6 Implantación y distancias de seguridad.
- **Criterios de Coherencia de Cálculo:**
  - Prescribir que el caudal másico agregado ($187,81 \text{ kg/h}$) debe ser consistente en el dimensionado del almacenamiento, el balance térmico de vaporización y el dimensionado hidráulico de tuberías de cobre.
  - Asegurar la trazabilidad cruzada de coeficientes normativos adoptados en León (temperatura de $-5\text{ ºC}$, factor de llenado del $85\%$, presión inicial de regulación de $1,7 \text{ bar relativos}$, velocidad límite de $10\text{ m/s}$ y pérdidas admisibles del $5\%$).
- **Criterios Comunes de Validación Documental:**
  - Mantener coherencia dimensional en el Sistema Internacional de Unidades ($SI$) y magnitudes de gas (m, mm, kg/h, $m^3/h$, kW, bar y bar a).
  - Indicar que esta especificación es directriz técnica y de validación cruzada y no se vuelca de forma literal a LaTeX.

## Estilo de redacción
Tono prescriptivo, procedimental y de gestión de calidad técnica. Redactado en forma de directrices numeradas y claras. Longitud orientativa: 1,5 páginas.

## Figuras, tablas y resultados
- No contiene tablas de cálculo numérico, sino un diagrama de flujo metodológico de dependencias de cálculo (Datos de partida $\rightarrow$ Caudales $\rightarrow$ Autonomía/Vaporización $\rightarrow$ Selección Depósito $\rightarrow$ Trazado Red $\rightarrow$ Pérdidas Hidráulicas $\rightarrow$ Distancias de Seguridad).

## Conexiones
- **Alcance:** Guía general de salida documental del proyecto.
- **Anotaciones:** Enlaza transversalmente con las 16 notas técnicas de `Proyecto/Anotaciones/`.

## Criterios de aceptación
- [ ] Prescribe explícitamente el orden secuencial lógico de cálculos del proyecto.
- [ ] Define la obligatoriedad de la coherencia en las magnitudes críticas (caudal másico agregando $187,81 \text{ kg/h}$ y presión de $1,7 \text{ bar}$).
- [ ] Establece reglas de validación dimensional.
- [ ] Queda marcado formalmente que no se vuelca literal a la plantilla LaTeX.
