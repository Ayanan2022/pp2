# Imports
import random
import time
import pygame
import sys
from pygame.locals import *

# Initializing pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
COIN_THRESHOLD = 5  # Increase enemy speed after collecting this many coins

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Loading images
background = pygame.image.load("/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/AnimatedStreet.png")

# Create a game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    """Represents enemy cars moving down the screen."""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        """Moves the enemy down the screen."""
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    """Represents the player-controlled car."""

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        """Handles player movement using arrow keys."""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def collect_coin(self, coins):
        """Detects collision with coins and returns the collected coin."""
        collisions = pygame.sprite.spritecollide(self, coins, True)
        if collisions:
            return collisions[0].value  # Return the value of the collected coin
        return 0


class Coin(pygame.sprite.Sprite):
    """Represents randomly generated coins with different values."""

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/coin-svgrepo-com.svg")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.value = random.choice([1, 2, 3])  # Different coin weights

    def move(self):
        """Moves the coin down the screen."""
        self.rect.move_ip(0, SPEED // 2)  # Coins move slower than enemies
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Initializing player, enemy, and first coin
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()

# Adding the first batch of coins
for _ in range(3):
    coins.add(Coin())

# Creating sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(*coins)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # Gradually increase enemy speed over time
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Drawing background
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_scores = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (SCREEN_WIDTH - 100, 10))

    # Updating and drawing all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check for coin collection
    collected_value = P1.collect_coin(coins)
    if collected_value > 0:
        COIN_SCORE += collected_value
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

        # Increase enemy speed when player earns N coins
        if COIN_SCORE % COIN_THRESHOLD == 0:
            SPEED += 1

    # Check for collision between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/crash.wav').play()
        time.sleep(0.5)

        # Display game over screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
