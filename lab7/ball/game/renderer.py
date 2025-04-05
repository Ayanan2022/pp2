import pygame
from game.constants import BALL_COLOR, BALL_RADIUS

def draw_ball(screen, position):
    pygame.draw.circle(screen, BALL_COLOR, (position[0], position[1]), BALL_RADIUS)
