# Plan por fases para desarrollar las especificaciones del proyecto

## Resumen

Se elaborará un conjunto de especificaciones en `Proyecto/Especificaciones/` que indiquen, para cada apartado de la memoria definido en `Practica_GLPs_LaTeX/plantilla.tex`, qué debe redactarse, con qué estilo, qué figuras/resultados deben incluirse y qué conexiones deben establecerse con `Proyecto/Anotaciones/` y `Proyecto/Alcance.md`.

La restricción inicial es no leer todavía los archivos; este plan los deja referenciados como fuentes obligatorias para una fase posterior de análisis.

## Fases

### Fase 1: Preparación documental

- Identificar las fuentes base que se revisarán después:
  - `Practica_GLPs_LaTeX/plantilla.tex`: estructura oficial de la memoria.
  - `Proyecto/Alcance.md`: contenido mínimo y límites del proyecto.
  - `Proyecto/Anotaciones/`: evidencias, ideas, decisiones y referencias conectables.
  - `Proyecto/Especificaciones/`: destino de la documentación ajustada.
- Definir una matriz de trazabilidad con este formato:
  - Apartado de memoria.
  - Objetivo del apartado.
  - Contenido requerido por alcance.
  - Anotaciones relacionadas.
  - Figuras/resultados esperados.
  - Estado de especificación.
  - Observaciones.

### Fase 2: Extracción de estructura de la memoria

- Revisar `plantilla.tex` para obtener todos los apartados, subapartados y requisitos implícitos de la memoria.
- Convertir esa estructura en una lista canónica de apartados que servirá como índice de `Proyecto/Especificaciones/`.
- Para cada apartado, decidir si necesita una especificación propia o si puede agruparse con otro apartado relacionado.

### Fase 3: Cruce con alcance del proyecto

- Revisar `Proyecto/Alcance.md` y mapear cada elemento del alcance contra los apartados de la memoria.
- Detectar huecos:
  - Apartados de la plantilla sin contenido definido por el alcance.
  - Elementos del alcance sin lugar claro en la memoria.
  - Resultados esperados que requieran figuras, tablas, diagramas o métricas.
- Ajustar la matriz de trazabilidad para que cada requisito del alcance tenga ubicación documental.

### Fase 4: Conexión con anotaciones

- Revisar `Proyecto/Anotaciones/` y clasificar las anotaciones por tema, decisión, evidencia o resultado.
- Vincular cada anotación relevante con uno o varios apartados de la memoria.
- Marcar conexiones explícitas en las especificaciones usando un formato estable, por ejemplo:
  - `Fuente: Proyecto/Anotaciones/<archivo>`
  - `Uso previsto: evidencia / justificación / resultado / decisión`
  - `Apartado destino: <apartado de plantilla.tex>`

### Fase 5: Diseño del formato de especificación

Cada especificación de apartado seguirá una plantilla común:

```md
# Especificación: <apartado de la memoria>

## Propósito
Qué debe demostrar este apartado dentro de la memoria.

## Contenido obligatorio
Puntos que deben aparecer según plantilla, alcance y anotaciones.

## Estilo de redacción
Tono, persona verbal, nivel técnico, longitud orientativa y criterios de claridad.

## Figuras, tablas y resultados
Elementos visuales o resultados que deben incluirse, con su función dentro del texto.

## Conexiones
Referencias a alcance, anotaciones y otros apartados relacionados.

## Criterios de aceptación
Condiciones mínimas para considerar completo el apartado.
```

### Fase 6: Redacción de especificaciones

- Crear o ajustar las especificaciones en `Proyecto/Especificaciones/`.
- Cada apartado de `plantilla.tex` debe tener instrucciones claras sobre:
  - Qué escribir.
  - Qué no incluir.
  - Qué evidencias usar.
  - Qué figuras/resultados aportar.
  - Qué conexiones internas mantener.
- Priorizar primero los apartados estructurales de la memoria y después los apartados de resultados, discusión, conclusiones y anexos.

### Fase 7: Revisión global de coherencia

- Comprobar que todas las especificaciones usan el mismo estilo documental.
- Verificar que no hay duplicación innecesaria entre apartados.
- Confirmar que cada elemento de `Proyecto/Alcance.md` aparece conectado a un apartado de memoria.
- Confirmar que las anotaciones relevantes están enlazadas desde alguna especificación.
- Revisar que las figuras, tablas y resultados propuestos tienen una función concreta dentro de la memoria.

## Cambios documentales previstos

- Añadir o reorganizar archivos dentro de `Proyecto/Especificaciones/`.
- Introducir una plantilla común para las especificaciones de apartados.
- Crear una matriz de trazabilidad entre memoria, alcance, anotaciones, figuras y resultados.
- Ajustar la documentación del proyecto para que la memoria pueda redactarse siguiendo instrucciones concretas y verificables.

## Criterios de aceptación

- Todos los apartados relevantes de `plantilla.tex` están cubiertos por una especificación.
- Cada especificación incluye estilo de redacción, contenido esperado, figuras/resultados y conexiones.
- Cada punto de `Proyecto/Alcance.md` tiene al menos una conexión documental clara.
- Las anotaciones de `Proyecto/Anotaciones/` quedan vinculadas a los apartados donde aportan valor.
- La documentación resultante permite redactar la memoria sin tener que decidir de nuevo la estructura ni el propósito de cada apartado.

## Supuestos

- `plantilla.tex` será la fuente principal para la estructura de la memoria.
- `Alcance.md` será la fuente principal para decidir qué debe incluirse.
- `Proyecto/Anotaciones/` se usará como fuente de evidencias, decisiones y conexiones, no como contenido que deba copiarse literalmente.
- No se modificará el contenido técnico del proyecto en esta fase; el trabajo se limita a especificaciones y organización documental.
