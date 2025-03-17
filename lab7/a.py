import pygame
import datetime
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CENTER = (200, 200)
BACKGROUND_COLOR = (255, 255, 255)

# Load Mickey's hands images
minute_hand_image = pygame.image.load("minute_hand.png")  # Load the image for the minute hand
second_hand_image = pygame.image.load("second_hand.png")  # Load the image for the second hand

# Scale hands to appropriate size
minute_hand = pygame.transform.scale(minute_hand_image, (20, 100))
second_hand = pygame.transform.scale(second_hand_image, (10, 100))

# Get hand image center points for rotation
minute_hand_center = (minute_hand.get_width() // 2, minute_hand.get_height() - 10)
second_hand_center = (int(second_hand_image.get_width() / 2), second_hand_image.get_height() - 20)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# Load background image
background = pygame.image.load("mickey_clock.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

def rotate_hand(image, angle, center):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=screen.get_rect().center)
    return pygame.transform.rotate(image, angle), new_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((255, 255, 255))  # White background
    
    # Get current time
    current_time = datetime.datetime.now()
    minutes = current_time.minute
    seconds = current_time.second
    
    # Calculate rotation angles
    minute_angle = -6 * minutes
    second_hand_angle = -6 * seconds  # 360°/60 seconds = 6° per second
    
    # Rotate hands
    rotated_minute, min_rect = rotate_hand(minute_hand, minutes_angle)
    rotated_second, sec_rect = rotate_hand(second_hand, seconds_angle)
    
    # Draw clock hands on the screen
    screen.fill((255, 255, 255))  # Clear screen
    screen.blit(rotated_minute, min_rect)
    screen.blit(rotated_second, sec_rect)
    
    pygame.display.flip()
    
    pygame.time.wait(1000)  # Update every second

pygame.quit()
