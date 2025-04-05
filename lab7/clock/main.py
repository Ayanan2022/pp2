from core.renderer import draw_clock
from datetime import datetime
import pygame

pygame.init()
screen = pygame.display.set_mode((829, 836))
pygame.display.set_caption("Mickey Clock")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.now().time()
    draw_clock(screen, current_time)

    pygame.display.flip()
