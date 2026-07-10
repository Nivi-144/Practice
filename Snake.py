import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
snake_block = 20
snake_speed = 10

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def show_score(score):
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [10, 10])

def game():
    game_over = False

    x = WIDTH // 2
    y = HEIGHT // 2

    dx = 0
    dy = 0

    snake = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - snake_block, snake_block)
    food_y = random.randrange(0, HEIGHT - snake_block, snake_block)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        screen.fill(WHITE)

        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

        head = [x, y]
        snake.append(head)

        if len(snake) > snake_length:
            del snake[0]

        for block in snake[:-1]:
            if block == head:
                game_over = True

        for block in snake:
            pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - snake_block, snake_block)
            food_y = random.randrange(0, HEIGHT - snake_block, snake_block)
            snake_length += 1

        show_score(snake_length - 1)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()

game()
