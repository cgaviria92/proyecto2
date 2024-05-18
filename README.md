
## Preparación

1. **Crear Carpetas de Entrada y Salida:**
    - `carpeta_entrada`: Coloca aquí los archivos CSV que deseas procesar.
    - `carpeta_salida_pandas`: Aquí se guardarán los resultados del script con Pandas.
    - `carpeta_salida_puro`: Aquí se guardarán los resultados del script con Python puro.

2. **Instalar Dependencias:**
    - Asegúrate de tener instaladas las bibliotecas necesarias (`pandas` y `unidecode`). Puedes instalarlas ejecutando:
      ```sh
      pip install pandas unidecode
      ```

## Ejecución de Scripts

### Script con Pandas

1. **Descripción:**
    - El script `pandas_script.py` procesa los archivos CSV de la carpeta de entrada y genera un resumen de las víctimas, guardando los resultados en la carpeta de salida correspondiente.

2. **Ejecución:**
    - Para ejecutar el script, usa el siguiente comando:
      ```sh
      python pandas_script.py
      ```

3. **Resultados:**
    - Los resultados procesados se guardarán en `carpeta_salida_pandas`, con un archivo de salida por cada archivo de entrada procesado.

### Script con Código Puro

1. **Descripción:**
    - El script `puro_script.py` procesa los archivos CSV de la carpeta de entrada utilizando solo código Python puro y genera un resumen de las víctimas, guardando los resultados en la carpeta de salida correspondiente.

2. **Ejecución:**
    - Para ejecutar el script, usa el siguiente comando:
      ```sh
      python puro_script.py
      ```

3. **Resultados:**
    - Los resultados procesados se guardarán en `carpeta_salida_puro`, con un archivo de salida por cada archivo de entrada procesado.

## Ejemplo de Uso

### Ejecutar el Script con Pandas

1. **Preparar los Datos:**
    - Coloca los archivos CSV en la carpeta `carpeta_entrada`.

2. **Ejecutar el Script:**
    ```sh
    python pandas_script.py
    ```

3. **Revisar los Resultados:**
    - Los resultados se guardarán en la carpeta `carpeta_salida_pandas`.

### Ejecutar el Script con Código Puro

1. **Preparar los Datos:**
    - Coloca los archivos CSV en la carpeta `carpeta_entrada`.

2. **Ejecutar el Script:**
    ```sh
    python puro_script.py
    ```

3. **Revisar los Resultados:**
    - Los resultados se guardarán en la carpeta `carpeta_salida_puro`.

