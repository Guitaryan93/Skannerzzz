# Import the barcode scanner function
from scanner.scanner import scan_barcode

# Import the function that creates a monster from a barcode
from game.monster_generator import generate_monster

# Import the database functions used to create, save and retrieve monsters
from database.database import setup_database, save_monster, get_monsters


# Ensure the monster database exists before the game starts
setup_database()

# Open the camera and wait for the user to scan a barcode
result = scan_barcode()

# Continue only if a barcode was successfully scanned
if result:

    # Generate a monster based on the barcode value and barcode type.
    # The same barcode will always generate the same monster.
    monster = generate_monster(result["value"], result["type"])

    # Attempt to save the monster to the player's collection.
    # The function returns True if it is a new monster,
    # or False if the barcode already exists in the database.
    was_saved = save_monster(monster)

    # Inform the player whether they have discovered
    # a new monster or already own this one.
    if was_saved:
        print("\nNew Monster Added!")
        print("------------------")
    else:
        print("\nYou already have this monster!")
        print("------------------------------")

    # Display the monster's details.
    print("Name:", monster["name"])
    print("Element:", monster["element"])
    print("Rarity:", monster["rarity"])
    print("HP:", monster["hp"])
    print("Attack:", monster["attack"])
    print("Defence:", monster["defence"])
    print("Speed:", monster["speed"])
    print("Barcode:", monster["barcode_value"])
    print("Type:", monster["barcode_type"])

# No barcode was detected before the scanner was closed.
else:
    print("No barcode found.")


# Display every monster currently stored in the player's collection.
print("\nYour Monster Library")
print("--------------------")

# Retrieve all saved monsters from the database.
monsters = get_monsters()

# Loop through each monster and display its information.
for monster in monsters:
    print(
        f"{monster[0]} | {monster[1]} | {monster[2]} | "
        f"HP: {monster[3]} | ATK: {monster[4]} | DEF: {monster[5]} | "
        f"SPD: {monster[6]} | Barcode: {monster[7]} | "
        f"Type: {monster[8]} | Added: {monster[9]}"
    )