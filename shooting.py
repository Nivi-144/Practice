import pygame
import random

# Initialize pygame
pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooting Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)

clock = pygame.time.Clock()

# Player
player_width = 50
player_height = 60
player_x = WIDTH // 2
player_y = HEIGHT - 80
player_speed = 7

# Bullet
bullets = []
bullet_speed = 10

# Enemies
enemies = []
enemy_speed = 4

score = 0
font = pygame.font.SysFont("Arial", 30)

running = True

while running:
    clock.tick(60)

    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_width//2 - 3, player_y])

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed

    if keys[pygame.K_RIGHT] and player_x < WIDTH-player_width:
        player_x += player_speed

    # Spawn enemy
    if random.randint(1, 35) == 1:
        enemies.append([random.randint(0, WIDTH-40), -40])

    # Draw Player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw Bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed

        if bullet[1] < 0:
            bullets.remove(bullet)
        else:
            pygame.draw.rect(screen, GREEN, (bullet[0], bullet[1], 6, 15))

    # Draw Enemies
    for enemy in enemies[:]:
        enemy[1] += enemy_speed

        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
            continue

        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], 40, 40))

        # Collision
        for bullet in bullets[:]:
            if (bullet[0] > enemy[0] and
                bullet[0] < enemy[0] + 40 and
                bullet[1] > enemy[1] and
                bullet[1] < enemy[1] + 40):

                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

        # Player collision
        if (enemy[1] + 40 >= player_y and
            enemy[0] < player_x + player_width and
            enemy[0] + 40 > player_x):

            running = False

    # Score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()

print("Game Over!")
print("Final Score:", score)
