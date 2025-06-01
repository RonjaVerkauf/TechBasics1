import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Animation with Classes")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Load your image
original_image = pygame.image.load("My_image.png")
original_image = pygame.transform.scale(original_image, (75, 75))  # Resize if needed

class AnimatedObject:
    def __init__(self):
        self.image = original_image.copy()
        # Add random color tint
        tint_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.image.fill(tint_color, special_flags=pygame.BLEND_RGBA_MULT)

        # Random position and speed
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)

        # Optional: Circular motion
        self.circle_mode = random.choice([True, False])
        self.radius = random.randint(30, 100)
        self.angle = random.uniform(0, 2 * math.pi)
        self.center_x = self.x
        self.center_y = self.y
        self.rotation_speed = random.uniform(0.01, 0.05)

    def update(self):
        if self.circle_mode:
            # Circular motion
            self.angle += self.rotation_speed
            self.x = self.center_x + math.cos(self.angle) * self.radius
            self.y = self.center_y + math.sin(self.angle) * self.radius
        else:
            # Linear motion with bounce
            self.x += self.speed_x
            self.y += self.speed_y

            if self.x <= 0 or self.x >= WIDTH - 50:
                self.speed_x *= -1
            if self.y <= 0 or self.y >= HEIGHT - 50:
                self.speed_y *= -1

    def draw(self, surface):
        # Add transparency (glow effect)
        glow = self.image.copy()
        glow.set_alpha(180)
        surface.blit(glow, (int(self.x), int(self.y)))

# Create multiple instances
objects = [AnimatedObject() for _ in range(10)]

# Main loop
running = True
while running:
    screen.fill((30, 30, 30))  # Dark background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for obj in objects:
        obj.update()
        obj.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
