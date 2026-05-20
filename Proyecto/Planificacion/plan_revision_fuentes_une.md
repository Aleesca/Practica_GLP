# Plan: Revisión de Accesorios (Fuentes Europeas y Normativa UNE)

> Source PRD: Requisito de actualizar `Proyecto/Anotaciones/reporte_accesorios.md` con fuentes europeas y verificar normativa UNE del notebook `control_system_guide`.

## Architectural decisions

Durable decisions that apply across all phases:
- **Restricción Geográfica:** Las fuentes y catálogos deben provenir estrictamente de dominios o divisiones europeas (ej. RegO Europe, Clesse Europe, distribuidores locales españoles).
- **Criterio de Validación:** Ningún componente se dará por válido si su datasheet europeo no acredita el cumplimiento de las normativas UNE o directivas EN equivalentes extraídas del notebook.
- **Moneda:** Todos los precios deben reportarse en Euros (€).

---

## Phase 1: Extracción de Requisitos Normativos (Notebook)

**User stories**:
- Identificar qué normativas UNE exactas aplican a la valvulería y regulación.

### What to build
Interacción con el notebook `control_system_guide` (utilizando la integración correspondiente en fase de ejecución) para extraer el listado de normativas UNE y directivas europeas que deben cumplir los accesorios de GLP.

### Acceptance criteria
- [ ] Listado de normas UNE/EN aplicables extraído con éxito del notebook.
- [ ] Identificación de los parámetros de validación obligatorios para cada tipo de válvula y regulador.

---

## Phase 2: Búsqueda de Proveedores Europeos

**User stories**:
- Localizar las fichas técnicas y tarifas de los accesorios en el mercado europeo.

### What to build
Búsqueda de catálogos y hojas de datos restringida al ámbito europeo para los modelos especificados (RegO 1588V, RS 3145, A 7508 AP; Clesse APS2000; Lapesa VPC30C, Giacomini R700).

### Acceptance criteria
- [ ] Enlaces a datasheets alojados en servidores europeos (.es, .eu, .de, etc.) u oficiales de la división europea del fabricante.
- [ ] Precios obtenidos en Euros (€) aplicables al mercado europeo (o justificación de su ausencia).

---

## Phase 3: Verificación UNE y Actualización del Reporte

**User stories**:
- Consolidar la información verificada en el reporte final, descartando fuentes estadounidenses.

### What to build
Revisión técnica de los datasheets encontrados en la Fase 2 frente a los criterios normativos de la Fase 1. Actualización estructural de `Proyecto/Anotaciones/reporte_accesorios.md` para reflejar el cumplimiento normativo.

### Acceptance criteria
- [ ] Verificación cruzada: confirmación de que el datasheet europeo menciona y cumple las normativas UNE/EN requeridas.
- [ ] Archivo `Proyecto/Anotaciones/reporte_accesorios.md` actualizado con los nuevos enlaces europeos y precios.
- [ ] Inclusión de una nota o columna explícita que confirme el estatus de cumplimiento UNE para cada equipo.
