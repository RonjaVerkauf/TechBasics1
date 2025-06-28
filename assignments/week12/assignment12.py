import pygame
import random

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Player class
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 70))
        self.speed = 6

    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        # Bonus: keep player within screen using clamp_ip
        self.rect.clamp_ip(screen.get_rect())

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((10, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10

    def update(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Enemy class
class Enemy:
    def __init__(self):
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        x = random.randint(0, WIDTH - 40)
        self.rect = self.image.get_rect(topleft=(x, -40))
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Power-up class using inflate and contains
class PowerUp:
    def __init__(self):
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 255, 0))
        x = random.randint(0, WIDTH - 30)
        y = random.randint(0, HEIGHT - 30)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hitbox = self.rect.inflate(10, 10)  # Bonus: larger hitbox

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Game objects
player = Player()
bullets = []
enemies = [Enemy() for _ in range(5)]
powerup = PowerUp()
score = 0

# Font
font = pygame.font.SysFont(None, 32)

# Main loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shoot bullets
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(Bullet(player.rect.centerx, player.rect.top))

    # Movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Update bullets
    for bullet in bullets[:]:
        bullet.update()
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    # Update enemies
    for enemy in enemies[:]:
        enemy.update()
        # Collision with bullets
        for bullet in bullets[:]:
            if enemy.rect.colliderect(bullet.rect):  # Collision detection
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break
        # Enemy passed player
        if enemy.rect.top > HEIGHT:
            enemies.remove(enemy)
            enemies.append(Enemy())

    # Collision with power-up (bonus: using contains)
    if player.rect.contains(powerup.hitbox):
        score += 5
        powerup = PowerUp()  # Respawn somewhere else

    # Draw everything
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    powerup.draw(screen)

    # Score display
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
