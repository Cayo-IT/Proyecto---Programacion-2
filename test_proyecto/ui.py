import pygame

class Boton:
    """Clase para crear botones interactivos en pantalla."""
    def __init__(self, x, y, ancho, alto, texto, fuente, color_normal, color_hover):
        #guardar las dimensiones y posición del botón
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.fuente = fuente
        self.color_normal = color_normal  #color cuando no se toca
        self.color_hover = color_hover    #color cuando el mouse pasa por encima
        self.color_actual = self.color_normal
        self.texto_color = (255, 255, 255) #blanco

    def dibujar(self, pantalla):
        #dibujar el rectangulo del boton en la pantalla
        pygame.draw.rect(pantalla, self.color_actual, self.rect, border_radius=8)
        #dibujamr un borde para que se vea mejor
        pygame.draw.rect(pantalla, (233, 69, 96), self.rect, 2, border_radius=8)
        
        #Renderizar el texto (crear la imagen del texto)
        texto_superficie = self.fuente.render(self.texto, True, self.texto_color)
        #Centrar el texto dentro del boton
        texto_rect = texto_superficie.get_rect(center=self.rect.center)
        pantalla.blit(texto_superficie, texto_rect)

    def manejar_evento(self, evento):
        """Verifica si el botón fue presionado o si el mouse está encima."""
        pos_mouse = pygame.mouse.get_pos()
        
        #cambiar el color si el mouse está sobre el botón (Efecto Hover)
        if self.rect.collidepoint(pos_mouse):
            self.color_actual = self.color_hover
            #si el evento es un clic izquierdo (botón 1) del mouse
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                return True #el botón fue presionado
        else:
            self.color_actual = self.color_normal
            
        return False #no fue presionado


class Slider:
    """Clase para crear barras ajustables (como las de volumen)."""
    def __init__(self, x, y, ancho, alto, valor_inicial):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.valor = valor_inicial #Valor entre 0.0 y 1.0 (0% a 100%)
        self.arrastrando = False

    def dibujar(self, pantalla):
        #dibujar el fondo del slider (gris oscuro)
        pygame.draw.rect(pantalla, (50, 50, 50), self.rect, border_radius=5)
        
        #dibujamos la parte "llena" del slider (color rojo/rosa)
        ancho_lleno = int(self.rect.width * self.valor)
        rect_lleno = pygame.Rect(self.rect.x, self.rect.y, ancho_lleno, self.rect.height)
        pygame.draw.rect(pantalla, (233, 69, 96), rect_lleno, border_radius=5)
        
        #dibujar el "boton" indicador del slider
        pygame.draw.circle(pantalla, (255, 255, 255), (self.rect.x + ancho_lleno, self.rect.y + self.rect.height // 2), self.rect.height)

    def manejar_evento(self, evento):
        """Permite arrastrar el slider para cambiar su valor."""
        pos_mouse = pygame.mouse.get_pos()
        
        #si hace clic dentro del área del slider
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.rect.collidepoint(pos_mouse):
                self.arrastrando = True
                
        #si soltamos el clic
        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            self.arrastrando = False
            
        #si estamos moviendo el mouse mientras arrastramos
        if self.arrastrando:
            #calcular el nuevo valor basado en la posición X del mouse
            nuevo_x = max(self.rect.x, min(pos_mouse[0], self.rect.x + self.rect.width))
            self.valor = (nuevo_x - self.rect.x) / self.rect.width
