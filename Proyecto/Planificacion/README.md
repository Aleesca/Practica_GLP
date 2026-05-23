# Planificacion del Proyecto GLP

Este directorio contiene los documentos activos que gobiernan la estructura de memoria, la trazabilidad tecnica y la coordinacion del sistema documental del proyecto.

## Documentos activos

- `esquema_memoria.md`: estructura objetivo de la memoria tecnica.
- `matriz_fuentes.md`: matriz principal de cobertura, fuentes, calculos, figuras y estado documental.
- `mapeo_markdown_a_latex.md`: contrato de encaje entre Markdown tecnico y plantilla LaTeX existente.
- `mapa_citas.md`: mapeo operativo de citas y claves bibliograficas.
- `manifiesto_tablas_metodologia.md`: inventario de tablas tecnicas esperadas.
- `manifiesto_figuras_memoria.md`: inventario editorial de figuras, planos y anexos.
- `Cronograma_responsables_dependencias.md`: referencia de ejecucion del grupo y dependencias operativas.
- `plan_revision_orquestador_agentes.md`: referencia de integracion del sistema de agentes.
- `plan_revision_limpieza_planificacion.md`: registro de criterios aplicados para archivar planes ya ejecutados.

## Archivo historico

- `_archivo/`: deposito de planes ejecutados y documentos de auditoria historica.

Los documentos dentro de `_archivo/` no deben cargarse como contexto de trabajo salvo que haga falta auditar decisiones antiguas. Sus resultados han sido sustituidos por `Proyecto/Especificaciones/`, `Proyecto/Anotaciones/` y `matriz_fuentes.md`.

## Reglas del directorio

- `Proyecto/Especificaciones/` es la salida tecnica primaria.
- `Proyecto/Anotaciones/` alimenta la metodologia y las decisiones de diseno.
- `matriz_fuentes.md` es la referencia principal para comprobar cobertura y trazabilidad.
- `.agents/skills/` es la ubicacion operativa de skills.
- `Proyecto/skills/` se mantiene solo como espejo temporal.
- `Practica_GLPs_LaTeX/` consolida el contenido ya cerrado y no debe gobernar el flujo activo.
