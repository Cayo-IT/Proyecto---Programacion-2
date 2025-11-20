'''
Calular el promedio de calificaciones del alumno
Cuantas materias?: Las que desee el usuario (Enter para terminar)
No hay calificacion aun?: Generar aleatorio [30, 100]
meter al diccionario?
dict[materia]    =  Calificacion
(Variable key)   (Variable value)
obtener datos del diccionario?: {dict.keys() <- llaves, dict.values() <- valores, len() <- cantidad}
ej: 
Nombre: Juan
Materia: Programacion(key)
Calificacion: 70(value)(Aleatorio [30, 100])
Materia: Pensamiento Matematico(key)
Calificacion: 100(value)
Salida: Juan debe tener un promedio de ## para el semestre 2025-2
Con: 
    Programacion 70
    Pensamiento Matematico 100
    . etc
'''
#Libreria
import random
#Diccionario  
materias = {}
#Solicitar el nombre al usuario
nombre = input("Introduzca su nombre: ")
if nombre == "":
    while True:
        nombre = input("Introduzca su nombre: ")
        if nombre != "":
            break
#Solicitar las materias y calificaciones
print("Introduzca las materias y calificaciones, presione Enter sin escribir nada para terminar:")
while True:
    materia = input("Introduzca la materia: ")
    if materia == "":
        break
    calificacion = input("Introduzca su calificacion: ")
    if calificacion == str or "" or float:
        calificacion = random.randint(30, 100)
    #Agregar al diccionario las calificaciones y materias
    materias[materia] = int(calificacion)
#Calcular el promedio
promedio = float(sum(materias.values()) / len(materias)) 
#Mostrar salida al usuario
print(nombre, "debe tener un promedio de", promedio, "para el semestre 2025-2, con las siguientes materias:")
for materia, calificacion in materias.items(): 
    print(f"{materia}: {calificacion}")
print("")
print("Elaborado por Carlos Omar Sanchez Torrescano")
