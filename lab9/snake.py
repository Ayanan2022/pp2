import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10
FOOD_LIFETIME = 5000  # Food disappears after 5 seconds

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font setup
font = pygame.font.Font(None, 36)
score = 0

# Snake setup
snake = [(100, 100), (90, 100), (80, 100)]
direction = (CELL_SIZE, 0)

# Food setup
def generate_food():
    x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    value = random.choice([1, 2, 3])  # Different weights
    return (x, y, value, pygame.time.get_ticks())

food = generate_food()

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
    
    # Move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)
    
    # Check if food is eaten
    if new_head[:2] == food[:2]:
        # Increase snake size based on food value
        score += food[2]
        for _ in range(food[2] - 1):
            snake.append(snake[-1])
        food = generate_food()
    else:
        snake.pop()
    
    # Check if food expired
    if pygame.time.get_ticks() - food[3] > FOOD_LIFETIME:
        food = generate_food()
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    
    # Draw food (size based on value)
    color = RED if food[2] == 1 else BLUE if food[2] == 2 else (255, 165, 0)
    pygame.draw.rect(screen, color, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # Check collisions
    if new_head in snake[1:] or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        running = False  # End game if collision happens
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
