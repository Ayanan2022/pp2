import pygame
from core.time_utils import get_angles

# Загружаем изображения один раз
bg_image = pygame.image.load("/Users/ayananauryzbaeva/Desktop/pp2/labky/lab7/clock/assets/mickey_clock.png")
sec_image = pygame.image.load("/Users/ayananauryzbaeva/Desktop/pp2/labky/lab7/clock/assets/second_hand.png")
min_image = pygame.image.load("/Users/ayananauryzbaeva/Desktop/pp2/labky/lab7/clock/assets/minute_hand.png")
rect = bg_image.get_rect(center=(415, 418))

def draw_clock(screen, time):
    screen.blit(bg_image, (0, 0))

    sec_angle, min_angle = get_angles(time)

    # Секундная стрелка
    rotated_sec = pygame.transform.rotate(sec_image, sec_angle)
    sec_rect = rotated_sec.get_rect(center=rect.center)
    screen.blit(rotated_sec, sec_rect.topleft)

    # Минутная стрелка
    rotated_min = pygame.transform.rotate(min_image, min_angle)
    min_rect = rotated_min.get_rect(center=rect.center)
    screen.blit(rotated_min, min_rect.topleft)
