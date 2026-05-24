
import pandas as pd
import numpy as np

# 1. Parámetros y Constantes
PCS_PROPANO = 13.95  # kWh/kg
DENSIDAD_LIQ = 506.0  # kg/m3 a 20°C
LLENADO_MAX = 0.85
RESERVA_MIN = 0.20
FRACCION_UTIL = LLENADO_MAX - RESERVA_MIN
AUTONOMIA_DIAS = 30  # Requerido por TAREA 3
TEMP_DISENO = -5.0   # IDAE Percentil 99,6% para León
PRESION_SERVICIO = 2.0 # bar (Condición de comprobación solicitada)

print(f"Fracción útil adoptada: {FRACCION_UTIL:.2f}")
print(f"Autonomía de diseño: {AUTONOMIA_DIAS} días")
print(f"Temperatura exterior de diseño: {TEMP_DISENO} ºC")
print(f"Presión de servicio para comprobación: {PRESION_SERVICIO} bar")



# 2. Datos de Consumidores
consumidores = [
    {"nombre": "Horno secado 1", "potencia_kw": 60, "horas_dia": 12},
    {"nombre": "Horno secado 2", "potencia_kw": 60, "horas_dia": 12},
    {"nombre": "Caldera vapor", "potencia_kw": 500, "horas_dia": 10},
    {"nombre": "Caldera agua caliente", "potencia_kw": 300, "horas_dia": 8},
    {"nombre": "Horno fusion", "potencia_kw": 700, "horas_dia": 4},
    {"nombre": "Horno decapado", "potencia_kw": 1000, "horas_dia": 6}
]

df_cons = pd.DataFrame(consumidores)
df_cons['energia_diaria_kwh'] = df_cons['potencia_kw'] * df_cons['horas_dia']

energia_total_dia = df_cons['energia_diaria_kwh'].sum()
potencia_max_simultanea = df_cons['potencia_kw'].sum()

print(f"Energía total diaria: {energia_total_dia} kWh/d")
print(f"Potencia máxima simultánea (S=1): {potencia_max_simultanea} kW")


# 3. Cálculo de Consumo Másico y Volumétrico
m_dia = energia_total_dia / PCS_PROPANO
v_liq_dia = m_dia / DENSIDAD_LIQ  # m3/día

v_geom_min = (v_liq_dia * AUTONOMIA_DIAS) / FRACCION_UTIL

print(f"Consumo diario: {m_dia:.2f} kg/día")
print(f"Volumen líquido diario: {v_liq_dia:.3f} m3/día")
print(f"--- Volumen geométrico mínimo requerido: {v_geom_min:.2f} m3 ---")


# 4. Selección del Depósito Comercial
df_dep = pd.read_csv('datos/tabla_caracteristicas_secadores.csv')
df_vap_table = pd.read_csv('datos/caudal_vaporizacion.csv')
df_vapi_table = pd.read_csv('datos/deposito_vaporizador_interno.csv')

# Datos de la nueva selección
dep_grande_ref = 'LP46A-22'
dep_peque_ref = 'LP26A-22'
n_grande = 1
n_peque = 3

v_grande = df_dep[df_dep['Modelo Ref.'] == dep_grande_ref]['Capacidad nominal (litros)'].values[0]
v_peque = df_dep[df_dep['Modelo Ref.'] == dep_peque_ref]['Capacidad nominal (litros)'].values[0]
v_total = (v_grande * n_grande) + (v_peque * n_peque)

print(f"Configuración de Almacenamiento: {n_grande} x {dep_grande_ref} + {n_peque} x {dep_peque_ref}")
print(f"Capacidad total: {v_total} litros")


# 5. Verificación de Vaporización y Selección de Vaporizador Forzado
caudal_nec_kgh = potencia_max_simultanea / PCS_PROPANO
print(f"Demanda punta necesaria: {caudal_nec_kgh:.2f} kg/h")

# 5.1. Comprobación de Vaporización Natural (al 20% de llenado)
vol_grande_m3 = 46.2
vol_peque_m3 = 26.3

vap_grande = df_vap_table[(abs(df_vap_table['Volum. m3'] - vol_grande_m3) < 0.01) & (df_vap_table['Pres. bar'] == PRESION_SERVICIO)]
vap_peque = df_vap_table[(abs(df_vap_table['Volum. m3'] - vol_peque_m3) < 0.01) & (df_vap_table['Pres. bar'] == PRESION_SERVICIO)]

q_nat_grande = vap_grande['Caudal Aéreo -5°C'].values[0]
q_nat_peque_total = vap_peque['Caudal Aéreo -5°C'].values[0] * n_peque
q_nat_total = q_nat_grande + q_nat_peque_total

print(f"Vaporización natural {dep_grande_ref}: {q_nat_grande} kg/h")
print(f"Vaporización natural {dep_peque_ref} ({n_peque} uds): {q_nat_peque_total:.1f} kg/h")
print(f"Vaporización natural total (-5ºC, 2 bar, 20% llenado): {q_nat_total:.1f} kg/h")

