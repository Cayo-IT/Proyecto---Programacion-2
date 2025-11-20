'''
Crear una lista con 3 elementos (str)
Le agregamos elementos
Importante -> Solicitar elementos al usuario (Enter para terminar: while)
Imprimir la cantidad
Imprimir los elementos ordenados (ordenar la lista, A -> Z) alfabeticamente
Recorrer la lista y eliminar todos los nombres que no empiecen con vocal
imprimir la cantidad
Importante -> Imprimir los elementos en orden descendente (Z -> A) .reverse()
'''
#Inicio de la lista
nombrealumnos = ['Demian', 'Luis', 'Cesar']
#Imprime nombres
print(nombrealumnos)
#Imprime la cantidad de nombres que hay
print(len(nombrealumnos), "alumnos")
#Insertar nuevo alumno manualmente
nombrealumnos.append("Ignacio")
#Pedir al usuario, los nombres de los demas alumnos
while True:
    nombres = input("Escribe el nombre del alumno: ")
    if nombres.strip() == "":
     break
    nombrealumnos.append(nombres)
#Imprimir los elementos ordenados alfabeticamente
nombrealumnos.sort(key=str.lower) #Ignorando las mayusculas
print("Nombre de los alumnos en orden alfabetico:")
print(nombrealumnos)
print(len(nombrealumnos), "alumnos")
#Recorrer la lista y eliminar todos los nombres que no empiecen con vocal
nombrealumnos = [nombre for nombre in nombrealumnos 
                 if nombre[0].lower() in 'aeiou']
#Imprimir los elementos en orden descendente
print("Nombres de los alumnos en orden descendente y que no empiecen con vocal:")
nombrealumnos.sort(key=str.lower, reverse=True) 
print(nombrealumnos)
#Imprimir nombres restantes
print(len(nombrealumnos), "alumnos")
print("")
print("Elaborado por Carlos Omar Sanchez Torrescano")