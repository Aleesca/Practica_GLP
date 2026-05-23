# Especificación: Índice de Anexos e Inserción de Planos (Subsección 3.1 y Capítulo de Planos)

## Propósito
Definir y estructurar la documentación de referencia para los anexos de la memoria (Subsección 3.1) y la inserción física de los planos técnicos mediante comandos de LaTeX en el Capítulo de Planos, alineándose con la arquitectura de `plantilla.tex`.

## Contenido obligatorio
- **Subsección 3.1: ÍNDICE DE ANEXOS.**
  - Documentar la relación y el propósito de cada uno de los anexos del proyecto, estructurados de la siguiente manera:
    - **Anexo I: Planos.** Referencia al capítulo de planos que contiene la representación gráfica de la instalación.
    - **Anexo II: Comprobaciones y tablas auxiliares.** Catálogos y tablas de selección comercial empleados (depósitos de Lapesa, vaporizador forzado VIA 150 en armario VPC30C, etc.).
    - **Anexo III: Cálculos desarrollados.** Referencia al desarrollo detallado de cálculos que justifica el dimensionamiento de las conducciones (método de pérdida de carga y balance de velocidad).
- **Capítulo de Planos (Inserción física sin subsecciones):**
  - Describir e integrar los tres planos técnicos obligatorios utilizando el paquete `pdfpages` de LaTeX, asegurando que se compile cada archivo PDF completo y a página completa bajo `\portadacapitulo{Planos}`:
    1. **Plano nº 1: Situación y Emplazamiento (`situacion-emplazamiento.pdf`).** Muestra la ubicación geográfica y orientación de la parcela catastral `8638004TN8183N` en León.
    2. **Plano nº 2: Distancias de Seguridad y Acondicionamiento del Recinto (`Plano_distancias_seguridad.pdf`).** Representa la batería mixta de depósitos, la cuna de apoyo de hormigón, los muros EI-120 de protección y las distancias de seguridad del recinto A-500.
    3. **Plano nº 3: Esquema de Principio (P&ID) y Conducciones (`plano_Esquema_instalacion.pdf`).** Esquema hidráulico de la estación de almacenamiento, colector común, reguladores de presión, trazado de tuberías y puntos de consumo C1 a C6.

## Estilo de redacción
Tono formal de índice técnico, claro, estructurado y preciso. Longitud orientativa: 1 página.

## Figuras, tablas y resultados
- **Planos a insertar en el Capítulo de Planos:**
  - [situacion-emplazamiento.pdf](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/situacion-emplazamiento.pdf): Plano nº 1 - Situación y Emplazamiento.
  - [Plano_distancias_seguridad.pdf](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/Plano_distancias_seguridad.pdf): Plano nº 2 - Distancias de Seguridad y Acondicionamiento de Recinto.
  - [plano_Esquema_instalacion.pdf](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/plano_Esquema_instalacion.pdf): Plano nº 3 - Esquema de Principio (P&ID) y Trazado de Conducciones de GLP.
- **Estructura requerida:**
  - **Índice ordenado de anexos:** Relación numerada de anexos que se incluye bajo la Subsección 3.1.
  - **Uso de comandos LaTeX:** Especificar que la inclusión se realiza bajo `\portadacapitulo{Planos}` utilizando `\includepdf[pages=-, fitpaper=true, pagecommand={\thispagestyle{empty}}]{Figuras/nombre_plano.pdf}` para cada uno de los 3 planos.

## Conexiones
- **Alcance:** Salida documental (planos y anexos de cálculo).
- **Anotaciones:** [trazado_red.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/trazado_red.md) (Esquema), [distancias_seguridad.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/distancias_seguridad.md) (Planos), [dimensionado_tuberias_glp.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/dimensionado_tuberias_glp.md) (Anexo III).
- **Planos:** Archivos PDF en `Practica_GLPs_LaTeX/Figuras/`.

## Criterios de aceptación
- [ ] La especificación distingue claramente entre la Subsección 3.1 (ÍNDICE DE ANEXOS) dentro de los Cálculos Justificados y el Capítulo de Planos (`\portadacapitulo{Planos}`) al final del documento.
- [ ] Se detalla la estructura del índice de anexos con los tres bloques (Planos, Tablas Auxiliares, Cálculos Desarrollados) para la Subsección 3.1.
- [ ] Se detalla la relación y nombres exactos de los 3 archivos PDF de planos a insertar en el capítulo de Planos.
- [ ] Se indica la instrucción precisa de LaTeX (`\includepdf`) para insertar los planos de forma limpia a pantalla completa y sin numeración superior/inferior visible.
