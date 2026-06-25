from scanner.scanner import scan_barcode
from game.monster_generator import generate_monster
from database.database import setup_database, save_monster, get_monsters


setup_database()

result = scan_barcode()

if result:
    monster = generate_monster(result["value"], result["type"])
    was_saved = save_monster(monster)

    if was_saved:
        print("\nNew Monster Added!")
        print("------------------")
    else:
        print("\nYou already have this monster!")
        print("------------------------------")

    print("Name:", monster["name"])
    print("Element:", monster["element"])
    print("Rarity:", monster["rarity"])
    print("HP:", monster["hp"])
    print("Attack:", monster["attack"])
    print("Defence:", monster["defence"])
    print("Speed:", monster["speed"])
    print("Barcode:", monster["barcode_value"])
    print("Type:", monster["barcode_type"])

else:
    print("No barcode found.")


print("\nYour Monster Library")
print("--------------------")

monsters = get_monsters()

for monster in monsters:
    print(
        f"{monster[0]} | {monster[1]} | {monster[2]} | "
        f"HP: {monster[3]} | ATK: {monster[4]} | DEF: {monster[5]} | "
        f"SPD: {monster[6]} | Barcode: {monster[7]} | Type: {monster[8]} | "
        f"Added: {monster[9]}"
    )