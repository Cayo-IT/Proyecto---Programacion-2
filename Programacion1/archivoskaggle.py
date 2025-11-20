'''
Obtencion de 2 archivos (Dataset, Kaggle)
-csv 
-json
Menu: 1) CSV 2) JSON
una vez seleccionado:
Menu CSV o JSON: 1) Grafica 1 2) Grafica 2
un aprox de 50000 datos es decir 10000 registros x 5 variables
que ambos sean de temas diferentes 
Mostrar informacion (resumido)
Elaborar 2 graficas por cada archivo
utilizando funciones
Obtener csv()
obtener json()
mostrarGrafica()
'''
#Librerias a utilizar
import pandas as pd
import matplotlib.pyplot as plt
import kaggle 
#Archivos
#Archivo csv: https://www.kaggle.com/datasets/anandshaw2001/video-game-sales
# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = ""

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "anandshaw2001/video-game-sales",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())

#Archivo json: 
