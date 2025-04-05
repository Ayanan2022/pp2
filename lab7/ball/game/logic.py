from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, STEP
import pygame 

def update_position(keys, pos):
    if keys[pygame.K_UP] and pos[1] - STEP > 0:
        pos[1] -= STEP
    if keys[pygame.K_DOWN] and pos[1] + STEP < SCREEN_HEIGHT:
        pos[1] += STEP
    if keys[pygame.K_LEFT] and pos[0] - STEP > 0:
        pos[0] -= STEP
    if keys[pygame.K_RIGHT] and pos[0] + STEP < SCREEN_WIDTH:
        pos[0] += STEP
