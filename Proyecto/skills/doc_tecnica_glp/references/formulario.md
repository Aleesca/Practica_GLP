# BLOQUE 5: GLPs

## Índice de Wobbe
$$ W = \frac{P.C.S.}{\sqrt{d}} $$

Existe otra expresión con el poder calorífico superior:
$$ H = \frac{H_s}{\sqrt{d}} $$

En la práctica:
$$ W' = W \times K_1 \times K_2 $$

Donde:
- $W'$: Índice de Wobbe corregido
- $W$: Índice de Wobbe
- $K_1, K_2$: Factores

**$K_1$ gases primera familia:**
$$ H_2 - C_nH_m - 2CO_2 $$

**$K_2$:**
- Primera familia: $1000 \frac{O_2}{P}$
- Segunda familia: $1000 \frac{CO + 4O_2 - 0.5}{P} CO_2$

## Potencial de combustión

**Primera familia:**
$$ C = u \cdot \frac{H_2 + 0.3 CH_4 + 0.7CO + v \cdot \sum a \cdot C_nH_m}{\sqrt{d}} $$

**Segunda familia:**
$$ C = u \cdot \frac{H_2 + 0.7 CO_2 + 0.3 CH_4 + v \cdot \sum a \cdot C_nH_m}{\sqrt{d}} $$

Donde:
- $u$: Coef. de corrección ($1000 \cdot O_2 / P$)
- $H_2, \dots$: % de componentes e hidrocarburos en el gas
- $v$: Coeficiente según $H_2$ o $W'$ (1ª y 2ª fam. respectivamente)
- $C_n H_m$: Hidrocarburos
- $d$: Densidad relativa

## Autonomía
$$ A = \frac{C}{c} $$

Donde:
- $A$: Autonomía
- $C$: Capacidad de almacenamiento en kg
- $c$: Consumo en kg/h

## Potencias
$$ \begin{aligned}
P_s & = H_s \times Q \\
P_i & = H_i \times Q \\
P_u & = A \times \Delta T \\
P_u & = P_s \times R_s = H_s \times Q \times R_s \\
P_u & = P_i \times R_i = H_i \times Q \times R_i
\end{aligned} $$

Donde:
- $P_s$: Potencia superior
- $P_i$: Potencia inferior o gasto calorífico
- $P_u$: Potencia útil
- $R_s$: Rendimiento superior
- $R_i$: Rendimiento inferior
- $Q$: Caudal de gas
- $\Delta T$: Incremento de temperatura ocasionado

**Deducciones:**
$$ \frac{H_i}{H_s} = \frac{R_s}{R_i} \quad ; \quad \frac{P_i}{P_s} = \frac{R_s}{R_i} \quad ; \quad \frac{R_s}{R_i} = \frac{H_i}{H_s} $$

## Número de botellas
$$ N = A \times \frac{C_d}{35} $$

Donde:
- $N$: Número de botellas
- $A$: Autonomía
- $C_d$: Capacidad de la botella en kg

De aquí se deduce la autonomía como:
$$ A = \frac{\text{Gas almacenado}}{\text{Consumo diario}} $$

**"Cocinado":**
$$ N \text{ (bot.)} \times 35 \text{ (kg/bot.)} = \text{Auton. (días)} \times \text{Cons. (kg/día)} $$

## Caudal de simultaneidad
Siendo $Q_1 \geq Q_2 \geq Q_3 \geq \dots \geq Q_n$:
$$ Q_{si} = Q_1 + Q_2 + \frac{1}{2} \cdot \left(Q_3 + Q_4 + \dots + Q_n\right) $$

## Potencia útil aparato
$$ P_u = \eta \cdot P_c $$

En los procesos de calentamiento:
$$ P_u = A \times Ce \times \Delta T $$

## Rendimiento aparato
$$ \eta = \frac{P_u}{P} $$
Donde $P$ es el gasto calorífico.

## Velocidad de un gas
$$ v = \frac{Q}{S} $$

Para consistencia dimensional:
$$ v = 378.04 \times \frac{Q}{P \times D^2} $$

En baja presión (BP):
$$ v = 360 \times \frac{Q}{D^2} $$

## Pérdidas de carga. Fórmulas de Renouard
Condición de aplicación:
$$ \frac{Q}{D} < 150 $$

