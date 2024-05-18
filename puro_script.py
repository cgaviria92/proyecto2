import csv
import unidecode
from collections import defaultdict
import os
import time

# Directorios de entrada y salida
input_dir = 'carpeta_entrada'
output_dir = 'carpeta_salida_puro'

os.makedirs(output_dir, exist_ok=True)

# limpiar los caracteres especiales
def clean_string(s):
    return unidecode.unidecode(s).replace(' ', '_').lower()

#Recorremos los archivos guardados en la carpeta de entrada
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        start_time = time.time()
        
        # Cargar el archivo CSV
        file_path = os.path.join(input_dir, filename)
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        # Limpiar olumnas 
        cleaned_columns = {col: clean_string(col) for col in reader.fieldnames}
        cleaned_data = []
        for row in data:
            cleaned_row = {cleaned_columns[key]: unidecode.unidecode(value) for key, value in row.items()}
            cleaned_data.append(cleaned_row)

        # Corregir valores
        for row in cleaned_data:
            if row['genero'].lower() in ['m', 'h']:
                row['genero'] = 'hombre'
            elif row['genero'].lower() in ['f', 'mujer']:
                row['genero'] = 'mujer'
            
            # Eliminar comas de los valores de 'ano' y 'mes'
            row['ano'] = int(row['ano'].replace(',', ''))
            row['mes'] = int(row['mes'].replace(',', ''))

        # diccionarios para almacenar
        total_victimas_anio = defaultdict(int)
        total_victimas_mes = defaultdict(int)
        total_victimas_departamento = defaultdict(int)
        total_victimas_actividad = defaultdict(int)
        total_victimas_genero = defaultdict(int)
        total_victimas_estado = defaultdict(int)

        # Calcular totales
        for row in cleaned_data:
            total_victimas_anio[row['ano']] += 1
            total_victimas_mes[row['mes']] += 1
            total_victimas_departamento[row['departamento']] += 1
            total_victimas_actividad[row['actividad']] += 1
            total_victimas_genero[row['genero']] += 1
            total_victimas_estado[row['estado']] += 1

        # Salida archivo de texto
        output_file = os.path.join(output_dir, f'resumen_{filename.replace(".csv", "")}.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Total víctimas por año:\n")
            for key, value in total_victimas_anio.items():
                f.write(f"{key}: {value}\n")
            
            f.write("\nTotal víctimas por mes (Independiente del año):\n")
            for key, value in total_victimas_mes.items():
                f.write(f"{key}: {value}\n")
            
            f.write("\nTotal víctimas por departamento:\n")
            for key, value in total_victimas_departamento.items():
                f.write(f"{key}: {value}\n")
            
            f.write("\nTotal víctimas por actividad:\n")
            for key, value in total_victimas_actividad.items():
                f.write(f"{key}: {value}\n")
            
            f.write("\nTotal víctimas por género:\n")
            for key, value in total_victimas_genero.items():
                f.write(f"{key}: {value}\n")
            
            f.write("\nTotal víctimas por estado:\n")
            for key, value in total_victimas_estado.items():
                f.write(f"{key}: {value}\n")

        end_time = time.time()
        print(f"Procesado {filename} en {end_time - start_time} segundos")
