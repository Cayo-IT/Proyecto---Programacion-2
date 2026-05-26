import random as rm
import pygame as py

#Resolucion

ANCHO = 800
ALTO = 600

# JUGADOR y BALAS

pos_x = ANCHO * 0.5
pos_y = ALTO * 0.5
player_scale = 10
vel_player = 3
vel_bal = 5

#Frames por segundo

FPS = 60

#enemigos

enemy_pos = [700, 300]
vel_enemy = 6
enemy_live = True
enemy_dir = 1

# Colision

jugador_rect = py.Rect(pos_x, pos_y, 20, 20)
enemigo_rect = py.Rect(enemy_pos[0], enemy_pos[1], 30, 30)