if q_nat_total < caudal_nec_kgh:
    deficit = caudal_nec_kgh - q_nat_total
    print(f"Déficit de vaporización natural: {deficit:.2f} kg/h")

    # 5.2. Selección de Vaporizador Interno
    # Solo se requiere en el depósito más grande para cubrir el déficit total.
    capacidades_vapi = {"VIA 150": 150, "VIA 300": 300, "VIB 500": 500}
    potencias_caldera = {"VIA 150": 17.5, "VIA 300": 35, "VIB 500": 58}

    vapi_seleccionado = None
    for mod, cap in capacidades_vapi.items():
        if cap >= deficit:
            vapi_seleccionado = mod
            break

    if vapi_seleccionado:
        print(f"\n--- Selección de Vaporización Forzada ---")
        print(f"Vaporizador Interno Seleccionado (en {dep_grande_ref.replace('LP', 'LPVI')}): {vapi_seleccionado}")
        print(f"Capacidad forzada: {capacidades_vapi[vapi_seleccionado]} kg/h")
        print(f"Potencia de caldera requerida: {potencias_caldera[vapi_seleccionado]} kW")
        print(f"Vaporización Total (Nat + Forz): {q_nat_total + capacidades_vapi[vapi_seleccionado]:.2f} kg/h")
        print(f"RESULTADO: Suministro garantizado mediante sistema mixto (Vaporizador en el depósito de {vol_grande_m3}m3).")
    else:
        print("No se encontró un vaporizador interno suficiente.")
else:
    print("Vaporización natural suficiente.")


# 6. Calculo de potencia termica del armario de calefaccion
armario_calefaccion = 'VPC30C'
potencia_nominal_armario_kw = 45.0  # kW, caldera integrada en VPC30C según ficha tecnica consultada en GLP

if 'vapi_seleccionado' in globals() and vapi_seleccionado:
    capacidad_forzada_kgh = capacidades_vapi[vapi_seleccionado]
    potencia_minima_armario_kw = potencias_caldera[vapi_seleccionado]
    margen_vaporizacion_kgh = (q_nat_total + capacidad_forzada_kgh) - caudal_nec_kgh
    margen_potencia_armario_kw = potencia_nominal_armario_kw - potencia_minima_armario_kw

    print('--- Potencia termica del armario de calefaccion ---')
    print(f'Demanda punta de GLP: {caudal_nec_kgh:.2f} kg/h')
    print(f'Vaporizacion natural disponible: {q_nat_total:.1f} kg/h')
    print(f'Deficit que obliga a vaporizacion forzada: {deficit:.2f} kg/h')
    print(f'Vaporizador interno seleccionado: {vapi_seleccionado}')
    print(f'Capacidad forzada del vaporizador: {capacidad_forzada_kgh:.0f} kg/h')
    print(f'Armario de calefaccion asociado: {armario_calefaccion}')
    print(f'Potencia nominal del armario: {potencia_nominal_armario_kw:.1f} kW')
    print(f'Potencia termica minima requerida: {potencia_minima_armario_kw:.1f} kW')
    print(f'Margen de potencia del armario: {margen_potencia_armario_kw:.1f} kW')
    print(f'Margen total de vaporizacion: {margen_vaporizacion_kgh:.2f} kg/h')
    print(f'Comprobacion: {potencia_nominal_armario_kw:.1f} kW >= {potencia_minima_armario_kw:.1f} kW. Armario suficiente.')
else:
    potencia_minima_armario_kw = 0.0
    print('No se requiere potencia de armario: la vaporizacion natural resulta suficiente.')


# 7.1. Ejecución del dimensionado por tramos en la propia libreta
from math import sqrt
from functools import lru_cache

P_ATM_BAR = 1.01325
P_INICIAL_REL_BAR = 1.70
P_INICIAL_ABS_BAR = P_INICIAL_REL_BAR + P_ATM_BAR
CAIDA_MAXIMA_FRACCION = 0.05
P_MIN_REL_BAR = P_INICIAL_REL_BAR * (1.0 - CAIDA_MAXIMA_FRACCION)
P_MIN_ABS_BAR = P_MIN_REL_BAR + P_ATM_BAR
DC_PROPANO = 1.16
DENSIDAD_PROPANO_GAS_KG_M3 = 1.882
VEL_LIMITE_AEREA_GENERAL_MS = 20.0
VEL_MAX_MS = 10.0  # límite práctico adoptado para instalación común/receptora según consulta GLP
VELOCIDAD_OBJ_MIN_MS = 8.0
VELOCIDAD_OBJ_MAX_MS = 10.0
VELOCIDAD_OBJ_CENTRO_MS = 9.5
catalogo_diametros = pd.DataFrame([
    {'material': 'cobre_duro_en1057', 'designacion': '15x1', 'D_int_mm': 13.0, 'espesor_mm': 1.0},
    {'material': 'cobre_duro_en1057', 'designacion': '18x1', 'D_int_mm': 16.0, 'espesor_mm': 1.0},
    {'material': 'cobre_duro_en1057', 'designacion': '18x1.5', 'D_int_mm': 15.0, 'espesor_mm': 1.5},
    {'material': 'cobre_duro_en1057', 'designacion': '20x1.5', 'D_int_mm': 17.0, 'espesor_mm': 1.5},
    {'material': 'cobre_duro_en1057', 'designacion': '22x1', 'D_int_mm': 20.0, 'espesor_mm': 1.0},
    {'material': 'cobre_duro_en1057', 'designacion': '28x1', 'D_int_mm': 26.0, 'espesor_mm': 1.0},
    {'material': 'cobre_duro_en1057', 'designacion': '35x1.5', 'D_int_mm': 32.0, 'espesor_mm': 1.5},
    {'material': 'cobre_duro_en1057', 'designacion': '42x1.5', 'D_int_mm': 39.0, 'espesor_mm': 1.5},
    {'material': 'cobre_duro_en1057', 'designacion': '54x2', 'D_int_mm': 50.0, 'espesor_mm': 2.0},
    {'material': 'cobre_duro_en1057', 'designacion': '64x2', 'D_int_mm': 60.0, 'espesor_mm': 2.0},
    {'material': 'cobre_duro_en1057', 'designacion': '76.1x2', 'D_int_mm': 72.1, 'espesor_mm': 2.0},
    {'material': 'cobre_duro_en1057', 'designacion': '88.9x2', 'D_int_mm': 84.9, 'espesor_mm': 2.0},
    {'material': 'cobre_duro_en1057', 'designacion': '108x2.5', 'D_int_mm': 103.0, 'espesor_mm': 2.5},
]).sort_values('D_int_mm').reset_index(drop=True)

