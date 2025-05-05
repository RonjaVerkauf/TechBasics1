import time
import sys

# Constants
MAX_AGE = 120
MIN_AGE = 10
VALID_DOORS = ['left', 'right', 'forward']
TYPING_SPEED = 0.03  # seconds per character

def type_text(text):
    """Simulates typing effect for suspense."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(TYPING_SPEED)
    print()

def get_valid_age():
    """Asks the user for a valid age within range."""
    while True:
        age_input = input("How old are you? ")
        if age_input.isdigit():
            age = int(age_input)
            if MIN_AGE <= age <= MAX_AGE:
                return age
            else:
                print(f"Please enter an age between {MIN_AGE} and {MAX_AGE}.")
        else:
            print("Please enter a valid number.")

def get_choice(prompt, options):
    """Prompts the user to choose from a list of valid options."""
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print(f"Please choose from: {', '.join(options)}")

def intro():
    """Introductory scene of the game."""
    type_text("You wake up in a cold, dark room.")
    time.sleep(1)
    type_text("You have no idea how you got here...")
    time.sleep(1)

def hallway_scene():
    """First branching choice."""
    type_text("You see three doors: one to your LEFT, one to your RIGHT, and one FORWARD.")
    door = get_choice("Which door do you choose? (left/right/forward): ", VALID_DOORS)

    if door == "left":
        return kitchen_scene()
    elif door == "right":
        return library_scene()
    else:
        return trap_scene()

def kitchen_scene():
    """Left door leads to the kitchen."""
    type_text("You step into a strange smelling kitchen.")
    open_fridge = get_choice("Do you open the fridge? (yes/no): ", ["yes", "no"])
    if open_fridge == "yes":
        type_text("Something jumps out and you scream... but it's just a raccoon.")
        time.sleep(1)
        return hallway_scene()
    else:
        type_text("You hear a whisper behind you...")
        return game_over("A ghost attacks you away. You should've checked the fridge.")

def library_scene():
    """Right door leads to the library."""
    type_text("You enter a old, hunted library.")
    read_book = get_choice("Do you read the ancient book on the table? (yes/no): ", ["yes", "no"])
    if read_book == "yes":
        type_text("The book provided magical knowledge which allows you to teleport out! You escaped!")
        return win_game()
    else:
        type_text("The door closes behind you. Only the books could have taught you how to escape this deadly library.")
        return game_over("Curiosity could have saved you.")

def trap_scene():
    """Forward door leads to a trap."""
    type_text("The floor collapses as you step forward!")
    reaction = get_choice("Do you grab the ledge or try to jump? (grab/jump): ", ["grab", "jump"])
    if reaction == "grab":
        type_text("You barely hold on and climb back up.")
        return hallway_scene()
    else:
        return game_over("You fall into the abyss...")

def game_over(reason):
    """Ends the game with failure."""
    type_text(f"GAME OVER: {reason}")
    return False

def win_game():
    """Ends the game with success."""
    type_text("🎉 YOU WIN! You have escaped the haunted house. 🎉")
    return True

def main():
    """Main function to run the game."""
    intro()
    name = input("What's your name, brave soul? ")
    age = get_valid_age()

    if age < 18:
        type_text(f"You're quite young, {name}... Are you sure about this?")
    else:
        type_text(f"Alright {name}, let's begin your escape journey...")

    survived = hallway_scene()
    if not survived:
        type_text("Better luck next time!")

if __name__ == "__main__":
    main()