**Para media presión (MP) $0.05 \text{ bar} < P < 5 \text{ bar}$:**
$$ P_A^2 - P_B^2 = 51.5 \cdot d_c \cdot L_c \cdot \frac{Q^{1.82}}{D^{4.82}} $$

Donde:
- $P_A, P_B$: Presiones abs. (origen y final) [bar a] (Relativa + 1.01325 bar)
- $d_c$: Densidad corregida (Propano: 1.16; Butano: 1.44)
- $L_c$: Longitud de cálculo de la conducción [m]
- $Q$: Caudal de gas en el tramo [$m^3/h$]
- $D$: Diámetro interior de la tubería [mm]

**Para baja presión $P < 0.05$ bar:**
$$ P_A - P_B = 25076 \cdot d_c \cdot L_c \cdot \frac{Q^{1.82}}{D^{4.82}} $$

## Longitudes de cálculo
- **BP:** $L_c = 1.05 \times L$
- **MP:** $L_c = 1.05 \times L$

## Pérdida de carga lineal
- **BP:** $J = \frac{P_A - P_B}{L_c} = 25076 \times d_c \times \frac{Q^{1.82}}{D^{4.82}}$
- **MP:** $J = \frac{P_A^2 - P_B^2}{L_c} = 51.5 \times d_c \times \frac{Q^{1.82}}{D^{4.82}}$

## Pérdida de carga
$$ J^c = \frac{P_A^2 - P_B^2}{L_c} $$

## Fórmulas de vaporización natural
$$ Q = P \cdot S \cdot K \cdot \frac{T_e - T_g}{CLV} $$

Donde:
- $Q$: Caudal másico de vaporización [kg/h]
- $P$: Coef. superficie mojada (20%: 0.336; 30%: 0.397)
- $S$: Superficie del depósito [$m^2$]
- $K$: Coef. transmisión de calor [$kW/m^2 \cdot \text{ºC}$] (Aéreos: 0.0116; Enterrados: 0.0086)
- $T_e$: Temp. exterior mín. media prevista [ºC]
- $T_g$: Temp. equilibrio líquido-gas del gas [ºC]
- $CLV$: Calor latente de vaporización [0.11 kWh/kg]

## Carga
$$ \text{Carga} = 0.85 \times V \times \rho = 0.85 \cdot 506 \cdot V = 430.1 \cdot V $$
*Nota: La fórmula original indica $5.284 \cdot V$*

## Presión máxima de servicio
$$ P_{mxs} = \frac{PN}{Cs} $$

## Potencia nominal de utilización simultánea
$$ P_{si} = P_A + P_B + \frac{P_C + P_D + \dots + P_N}{3} $$

## Caudal de utilización simultánea individual
$$ Q_{si} = Q_A + Q_B + \frac{Q_C + Q_D + \dots + Q_N}{2} $$

## Consumo diario
$$ C_{\text{diario}} = Q \times T \text{ ($m^3$/día)} $$

## Contenido mínimo del depósito
$$ \text{Contenido} = C_{\text{diario}} \times N_{\text{días}} $$

## Pérdida de carga linea por metro de conducción de cálculo
$$ J = \frac{PCd}{Lc} $$

## Espesor de la plataforma (Flotación)
$$ e = \frac{1000 \cdot V - T}{2400 \cdot A \cdot L} $$

Donde:
- $e$: espesor de la plataforma (m)
- $V$: volumen del depósito ($m^3$)
- $T$: Tara (masa) del depósito (kg)
- $A$: Ancho de la plataforma (m) (mínimo el diámetro del depósito)
- $L$: Longitud de la plataforma (m) (mínimo la longitud del depósito)

## Espárragos de sujeción
$$ T_u = \frac{E}{n} $$

Donde:
- $T_u$: Tensión unitaria
- $E$: esfuerzo vertical ascendente
- $n$: número de espárragos
- $g$: aceleración de la gravedad

Para un coeficiente de trabajo de $C_t = 4100 \cdot g$ del acero (tetracero, en $kg/cm^2$), resulta necesaria una sección de:
$$ S = \frac{T_u}{C_t} $$

$$ D = \frac{\sqrt{1000 \times V - T}}{226.98} $$

Donde:
- $D$: diámetro del espárrago (mm)
- $V$: volumen del depósito ($m^3$)
- $T$: Tara del depósito (kg)
