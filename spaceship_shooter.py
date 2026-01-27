import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

clock = pygame.time.Clock()

# Player
player_width = 50
player_height = 40
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 7

# Bullet
bullet_width = 5
bullet_height = 10
bullet_speed = 10
bullets = []

# Enemy
enemy_width = 40
enemy_height = 30
enemy_speed = 3
enemies = []

# Score
score = 0
font = pygame.font.SysFont(None, 30)

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

def spawn_enemy():
    x = random.randint(0, WIDTH - enemy_width)
    y = -enemy_height
    enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

running = True
spawn_timer = 0

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(
                    pygame.Rect(
                        player_x + player_width // 2 - bullet_width // 2,
                        player_y,
                        bullet_width,
                        bullet_height
                    )
                )

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Spawn enemies
    spawn_timer += 1
    if spawn_timer > 40:
        spawn_enemy()
        spawn_timer = 0

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            running = False

    # Collision
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break

    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Score
    draw_text(f"Score: {score}", 10, 10)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
