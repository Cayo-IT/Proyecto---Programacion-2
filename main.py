import pygame
import constantes as const
import random as rm

pygame.init()
pantalla = pygame.display.set_mode((const.ANCHO, const.ALTO))
reloj = pygame.time.Clock()
ejecutor = True

balas = []


while ejecutor:      # Bucle principal
    
    # Captura eventos (Teclado)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutor = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nueva_bala = [const.pos_x, const.pos_y]
                balas.append(nueva_bala)
                
    # logica ( movimiento, balas, colisiones)
    
    tecla = pygame.key.get_pressed()
    
    if tecla[pygame.K_a]:
        const.pos_x -= const.vel_player
        if const.pos_x < 0:     # limite de pantalla
            const.pos_x = 0
    if tecla[pygame.K_d]:
        const.pos_x += const.vel_player
        if const.pos_x > const.ANCHO:     # limite de pantalla
            const.pos_x = const.ANCHO
    if tecla[pygame.K_w]:
        const.pos_y -= const.vel_player
        if const.pos_y < 0:    # limite de pantalla
            const.pos_y = 0
    if tecla[pygame.K_s]:
        const.pos_y += const.vel_player
        if const.pos_y > const.ALTO:     # limite de pantalla
            const.pos_y = const.ALTO

    const.enemy_pos[1] += 3 * const.enemy_dir
    if const.enemy_pos[1] > const.ALTO - 10 or const.enemy_pos[1] < 0:
        const.enemy_dir *= -1
    
    for b in balas:
        b[0] += const.vel_bal
        if b[0] > const.ANCHO:
            balas.remove(b)
        if const.enemy_live:
            if const.enemy_pos[0] < b[0] < const.enemy_pos[0] + 40 and \
               const.enemy_pos[1] < b[1] < const.enemy_pos[1] + 40:
                const.enemy_live = False
                balas.remove(b)   
                
    # Dibujo ( Renderizado)
    
    for b in balas:
        pygame.draw.circle(pantalla, (225, 225, 0), (b[0], b[1]), 3)
        
    pygame.draw.circle(pantalla, (0, 240, 0), (const.pos_x, const.pos_y), const.player_scale) # Jugador
    if const.enemy_live:
        pygame.draw.rect(pantalla, (0, 100, 0), (const.enemy_pos[0], const.enemy_pos[1], 30, 30))
    if const.jugador_rect.colliderect(const.enemigo_rect):
        print("piro")
    pygame.display.flip()  # actualiza ventana
    pantalla.fill((0, 0, 0)) # limpia ventana
    reloj.tick(const.FPS) # FPS 

pygame.quit()