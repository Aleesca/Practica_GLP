---
name: doc_tecnica_glp
description: "Guidance on GLP storage, distribution, safety distances, autonomy, vaporization, and technical project documentation. Use when the user requests information derived from the project's technical references or says 'escriba segun la doc tecnica'."
---

# Skill: Documentacion Tecnica de GLP

Esta skill proporciona acceso y guia sobre la documentacion tecnica del proyecto de GLP, incluyendo datos del grupo, criterios de calculo, referencias normativas y organizacion de fuentes.

## Flujo de trabajo

Cuando el usuario solicite informacion tecnica o diga "escriba segun la doc tecnica", sigue estos pasos:

1. Analizar si necesita datos del grupo, criterio de calculo, normativa o apoyo de catalogo.
2. Consultar `references/doc_map.md` para localizar la fuente adecuada.
3. Consultar `references/formulario.md` cuando la peticion afecte a formulas, criterios o magnitudes base.
4. Consultar `references/datos_grupo_G1-1.md` cuando la respuesta dependa de los datos operativos del grupo.
5. Responder con precision, indicando explicitamente la fuente empleada.

## Recursos disponibles

- `references/formulario.md`: formulario base y criterios comunes.
- `references/doc_map.md`: mapa de documentacion y rutas de consulta.
- `references/datos_grupo_G1-1.md`: normalizacion operativa de datos del grupo.

## Temas cubiertos

- Demanda y caudal de calculo.
- Autonomia de almacenamiento.
- Vaporizacion natural del deposito.
- Seleccion del deposito.
- Red de distribucion.
- Implantacion y distancias de seguridad.
