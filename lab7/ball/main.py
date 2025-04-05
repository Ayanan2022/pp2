import pygame
import sys
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.logic import update_position
from game.renderer import draw_ball
from game.handler import process_events

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

ball_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

clock = pygame.time.Clock()

while True:
    if process_events():  # выход
        pygame.quit()
        sys.exit()

    keys = pygame.key.get_pressed()
    update_position(keys, ball_position)

    screen.fill((255, 255, 255))
    draw_ball(screen, ball_position)

    pygame.display.flip()
    clock.tick(FPS)
