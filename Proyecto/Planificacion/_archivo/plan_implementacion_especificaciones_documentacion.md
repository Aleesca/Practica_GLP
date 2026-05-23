# Plan: Implementación de especificaciones documentales de la memoria

> Fuente PRD: `Proyecto/Planificacion/plan_especificaciones_documentacion.md`  
> Archivo objetivo del plan: `Proyecto/Planificacion/plan_implementacion_especificaciones_documentacion.md`

## Resumen

El trabajo implementará el plan de especificaciones ya definido, usando fases trazables que produzcan entregables verificables dentro de `Proyecto/Especificaciones/` y `Proyecto/Planificacion/`. La implementación no debe reescribir la memoria final, sino preparar la documentación que indique cómo redactarla, qué evidencias usar, qué figuras/tablas incluir y cómo conectar cada apartado con alcance y anotaciones.

## Decisiones duraderas

- **Fuente estructural principal**: `Practica_GLPs_LaTeX/plantilla.tex`.
- **Fuente de alcance**: `Proyecto/Alcance.md`.
- **Fuentes de evidencia**: `Proyecto/Anotaciones/`.
- **Destino principal**: `Proyecto/Especificaciones/`.
- **Artefactos auxiliares**: reutilizar planificación existente en `Proyecto/Planificacion/`, especialmente esquema de memoria, matriz de fuentes, mapa de citas y manifiestos de figuras/tablas si aplican.
- **Formato de especificación**: cada apartado debe incluir propósito, contenido obligatorio, estilo de redacción, figuras/tablas/resultados, conexiones y criterios de aceptación.
- **Criterio de implementación**: ajustar documentación existente antes de crear documentos nuevos duplicados.

## Historias de usuario

1. Como redactor de la memoria, quiero conocer qué debe incluir cada apartado, para redactar sin reinterpretar la plantilla.
2. Como responsable técnico, quiero conectar alcance, anotaciones y apartados, para asegurar trazabilidad documental.
3. Como revisor, quiero criterios de aceptación por apartado, para validar si la memoria está completa.
4. Como autor del proyecto, quiero identificar figuras, tablas y resultados esperados, para preparar evidencias visuales coherentes.
5. Como mantenedor de la documentación, quiero un formato uniforme de especificaciones, para evitar duplicidades y contradicciones.

## Fase 1: Inventario documental verificable

**Historias cubiertas**: 1, 2, 5

### Qué construir

Revisar la estructura existente de planificación, especificaciones, anotaciones, alcance y plantilla LaTeX. Producir un inventario base que indique qué documentos existen, qué función cumplen y cuáles serán usados como fuentes para las fases siguientes.

### Criterios de aceptación

- [ ] Está identificado el conjunto real de archivos en `Proyecto/Especificaciones/`.
- [ ] Está identificado el conjunto real de archivos en `Proyecto/Anotaciones/`.
- [ ] Están marcados los artefactos de planificación reutilizables.
- [ ] No se crean especificaciones nuevas antes de saber si ya existe una equivalente.

---

## Fase 2: Extracción de estructura desde la plantilla

**Historias cubiertas**: 1, 3

### Qué construir

Extraer de `plantilla.tex` la estructura canónica de la memoria: apartados, subapartados y anexos. Compararla con las especificaciones existentes para detectar cobertura, duplicados y huecos.

### Criterios de aceptación

- [ ] Existe una lista canónica de apartados de la memoria.
- [ ] Cada especificación existente queda asociada a uno o varios apartados de la plantilla.
- [ ] Se identifican apartados sin especificación.
- [ ] Se identifican especificaciones que no encajan claramente con la plantilla.

---

## Fase 3: Mapeo contra alcance

**Historias cubiertas**: 1, 2, 3

### Qué construir

Cruzar `Proyecto/Alcance.md` con la estructura canónica de la memoria para asegurar que cada requisito o entrega prevista tiene ubicación documental. Registrar también los huecos donde el alcance exige contenido que todavía no esté especificado.

### Criterios de aceptación

