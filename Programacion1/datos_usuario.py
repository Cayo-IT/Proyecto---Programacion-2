#Ejercicio: Datos de usuario
#Asignar (multiple) valores a variables (3 tipos de diferentes almenos)
#Solicitar datos al usuario 
#print/input
#Hacer conversiones o datos numericos
#imprimir datos del usuario con su tipo de dato
#ejm: "Juan(str) tiene 32(int) anios y pesa 67(float) kg"

#Inicio del programa y solicitar datos al usuario
nombre , edad, peso = "Juan" , 32, 67 #Asignacion multiple de variables

#Solicitar datos al usuario
#Guardar datos proporcionados por el usuario 
nombre =input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
peso = input("Introduzca su peso: ")
#Hacer conversiones en caso de requerirlo
nombre = str(nombre)
edad = int(edad)
peso = float(peso)

#Mostrar datos
print(nombre,type(nombre),"tiene",edad,type(edad),"anios y pesa",peso,type(peso))