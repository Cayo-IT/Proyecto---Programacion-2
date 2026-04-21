import pygame 

#1. Inicio del programa
pygame.init()

#2. Configuracion de la ventana
#Ancho
WIDTH = 1000
#Alto
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test")

#El reloj controla la velocidad del juego (los FPS)
clock = pygame.time.Clock()

#Bandera para mantener el ciclo activo
running = True

#3. GAME LOOP 
while running:
    for event in pygame.event.get():
        #Si el usuario hace clic en la "X" de la ventana
        if event.type == pygame.QUIT:
            running = False

    #Actualización de Lógica
    #(Aquí programaremos el movimiento, colisiones y aparición de enemigos)

    #Renderizado (Dibujar en pantalla)
    #Limpiamos la pantalla en cada frame con un color RGB (un azul oscuro)
    screen.fill((20, 20, 40))

    #(Aquí dibujaremos las naves y balas más adelante)

    #Actualizamos la pantalla completa para mostrar lo que dibujamos
    pygame.display.flip()

    #Limitamos el juego a 60 Fotogramas Por Segundo (FPS)
    clock.tick(60)

#4. Cierre del programa
pygame.quit()