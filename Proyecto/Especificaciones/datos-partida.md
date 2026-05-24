# Memoria: Hipótesis y Datos de Partida

## 1. Identificación y Emplazamiento de las Instalaciones
La instalación de almacenamiento común y red de distribución se ubica en la parcela catastral **8638004TN8183N**, situada en el término municipal de León.
*   **Zona Climática:** León (Virgen del Camino).
*   **Temperatura Exterior de Cálculo:** Se adopta una temperatura mínima de diseño de **$-5\text{ ºC}$**, obtenida a partir de la *Guía técnica: Condiciones climáticas exteriores de proyecto* editada por el IDAE, seleccionando el percentil del $99,6\%$ para la estación meteorológica de referencia (León - Virgen del Camino). Esta hipótesis es crítica para garantizar el balance de vaporización natural de los depósitos en las condiciones más desfavorables del invierno leonés.

## 2. Reglamentación y Normas Técnicas Consideradas
El diseño y los cálculos de la instalación se realizan bajo el cumplimiento estricto del marco regulatorio aplicable en España:
*   **Real Decreto 919/2006:** *Reglamento técnico de distribución y utilización de combustibles gaseosos* y sus Instrucciones Técnicas Complementarias (ITC-ICG 01 a 11).
*   **Norma UNE 60250:2008:** *Instalaciones de almacenamiento de gases licuados del petróleo (GLP) en depósitos fijos para su consumo en instalaciones receptoras.*
*   **Norma UNE 60670:2014:** *Instalaciones receptoras de gas suministradas a presiones de operación de hasta 5 bar.*
*   **Código Técnico de la Edificación (CTE):** Documentos Básicos DB-SI (Seguridad en caso de incendio) y DB-SUA (Seguridad de utilización y accesibilidad).

## 3. Consumidores de la Planta (Grupo G1-1)
La instalación común de propano da suministro a seis receptores térmicos independientes que funcionan a turnos definidos por el régimen de producción de la fábrica:

| Consumidor | Identificación | Potencia Nominal ($P_n$) | Horas de Funcionamiento | Energía Diaria Demandada |
| :--- | :--- | :---: | :---: | :---: |
| Consumidor 1 | Horno de secado 1 | $60\text{ kW}$ | $12\text{ h/día}$ | $720\text{ kWh/día}$ |
| Consumidor 2 | Horno de secado 2 | $60\text{ kW}$ | $12\text{ h/día}$ | $720\text{ kWh/día}$ |
| Consumidor 3 | Caldera de vapor | $500\text{ kW}$ | $10\text{ h/día}$ | $5.000\text{ kWh/día}$ |
| Consumidor 4 | Caldera de agua caliente | $300\text{ kW}$ | $8\text{ h/día}$ | $2.400\text{ kWh/día}$ |
| Consumidor 5 | Horno de fusión | $700\text{ kW}$ | $4\text{ h/día}$ | $2.800\text{ kWh/día}$ |
| Consumidor 6 | Horno de decapado | $1.000\text{ kW}$ | $6\text{ h/día}$ | $6.000\text{ kWh/día}$ |
| **Total** | **Potencia Agregada** | **$2.620\text{ kW}$** | — | **$17.640\text{ kWh/día}$** |

## 4. Características del Gas Suministrado
Se adopta como combustible el **propano comercial** (según especificaciones técnicas normalizadas):
*   **Poder Calorífico Superior (PCS):** $13,95\text{ kWh/kg}$ ($12.000\text{ kcal/kg}$).
*   **Poder Calorífico Inferior (PCI):** $12,838\text{ kWh/kg}$ ($11.040\text{ kcal/kg}$).
*   **Densidad en Fase Líquida ($\rho_{liq}$):** $506\text{ kg/m}^3$ (a $15\text{ ºC}$).
*   **Densidad en Fase Gas ($\rho_{gas}$):** $1,882\text{ kg/m}^3$ (en condiciones normales de $1\text{ atm}$ y $0\text{ ºC}$).
*   **Densidad Relativa del Gas respecto al Aire ($d$):** $1,54$ (al ser mayor que 1, el propano es más pesado que el aire y tiende a acumularse en zonas bajas).
*   **Calor Latente de Vaporización (CLV):** $0,11\text{ kWh/kg}$ ($94,6\text{ kcal/kg}$).
*   **Temperatura de Equilibrio Líquido-Gas ($T_g$):** $-15\text{ ºC}$ (temperatura adoptada para el propano líquido dentro del tanque bajo condiciones de máxima evaporación).

## 5. Hipótesis Operativas y de Diseño
*   **Topología de la Red:** La canalización de gas será **enteramente aérea**, fijada sobre soportes y fachadas en el exterior del edificio, lo cual descarta la necesidad de zanjas, protección catódica activa por ánodos de sacrificio de magnesio, o problemas de flotabilidad de tuberías.
*   **Material de las Conducciones:** Se emplearán tuberías de **cobre desoxidado al fósforo** en barra (UNE-EN 1057), con un espesor mínimo de $1,0\text{ mm}$ en los tramos generales y $1,5\text{ mm}$ en las conexiones de servicio de los tanques.
*   **Presiones de Trabajo:** 
    *   Presión de diseño en Media Presión B (MPB): Presión inicial de regulación regulada a la salida del colector común de depósitos de **$1,7\text{ bar relativos}$**.
    *   Pérdida de carga admisible en la red exterior de distribución: máxima del $5\%$ de la presión de regulación ($0,085\text{ bar}$).
    *   Presión de utilización a la entrada de los quemadores: regulada localmente a **$37\text{ mbar}$** (Baja Presión / Media Presión A).
*   **Límites de Velocidad del Gas:** Se establece un límite de velocidad de circulación del fluido de **$10\text{ m/s}$** para la red general de distribución, extendiéndose a un límite de **$20\text{ m/s}$** únicamente en las tuberías cortas de interconexión y valvulería de la propia estación de almacenamiento.
*   **Coeficiente de Simultaneidad ($f_s$):** Dado el carácter industrial y continuo de los procesos de fabricación de la planta (hornos de fusión y decapado), se establece un coeficiente de simultaneidad **$f_s = 1$**. Se diseña para el escenario punta más desfavorable en el que todos los equipos demandan potencia máxima al mismo tiempo.

## Referencias relacionadas
- [Memoria: Demanda y caudales de cálculo](demanda-consumo.md)
- [Memoria: Autonomía de almacenamiento](autonomia.md)
- [Memoria: Red de distribución y regulación](red-distribucion.md)
- [Temperatura exterior de cálculo](../Anotaciones/temperatura_diseno.md)
- [Criterios normativos](../Anotaciones/criterios_normativos.md)
- [Caudales de consumidores](../Anotaciones/caudales_consumidores.md)
