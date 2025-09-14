import random
import time
import sys

def type_print(text, delay=0.02, end="\n"):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def ask_int_in_range(prompt, lo, hi):
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print(f"⚠️ Please enter a valid integer between {lo} and {hi}.")
            continue
        if lo <= val <= hi:
            return val
        print(f"⚠️ Number must be between {lo} and {hi}.")

def ask_nonempty_str(prompt, max_len=24):
    while True:
        s = input(prompt).strip()
        if not s:
            print("⚠️ Please enter a non-empty name.")
            continue
        if len(s) > max_len:
            print(f"⚠️ Keep it short (≤ {max_len} chars).")
            continue
        return s

type_print("🌷 Welcome to the ASCII Garden Generator!", 0.015)
num_flowers   = ask_int_in_range("How many flowers do you want to grow? (3–10): ", 3, 10)
flower_height = ask_int_in_range("How tall should the flowers be? (3–12): ", 3, 12)
garden_name   = ask_nonempty_str("What should we name your garden? ")

wind_strength = ask_int_in_range("Pick wind level (0=calm, 1=breeze, 2=windy): ", 0, 2)

stems   = ['|', '!', ':', 'i']
leaves  = ['/', '\\', 'v', '']
petals  = ['@', '*', 'O', '✿', '❀', '✸', '+']
visitors = ['🦋', '🐝', '🪲', '🐞', '🦗']

tile_width = num_flowers * 3 + 2
border_width = max(tile_width, len(garden_name) + 8)

print("\n" + garden_name.center(border_width, '='))
type_print("Sowing seeds…", 0.01)
time.sleep(0.4)

if random.random() < 0.6:
    parade = "".join(random.choice(visitors) for _ in range(random.randint(5, 10)))
    print(parade.center(border_width))
    time.sleep(0.3)

flower_styles = []
for _ in range(num_flowers):
    style = {
        "petal": random.choice(petals),
        "stem": random.choice(stems),
    }
    flower_styles.append(style)

def sway_offset(frame_idx, level):
    if wind_strength == 0:
        return 0
    base = (-1 if frame_idx % 2 == 0 else 1)
    extra = 1 if wind_strength == 2 and level % 2 == 0 else 0
    return base + extra

def build_tops():
    parts = []
    for style in flower_styles:
        pet = style["petal"]
        k = random.choice([2, 3, 3, 4])
        parts.append(" " + pet * k + " ")
    return "".join(parts)

def build_stems(level, final_level):
    row = []
    for style in flower_styles:
        stem_char = style["stem"]
        if level >= final_level - 2 and random.random() < 0.55:
            left  = random.choice(leaves)
            right = random.choice(leaves)
            row.append(f"{left}{stem_char}{right}")
        else:
            row.append(f" {stem_char} ")
    return "".join(row)

frames = []

tops = build_tops()
frames.append(tops)

for level in range(flower_height):
    frames.append(build_stems(level, flower_height - 1))

ground = "=" * border_width

time.sleep(0.3)
for frame_idx, content in enumerate(frames):
    flair = " ✨" if any(ch in garden_name.lower() for ch in "aeiou") and frame_idx == 0 else ""
    offset = sway_offset(frame_idx, level=frame_idx)
    pad_left = " " * max(0, offset)
    line = (pad_left + content) if offset >= 0 else content[max(0, -offset):]
    print(line.center(border_width) + flair)
    time.sleep(0.15)

print(ground)


rows_of_tiles = 2 if flower_height < 8 else 3
cols_of_tiles = 1 if num_flowers <= 4 else 2

type_print("\nArranging beds…", 0.01)
time.sleep(0.25)

tile = frames[:]
for r in range(rows_of_tiles):
    for line_idx, content in enumerate(tile):
        row_line = []
        for c in range(cols_of_tiles):

            if line_idx == 0 and random.random() < 0.2:
                deco = random.choice(visitors)
            else:
                deco = " "

            offset = sway_offset(line_idx + c, level=line_idx)
            pad_left = " " * max(0, offset)
            seg = (pad_left + content) if offset >= 0 else content[max(0, -offset):]
            row_line.append(seg.ljust(tile_width) + deco)
        print(" ".join(row_line).center(border_width))
        time.sleep(0.05 if r == rows_of_tiles - 1 else 0.03)
    print("=" * border_width)

if garden_name.strip().lower() in {"eden", "paradise", "secret garden"}:
    type_print("\nA unicorn visits your garden… 🦄", 0.02)
else:
    type_print("\n🌼 Your garden is ready! Enjoy! 🌼", 0.02)