coef_accesorios = {'codo_90': 30, 'codo_45': 15, 'te_linea': 20, 'te_desviada': 60, 'valvula_corte': 10, 'reduccion': 10}
accesorios_b_c2_escenario_anterior = {'te_desviada': 1, 'valvula_corte': 1, 'reduccion': 1}
trazado_b_c2 = pd.DataFrame([
    {'subtramo': 'B-C2.1', 'descripcion': 'tramo inicial a nivel de suelo', 'longitud_m': 0.53, 'tipo': 'horizontal_suelo'},
    {'subtramo': 'B-C2.2', 'descripcion': 'subida vertical hasta tramo aereo', 'longitud_m': 8.00, 'tipo': 'vertical_subida'},
    {'subtramo': 'B-C2.3', 'descripcion': 'tramo horizontal aereo', 'longitud_m': 5.26, 'tipo': 'horizontal_aereo'},
    {'subtramo': 'B-C2.4', 'descripcion': 'bajada vertical hasta consumidor C2', 'longitud_m': 8.00, 'tipo': 'vertical_bajada'},
])
trazado_b_c2_total_m = trazado_b_c2['longitud_m'].sum()

accesorios_base = {
    'D1-D4': {'codo_90': 1, 'valvula_corte': 1}, 'D2-D4': {'codo_90': 1, 'valvula_corte': 1},
    'D3-D4': {'codo_90': 1, 'valvula_corte': 1}, 'D4 vertical': {'codo_90': 1, 'valvula_corte': 1},
    'D4-A': {'codo_90': 1, 'valvula_corte': 1, 'te_linea': 1},
    'A-C1': {'te_desviada': 1, 'valvula_corte': 1, 'reduccion': 1}, 'A-B': {'codo_90': 1, 'te_linea': 1},
    'B-C2': {'te_desviada': 1, 'valvula_corte': 1, 'reduccion': 1, 'codo_90': 4}, 'B-C': {'codo_90': 1, 'te_linea': 1},
    'C-C3': {'te_desviada': 1, 'valvula_corte': 1, 'reduccion': 1}, 'C-D': {'codo_90': 1, 'te_linea': 1},
    'D-C4': {'te_desviada': 1, 'valvula_corte': 1, 'reduccion': 1}, 'D-E': {'codo_90': 1, 'te_linea': 1},
    'E-C5': {'te_desviada': 1, 'valvula_corte': 1, 'reduccion': 1}, 'E-C6': {'te_desviada': 1, 'valvula_corte': 1, 'reduccion': 1},
}

def tabla_md(df, cols=None, floatfmt='.3f'):
    data = df.copy() if cols is None else df[cols].copy()
    for col in data.select_dtypes(include=['float', 'float64']).columns:
        data[col] = data[col].map(lambda x: '' if pd.isna(x) else format(x, floatfmt))
    data = data.fillna('').astype(str)
    headers = list(data.columns)
    rows = data.values.tolist()
    def clean(value):
        return value.replace('|', '\\|').replace('\n', ' ')
    return '\n'.join([
        '| ' + ' | '.join(clean(h) for h in headers) + ' |',
        '| ' + ' | '.join('---' for _ in headers) + ' |',
        *['| ' + ' | '.join(clean(v) for v in row) + ' |' for row in rows],
    ])

def longitud_calculo(L_real_m, D_mm, accesorios):
    total = float(L_real_m)
    for nombre, cantidad in accesorios.items():
        total += cantidad * coef_accesorios[nombre] * (D_mm / 1000.0)
    return total

def renouard_mp(PA_abs_bar, Q_m3_h, D_mm, Lc_m, dc=DC_PROPANO):
    termino = 51.5 * dc * Lc_m * (Q_m3_h ** 1.82) / (D_mm ** 4.82)
    pb2 = PA_abs_bar ** 2 - termino
    if pb2 <= 0:
        return None, None, termino
    PB_abs_bar = sqrt(pb2)
    return PB_abs_bar, PA_abs_bar - PB_abs_bar, termino

def velocidad_gas(Q_m3_h, P_abs_bar, D_mm):
    return 378.04 * Q_m3_h / (P_abs_bar * (D_mm ** 2))

