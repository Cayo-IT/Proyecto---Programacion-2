import pygame
import sys
from ui import Boton, Slider

#Inicializacion de Pygame
pygame.init()

#configuraciones de la pantalla
ANCHO_PANTALLA = 1280
ALTO_PANTALLA = 720
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Proyecto - Programacion 2")
pantalla_completa = False

#definicion de colores (Formato RGB)
COLOR_FONDO = (26, 26, 46)      #Azul muy oscuro
COLOR_BOTON = (15, 52, 96)      #Azul marino
COLOR_HOVER = (233, 69, 96)     #Rojo/Rosa oscuro para cuando pasas el mouse
COLOR_TEXTO = (255, 255, 255)   #Blanco
COLOR_TITULO = (241, 196, 15)   #Dorado

#definicion de Fuentes (Tamaños)// PLACEHOLDERS por mientras
fuente_titulo = pygame.font.Font(None, 100)
fuente_subtitulo = pygame.font.Font(None, 60)
fuente_botones = pygame.font.Font(None, 40)
fuente_tabla = pygame.font.Font(None, 35)

#CREACION DE BOTONES PRINCIPALES
#Centramos los botones en X restando la mitad de su ancho (300/2 = 150)
centro_x = ANCHO_PANTALLA // 2 - 150

btn_jugar = Boton(centro_x, 300, 300, 60, "JUGAR", fuente_botones, COLOR_BOTON, COLOR_HOVER)
btn_puntos = Boton(centro_x, 380, 300, 60, "PUNTUACIONES", fuente_botones, COLOR_BOTON, COLOR_HOVER)
btn_config = Boton(centro_x, 460, 300, 60, "CONFIGURACIÓN", fuente_botones, COLOR_BOTON, COLOR_HOVER)
btn_salir = Boton(centro_x, 540, 300, 60, "SALIR", fuente_botones, COLOR_BOTON, COLOR_HOVER)

#BOTON PARA VOLVER ATRAS
#Ubicado abajo a la izquierda
btn_volver = Boton(30, ALTO_PANTALLA - 90, 200, 50, "Volver Atrás", fuente_botones, (127, 140, 141), (149, 165, 166))

#BOTONES DE DIFICULTAD (Personajes) 
btn_facil = Boton(200, 350, 180, 250, "Fácil", fuente_botones, COLOR_BOTON, COLOR_HOVER)
btn_normal = Boton(422, 350, 180, 250, "Normal", fuente_botones, COLOR_BOTON, COLOR_HOVER)
btn_dificil = Boton(644, 350, 180, 250, "Difícil", fuente_botones, COLOR_BOTON, COLOR_HOVER)

#CONTROLES DE CONFIGURACION 
slider_musica = Slider(400, 300, 300, 20, 0.5) #50% por default
slider_sonido = Slider(400, 400, 300, 20, 0.75) #75% por default
btn_pantalla = Boton(centro_x, 500, 300, 60, "Pantalla Completa", fuente_botones, COLOR_BOTON, COLOR_HOVER)

