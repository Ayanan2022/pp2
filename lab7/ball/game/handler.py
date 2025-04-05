import pygame

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False
