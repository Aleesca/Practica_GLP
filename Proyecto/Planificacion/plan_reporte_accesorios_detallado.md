# Plan de Implementación: Reporte Detallado de Accesorios y Presupuesto de Cobre

Este documento detalla el plan de acción para generar el reporte unificado de accesorios, diámetros y presupuesto de tuberías de cobre de la instalación industrial de GLP, asegurando el cumplimiento de la normativa UNE y el uso de fuentes europeas contrastadas para precios.

## 1. Objetivos del Plan
1. **Inventario y Mapeo de Accesorios:** Consolidar el conteo de accesorios clave (válvulas de corte, codos, tes, reducciones, reguladores, vaporizadores) asociados a cada tramo de la red y a su correspondiente diámetro comercial (15x1, 22x1, 28x1, 42x1.5), partiendo de `calculos/datos/longitudes_Tramos.csv` y de los resultados de `dimensionado_tuberias_glp.md`.
2. **Presupuesto Basado en Fuentes Reales:** Obtener e incorporar precios reales del cobre en barra y accesorios a partir de distribuidores españoles especializados (Salvador Escoda, Obramat, Leroy Merlin), guardando los enlaces a las fuentes y descartando cualquier estimación o valor hipotético.
3. **Verificación Normativa UNE:** Analizar el cumplimiento del diseño frente a las normas UNE 60250 (área de almacenamiento) y UNE 60670 (red receptora aérea), detallando el estado de la tubería de `22x1` en los tramos verticales de depósito y ofreciendo una alternativa conforme a norma (`20x1.5` o `18x1.5`).

---

## 2. Estructura y Fases de Trabajo

### Fase 1: Inventario Detallado de Tramos y Accesorios
- **Acción:** Analizar `calculos/calculos.ipynb` y `Proyecto/Anotaciones/dimensionado_tuberias_glp.md` para extraer la relación unívoca entre tramos, diámetros y accesorios.
- **Detalle de Tramos:**
  - Tramos de depósito (`D1-D4`, `D2-D4`, `D3-D4`, `D4 vertical`): Diámetro `22x1` (20 mm interior), con 1 codo de 90° y 1 válvula de corte cada uno.
  - Tramo colector principal (`D4-A`): Diámetro `42x1.5` (39 mm interior), con 1 codo de 90°, 1 válvula de corte y 1 te en línea.
  - Tramos principales de distribución (`A-B`, `B-C`, `C-D`, `D-E`): Diámetro `42x1.5` (39 mm interior).
  - Tramos de derivación a consumidores:
    - `A-C1` (Horno 1): Diámetro `15x1` (13 mm interior).
    - `B-C2` (Horno 2): Diámetro `15x1` (13 mm interior) - con 4 codos de 90° por subida/bajada aérea.
    - `C-C3` (Caldera Vapor): Diámetro `22x1` (20 mm interior).
    - `D-C4` (Caldera Agua Caliente): Diámetro `15x1` (13 mm interior).
    - `E-C5` (Horno Fusión): Diámetro `22x1` (20 mm interior).
    - `E-C6` (Horno Decapado): Diámetro `28x1` (26 mm interior).
- **Entregable:** Tabla del inventario consolidado por tramos, identificando el tipo de accesorio (válvula de corte, codo, te, reductor) y su diámetro correspondiente.

### Fase 2: Recopilación de Tarifas y Referencias de Cobre
- **Acción:** Consolidar las tarifas reales de tubería de cobre rígido en barra (norma UNE-EN 1057) y de accesorios de cobre para soldar por capilaridad en el mercado español/europeo.
- **Detalle de Precios (referenciados):**
  - **Tubo Cobre 15x1 mm:** ~5,00 €/m (~12,50 € por barra de 2,5 m en Obramat).
  - **Tubo Cobre 22x1 mm:** ~7,26 €/m (~18,15 € por barra de 2,5 m en Obramat).
  - **Tubo Cobre 28x1 mm:** ~11,32 €/m (~28,29 € por barra de 2,5 m en Obramat).
  - **Tubo Cobre 42x1.5 mm:** ~25,00 - 30,00 €/m (según tarifa de Salvador Escoda).
  - **Tubo Cobre 18x1.5 mm (Alternativa UNE 60250):** ~10,72 €/m (según mercado español).
  - **Tubo Cobre 20x1.5 mm (Alternativa UNE 60250):** ~12,50 €/m (según mercado español).
  - **Accesorios (Codos, Tes, Reducciones, Válvulas):** Precios del mercado local (Giacomini R700, válvulas de corte UNE-EN 331, y accesorios de unión UNE-EN 1254-1).
- **Entregable:** Matriz de costes con las referencias guardadas de la web de distribuidores españoles contrastados.

### Fase 3: Elaboración del Presupuesto de la Instalación
- **Acción:** Multiplicar las longitudes geométricas de cada tramo y el número de accesorios por sus costes unitarios.
- **Detalle:**
  - Presupuesto Escenario Base (Dimensionado Actual): Utiliza la tubería `22x1` para las derivaciones verticales de depósito.
  - Presupuesto Escenario Alternativo (Cumplimiento UNE 60250): Sustituye la tubería de depósito por `20x1.5` o `18x1.5` de cobre para garantizar el cumplimiento del espesor mínimo de 1.5 mm exigido en el centro de almacenamiento.
- **Entregable:** Tabla comparativa de presupuestos para tuberías y accesorios.

### Fase 4: Justificación de Cumplimiento Normativo (UNE)
- **Acción:** Redactar la sección de verificación técnica:
  - **UNE 60250 (Centro de Almacenamiento):** Explicar que el cobre en la zona de depósitos debe tener un espesor mínimo de 1.5 mm y un diámetro exterior máximo de DN 20 (20 mm). Justificar la no conformidad de los tramos `D1-D4`, `D2-D4`, `D3-D4`, `D4 vertical` en su diseño de `22x1` (espesor insuficiente de 1 mm y diámetro excesivo de 22 mm). Proponer el cambio formal a `20x1.5` o `18x1.5` en el área de almacenamiento.
  - **UNE 60670 (Instalación Receptora Común/Individual):** Justificar que el resto de la red aérea (fuera del almacenamiento) con espesor de 1 mm (`15x1`, `28x1`) cumple la exigencia de espesor mínimo de 1 mm para trazados aéreos de cobre.
  - **UNE-EN 1254-1 / UNE 60250 (Accesorios de unión):** Especificar que las uniones deben realizarse por soldadura capilar fuerte (punto de fusión superior a 450 °C).

---

## 3. Entregable Final del Proyecto
El resultado se guardará en `Proyecto/Anotaciones/reporte_accesorios_detallado.md` (nombre que no genera conflictos con el informe resumido anterior), incluyendo:
1. Resumen ejecutivo.
2. Marco normativo de referencia.
3. Tabla de tramos y accesorios detallada con diámetros.
4. Inventario agrupado de valvulería y accesorios con precios de mercado contrastados.
5. Presupuesto detallado (tubería y accesorios).
6. Verificación técnica de cumplimiento de normas UNE.
7. Listado de referencias web guardadas de las fuentes de precios.
