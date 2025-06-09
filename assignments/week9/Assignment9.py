import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emoji Drawing Game")
clock = pygame.time.Clock()

# Base Brush class
class Brush:
    def __init__(self, emoji, size=36):
        self._emoji = emoji
        self._size = size

    def draw(self, surface, pos):
        emoji_font = pygame.font.Font(None, self._size)

        # Make sure the emoji is valid and non-empty
        if not self._emoji.strip():
            return  # skip drawing

        emoji_surface = emoji_font.render(self._emoji, True, (0, 0, 0))
        if emoji_surface.get_width() > 0:
            surface.blit(emoji_surface, (pos[0] - self._size // 2, pos[1] - self._size // 2))

    def set_emoji(self, emoji):
        self._emoji = emoji

    def get_emoji(self):
        return self._emoji

    def set_size(self, size):
        self._size = size

    def get_size(self):
        return self._size

# Subclass with extra method (optional)
class FancyBrush(Brush):
    def sparkle(self):
        print(f"{self._emoji} sparkles!")

# Instruction screen
def instruction_screen():
    font = pygame.font.SysFont(None, 42)
    screen.fill((255, 255, 255))
    instructions = [
        "🎨 Emoji Drawing Game 🎨",
        "Click and drag to draw with emojis.",
        "Press 1/2/3 to change brush.",
        "Arrow Up/Down to change size.",
        "Press 'C' to clear.",
        "Click anywhere to start!"
    ]
    for i, line in enumerate(instructions):
        text = font.render(line, True, (0, 0, 0))
        screen.blit(text, (50, 60 + i * 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

# Main game loop
def main():
    instruction_screen()

    current_brush = FancyBrush("🌸", size=36)
    is_drawing = False

    screen.fill((255, 255, 255))  # Clear background

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:
                is_drawing = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_brush.set_emoji("🌸")
                elif event.key == pygame.K_2:
                    current_brush.set_emoji("🌟")
                elif event.key == pygame.K_3:
                    current_brush.set_emoji("🍀")
                elif event.key == pygame.K_UP:
                    current_brush.set_size(min(100, current_brush.get_size() + 10))
                elif event.key == pygame.K_DOWN:
                    current_brush.set_size(max(20, current_brush.get_size() - 10))
                elif event.key == pygame.K_c:
                    screen.fill((255, 255, 255))  # Clear canvas

        if is_drawing:
            pos = pygame.mouse.get_pos()
            current_brush.draw(screen, pos)

        pygame.display.flip()
        clock.tick(60)

# Start the game
if __name__ == "__main__":
    main()

"""
🎮 How to Play:

- Click and drag with your mouse to paint emojis on the canvas.
- Press 1 = 🌸 | 2 = 🌟 | 3 = 🍀 to change brush.
- ↑ = Increase brush size, ↓ = Decrease brush size.
- Press 'C' to clear the screen.
- Close the window to quit the game.
"""