- [ ] Cada elemento del alcance tiene al menos un apartado destino.
- [ ] Cada apartado relevante indica qué parte del alcance cubre.
- [ ] Los huecos de cobertura quedan registrados como tareas documentales.
- [ ] Los contenidos fuera de alcance quedan señalados para evitar expansión innecesaria.

---

## Fase 4: Conexión con anotaciones y evidencias

**Historias cubiertas**: 2, 4

### Qué construir

Clasificar las anotaciones por tema técnico y conectarlas con los apartados de la memoria. Para cada conexión, indicar si la anotación sirve como evidencia, decisión, cálculo, criterio normativo, figura, tabla o resultado.

### Criterios de aceptación

- [ ] Cada anotación relevante tiene un uso documental explícito.
- [ ] Cada especificación temática enlaza las anotaciones que debe usar.
- [ ] Las conexiones distinguen entre evidencia, cálculo, decisión y resultado.
- [ ] Las anotaciones no se copian literalmente salvo que se justifique como cita o dato.

---

## Fase 5: Normalización del formato de especificaciones

**Historias cubiertas**: 1, 3, 5

### Qué construir

Aplicar una plantilla común a las especificaciones existentes y futuras. Cada documento debe dejar claro el propósito del apartado, contenido obligatorio, estilo de redacción, figuras/tablas/resultados, conexiones y criterios de aceptación.

### Criterios de aceptación

- [ ] Todas las especificaciones relevantes siguen una estructura homogénea.
- [ ] Cada especificación incluye instrucciones de estilo de redacción.
- [ ] Cada especificación indica figuras, tablas o resultados esperados cuando corresponda.
- [ ] Cada especificación incluye criterios de aceptación verificables.

---

## Fase 6: Completar y ajustar especificaciones

**Historias cubiertas**: 1, 2, 3, 4, 5

### Qué construir

Actualizar la documentación de `Proyecto/Especificaciones/` para cubrir los apartados faltantes, fusionar o aclarar especificaciones solapadas y asegurar que cada apartado de la memoria tiene una guía de redacción suficiente.

### Criterios de aceptación

- [ ] Los apartados estructurales de la memoria están cubiertos.
- [ ] Los apartados técnicos tienen conexiones con alcance y anotaciones.
- [ ] Los apartados de resultados, discusión, conclusiones y anexos tienen criterios propios.
- [ ] No quedan especificaciones duplicadas con instrucciones contradictorias.

---

## Fase 7: Revisión global y cierre documental

**Historias cubiertas**: 2, 3, 4, 5

### Qué construir

Realizar una revisión final de coherencia, trazabilidad y completitud. Actualizar los artefactos de planificación necesarios para que el estado final muestre qué está cubierto, qué fuentes se usan y qué queda pendiente.

### Criterios de aceptación

- [ ] Todos los apartados relevantes de `plantilla.tex` están cubiertos o justificados.
- [ ] Todos los elementos de `Alcance.md` están conectados a la memoria.
- [ ] Las anotaciones relevantes están conectadas a especificaciones.
- [ ] Figuras, tablas y resultados esperados tienen ubicación documental.
- [ ] La documentación permite redactar la memoria sin nuevas decisiones estructurales.

## Plan de prueba

- Revisar trazabilidad plantilla-alcance-especificaciones-anotaciones.
- Comprobar que cada especificación contiene las secciones obligatorias.
- Verificar que no hay apartados huérfanos en la plantilla ni requisitos huérfanos en el alcance.
- Revisar coherencia terminológica entre especificaciones relacionadas.
- Validar que las figuras, tablas y resultados propuestos tienen propósito documental claro.

## Supuestos

- La implementación se limitará a documentación Markdown y no modificará cálculos técnicos salvo para referenciarlos.
- Las especificaciones existentes se conservarán siempre que puedan adaptarse al formato común.
- Los documentos de planificación existentes pueden actuar como fuentes auxiliares, pero la autoridad principal será la combinación de plantilla, alcance y anotaciones.
- La granularidad elegida es de siete fases trazables, siguiendo el plan original.
