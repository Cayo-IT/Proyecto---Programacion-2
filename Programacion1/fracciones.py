'''
Tener dos fracciones f1=n1/d1 y f2= n2/d2
donde, n1: 0 al 9 y donde d1 mayor o igual a n1
f1<1, f2<1
para los siguientes casos
a) suma (n1/d1)+(n2/d2) = n3/d3
b) resta (n1/d1)-(n2/d2) = n3/d3
c) multiplicacion (n1/d1)*(n2/d2) = n3/d3
d) division (n1/d1)/(n2/d2) = n3/d3
Que el resultado sea simplificado ej: 3/9 = 1/3, 20/40 = 1/2
la manera de tener un numero aleatorio es mediante librerias:
import math <-- uso de Maximo comun divisor para la simplificacion de fracciones
import random <-- libreria clave
random.randint()

'''
import random
import math 
random.randint(0,9)

#Variables para las fracciones
n1, n2  = random.randint(0,9), random.randint(0,9)
d1, d2 = random.randint(0,9), random.randint(0,9)
operacion = True 
n3 = 0
d3 = 0 

#Repitir hasta que no de 0 para que sea valida las fracciones
while n1 >= d1 or n2 >= d2 or d1 == 0 or d2 == 0:
     n1, n2  = random.randint(0,9), random.randint(0,9)
     d1, d2 = random.randint(0,9), random.randint(0,9)

#Bienvenida
print("Hola!, aqui podras observar como funciona las fracciones con distintos operadores")
print("Escoja que operacion quiera realizar (1,2,3,4): 1 = Suma, 2 = Resta, 3 = Multiplicacion, 4 = Division")
x = int(input())

match x:
    case 1:
        #Suma
         print("Suma:")
         n3 = ((n1*d2)+(d1*n2))
         d3 = d1*d2
         if operacion: 
             #Encontrar el Maximo Comun Divisor (MCD)
             mcd = math.gcd(n3, d3)
             #Dividir numerador y denominador por el MCD
             n3_simplificado = n3 // mcd
             d3_simplificado = d3 // mcd
         print("(",n1,"/",d1,")","+","(",n2,"/",d2,")","=","(",n3,"/",d3,")")
         print("Fraccion simplificada:", n3_simplificado,"/",d3_simplificado)
    case 2:
         #Resta
         print("Resta:")
         n3 = ((n1*d2)-(d1*n2))
         d3 = d1*d2
         if operacion: 
             #Encontrar el Maximo Comun Divisor (MCD)
             mcd = math.gcd(n3, d3)
             #Dividir numerador y denominador por el MCD
             n3_simplificado = n3 // mcd
             d3_simplificado = d3 // mcd
         print("(",n1,"/",d1,")","-","(",n2,"/",d2,")","=","(",n3,"/",d3,")")
         print("Fraccion simplificada:", n3_simplificado,"/",d3_simplificado)
    case 3: 
         #Multiplicacion
         print("Multiplicacion:")
         n3 = n1*d1
         d3 = n2*d2
         if operacion:
             #Encontrar el Maximo Comun Divisor (MCD)
             mcd = math.gcd(n3, d3)
             #Dividir numerador y denominador por el MCD
             n3_simplificado = n3 // mcd
             d3_simplificado = d3 // mcd
         print("(",n1,"/",d1,")","x","(",n2,"/",d2,")","=","(",n3,"/",d3,")")
         print("Fraccion simplificada:", n3_simplificado,"/",d3_simplificado)
    case 4: 
         #Division
         print("Division:")
         n3 = n1*d2
         d3 = n2*d1
         if operacion:
             #Encontrar el Maximo Comun Divisor (MCD)
             mcd = math.gcd(n3, d3)
             #Dividir numerador y denominador por el MCD
             n3_simplificado = n3 // mcd
             d3_simplificado = d3 // mcd
         print("(",n1,"/",d1,")","/","(",n2,"/",d2,")","=","(",n3,"/",d3,")")
         print("Fraccion simplificada:", n3_simplificado,"/",d3_simplificado)


print("")
print("Elaborado por Carlos Omar Sanchez Torrescano")