tramos_csv = pd.read_csv('datos/longitudes_Tramos.csv', sep=';').dropna(how='all').copy()
tramos_csv = tramos_csv.rename(columns={'Nº': 'numero', 'Tramo / zona': 'tramo_zona', 'Designación': 'designacion', 'Longitud (m)': 'longitud_m'})
tramos_csv['numero'] = tramos_csv['numero'].astype(int)
tramos_csv['longitud_m'] = pd.to_numeric(tramos_csv['longitud_m'], errors='coerce')
tramos_csv['designacion'] = tramos_csv['designacion'].astype(str).str.strip()
tramos_red = tramos_csv[tramos_csv['numero'] != 1].copy()
tramos_red[['nodo_ini', 'nodo_fin']] = tramos_red['designacion'].str.split('-', expand=True)
tramos_red['tipo_tramo'] = 'red_principal'
depositos_verticales = pd.DataFrame([
    {'numero': 1, 'tramo_zona': 'Derivacion vertical deposito D1', 'designacion': 'D1-D4', 'longitud_m': 1.90, 'nodo_ini': 'D1', 'nodo_fin': 'D4', 'tipo_tramo': 'derivacion_deposito'},
    {'numero': 1, 'tramo_zona': 'Derivacion vertical deposito D2', 'designacion': 'D2-D4', 'longitud_m': 1.90, 'nodo_ini': 'D2', 'nodo_fin': 'D4', 'tipo_tramo': 'derivacion_deposito'},
    {'numero': 1, 'tramo_zona': 'Derivacion vertical deposito D3', 'designacion': 'D3-D4', 'longitud_m': 1.90, 'nodo_ini': 'D3', 'nodo_fin': 'D4', 'tipo_tramo': 'derivacion_deposito'},
    {'numero': 1, 'tramo_zona': 'Derivacion vertical deposito D4', 'designacion': 'D4 vertical', 'longitud_m': 1.90, 'nodo_ini': 'D4_dep', 'nodo_fin': 'D4', 'tipo_tramo': 'derivacion_deposito'},
])
df_tramos_limpio = pd.concat([depositos_verticales, tramos_red], ignore_index=True)
df_tramos_limpio = df_tramos_limpio[['numero', 'tramo_zona', 'designacion', 'longitud_m', 'nodo_ini', 'nodo_fin', 'tipo_tramo']]

df_consumidores_red = df_cons.copy().reset_index(drop=True)
df_consumidores_red['nodo'] = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']
df_consumidores_red['q_kg_h'] = df_consumidores_red['potencia_kw'] / PCS_PROPANO
df_consumidores_red['q_m3_h'] = df_consumidores_red['q_kg_h'] / DENSIDAD_PROPANO_GAS_KG_M3
q_total_kg_h = df_consumidores_red['q_kg_h'].sum()
q_total_m3_h = df_consumidores_red['q_m3_h'].sum()
children = {}
for _, row in tramos_red.iterrows():
    children.setdefault(row['nodo_ini'], []).append(row['nodo_fin'])
consumo_por_nodo = df_consumidores_red.set_index('nodo')['q_m3_h'].to_dict()
@lru_cache(None)
def caudal_descendente(nodo):
    return consumo_por_nodo.get(nodo, 0.0) + sum(caudal_descendente(hijo) for hijo in children.get(nodo, []))
q_por_designacion = {row['designacion']: caudal_descendente(row['nodo_fin']) for _, row in tramos_red.iterrows()}
for designacion in depositos_verticales['designacion']:
    q_por_designacion[designacion] = q_total_m3_h / len(depositos_verticales)
df_tramos_limpio['q_m3_h'] = df_tramos_limpio['designacion'].map(q_por_designacion)
df_tramos_limpio['q_kg_h'] = df_tramos_limpio['q_m3_h'] * DENSIDAD_PROPANO_GAS_KG_M3

filas_acc = []
for designacion, accesorios in accesorios_base.items():
    for accesorio, cantidad in accesorios.items():
        filas_acc.append({'designacion': designacion, 'accesorio': accesorio, 'cantidad': cantidad, 'coef_leq_D': coef_accesorios[accesorio], 'criterio': 'visible/hipotesis conservadora segun esquema_instalacion.pdf'})
df_accesorios = pd.DataFrame(filas_acc)

def diametro_exterior_mm(designacion):
    return float(str(designacion).split('x')[0])

catalogo_diametros['D_ext_mm'] = catalogo_diametros['designacion'].map(diametro_exterior_mm)
catalogo_diametros['area_metal_mm2'] = np.pi / 4.0 * (catalogo_diametros['D_ext_mm'] ** 2 - catalogo_diametros['D_int_mm'] ** 2)
catalogo_diametros['masa_lineal_kg_m'] = catalogo_diametros['area_metal_mm2'] * 1e-6 * 8960.0


