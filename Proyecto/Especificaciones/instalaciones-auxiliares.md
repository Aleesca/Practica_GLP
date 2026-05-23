# Especificación: Instalaciones y Servicios Auxiliares (Secciones 2.14, 2.15, 2.16)

## Propósito
Describir y justificar las medidas de seguridad activa y pasiva asociadas a la instalación eléctrica (clasificación ATEX), la red de refrigeración y extinción de incendios, y la puesta a tierra de depósitos y tuberías.

## Contenido obligatorio

### Sección 2.14: INSTALACIÓN ELÉCTRICA.
- Clasificación de zonas ATEX (Zonas 1 y 2) en el recinto de almacenamiento de depósitos y el vaporizador según ITC-ICG 03 y UNE 60250.
- Especificar los requisitos de la acometida eléctrica para el armario del vaporizador (caldera de calefacción y bomba de recirculación de agua caliente) y para el alumbrado del recinto.
- Garantizar que todos los equipos eléctricos instalados en zonas clasificadas cuenten con marcado y certificado ATEX adecuado (categoría II 2G Ex d IIA T3 o equivalente).

### Sección 2.15: INSTALACIONES DE PROTECCIÓN CONTRAINCENDIOS.
- Describir los sistemas de seguridad pasiva: vallado de cerramiento, cartelería de advertencia de "Peligro Inflamable", y extintores portátiles de polvo seco de eficacia 21A-113B distribuidos en el recinto.
- Especificar el sistema de refrigeración activo por pulverización de agua sobre la superficie exterior de la batería de depósitos en caso de incendio (según UNE 60250):
  - Caudal unitario mínimo de pulverización: $3\ \text{l/min}\cdot\text{m}^2$ de superficie de chapa.
  - Válvulas de diluvio de accionamiento manual y automático.
  - Conexión al colector de agua municipal o reserva propia si procede.

### Sección 2.16: PUESTA A TIERRA.
- Describir el circuito equipotencial de puesta a tierra para la disipación de cargas electrostáticas y descargas atmosféricas.
- Especificar la conexión equipotencial de las cunas metálicas de los depósitos, del vaporizador, del vallado metálico de cerramiento, y de las bridas de las canalizaciones viales.
- Definir la instalación de picas de cobre de $2 \text{ m}$ de longitud mínima hincadas en el terreno para asegurar una resistencia de paso a tierra inferior a $20\ \Omega$ (preferiblemente $<10\ \Omega$).

## Estilo de redacción
Tono formal, impersonal y técnico de ingeniería. Longitud orientativa: 1,5 a 2 páginas.

## Figuras, tablas y resultados
- **Figuras a integrar:**
  - [cerramiento.jpeg](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/Figuras/cerramiento.jpeg): Ilustración física y constructiva del cerramiento perimetral de seguridad para la estación de almacenamiento de GLP, compuesto por malla metálica y zócalo inferior.
- **Tablas obligatorias:**
  - **Tabla de clasificación ATEX:** Zonas 1 y 2, extensión del radio de clasificación según UNE 60250 y marcado exigido de equipos.
- **Resultado de diseño:** Resistencia máxima de paso a tierra ($20\ \Omega$) y caudal de agua por rociador.

## Conexiones
- **Alcance:** Requisito 3 (Vaporización forzada - parte eléctrica) y Requisito 6 (Esquema y distancias - PCI y puesta a tierra).
- **Anotaciones:** [distancias_seguridad.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/distancias_seguridad.md) (Criterio Normativo), [criterios_normativos.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/criterios_normativos.md) (Reglamentación), [pliego_condiciones_equipos_glp.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/pliego_condiciones_equipos_glp.md) (Criterio Normativo).

## Criterios de aceptación
- [ ] Se detalla la extensión radial de las áreas ATEX (Zona 1 y Zona 2) para depósitos aéreos.
- [ ] Se especifica el caudal de diseño de refrigeración de $3\ \text{l/min}\cdot\text{m}^2$.
- [ ] Se define el número y tipo de extintores (21A-113B) del recinto.
- [ ] Se especifica el valor límite de resistencia a tierra ($20\ \Omega$).
