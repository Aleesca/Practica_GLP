# Memoria: Conclusiones y Limitaciones del Proyecto

## 1. Conclusiones y Valoración de la Solución
El análisis técnico, el diseño hidráulico y el replanteo geométrico realizados en el presente proyecto permiten extraer las siguientes conclusiones sobre la instalación común de almacenamiento y red de propano del Grupo G1-1:

*   **Viabilidad y Flexibilidad de la Batería Mixta:** La configuración seleccionada ($1 \times \text{LP46A-22} + 3 \times \text{LP26A-22}$) es la única alternativa viable comercialmente que proporciona la capacidad geométrica requerida ($124,30\text{ m}^3$) respetando los límites de propiedad de la parcela catastral. Su diseño modular permite la operación independiente de tanques durante mantenimientos y asegura una autonomía real de $32,5\text{ días}$, superando la exigencia de 30 días.
*   **Garantía de Suministro por Vaporización Mixta:** El balance térmico a la temperatura exterior mínima de León ($-5\text{ ºC}$) demostró un déficit de vaporización natural de $56,51\text{ kg/h}$. Este déficit se cubre con seguridad mediante el intercambiador interno VIA 150 ($150\text{ kg/h}$ forzados) alimentado por la caldera del armario exterior VPC30C ($45\text{ kW}$), proporcionando un margen de seguridad del $49,8\%$ sobre el caudal de cálculo punta ($187,81\text{ kg/h}$).
*   **Cumplimiento Normativo y Seguridad:** La estación del Tipo A-500 cumple con todas las distancias de seguridad reglamentarias de la norma UNE 60250 gracias a la instalación estratégica de muros cortafuegos EI-120 en los linderos norte y oeste. La red de cobre aéreo UNE-EN 1057 a $1,7\text{ bar}$ relativos se proyecta vista y visible, facilitando el control de fugas y la señalización amarilla RAL 1021.
*   **Eficacia Operativa:** El sistema de regulación en doble salto (MPB a $1,7\text{ bar}$ en colector general y reducción a $37\text{ mbar}$ local en hornos) asegura una presión constante en los quemadores industriales, independientemente de fluctuaciones de temperatura exterior o nivel de los tanques, optimizando el rendimiento de la planta.

## 2. Limitaciones del Proyecto y del Modelo de Cálculo
El diseño propuesto está sujeto a las siguientes limitaciones y condicionantes de partida:

*   **Dependencia Climática y Meteorológica:** Los cálculos de vaporización natural asumen una temperatura mínima de $-5\text{ ºC}$ correspondiente a las condiciones históricas de León según IDAE. Descensos térmicos extremos por debajo de $-12\text{ ºC}$ de forma prolongada reducirán drásticamente el rendimiento de auto-vaporización de los tanques, obligando a una mayor dependencia del sistema de calefacción forzada VPC30C.
*   **Sobredimensionamiento por Simultaneidad:** La adopción del coeficiente de simultaneidad $f_s = 1$ responde a criterios de seguridad en procesos continuos, pero conduce a un sobredimensionamiento de los diámetros de tuberías y equipos de regulación si la planta industrial opera habitualmente con cargas alternas.
*   **Rigidez Espacial de la Estación de Almacenamiento:** Debido al exhaustivo aprovechamiento de las distancias de seguridad reducidas mediante muros EI-120, la estación de almacenamiento común se encuentra al límite físico de la parcela catastral. Cualquier necesidad de ampliación futura de volumen de almacenamiento (por ejemplo, para aumentar producción) requerirá la reubicación completa de la estación o la compra de terrenos colindantes.
*   **Exclusiones del Alcance de Red:** Este diseño finaliza en las llaves de corte individuales situadas en los armarios de regulación de segundo salto. La red interior, quemadores, sistemas de ventilación de naves y chimeneas de evacuación quedan fuera del alcance del presente proyecto y deberán legalizarse de forma independiente.

## Referencias relacionadas
- [Memoria: Autonomía de almacenamiento](autonomia.md)
- [Memoria: Selección y dimensionado del depósito](deposito.md)
- [Memoria: Vaporización natural vs. vaporización forzada](vaporizacion.md)
- [Memoria: Red de distribución y regulación](red-distribucion.md)
- [Memoria: Implantación y distancias de seguridad](implantacion-seguridad.md)
- [Selección del depósito](../Anotaciones/seleccion_deposito.md)
- [Dimensionado de tuberías GLP](../Anotaciones/dimensionado_tuberias_glp.md)
- [Implantación y distancias de seguridad](../Anotaciones/distancias_seguridad.md)