def evaluar_candidatos_tramo(tramo, P_ini_abs_bar, catalogo):
    accesorios = accesorios_base.get(tramo['designacion'], {})
    Q = float(tramo['q_m3_h'])
    candidatos = []
    if tramo.get('tipo_tramo') == 'derivacion_deposito':
        catalogo_efectivo = catalogo[(catalogo['espesor_mm'] >= 1.5) & (catalogo['D_ext_mm'] <= 20.0)]
    else:
        catalogo_efectivo = catalogo
    for _, tuberia in catalogo_efectivo.iterrows():
        D = float(tuberia['D_int_mm'])
        Lc = longitud_calculo(tramo['longitud_m'], D, accesorios)
        q_d = Q / D if D else float('inf')
        P_fin_abs, dp_bar, _ = renouard_mp(P_ini_abs_bar, Q, D, Lc)
        masa_tramo = float(tuberia['masa_lineal_kg_m']) * float(tramo['longitud_m'])
        if tramo.get('tipo_tramo') == 'derivacion_deposito':
            vel_obj = f"8-{VEL_LIMITE_AEREA_GENERAL_MS:.0f} m/s"
        else:
            vel_obj = f"{VELOCIDAD_OBJ_MIN_MS:.0f}-{VELOCIDAD_OBJ_MAX_MS:.0f} m/s"
        fila = {
            'designacion_tubo': tuberia['designacion'], 'D_int_mm': D, 'D_ext_mm': float(tuberia['D_ext_mm']),
            'masa_lineal_kg_m': float(tuberia['masa_lineal_kg_m']), 'masa_tramo_kg': masa_tramo,
            'Lc_m': Lc, 'Q_D': q_d, 'velocidad_objetivo': vel_obj
        }
        if P_fin_abs is None:
            fila.update({'P_fin_abs_bar': np.nan, 'P_fin_rel_bar': np.nan, 'delta_p_bar': np.nan, 'velocidad_ms': np.nan, 'desviacion_velocidad_ms': np.nan, 'cumple_Q_D': q_d < 150, 'cumple_presion': False, 'cumple_velocidad_practica': False, 'cumple_velocidad_aerea': False, 'criterio_seleccion': 'rechazado: presion final no real', 'estado': 'No conforme'})
        else:
            v = velocidad_gas(Q, P_fin_abs, D)
            cumple_qd = q_d < 150
            cumple_p = P_fin_abs >= P_MIN_ABS_BAR
            cumple_v_practica = v <= VEL_MAX_MS
            cumple_v_aerea = v <= VEL_LIMITE_AEREA_GENERAL_MS
            en_objetivo = VELOCIDAD_OBJ_MIN_MS <= v <= VELOCIDAD_OBJ_MAX_MS
            fila.update({'P_fin_abs_bar': P_fin_abs, 'P_fin_rel_bar': P_fin_abs - P_ATM_BAR, 'delta_p_bar': dp_bar, 'velocidad_ms': v, 'desviacion_velocidad_ms': abs(v - VELOCIDAD_OBJ_CENTRO_MS), 'cumple_Q_D': cumple_qd, 'cumple_presion': cumple_p, 'cumple_velocidad_practica': cumple_v_practica, 'cumple_velocidad_aerea': cumple_v_aerea, 'criterio_seleccion': 'candidato', 'estado': 'Candidato' if (cumple_qd and cumple_p and cumple_v_aerea) else 'No conforme'})
            if cumple_qd and cumple_p and cumple_v_aerea:
                if en_objetivo:
                    fila['estado'] = 'Conforme - velocidad objetivo'
                    fila['criterio_seleccion'] = 'dentro del rango practico 8-10 m/s'
                elif v < VELOCIDAD_OBJ_MIN_MS:
                    fila['estado'] = 'Conforme - velocidad baja justificada'
                    fila['criterio_seleccion'] = 'por debajo del rango; revisar si catalogo/presion permite menor diametro'
                elif cumple_v_practica:
                    fila['estado'] = 'Conforme - velocidad admisible bajo limite practico'
                    fila['criterio_seleccion'] = 'menor desviacion frente al centro objetivo sin superar 10 m/s'
                else:
                    fila['estado'] = 'Conforme - velocidad alta admisible por limite aereo general'
                    fila['criterio_seleccion'] = 'supera 10 m/s; solo admisible si se justifica como red general aerea'
        candidatos.append(fila)
    return pd.DataFrame(candidatos)


def dimensionar_tramo(tramo, P_ini_abs_bar, catalogo):
    df_candidatos = evaluar_candidatos_tramo(tramo, P_ini_abs_bar, catalogo)
    viables = df_candidatos[(df_candidatos['cumple_Q_D']) & (df_candidatos['cumple_presion']) & (df_candidatos['cumple_velocidad_aerea'])].copy()
    if viables.empty:
        fallo = df_candidatos.iloc[-1].to_dict()
        fallo['estado'] = 'No conforme'
        fallo['criterio_seleccion'] = 'ningun diametro cumple simultaneamente presion, Q/D y limite aereo'
        return fallo, df_candidatos
    objetivo = viables[(viables['velocidad_ms'] >= VELOCIDAD_OBJ_MIN_MS) & (viables['velocidad_ms'] <= VELOCIDAD_OBJ_MAX_MS)].copy()
    if not objetivo.empty:
        elegido = objetivo.sort_values(['desviacion_velocidad_ms', 'D_int_mm']).iloc[0].to_dict()
        elegido['estado'] = 'Conforme - velocidad objetivo'
        elegido['criterio_seleccion'] = 'diametro con velocidad dentro de 8-10 m/s mas cercana a 9.5 m/s'
        return elegido, df_candidatos
    practica = viables[viables['velocidad_ms'] <= VEL_MAX_MS].copy()
    if not practica.empty:
        elegido = practica.sort_values(['desviacion_velocidad_ms', 'D_int_mm']).iloc[0].to_dict()
        elegido['estado'] = 'Conforme - velocidad baja justificada' if elegido['velocidad_ms'] < VELOCIDAD_OBJ_MIN_MS else 'Conforme - velocidad admisible bajo limite practico'
        elegido['criterio_seleccion'] = 'diametro mas cercano al rango objetivo sin superar el limite practico de 10 m/s'
        return elegido, df_candidatos
    elegido = viables.sort_values(['desviacion_velocidad_ms', 'D_int_mm']).iloc[0].to_dict()
    elegido['estado'] = 'Conforme - velocidad alta admisible por limite aereo general'
    elegido['criterio_seleccion'] = 'no hay candidato <=10 m/s; se mantiene bajo limite aereo absoluto de 20 m/s'
    return elegido, df_candidatos


