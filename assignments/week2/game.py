import time
import random
import sys

def type_effect(text, delay=0.02, newline=True):
    """Bonus: Schreibmaschinen-Effekt."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def slow_print(text, delay=0.04):
    """Langsamer Druck (wie in deiner Abgabe)."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_valid_number(prompt, min_val, max_val):
    """Fragt eine int-Zahl ab und validiert: (1) Zahl, (2) im Bereich. Wiederholt bei Fehlern."""
    while True:
        try:
            raw = input(prompt)
            num = int(raw.strip())
            if min_val <= num <= max_val:
                return num
            else:
                print(f"⚠️ Bitte eine Zahl zwischen {min_val} und {max_val} eingeben!")
        except ValueError:
            print("⚠️ Das war keine gültige Zahl. Bitte erneut versuchen.")

def ask_choice(prompt, options):
    """Fragt eine Option ab (case-insensitive)."""
    opts = {opt.lower(): opt for opt in options}
    while True:
        ans = input(prompt).strip().lower()
        if ans in opts:
            return opts[ans]
        print(f"⚠️ Ungültig. Erlaubt: {', '.join(options)}")

def pause(t=0.8):
    time.sleep(t)

animals = [
    {"name": "African Elephant", "family": "Elephantidae", "average_size": "3000 kg", "geography": "Africa", "nutrition": "Herbivore", "legs": 4},
    {"name": "Bald Eagle", "family": "Accipitridae", "average_size": "3.5 kg", "geography": "North America", "nutrition": "Carnivore", "legs": 2},
    {"name": "Giant Panda", "family": "Ursidae", "average_size": "100 kg", "geography": "Asia", "nutrition": "Herbivore", "legs": 4},
    {"name": "Bengal Tiger", "family": "Felidae", "average_size": "220 kg", "geography": "Asia", "nutrition": "Carnivore", "legs": 4},
    {"name": "Kangaroo", "family": "Macropodidae", "average_size": "85 kg", "geography": "Australia", "nutrition": "Herbivore", "legs": 2},
]

hints = {
    "African Elephant": {
        "size": "Größtes Landsäugetier.",
        "geo": "Sahara? Nein – eher südlicher.",
        "nutri": "Frisst Blätter, Rinde, Früchte."
    },
    "Bald Eagle": {
        "size": "Nicht schwer, aber mit großer Spannweite.",
        "geo": "Nationalvogel der USA.",
        "nutri": "Fisch steht häufig auf dem Speiseplan."
    },
    "Giant Panda": {
        "size": "Nicht klein – und rundlich.",
        "geo": "Gebirge in China.",
        "nutri": "Bambus, Bambus, Bambus."
    },
    "Bengal Tiger": {
        "size": "Große Katze.",
        "geo": "Indischer Subkontinent.",
        "nutri": "Ein Spitzenprädator."
    },
    "Kangaroo": {
        "size": "Mittelgroß bis groß, kräftige Hinterläufe.",
        "geo": "Kontinent der Beuteltiere.",
        "nutri": "Gräser & Kräuter."
    },
}


