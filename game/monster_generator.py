import random


# Available elemental affinities that a monster can have.
ELEMENTS = ["Fire", "Water", "Earth", "Air", "Shadow", "Light"]


# Monster rarity levels.
# These are selected using weighted probabilities later in the generator.
RARITIES = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]


# First half of a monster's randomly generated name.
FIRST_NAMES = [
    "Flame", "Aqua", "Stone", "Storm", "Shadow",
    "Bright", "Iron", "Wild", "Venom", "Frost"
]


# Second half of a monster's randomly generated name.
MONSTER_TYPES = [
    "Goblin", "Dragon", "Wolf", "Slime", "Golem",
    "Serpent", "Beast", "Wraith", "Imp", "Titan"
]


def generate_monster(barcode_value, barcode_type):
    """
    Generates a monster from a barcode.

    The barcode value and barcode type are combined to create a
    deterministic random seed. This means that scanning the same
    barcode will always generate exactly the same monster.

    Parameters:
        barcode_value (str): The scanned barcode number.
        barcode_type (str): The barcode format (EAN13, QR, Code128, etc.)

    Returns:
        dict: A dictionary containing all of the generated monster's data.
    """

    # Create a unique seed from the barcode information.
    seed = barcode_value + barcode_type

    # Create a dedicated random number generator using the seed.
    # This ensures the same barcode always produces the same results.
    rng = random.Random(seed)

    # Select the monster's rarity.
    # Common monsters are much more likely than Legendary monsters.
    rarity = rng.choices(
        RARITIES,
        weights=[60, 25, 10, 4, 1],
        k=1
    )[0]

    # Build the monster's name by combining two random words.
    name = rng.choice(FIRST_NAMES) + " " + rng.choice(MONSTER_TYPES)

    # Randomly assign an elemental affinity.
    element = rng.choice(ELEMENTS)

    # Generate the monster's base combat statistics.
    hp = rng.randint(30, 100)
    attack = rng.randint(5, 30)
    defence = rng.randint(5, 30)
    speed = rng.randint(5, 30)

    # Return the completed monster as a dictionary.
    return {
        "name": name,
        "element": element,
        "rarity": rarity,
        "hp": hp,
        "attack": attack,
        "defence": defence,
        "speed": speed,

        # Store the barcode information so the monster
        # can always be linked back to its source.
        "barcode_value": barcode_value,
        "barcode_type": barcode_type
    }