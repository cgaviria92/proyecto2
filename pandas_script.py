import pandas as pd
import unidecode
import os
import time

# Carpetas de entrada y salida
input_dir = 'carpeta_entrada'
output_dir = 'carpeta_salida_pandas'

# Se crea carpeta de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# Función para limpiar los caracteres especiales
def clean_column_names(column_name):
    cleaned_name = unidecode.unidecode(column_name)
    cleaned_name = cleaned_name.replace(' ', '_').replace('?', '').replace('>', '').lower()
    return cleaned_name

# Recorre los archivos en la carpeta
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        start_time = time.time()
    
        file_path = os.path.join(input_dir, filename)
        df = pd.read_csv(file_path, encoding='latin1')  # Cambia el encoding si es necesario

        # Limpiar nombres de columnas y los agrega a un Dataframe
        df.columns = [clean_column_names(col) for col in df.columns]

        # Se corrije nombre departamento
        if 'idepartamento' in df.columns:
            df.rename(columns={'idepartamento': 'departamento'}, inplace=True)

        # Verificar los nombres de las columnas
        print(f"Columnas después de la limpieza: {df.columns}")

        # Limpiar datos 
        df['genero'] = df['genero'].apply(lambda x: unidecode.unidecode(str(x)).lower())
        df['estado'] = df['estado'].apply(lambda x: unidecode.unidecode(str(x)).lower())

        # Corregir valores
        df['genero'] = df['genero'].replace({'m': 'hombre', 'f': 'mujer'})

        # eliminando cualquier coma
        df['ano'] = pd.to_numeric(df['ano'].astype(str).str.replace(',', ''), errors='coerce')
        df['mes'] = pd.to_numeric(df['mes'].astype(str).str.replace(',', ''), errors='coerce')

        # se imprime conversion para validar
        print("Valores únicos en la columna 'ano' después de la conversión:", df['ano'].unique())

        # Información resumida
        try:
            total_victimas_anio = df.groupby('ano').size()
            total_victimas_mes = df.groupby('mes').size()
            total_victimas_departamento = df.groupby('departamento').size()
            total_victimas_actividad = df.groupby('actividad').size()
            total_victimas_genero = df.groupby('genero').size()
            total_victimas_estado = df.groupby('estado').size()
        except KeyError as e:
            print(f"Error: {e}")
            print("Nombres de columnas disponibles:", df.columns)
            continue

        # Guardar resultados en un archivo de texto en la carpeta de salida
        output_file = os.path.join(output_dir, f'resumen_{filename.replace(".csv", "")}.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Total víctimas por año:\n")
            f.write(total_victimas_anio.to_string())
            f.write("\n\nTotal víctimas por mes (Independiente del año):\n")
            f.write(total_victimas_mes.to_string())
            f.write("\n\nTotal víctimas por departamento:\n")
            f.write(total_victimas_departamento.to_string())
            f.write("\n\nTotal víctimas por actividad:\n")
            f.write(total_victimas_actividad.to_string())
            f.write("\n\nTotal víctimas por género:\n")
            f.write(total_victimas_genero.to_string())
            f.write("\n\nTotal víctimas por estado:\n")
            f.write(total_victimas_estado.to_string())

        end_time = time.time()
        print(f"Procesado {filename} en {end_time - start_time} segundos")
