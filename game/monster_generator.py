import random


ELEMENTS = ["Fire", "Water", "Earth", "Air", "Shadow", "Light"]

RARITIES = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]

FIRST_NAMES = [
    "Flame", "Aqua", "Stone", "Storm", "Shadow",
    "Bright", "Iron", "Wild", "Venom", "Frost"
]

MONSTER_TYPES = [
    "Goblin", "Dragon", "Wolf", "Slime", "Golem",
    "Serpent", "Beast", "Wraith", "Imp", "Titan"
]


def generate_monster(barcode_value, barcode_type):
    seed = barcode_value + barcode_type

    rng = random.Random(seed)

    rarity = rng.choices(
        RARITIES,
        weights=[60, 25, 10, 4, 1],
        k=1
    )[0]

    name = rng.choice(FIRST_NAMES) + " " + rng.choice(MONSTER_TYPES)
    element = rng.choice(ELEMENTS)

    hp = rng.randint(30, 100)
    attack = rng.randint(5, 30)
    defence = rng.randint(5, 30)
    speed = rng.randint(5, 30)

    return {
        "name": name,
        "element": element,
        "rarity": rarity,
        "hp": hp,
        "attack": attack,
        "defence": defence,
        "speed": speed,
        "barcode_value": barcode_value,
        "barcode_type": barcode_type
    }