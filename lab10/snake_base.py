import pygame
import random
import sys
import psycopg2
import time

# Initialize Pygame
pygame.init()

# Database connection
conn = psycopg2.connect(database="testdb", user="postgres", password="1234", host="localhost", port="5432")
cur = conn.cursor()

# Define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)

# Game setup
display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake_block = 10

# Define tables
def create_tables():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS "User" (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS user_score (
        score_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES "User"(user_id),
        level INT NOT NULL,
        score INT NOT NULL
    );
    """)
    conn.commit()

# DB interaction functions
def get_user_id(username):
    cur.execute("SELECT user_id FROM \"User\" WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        cur.execute("INSERT INTO \"User\" (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

def insert_user_score(user_id, level, score):
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()

def show_current_level(username):
    cur.execute("""
    SELECT level FROM user_score 
    INNER JOIN "User" ON user_score.user_id = "User".user_id 
    WHERE "User".username = %s ORDER BY score_id DESC LIMIT 1
    """, (username,))
    row = cur.fetchone()
    if row:
        print(f"Welcome back, {username}! Your current level is: {row[0]}")
    else:
        print(f"Welcome, {username}! New player.")

# Snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.body = [[300, 200]]
        self.direction = "RIGHT"

    def change_dir_to(self, dir):
        if dir == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if dir == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if dir == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if dir == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'

    def move(self):
        head = self.body[0][:]
        if self.direction == 'RIGHT':
            head[0] += snake_block
        elif self.direction == 'LEFT':
            head[0] -= snake_block
        elif self.direction == 'UP':
            head[1] -= snake_block
        elif self.direction == 'DOWN':
            head[1] += snake_block
        self.body.insert(0, head)
        if len(self.body) > self.size:
            self.body.pop()

    def grow(self):
        self.size += 1

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:] or \
               head[0] < 0 or head[0] >= display_width or \
               head[1] < 0 or head[1] >= display_height

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, (0, 255, 0), [segment[0], segment[1], snake_block, snake_block])

# Food class
class Food:
    def __init__(self):
        self.position = [random.randrange(0, display_width - snake_block, snake_block),
                         random.randrange(0, display_height - snake_block, snake_block)]

    def respawn(self, snake_body):
        while True:
            new_pos = [random.randrange(0, display_width - snake_block, snake_block),
                       random.randrange(0, display_height - snake_block, snake_block)]
            if new_pos not in snake_body:
                self.position = new_pos
                break

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), [self.position[0], self.position[1], snake_block, snake_block])

# UI messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])

def show_score(username, score, level):
    value = score_font.render(f"{username} Score: {score}  Level: {level}", True, (0, 0, 0))
    dis.blit(value, [10, 10])

# Main game loop
def game_loop(username):
    user_id = get_user_id(username)
    snake = Snake()
    food = Food()
    game_over = False
    game_close = False
    level = 1
    score = 0
    snake_speed = 15

    while not game_over:
        while game_close:
            dis.fill((50, 153, 213))
            message("You lost! Press Q-Quit or C-Play Again", (213, 50, 80))
            show_score(username, score, level)  # Include the username
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop(username)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_dir_to('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_dir_to('RIGHT')
                elif event.key == pygame.K_UP:
                    snake.change_dir_to('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_dir_to('DOWN')

        snake.move()

        # Check collision
        if snake.check_collision():
            insert_user_score(user_id, level, score)
            game_close = True

        # Eat food
        if snake.body[0] == food.position:
            snake.grow()
            score += 10
            food.respawn(snake.body)
            if score % 50 == 0:
                level += 1
                snake_speed += 2

        dis.fill((255, 255, 255))
        snake.draw(dis)
        food.draw(dis)
        show_score(username, score, level)  # Include the username
        pygame.display.update()
        clock.tick(snake_speed)

# Main entry
def main():
    create_tables()
    username = input("Enter your username: ")
    show_current_level(username)
    game_loop(username)
    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()
