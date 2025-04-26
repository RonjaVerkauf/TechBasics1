import random
import time

# 🌷 Get user input
num_flowers = int(input("How many flowers do you want to grow? (3–10): "))
flower_height = int(input("How tall should the flowers be? (3–10): "))
garden_name = input("What do you want to name your garden? ")

# Sanitize input
num_flowers = max(3, min(10, num_flowers))
flower_height = max(3, min(10, flower_height))
garden_name = garden_name.strip()

# 🌺 Flower styles
stems = ['|', '!', ':', 'i']
leaves = ['/', '\\', 'v', '']
petals = ['@', '*', 'O', '✿', '❀', '🌸']

# 🌼 Set garden width
total_width = num_flowers * 5

# 🌼 Display garden name
print("\n" + garden_name.center(total_width, '=') + "\n")
time.sleep(1)

# 🌸 Add flower tops FIRST
tops = ''
for _ in range(num_flowers):
    top = random.choice(petals)
    tops += f" {top*3} "
print(tops)
time.sleep(0.3)

# 🌱 Animate growth of each flower
for level in range(flower_height):
    row = ''
    for _ in range(num_flowers):
        stem_char = random.choice(stems)
        if level == flower_height - 2:
            # Occasionally grow a leaf
            left = random.choice(leaves)
            right = random.choice(leaves)
            row += f"{left}{stem_char}{right} "
        else:
            row += f" {stem_char}  "
    print(row)
    time.sleep(0.2)

# 🌍 Add ground
print("=" * total_width)
print("\n🌼 Your garden is ready! 🌼")