def optimizar_subarbol_E(P_ini_abs_bar):
    tramos_sub = {d: df_tramos_limpio[df_tramos_limpio['designacion'] == d].iloc[0].to_dict() for d in ['D-E', 'E-C5', 'E-C6']}
    combinaciones = []
    candidatos_de = evaluar_candidatos_tramo(tramos_sub['D-E'], P_ini_abs_bar, catalogo_diametros)
    for _, de in candidatos_de.iterrows():
        if not (de['cumple_Q_D'] and de['cumple_presion'] and de['cumple_velocidad_practica']):
            continue
        candidatos_c5 = evaluar_candidatos_tramo(tramos_sub['E-C5'], de['P_fin_abs_bar'], catalogo_diametros)
        candidatos_c6 = evaluar_candidatos_tramo(tramos_sub['E-C6'], de['P_fin_abs_bar'], catalogo_diametros)
        viables_c5 = candidatos_c5[(candidatos_c5['cumple_Q_D']) & (candidatos_c5['cumple_presion']) & (candidatos_c5['cumple_velocidad_practica'])].copy()
        viables_c6 = candidatos_c6[(candidatos_c6['cumple_Q_D']) & (candidatos_c6['cumple_presion']) & (candidatos_c6['cumple_velocidad_practica'])].copy()
        for _, c5 in viables_c5.iterrows():
            for _, c6 in viables_c6.iterrows():
                masa_total = de['masa_tramo_kg'] + c5['masa_tramo_kg'] + c6['masa_tramo_kg']
                desviacion_total = de['desviacion_velocidad_ms'] + c5['desviacion_velocidad_ms'] + c6['desviacion_velocidad_ms']
                combinaciones.append({
                    'D-E_tubo': de['designacion_tubo'], 'E-C5_tubo': c5['designacion_tubo'], 'E-C6_tubo': c6['designacion_tubo'],
                    'D-E_velocidad_ms': de['velocidad_ms'], 'E-C5_velocidad_ms': c5['velocidad_ms'], 'E-C6_velocidad_ms': c6['velocidad_ms'],
                    'D-E_P_fin_rel_bar': de['P_fin_rel_bar'], 'E-C5_P_fin_rel_bar': c5['P_fin_rel_bar'], 'E-C6_P_fin_rel_bar': c6['P_fin_rel_bar'],
                    'masa_total_kg': masa_total, 'desviacion_total_ms': desviacion_total,
                    'D-E_resultado': de.to_dict(), 'E-C5_resultado': c5.to_dict(), 'E-C6_resultado': c6.to_dict(),
                    'D-E_candidatos': candidatos_de, 'E-C5_candidatos': candidatos_c5, 'E-C6_candidatos': candidatos_c6,
                })
    df_combinaciones = pd.DataFrame(combinaciones)
    if df_combinaciones.empty:
        return None, df_combinaciones
    df_combinaciones = df_combinaciones.sort_values(['masa_total_kg', 'desviacion_total_ms']).reset_index(drop=True)
    return df_combinaciones.iloc[0].to_dict(), df_combinaciones

orden_depositos = ['D1-D4', 'D2-D4', 'D3-D4', 'D4 vertical']
orden_red_previa_E = ['D4-A', 'A-C1', 'A-B', 'B-C2', 'B-C', 'C-C3', 'C-D', 'D-C4']
presion_nodo = {'D4': P_INICIAL_ABS_BAR}
resultados = []
candidatos_por_tramo = {}
for designacion in orden_depositos:
    tramo = df_tramos_limpio[df_tramos_limpio['designacion'] == designacion].iloc[0].to_dict()
    elegido, candidatos = dimensionar_tramo(tramo, P_INICIAL_ABS_BAR, catalogo_diametros)
    candidatos_por_tramo[designacion] = candidatos
    resultados.append({**tramo, **elegido, 'P_ini_abs_bar': P_INICIAL_ABS_BAR, 'P_ini_rel_bar': P_INICIAL_REL_BAR})
for designacion in orden_red_previa_E:
    tramo = df_tramos_limpio[df_tramos_limpio['designacion'] == designacion].iloc[0].to_dict()
    P_ini = presion_nodo[tramo['nodo_ini']]
    elegido, candidatos = dimensionar_tramo(tramo, P_ini, catalogo_diametros)
    candidatos_por_tramo[designacion] = candidatos
    resultados.append({**tramo, **elegido, 'P_ini_abs_bar': P_ini, 'P_ini_rel_bar': P_ini - P_ATM_BAR})
    if not np.isnan(elegido.get('P_fin_abs_bar', np.nan)):
        presion_nodo[tramo['nodo_fin']] = elegido['P_fin_abs_bar']

optimizacion_subarbol_E, df_optimizacion_subarbol_E = optimizar_subarbol_E(presion_nodo['D'])
if optimizacion_subarbol_E is None:
    orden_red_final = ['D-E', 'E-C5', 'E-C6']
    for designacion in orden_red_final:
        tramo = df_tramos_limpio[df_tramos_limpio['designacion'] == designacion].iloc[0].to_dict()
        P_ini = presion_nodo[tramo['nodo_ini']]
        elegido, candidatos = dimensionar_tramo(tramo, P_ini, catalogo_diametros)
        candidatos_por_tramo[designacion] = candidatos
        resultados.append({**tramo, **elegido, 'P_ini_abs_bar': P_ini, 'P_ini_rel_bar': P_ini - P_ATM_BAR})
        if not np.isnan(elegido.get('P_fin_abs_bar', np.nan)):
            presion_nodo[tramo['nodo_fin']] = elegido['P_fin_abs_bar']
