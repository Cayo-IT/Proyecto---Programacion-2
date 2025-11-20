'''
Simular Cajero Automatico
1. Saldo azar [3800, 4600]
NIP = 2025
ingreso = 3 intentos posibles
4. Menu opciones:
A. Cambiar Nip -> Pedir NIP -> Cambiar -> Repetir
B. Retirar 
C. Depositar
D. Movimientos -> ultimos 3 movimientos
E. Consulta Saldo
F. Salir (de la cuenta)
RESTRICCIONES:
a. NIP incorrecto: 3 intentos
b. Retiro > 0 y menor saldo y multiplos de 50
c. Deposito: $25000, exceso cobrar 10% comision > 0
d. 3 movimientos (ultimos) B y C, en caso de no moviemientos -> "No hay movimientos"

'''
#Librerias
import random

#Variables de la Cuenta
dinero = random.randint(3800, 4600)
nip_guardado = 2025

#Variables para movimientos
movimiento_1 = "" #El mas antiguo
movimiento_2 = ""
movimiento_3 = "" #El más reciente

#Inicio del programa
while True:
    
    #Pantalla de Bienvenida
    print("Bienvenido cliente a nuesto cajero virtual")
    print("NIP solo es numerico")

    #Variables de la sesion
    intentos = 3 
    login_exitoso = False

    #Inicio de sesion
    while intentos > 0:
        print(f"Introduzca su NIP (Intentos restantes: {intentos}):")
        nip_texto = input()
        
        if not nip_texto.isdigit():
            print("Error: Ingrese solo números.")
            intentos -= 1
            continue
        
        NIP = int(nip_texto)

        if NIP == nip_guardado:
            login_exitoso = True
            print("NIP Correcto")
            break 
        else:
            print("NIP Incorrecto: ")
            intentos -= 1
    
    if intentos == 0:
        print("Ha agotado sus 3 intentos. Su tarjeta ha sido bloqueada.")
        continue 

    #Menu
    if login_exitoso:
        
        while True: 
            print("Menu:")
            print("[1] Cambiar NIP")
            print("[2] Retirar")
            print("[3] Depositar")
            print("[4] Movimientos")
            print("[5] Consultar Saldo")
            print("[6] Salir de la cuenta")
            
            opcion_texto = input("Seleccione una opcion: ")

            if not opcion_texto.isdigit():
                 print("Error, vuelva a escribir correctamente un digito del 1 al 6")
                 continue
            
            x = int(opcion_texto)
            
            match x:
                #Cambiar NIP
                case 1:
                    print("Cambiar NIP")
                    print("Introduzca su NIP actual:")
                    actual_texto = input()
                    
                    if actual_texto.isdigit() and int(actual_texto) == nip_guardado:
                        print("Introduzca su NUEVO NIP:")
                        nuevo_1_texto = input()
                        print("Repita su NUEVO NIP:")
                        nuevo_2_texto = input()
                        
                        if nuevo_1_texto.isdigit() and nuevo_2_texto.isdigit():
                            if nuevo_1_texto == nuevo_2_texto:
                                nip_guardado = int(nuevo_1_texto)
                                print("NIP cambiado exitosamente")
                            else:
                                print("Error: Los NIPs nuevos no coinciden.")
                        else:
                            print("Error: El nuevo NIP debe ser solo numerico.")
                    else:
                        print("Error: NIP actual incorrecto.")
                
                #Retirar
                case 2:
                    print("Retirar")
                    print(f"Su saldo disponible es: ${dinero}")
                    print("Cuánto desea retirar? (Multiplos de $50):")
                    retiro_texto = input()
                    
                    if not retiro_texto.isdigit():
                        print("Error: Ingrese solo números.")
                    else:
                        monto = int(retiro_texto)
                        
                        if monto <= 0:
                            print("Error: El monto debe ser mayor a 0.")
                        elif monto > dinero:
                            print("Error: Saldo insuficiente.")
                        elif monto % 50 != 0:
                            print("Error: El monto debe ser múltiplo de $50.")
                        else:
                            dinero -= monto
                            print(f"Retiro exitoso. Su nuevo saldo es: ${dinero}")
                            
                            # Actualizar movimientos
                            movimiento_1 = movimiento_2
                            movimiento_2 = movimiento_3
                            movimiento_3 = f"Retiro: -${monto}"

                #Depositar
                case 3:
                    print("Depositar")
                    print("Cuanto desea depositar?:")
                    deposito_texto = input()
                    
                    if not deposito_texto.isdigit():
                        print("Error: Ingrese solo numeros.")
                    else:
                        monto = int(deposito_texto)
                        nuevo_movimiento = "" #Variable temporal
                        
                        if monto <= 0:
                            print("Error: El monto debe ser mayor a 0.")
                        elif monto > 25000:
                            comision = monto * 0.10
                            monto_neto = monto - comision
                            dinero += monto_neto
                            print(f"Se aplico comision del 10% (${comision:.2f}) por exceder $25,000.")
                            print(f"Deposito exitoso de ${monto_neto:.2f}. Su nuevo saldo es: ${dinero}")
                            nuevo_movimiento = f"Deposito: +${monto_neto:.2f} (Comision: -${comision:.2f})"
                        else:
                            dinero += monto
                            print(f"Deposito exitoso. Su nuevo saldo es: ${dinero}")
                            nuevo_movimiento = f"Depósito: +${monto}"
                        
                        #Actualizar movimientos
                        movimiento_1 = movimiento_2
                        movimiento_2 = movimiento_3
                        movimiento_3 = nuevo_movimiento

                #Movimientos
                case 4:
                    print("Ultimos 3 Movimientos")
                    # Comprobar si todas las variables estan vacias
                    if movimiento_1 == "" and movimiento_2 == "" and movimiento_3 == "":
                        print("No hay movimientos.")
                    else:
                        # Imprimir solo las que no esten vacias
                        if movimiento_1 != "":
                            print(movimiento_1)
                        if movimiento_2 != "":
                            print(movimiento_2)
                        if movimiento_3 != "":
                            print(movimiento_3)

                #Consultar Saldo
                case 5:
                    print(f"Su Saldo actual es de: ${dinero}")
                
                #Salir
                case 6:
                    print("Que tenga buen dia!")
                    print("Elaborado por Carlos Omar Sanchez Torrescano")
                    break
                
                #Opcion invalida
                case _: 
                    print("Error, vuelva a escribir correctamente un digito del 1 al 6") 
