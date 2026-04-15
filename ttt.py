import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game 🚗")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player car
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 10
car_speed = 5

# Enemy car
enemy_width = 50
enemy_height = 100
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -100
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()
running = True

def draw_car(x, y):
    pygame.draw.rect(screen, (0, 0, 255), (x, y, car_width, car_height))

def draw_enemy(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, enemy_width, enemy_height))

def show_score(score):
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

# Game loop
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - enemy_width)
        score += 1

    # Collision detection
    if (car_x < enemy_x + enemy_width and
        car_x + car_width > enemy_x and
        car_y < enemy_y + enemy_height and
        car_y + car_height > enemy_y):
        print("Game Over!")
        running = False

    # Draw everything
    draw_car(car_x, car_y)
    draw_enemy(enemy_x, enemy_y)
    show_score(score)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