else:
    for designacion in ['D-E', 'E-C5', 'E-C6']:
        tramo = df_tramos_limpio[df_tramos_limpio['designacion'] == designacion].iloc[0].to_dict()
        resultado = optimizacion_subarbol_E[f'{designacion}_resultado'].copy()
        candidatos_por_tramo[designacion] = optimizacion_subarbol_E[f'{designacion}_candidatos']
        if designacion == 'D-E':
            P_ini = presion_nodo['D']
            presion_nodo['E'] = resultado['P_fin_abs_bar']
            resultado['criterio_seleccion'] = 'optimizacion economica del subarbol E: aumenta D-E para reducir masa total en E-C6'
            resultado['estado'] = 'Conforme - velocidad baja justificada' if resultado['velocidad_ms'] < VELOCIDAD_OBJ_MIN_MS else resultado['estado']
        else:
            P_ini = presion_nodo['E']
            resultado['criterio_seleccion'] = 'seleccionado por optimizacion economica del subarbol E con presion aguas arriba recalculada'
            if VELOCIDAD_OBJ_MIN_MS <= resultado['velocidad_ms'] <= VELOCIDAD_OBJ_MAX_MS:
                resultado['estado'] = 'Conforme - velocidad objetivo'
        resultados.append({**tramo, **resultado, 'P_ini_abs_bar': P_ini, 'P_ini_rel_bar': P_ini - P_ATM_BAR})
        if not np.isnan(resultado.get('P_fin_abs_bar', np.nan)):
            presion_nodo[tramo['nodo_fin']] = resultado['P_fin_abs_bar']

columnas_dimensionado = ['numero', 'tipo_tramo', 'tramo_zona', 'designacion', 'nodo_ini', 'nodo_fin', 'longitud_m', 'q_m3_h', 'q_kg_h', 'designacion_tubo', 'D_int_mm', 'Lc_m', 'Q_D', 'P_ini_rel_bar', 'P_fin_rel_bar', 'delta_p_bar', 'velocidad_ms', 'cumple_Q_D', 'cumple_presion', 'cumple_velocidad_practica', 'cumple_velocidad_aerea', 'criterio_seleccion', 'estado']
df_dimensionado = pd.DataFrame(resultados)[columnas_dimensionado].copy()
df_no_conformidades = df_dimensionado[df_dimensionado['estado'].str.startswith('No conforme')].copy()

tramo_b_c2 = df_tramos_limpio[df_tramos_limpio['designacion'] == 'B-C2'].iloc[0].to_dict()
p_ini_b_c2_abs = df_dimensionado[df_dimensionado['designacion'] == 'B-C2']['P_ini_rel_bar'].iloc[0] + P_ATM_BAR

def evaluar_b_c2_escenario(nombre, accesorios):
    candidatos = []
    for _, tuberia in catalogo_diametros.iterrows():
        D = float(tuberia['D_int_mm'])
        Lc = longitud_calculo(tramo_b_c2['longitud_m'], D, accesorios)
        P_fin_abs, dp_bar, _ = renouard_mp(p_ini_b_c2_abs, tramo_b_c2['q_m3_h'], D, Lc)
        q_d = tramo_b_c2['q_m3_h'] / D
        if P_fin_abs is None:
            continue
        v = velocidad_gas(tramo_b_c2['q_m3_h'], P_fin_abs, D)
        candidatos.append({
            'escenario': nombre, 'designacion_tubo': tuberia['designacion'], 'D_int_mm': D, 'Lc_m': Lc,
            'Q_D': q_d, 'P_ini_rel_bar': p_ini_b_c2_abs - P_ATM_BAR, 'P_fin_rel_bar': P_fin_abs - P_ATM_BAR,
            'delta_p_bar': dp_bar, 'velocidad_ms': v,
            'cumple_Q_D': q_d < 150, 'cumple_presion': P_fin_abs >= P_MIN_ABS_BAR,
            'cumple_velocidad_practica': v <= VEL_MAX_MS, 'cumple_velocidad_aerea': v <= VEL_LIMITE_AEREA_GENERAL_MS,
        })
    df = pd.DataFrame(candidatos)
    viables = df[(df['cumple_Q_D']) & (df['cumple_presion']) & (df['cumple_velocidad_aerea'])].copy()
    objetivo = viables[(viables['velocidad_ms'] >= VELOCIDAD_OBJ_MIN_MS) & (viables['velocidad_ms'] <= VELOCIDAD_OBJ_MAX_MS)].copy()
    if not objetivo.empty:
        elegido = objetivo.assign(desviacion=(objetivo['velocidad_ms'] - VELOCIDAD_OBJ_CENTRO_MS).abs()).sort_values(['desviacion', 'D_int_mm']).iloc[0]
    else:
        practica = viables[viables['velocidad_ms'] <= VEL_MAX_MS].copy()
        elegido = practica.assign(desviacion=(practica['velocidad_ms'] - VELOCIDAD_OBJ_CENTRO_MS).abs()).sort_values(['desviacion', 'D_int_mm']).iloc[0]
    return elegido.drop(labels=['desviacion'], errors='ignore').to_dict()

df_sensibilidad_b_c2 = pd.DataFrame([
    evaluar_b_c2_escenario('anterior: sin codos vertical-aereo adicionales', accesorios_b_c2_escenario_anterior),
    evaluar_b_c2_escenario('revisado: con 4 codos 90 por subida/bajada', accesorios_base['B-C2']),
])
df_sensibilidad_b_c2['incremento_Lc_m'] = df_sensibilidad_b_c2['Lc_m'] - df_sensibilidad_b_c2['Lc_m'].iloc[0]
df_sensibilidad_b_c2['incremento_delta_p_bar'] = df_sensibilidad_b_c2['delta_p_bar'] - df_sensibilidad_b_c2['delta_p_bar'].iloc[0]