def play_once():
    score = 0

    type_effect("🦁 Welcome to the Ultimate Animal Guessing Game! 🌍", 0.02)
    pause(0.6)
    type_effect("Are you ready to test your animal knowledge? 🧠", 0.02)
    pause(0.6)

    print("\nChoose difficulty: easy / normal / hard")
    difficulty = ask_choice("> ", ["easy", "normal", "hard"])
    allow_hints = (difficulty != "hard")
    base_points = 2 if difficulty == "hard" else (1 if difficulty == "normal" else 0)

    index = get_valid_number(f"\n🎲 Choose a number between 1 and {len(animals)} to get a mystery animal: ",
                             1, len(animals))
    selected_animal = animals[index - 1]
    animal_name = selected_animal["name"]
    print(f"🎉 You got: {animal_name}!")
    pause(0.8)

    print("\nWhat do you want to guess about this animal?")
    print("1️⃣ Average Size")
    print("2️⃣ Habitat Geography")
    print("3️⃣ Nutrition Type")
    guess_choice = get_valid_number("👉 Enter 1, 2 or 3: ", 1, 3)

    if allow_hints:
        want_hint = ask_choice("💡 Do you want a hint? (yes/no): ", ["yes", "no"])
        if want_hint.lower() == "yes":
            if animal_name in hints:
                if guess_choice == 1:
                    print("🔎 Hint:", hints[animal_name]["size"]); pause(0.4)
                elif guess_choice == 2:
                    print("🔎 Hint:", hints[animal_name]["geo"]); pause(0.4)
                else:
                    print("🔎 Hint:", hints[animal_name]["nutri"]); pause(0.4)
            else:
                print("🔎 Hint: Trust your instincts!"); pause(0.3)
    else:
        print("🚫 Hints are disabled on hard difficulty.")
        pause(0.4)

    if guess_choice == 1:
        user_guess = input(f"💭 Guess the average size of a {animal_name} (e.g. '100 kg'): ").strip().lower()
        if user_guess == selected_animal['average_size'].lower():  # (2)
            print("✅ Correct! You're a size expert!")
            score += 2 + base_points
        else:
            print(f"❌ Nope! The correct size is {selected_animal['average_size']}.")
    elif guess_choice == 2:
        user_guess = input(f"🌍 Guess where the {animal_name} lives: ").strip().title()
        if user_guess == selected_animal['geography']:  # (3)
            print("✅ Correct geography!")
            score += 2 + base_points
        else:
            print(f"❌ Actually, it lives in {selected_animal['geography']}.")
    else:
        user_guess = input(f"🍽️ Is the {animal_name} a Herbivore, Carnivore, or Omnivore? ").strip().capitalize()
        if user_guess == selected_animal['nutrition']:  # (4)
            print("✅ You're right!")
            score += 2 + base_points
        else:
            print(f"❌ Nope, it's a {selected_animal['nutrition']}.")

    pause(0.8)
    print("\n🔁 Quick knowledge round!\n"); pause(0.4)

    q2 = input("🦷 Does a carnivore eat plants? (yes/no): ").strip().lower()
    if q2 == "no":
        print("✅ Correct!"); score += 1
    else:
        print("❌ Wrong, carnivores eat meat.")

    q3 = input("🌱 Is a panda a herbivore? (yes/no): ").strip().lower()
    if q3 == "yes":
        print("✅ Yep, it loves bamboo!"); score += 1
    else:
        print("❌ Actually, it's a herbivore.")

    q4 = input("🏝️ Do you think all big animals live in Africa? (yes/no): ").strip().lower()
    if q4 == "yes":
        print("❌ Not really! What about whales?")
    else:
        print("✅ Good thinking!"); score += 1

    q5 = input("🧊 Can polar bears and penguins meet in nature? (yes/no): ").strip().lower()
    if q5 == "yes":
        print("❌ That's a trick! One's in the Arctic, one's in Antarctica.")
    else:
        print("✅ Exactly! They live at opposite poles."); score += 1

    pause(0.6)

    print("\n🦵 Bonus round: How many legs does your animal have?")
    legs = get_valid_number("👉 Enter a number between 0 and 8: ", 0, 8)
    if legs == selected_animal["legs"]:
        print("✅ Correct!"); score += 2
    else:
        diff = abs(legs - selected_animal["legs"])
        if diff == 1:
            print(f"😬 Close! It actually has {selected_animal['legs']}.")
        else:
            print(f"❌ Nope. It has {selected_animal['legs']} legs.")

    pause(0.8)

    print("\n🎯 Final score:", score)
    if score >= 7 + base_points:
        slow_print("🌟 You are an Animal Master! The savannah applauds you! 🐘🦅🐼", 0.02)
        outcome = "win"
    elif score >= 5:
        slow_print("✨ Solid knowledge! With a bit more practice you'll be unstoppable.", 0.02)
        outcome = "ok"
    else:
        slow_print("💀 Not your day… The jungle remains a mystery.", 0.02)
        outcome = "lose"


    if difficulty == "hard" and outcome == "ok":
        print("🏆 Hard-mode bonus: Your 'OK' becomes a secret victory!")
        outcome = "win"

    pause(0.6)
    return outcome

def main():
    while True:
        result = play_once()
        again = ask_choice("\n🔁 Play again? (yes/no): ", ["yes", "no"])
        if again.lower() == "no":
            type_effect("🖐️ Thanks for playing! Bye!", 0.02)
            break
        print()

if __name__ == "__main__":
    main()

