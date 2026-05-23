# Propuesta de Segmentación de Orquestaciones (GLP)

Este documento detalla el análisis para dividir el flujo de orquestación del proyecto en dos partes diferenciadas: la redacción de la **Memoria** descriptiva y el desarrollo de los **Cálculos Justificados**, basándose en la estructura editorial fijada en [plantilla.tex](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Practica_GLPs_LaTeX/plantilla.tex).

---

## 1. Correspondencia de Bloques y Documentos

Según las pautas de [mapeo_markdown_a_latex.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Planificacion/mapeo_markdown_a_latex.md), los contenidos del proyecto se dividen en dos bloques:

### Bloque Memoria (Sección 2 de la Plantilla)
*   **Especificaciones de entrada (Markdown):**
    *   [intro.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/intro.md)
    *   [datos-partida.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/datos-partida.md)
    *   [promotor-plazo-accesos.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/promotor-plazo-accesos.md)
    *   [deposito.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/deposito.md)
    *   [red-distribucion.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/red-distribucion.md)
    *   [implantacion-seguridad.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/implantacion-seguridad.md) (justificación y distancias)
    *   [conclusiones-limitaciones.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/conclusiones-limitaciones.md)
*   **Anotaciones de soporte (Criterios y notas técnicas):**
    *   [criterios_normativos.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/criterios_normativos.md)
    *   [seleccion_deposito.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/seleccion_deposito.md)
    *   [trazado_red.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/trazado_red.md)

### Bloque Cálculos Justificados (Sección 3 de la Plantilla)
*   **Especificaciones de entrada (Markdown):**
    *   [calculos-auxiliares.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/calculos-auxiliares.md)
    *   [anejos.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/anejos.md)
    *   Desarrollo numérico en [demanda-consumo.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/demanda-consumo.md)
    *   Desarrollo numérico en [autonomia.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/autonomia.md)
    *   Desarrollo numérico en [vaporizacion.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Especificaciones/vaporizacion.md)
*   **Anotaciones de soporte (Cálculos):**
    *   [caudales_consumidores.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/caudales_consumidores.md)
    *   [calculo_volumen_deposito.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/calculo_volumen_deposito.md)
    *   [vaporizacion_natural.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/vaporizacion_natural.md)
    *   [vaporizacion_forzada.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/vaporizacion_forzada.md)
    *   [dimensionado_tuberias_glp.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Anotaciones/dimensionado_tuberias_glp.md)

---

## 2. Alternativas de Segmentación de Orquestaciones

Para independizar o secuenciar el trabajo de ambas partes utilizando el sistema de agentes existente, se proponen las siguientes opciones:

### Opción A: Invocación acotada por prompt
*   **Descripción:** Mantener la configuración genérica del [task-orchestrator.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/.agents/agents/task-orchestrator.md) y restringir su ámbito dinámicamente al iniciarlo mediante instrucciones de control.
*   **Ejemplo:** *"Orquesta la generación únicamente para el bloque Memoria a partir de los documentos de especificaciones asignados."*

### Opción B: Subagentes especializados (Recomendado para robustez)
*   **Descripción:** Dividir la configuración del orquestador en dos archivos independientes dentro de `.agents/agents/` para limitar de forma rígida su alcance técnico y reglas de transición.
*   **Estructura propuesta:**
    *   `task-orchestrator-memoria.md`: Gestionará y validará exclusivamente las secciones de la Memoria descriptiva (Capítulo 2, 4 y 5 de la plantilla).
    *   `task-orchestrator-calculos.md`: Gestionará y validará las secciones del Capítulo 3 de la plantilla y el procesado de anejos numéricos.

### Opción C: Etiquetado en la planificación
*   **Descripción:** Incorporar identificadores de ámbito (p. ej., `[MEMORIA]` y `[CALCULOS]`) directamente en los archivos de gobierno [esquema_memoria.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Planificacion/esquema_memoria.md) y [mapeo_markdown_a_latex.md](file:///H:/Unidades%20compartidas/Practicas_Inst2/4_GLPs/Proyecto/Planificacion/mapeo_markdown_a_latex.md) para permitir al orquestador discriminar automáticamente el contenido a procesar.