#BOTON DE SALIDA
btn_si = Boton(ANCHO_PANTALLA//2 - 160, 450, 140, 60, "SÍ", fuente_botones, (39, 174, 96), (46, 204, 113))
btn_no = Boton(ANCHO_PANTALLA//2 + 20, 450, 140, 60, "NO", fuente_botones, (192, 57, 43), (231, 76, 60))

#variable de estado que controla que pantalla estamos viendo
estado_juego = "MENU_PRINCIPAL"

#funcion para dibujar texto simple en pantalla
def dibujar_texto(texto, fuente, color, superficie, x, y, centrado=False):
    img_texto = fuente.render(texto, True, color)
    rect_texto = img_texto.get_rect()
    if centrado:
        rect_texto.center = (x, y)
    else:
        rect_texto.topleft = (x, y)
    superficie.blit(img_texto, rect_texto)

#GAMELOOP
#reloj = FPS 60 por default
reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
    #llenar la pantalla con el color de fondo en cada frame
    pantalla.fill(COLOR_FONDO)

    #manejo de eventos (Clics del teclado y mouse)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            ejecutando = False #cierra el juego si le dan a la "X" de la ventana

        #MENU PRINCIPAL
        if estado_juego == "MENU_PRINCIPAL":
            if btn_jugar.manejar_evento(evento):
                estado_juego = "MENU_DIFICULTAD"
            if btn_puntos.manejar_evento(evento):
                estado_juego = "MENU_PUNTUACIONES"
            if btn_config.manejar_evento(evento):
                estado_juego = "MENU_CONFIGURACION"
            if btn_salir.manejar_evento(evento):
                estado_juego = "MODAL_SALIR"

        #MENU DIFICULTAD
        elif estado_juego == "MENU_DIFICULTAD":
            if btn_volver.manejar_evento(evento):
                estado_juego = "MENU_PRINCIPAL"
            
            #placeholders para iniciar el juego
            if btn_facil.manejar_evento(evento):
                print("Iniciando juego con Personaje 1 (Fácil)...")
            if btn_normal.manejar_evento(evento):
                print("Iniciando juego con Personaje 2 (Normal)...")
            if btn_dificil.manejar_evento(evento):
                print("Iniciando juego con Personaje 3 (Difícil)...")

        #MENU PUNTUACIONES 
        elif estado_juego == "MENU_PUNTUACIONES":
            if btn_volver.manejar_evento(evento):
                estado_juego = "MENU_PRINCIPAL"

        #MENU CONFIGURACION
        elif estado_juego == "MENU_CONFIGURACION":
            slider_musica.manejar_evento(evento)
            slider_sonido.manejar_evento(evento)
            if btn_pantalla.manejar_evento(evento):
                #cambiar Pantalla completa
                pantalla_completa = not pantalla_completa
                if pantalla_completa:
                    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA), pygame.FULLSCREEN)
                else:
                    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
                    
            if btn_volver.manejar_evento(evento):
                estado_juego = "MENU_PRINCIPAL"

        #MODAL SALIR
        elif estado_juego == "MODAL_SALIR":
            if btn_si.manejar_evento(evento):
                ejecutando = False #termina el bucle, cierra el juego
            if btn_no.manejar_evento(evento):
                estado_juego = "MENU_PRINCIPAL" #regresa al menu

    #dibujado en Pantalla (renderizado)
    
    if estado_juego == "MENU_PRINCIPAL":
        #titulo centrado
        dibujar_texto("RUNMEAL", fuente_titulo, COLOR_TITULO, pantalla, ANCHO_PANTALLA//2, 150, centrado=True)
        #dibujar botones
        btn_jugar.dibujar(pantalla)
        btn_puntos.dibujar(pantalla)
        btn_config.dibujar(pantalla)
        btn_salir.dibujar(pantalla)

    elif estado_juego == "MENU_DIFICULTAD":
        dibujar_texto("Selecciona Dificultad (Personaje)", fuente_subtitulo, COLOR_TEXTO, pantalla, ANCHO_PANTALLA//2, 150, centrado=True)
        #placeholder del arte (Los botones actuan como las opciones por ahora)
        btn_facil.dibujar(pantalla)
        btn_normal.dibujar(pantalla)
        btn_dificil.dibujar(pantalla)
        btn_volver.dibujar(pantalla)

    elif estado_juego == "MENU_PUNTUACIONES":
        dibujar_texto("TABLA DE PUNTUACIONES", fuente_subtitulo, COLOR_TITULO, pantalla, ANCHO_PANTALLA//2, 100, centrado=True)
        
        #textos placeholders de la tabla (puestos fijos por ahora)
        columnas = ["Posición", "Jugador", "Puntuación", "Dificultad"]
        datos = [
            ["1", "jose", "699,999", "Difícil"],
            ["2", "Hustavo", "8507,500", "Normal"],
            ["3", "Tengo ambre", "420,069", "Fácil"]
        ]
        
        #dibujar encabezados
        for i, col in enumerate(columnas):
            dibujar_texto(col, fuente_tabla, COLOR_HOVER, pantalla, 200 + (i*180), 200, centrado=True)
            
        #dibujar datos falsos
        for fila_idx, fila_datos in enumerate(datos):
            for col_idx, dato in enumerate(fila_datos):
                dibujar_texto(dato, fuente_tabla, COLOR_TEXTO, pantalla, 200 + (col_idx*180), 280 + (fila_idx*60), centrado=True)
                
        btn_volver.dibujar(pantalla)

    elif estado_juego == "MENU_CONFIGURACION":
        dibujar_texto("CONFIGURACIÓN", fuente_subtitulo, COLOR_TITULO, pantalla, ANCHO_PANTALLA//2, 150, centrado=True)
        
        dibujar_texto("Música:", fuente_botones, COLOR_TEXTO, pantalla, 250, 300)
        slider_musica.dibujar(pantalla)
        
        dibujar_texto("Sonidos:", fuente_botones, COLOR_TEXTO, pantalla, 250, 400)
        slider_sonido.dibujar(pantalla)
        
        btn_pantalla.dibujar(pantalla)
        btn_volver.dibujar(pantalla)

    elif estado_juego == "MODAL_SALIR":
        #para hacer el "pop-up" primero dibujar el menu principal de fondo
        dibujar_texto("NOMBRE DEL JUEGO", fuente_titulo, COLOR_TITULO, pantalla, ANCHO_PANTALLA//2, 150, centrado=True)
        btn_jugar.dibujar(pantalla)
        btn_puntos.dibujar(pantalla)
        btn_config.dibujar(pantalla)
        btn_salir.dibujar(pantalla)
        
        #crear una capa oscura semi-transparente
        capa_oscura = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
        capa_oscura.set_alpha(200) #nivel de transparencia (0-255)
        capa_oscura.fill((0, 0, 0))
        pantalla.blit(capa_oscura, (0,0))
        
        #dibujamos el cuadro de la pregunta
        rect_modal = pygame.Rect(ANCHO_PANTALLA//2 - 250, 300, 500, 250)
        pygame.draw.rect(pantalla, COLOR_BOTON, rect_modal, border_radius=15)
        pygame.draw.rect(pantalla, COLOR_HOVER, rect_modal, 4, border_radius=15)
        
        dibujar_texto("¿Deseas salir del juego?", fuente_subtitulo, COLOR_TEXTO, pantalla, ANCHO_PANTALLA//2, 380, centrado=True)
        
        btn_si.dibujar(pantalla)
        btn_no.dibujar(pantalla)

    #actualizacion de la pantalla
    pygame.display.flip()
    
    #Controlar a cuantos fps va el juego (60 fps)
    reloj.tick(60)

#salir del programa si el bucle termina
pygame.quit()
sys.exit()
