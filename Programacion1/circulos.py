#preguntarle al usuario si quiere un circulo en 2D o 3D
#Si es 2D: Pedir el radio para luego calcular el area y perimetro
#Mostrar salida al usuario
#Si es 3D: Pedir radio para luego calcular volumen y area
#Mostrar salida al usuario
#Usar libreria para valores matematicos (pi)
import math
print("Buenas, como desea que sea el circulo: 2D o 3D?, introduzca el que desee seleccionar: ")

#Se lee y se guarda la variable a comparar
figura = input()

#Inicio de la condicional
if figura == "2D":
    print("Introduzca el Radio: ")
    radio = float(input())
    #Formulas 2D
    area2D = math.pi * (radio*radio)
    perimetro = 2*(math.pi)*radio
    print("El circulo de radio", radio, "tiene un perimetro de,", perimetro, "unidades y un area de,", area2D, "unidades cuadradas")
else:
   if figura == "3D":
    print("Introduzca el Radio: ")
    radio = float(input())
    print("Introfuzca la altura: ")
    h = float(input())
    #Formulas 3D
    volumen = (math.pi)*(radio*radio)*(h) 
    area3D = 2*(math.pi*radio)*(radio+h)
    print("El ciruclo de radio", radio,"tiene un volumen de", volumen,"y cuenta con un area de",area3D,"unidades cubicas")
print("")
print("Elaborado por Carlos Omar Sanchez Torrescano")