import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Player
player_width = 50
player_height = 60
player_x = WIDTH // 2
player_y = HEIGHT - 80
player_speed = 7

# Bullet
bullets = []
bullet_speed = 8

# Enemy
enemy_width = 50
enemy_height = 50
enemies = []

for i in range(5):
    enemy_x = random.randint(0, WIDTH - enemy_width)
    enemy_y = random.randint(50, 200)
    enemies.append([enemy_x, enemy_y])

enemy_speed = 3

# Score
score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shoot bullet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + 22, player_y])

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player inside screen
    player_x = max(0, min(WIDTH - player_width, player_x))

    # Draw player
    pygame.draw.rect(screen, GREEN,
                     (player_x, player_y,
                      player_width, player_height))

    # Move bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        pygame.draw.rect(screen, WHITE,
                         (bullet[0], bullet[1], 5, 10))

        if bullet[1] < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy[1] += enemy_speed

        pygame.draw.rect(screen, RED,
                         (enemy[0], enemy[1],
                          enemy_width, enemy_height))

        # Respawn enemy
        if enemy[1] > HEIGHT:
            enemy[0] = random.randint(0, WIDTH - enemy_width)
            enemy[1] = random.randint(50, 200)

        # Collision
        for bullet in bullets[:]:
            if (enemy[0] < bullet[0] < enemy[0] + enemy_width and
                    enemy[1] < bullet[1] < enemy[1] + enemy_height):

                enemies.remove(enemy)
                bullets.remove(bullet)

                new_enemy_x = random.randint(0, WIDTH - enemy_width)
                enemies.append([new_enemy_x, 50])

                score += 1
                break

    # Display score
    score_text = font.render(f"Score: {score}",
                             True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
