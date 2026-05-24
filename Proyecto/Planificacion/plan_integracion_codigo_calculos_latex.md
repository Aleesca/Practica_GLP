# Plan: Extraer `calculos.ipynb` e Integrarlo en LaTeX como Capitulo de Codigo

## Summary

Convertir `calculos/calculos.ipynb` en un script Python mantenible y enlazar ese script desde `Practica_GLPs_LaTeX/plantilla.tex` mediante un listing en un capitulo independiente llamado `Codigo`.

El archivo `.py` sera la fuente unica del codigo mostrado: cualquier cambio posterior en el script se reflejara automaticamente en el PDF al recompilar LaTeX, sin copiar y pegar codigo dentro de la plantilla.

## Decisiones Tecnicas

- La extraccion desde Jupyter se hara hacia un archivo Python versionable, por ejemplo `calculos/calculos.py`.
- La plantilla LaTeX no contendra el codigo embebido, solo una referencia externa al `.py`.
- En la implementacion se usara Context7 para confirmar la opcion recomendada para incluir codigo externo en LaTeX, priorizando `listings` por no requerir `shell-escape`.
- La integracion esperada sera mediante `\lstinputlisting{...}` o equivalente, de forma que LaTeX lea el archivo Python en cada compilacion.
- El capitulo se llamara `Codigo` y estara separado del resto del documento.

## Fases

### Fase 1: Verificacion y Decision LaTeX

**Objetivo:** confirmar la forma correcta y mas robusta de incluir codigo Python externo en LaTeX.

**Tareas:**

- Consultar Context7 durante la implementacion sobre integracion de codigo fuente externo en LaTeX.
- Comparar `listings` frente a alternativas como `minted`.
- Elegir `listings` salvo que el proyecto ya use explicitamente otra solucion.
- Definir la configuracion minima para Python: lenguaje, numeracion de lineas, estilo monoespaciado, saltos de linea y marco opcional.

**Criterios de aceptacion:**

- La decision queda justificada.
- No se introduce una dependencia innecesaria como `shell-escape` si no hace falta.
- El codigo externo se actualizara al recompilar LaTeX.

### Fase 2: Extraccion del Notebook a Script Python

**Objetivo:** generar un archivo `.py` limpio a partir de `calculos/calculos.ipynb`.

**Tareas:**

- Extraer las celdas de codigo del notebook.
- Eliminar o revisar artefactos propios del notebook que no sean adecuados en un script, como comandos magicos, salidas interactivas o dependencias implicitas del kernel.
- Mantener el orden logico de ejecucion.
- Anadir separadores o comentarios minimos si ayudan a preservar la estructura del notebook.

**Criterios de aceptacion:**

- Existe un script Python unico con el contenido ejecutable relevante del notebook.
- El script puede abrirse y leerse como codigo Python normal.
- No se copian resultados renderizados del notebook al `.py`.

### Fase 3: Integracion en `plantilla.tex`

**Objetivo:** anadir un capitulo independiente llamado `Codigo` que incluya el script Python externo.

**Tareas:**

- Anadir el paquete LaTeX necesario para listings si no esta ya presente.
- Configurar un estilo basico para codigo Python.
- Insertar un capitulo `Codigo`.
- Incluir el archivo Python con una referencia externa, no con codigo pegado manualmente.
- Usar una ruta relativa estable desde la ubicacion de `plantilla.tex`.

**Criterios de aceptacion:**

- El PDF generado contiene un capitulo llamado `Codigo`.
- El capitulo muestra el contenido del script Python.
- Al modificar el `.py` y recompilar LaTeX, el contenido mostrado se actualiza automaticamente.

### Fase 4: Validacion de Compilacion

**Objetivo:** comprobar que el flujo completo funciona.

**Tareas:**

- Compilar el proyecto LaTeX.
- Confirmar que no hay errores por rutas, paquetes o caracteres especiales del codigo Python.
- Hacer una modificacion pequena de prueba en el `.py` y recompilar para verificar que el cambio aparece en el documento.
- Revertir cualquier modificacion de prueba antes de finalizar la implementacion.

**Criterios de aceptacion:**

- La plantilla compila correctamente.
- El capitulo `Codigo` aparece en el documento final.
- El contenido procede directamente del archivo Python.
- No queda codigo duplicado entre `.tex` y `.py`.

## Supuestos

- El notebook `calculos/calculos.ipynb` contiene el codigo fuente que debe documentarse.
- El capitulo `Codigo` debe anadirse dentro de `plantilla.tex`, no en un archivo `.tex` separado, salvo que durante la implementacion se observe que el proyecto ya organiza capitulos mediante includes.
- Se prioriza una solucion simple y reproducible con `listings`.
- Context7 se usara solo durante la implementacion, no durante esta fase de planificacion.