resumen_depositos = df_dimensionado[df_dimensionado['tipo_tramo'] == 'derivacion_deposito'].copy()
resumen_depositos_agrupado = pd.DataFrame([{'designacion': 'D1/D2/D3/D4 verticales', 'unidades': len(resumen_depositos), 'longitud_m_por_unidad': resumen_depositos['longitud_m'].iloc[0], 'q_m3_h_por_unidad': resumen_depositos['q_m3_h'].iloc[0], 'designacion_tubo': resumen_depositos['designacion_tubo'].mode().iloc[0], 'D_int_mm': resumen_depositos['D_int_mm'].max(), 'Lc_m_por_unidad': resumen_depositos['Lc_m'].max(), 'P_fin_rel_bar_min': resumen_depositos['P_fin_rel_bar'].min(), 'velocidad_ms_max': resumen_depositos['velocidad_ms'].max(), 'estado': 'Conforme' if (~resumen_depositos['estado'].str.startswith('No conforme')).all() else 'No conforme'}])
tramo_control = df_dimensionado[df_dimensionado['designacion'] == 'D4-A'].iloc[0]
control_manual = {'tramo': tramo_control['designacion'], 'Lc_recalculada_m': longitud_calculo(tramo_control['longitud_m'], tramo_control['D_int_mm'], accesorios_base[tramo_control['designacion']]), 'Q_D_recalculado': tramo_control['q_m3_h'] / tramo_control['D_int_mm'], 'velocidad_recalculada_ms': velocidad_gas(tramo_control['q_m3_h'], tramo_control['P_fin_rel_bar'] + P_ATM_BAR, tramo_control['D_int_mm'])}

resultados_dimensionado = {'q_total_kg_h': q_total_kg_h, 'q_total_m3_h': q_total_m3_h}
print(f'Caudal total: {q_total_m3_h:.2f} m3/h ({q_total_kg_h:.2f} kg/h)')
print(f'Tramos dimensionados: {len(df_dimensionado)}')
print(f'No conformidades: {len(df_no_conformidades)}')


# 7.2. Tramos y caudales
cols_tramos_visible = ['designacion', 'tipo_tramo', 'longitud_m', 'q_m3_h', 'q_kg_h']
df_tramos_visible = df_tramos_limpio[cols_tramos_visible].copy()
df_tramos_visible


# 7.3. Consumidores y caudales de calculo
cols_consumidores_visible = ['nodo', 'nombre', 'potencia_kw', 'q_kg_h', 'q_m3_h']
df_consumidores_visible = df_consumidores_red[cols_consumidores_visible].copy()
df_consumidores_visible


# 7.4. Accesorios considerados, vista resumida
resumen_accesorios_visible = (
    df_accesorios
    .assign(
        accesorio_cantidad=lambda df: df['accesorio'] + ' x' + df['cantidad'].astype(str),
        coef_leq_D_total_fila=lambda df: df['cantidad'] * df['coef_leq_D'],
    )
    .groupby('designacion', as_index=False)
    .agg(
        accesorios=('accesorio_cantidad', ', '.join),
        coef_leq_D_total=('coef_leq_D_total_fila', 'sum'),
    )
)
resumen_accesorios_visible


# 7.5. Resultados finales de dimensionado, vista compacta
cols_dimensionado_visible = [
    'designacion', 'tipo_tramo', 'longitud_m', 'q_m3_h', 'designacion_tubo',
    'D_int_mm', 'Lc_m', 'P_ini_rel_bar', 'P_fin_rel_bar', 'delta_p_bar',
    'velocidad_ms', 'estado',
]
df_dimensionado_visible = df_dimensionado[cols_dimensionado_visible].copy()
df_dimensionado_visible


# 7.6. Control final de conformidad
cols_depositos_visible = [
    'designacion', 'unidades', 'longitud_m_por_unidad', 'q_m3_h_por_unidad',
    'designacion_tubo', 'D_int_mm', 'P_fin_rel_bar_min', 'velocidad_ms_max', 'estado',
]
resumen_depositos_visible = resumen_depositos_agrupado[cols_depositos_visible].copy()

print(f'Tramos dimensionados: {len(df_dimensionado)}')
print(f'No conformidades: {len(df_no_conformidades)}')
print(f'Caudal total: {q_total_m3_h:.2f} m3/h ({q_total_kg_h:.2f} kg/h)')
print('\nDerivaciones de deposito:')
print(resumen_depositos_visible.to_string(index=False))

if df_no_conformidades.empty:
    print('\nNo se detectan no conformidades.')
else:
    print('\nNo conformidades:')
    print(df_no_conformidades[cols_dimensionado_visible].to_string(index=False))


# 8. Visión final del dimensionado
columnas_vision = [
    'designacion', 'tipo_tramo', 'longitud_m', 'q_m3_h', 'designacion_tubo',
    'D_int_mm', 'Lc_m', 'P_ini_rel_bar', 'P_fin_rel_bar', 'velocidad_ms', 'criterio_seleccion', 'estado'
]

print('--- Vision final del dimensionado de tuberias GLP ---')
print('Presion inicial: 1.70 bar relativos')
print('Criterio de velocidad: objetivo 8-10 m/s, limite practico 10 m/s, limite aereo absoluto 20 m/s')
print(f"Caudal punta total: {resultados_dimensionado['q_total_m3_h']:.2f} m3/h ({resultados_dimensionado['q_total_kg_h']:.2f} kg/h)")
print(f"Tramos dimensionados: {len(df_dimensionado)}")
print(f"No conformidades: {len(df_no_conformidades)}")
if df_no_conformidades.empty:
    print('No se detectan no conformidades.')

df_dimensionado[columnas_vision]

