inventory = []
MAX_INVENTORY = 5

rooms = {
    "Beach": [
        {"name": "Coconut", "type": "food", "uses": 1},
        {"name": "Raft Kit", "type": "tool"}
    ],
    "Jungle": [
        {"name": "Medicine", "type": "healing", "uses": 1},
        {"name": "Torch", "type": "tool"}
    ],
    "Cave": [
        {"name": "Map", "type": "tool"},
        {"name": "Apple", "type": "food", "uses": 1}
    ]
}

current_room = "Beach"

def show_room_items():
    print(f"\nYou are in the {current_room}. You see:")
    for item in rooms[current_room]:
        print(f"- {item['name']}")

def show_inventory():
    print("\nYour inventory contains:")
    for item in inventory:
        print(f"- {item['name']}")

def find_item_by_name(item_list, name):
    for item in item_list:
        if item["name"].lower() == name.lower():
            return item
    return None

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY:
        print("Your inventory is full!")
        return
    item = find_item_by_name(rooms[current_room], item_name)
    if item:
        inventory.append(item)
        rooms[current_room].remove(item)
        print(f"You picked up the {item['name']}.")
    else:
        print("That item isn't here.")

def drop(item_name):
    item = find_item_by_name(inventory, item_name)
    if item:
        inventory.remove(item)
        rooms[current_room].append(item)
        print(f"You dropped the {item['name']}.")
    else:
        print("You don't have that item.")

def use(item_name):
    item = find_item_by_name(inventory, item_name)
    if item:
        if "uses" in item and item["uses"] > 0:
            item["uses"] -= 1
            print(f"You used the {item['name']}. Remaining uses: {item['uses']}")
            if item["uses"] == 0:
                inventory.remove(item)
                print(f"The {item['name']} is used up.")
        else:
            print(f"The {item['name']} can't be used or has no effect.")
    else:
        print("You don't have that item.")

def examine(item_name):
    item = find_item_by_name(inventory, item_name)
    if item:
        print(f"{item['name']} - Type: {item['type']}, Uses: {item.get('uses', 'N/A')}")
    else:
        print("You don't have that item.")

def help_menu():
    print("""
Available commands:
- inventory
- pickup <item>
- drop <item>
- use <item>
- examine <item>
- move <room>
- help
- quit
""")

def move(room_name):
    global current_room
    if room_name.capitalize() in rooms:
        current_room = room_name.capitalize()
        print(f"You moved to the {current_room}.")
        show_room_items()
    else:
        print("That room doesn't exist.")

# Main game loop
print("Welcome to Island Escape!")
help_menu()
show_room_items()

while True:
    command = input("\n> ").strip().lower()
    if command == "inventory":
        show_inventory()
    elif command.startswith("pickup "):
        pick_up(command[7:].strip())
    elif command.startswith("drop "):
        drop(command[5:].strip())
    elif command.startswith("use "):
        use(command[4:].strip())
    elif command.startswith("examine "):
        examine(command[8:].strip())
    elif command.startswith("move "):
        move(command[5:].strip())
    elif command == "help":
        help_menu()
    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Unknown command. Type 'help' to see options.")
