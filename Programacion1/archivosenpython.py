import pandas as pd
import matplotlib.pyplot as plt
import kagglehub

# Download latest version
path = kagglehub.dataset_download("richave/tortilla-prices-in-mexico")

print("Path to dataset files:", path)

df=pd.read_csv('data.csv')
print("Resumen de datos:")
print(df)
#print("Datos completos:")
#print(df.to_string())
print("Informacion resumen:")
print(df.info())
print("Descripciones:")
print(df.describe())

#Graficas de datos

#General
df.plot()

#Grafica de puntos (Scatter / Dispersion)
x=df['Año']
y=df['Precio por Kg']
plt.xlabel('Año')
plt.ylabel('Precio por Kg')
plt.title("Precio de la tortilla(Kg) en Mexico por Año ")
plt.scatter(x, y)
plt.show()

#Linea
plt.plot(x, y)
plt.show()