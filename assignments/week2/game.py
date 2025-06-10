import time
import random

# --- Funktionen ---
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_valid_number(prompt, min_val, max_val):
    while True:
        try:
            num = int(input(prompt))
            if min_val <= num <= max_val:
                return num
            else:
                print(f"⚠️ Please enter a number between {min_val} and {max_val}!")
        except ValueError:
            print("⚠️ That wasn't a valid number. Try again.")

# --- Start ---
slow_print("🦁 Welcome to the Ultimate Animal Guessing Game! 🌍")
time.sleep(1)
slow_print("Are you ready to test your animal knowledge? 🧠")
time.sleep(1)

# --- Tierliste ---
animals = [
    {"name": "African Elephant", "family": "Elephantidae", "average_size": "3000 kg", "geography": "Africa", "nutrition": "Herbivore"},
    {"name": "Bald Eagle", "family": "Accipitridae", "average_size": "3.5 kg", "geography": "North America", "nutrition": "Carnivore"},
    {"name": "Giant Panda", "family": "Ursidae", "average_size": "100 kg", "geography": "Asia", "nutrition": "Herbivore"},
    {"name": "Bengal Tiger", "family": "Felidae", "average_size": "220 kg", "geography": "Asia", "nutrition": "Carnivore"},
    {"name": "Kangaroo", "family": "Macropodidae", "average_size": "85 kg", "geography": "Australia", "nutrition": "Herbivore"},
    # du kannst hier beliebig mehr einfügen
]

# --- Spielstart ---
index = get_valid_number("🎲 Choose a number between 1 and 5 to get a mystery animal: ", 1, len(animals))
selected_animal = animals[index - 1]
print(f"🎉 You got: {selected_animal['name']}!")

time.sleep(1)
print("\nWhat do you want to guess about this animal?")
print("1️⃣ Average Size")
print("2️⃣ Habitat Geography")
print("3️⃣ Nutrition Type")
guess_choice = get_valid_number("👉 Enter 1, 2 or 3: ", 1, 3)

# --- Abfrage ---
if guess_choice == 1:
    user_guess = input(f"💭 Guess the average size of a {selected_animal['name']} (e.g. '100 kg'): ").lower()
    if user_guess == selected_animal['average_size'].lower():
        print("✅ Correct! You're a size expert!")
    else:
        print(f"❌ Nope! The correct size is {selected_animal['average_size']}.")

elif guess_choice == 2:
    user_guess = input(f"🌍 Guess where the {selected_animal['name']} lives: ").title()
    if user_guess == selected_animal['geography']:
        print("✅ Correct geography!")
    else:
        print(f"❌ Actually, it lives in {selected_animal['geography']}.")

elif guess_choice == 3:
    user_guess = input(f"🍽️ Is the {selected_animal['name']} a Herbivore, Carnivore, or Omnivore? ").capitalize()
    if user_guess == selected_animal['nutrition']:
        print("✅ You're right!")
    else:
        print(f"❌ Nope, it's a {selected_animal['nutrition']}.")

# --- Zusatzfragen zur Punktzahlabsicherung ---
time.sleep(1)
print("\n🔁 Let's answer a few more to test your knowledge!\n")

# Frage 2
q2 = input("🦷 Does a carnivore eat plants? (yes/no): ").strip().lower()
if q2 == "no":
    print("✅ Correct!")
else:
    print("❌ Wrong, carnivores eat meat.")

# Frage 3
q3 = input("🌱 Is a panda a herbivore? (yes/no): ").strip().lower()
if q3 == "yes":
    print("✅ Yep, it loves bamboo!")
else:
    print("❌ Actually, it's a herbivore.")

# Frage 4 (verschachtelt)
q4 = input("🏝️ Do you think all big animals live in Africa? (yes/no): ").strip().lower()
if q4 == "yes":
    print("❌ Not really! What about whales?")
else:
    print("✅ Good thinking!")

# Frage 5 mit if-else-nesting
q5 = input("🧊 Can polar bears and penguins meet in nature? (yes/no): ").strip().lower()
if q5 == "yes":
    print("❌ That's a trick! One's in the Arctic, one's in Antarctica.")
else:
    print("✅ Exactly! They live at opposite poles.")

# --- Ende ---
time.sleep(1)
slow_print("\n🎊 Thanks for playing the Animal Guessing Game! 🐾 Come back soon!", 0.04)
