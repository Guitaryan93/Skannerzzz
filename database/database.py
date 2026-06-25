import sqlite3
from datetime import datetime


# Name of the SQLite database file.
# If the file does not already exist, SQLite will create it automatically.
DB_NAME = "monster_library.db"


def setup_database():
    """
    Creates the Monster Library database if it does not already exist.

    This function creates a table called 'monsters' which stores every
    unique monster the player has collected.
    """

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monsters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode_value TEXT NOT NULL UNIQUE,
            barcode_type TEXT NOT NULL,
            date_added TEXT NOT NULL,
            name TEXT NOT NULL,
            element TEXT NOT NULL,
            rarity TEXT NOT NULL,
            hp INTEGER NOT NULL,
            attack INTEGER NOT NULL,
            defence INTEGER NOT NULL,
            speed INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def get_monster_by_barcode(barcode_value):
    """
    Searches the database for a monster using its barcode.

    Returns:
        The monster record if found.
        None if the barcode does not exist.
    """

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM monsters
        WHERE barcode_value = ?
    """, (barcode_value,))

    monster = cursor.fetchone()

    connection.close()

    return monster


def save_monster(monster):
    """
    Saves a newly discovered monster to the database.

    Before saving, the barcode is checked to ensure the player
    does not already own this monster.

    Returns:
        True  - Monster successfully added.
        False - Monster already exists in the player's collection.
    """

    existing_monster = get_monster_by_barcode(monster["barcode_value"])

    if existing_monster:
        return False

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO monsters (
            barcode_value,
            barcode_type,
            date_added,
            name,
            element,
            rarity,
            hp,
            attack,
            defence,
            speed
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        monster["barcode_value"],
        monster["barcode_type"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        monster["name"],
        monster["element"],
        monster["rarity"],
        monster["hp"],
        monster["attack"],
        monster["defence"],
        monster["speed"]
    ))

    connection.commit()
    connection.close()

    return True


def get_monsters():
    """
    Retrieves every monster from the player's collection.

    Monsters are returned with the newest scans first.

    Returns:
        A list of all monsters stored in the database.
    """

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            name,
            element,
            rarity,
            hp,
            attack,
            defence,
            speed,
            barcode_value,
            barcode_type,
            date_added
        FROM monsters
        ORDER BY date_added DESC
    """)

    monsters = cursor.fetchall()

    connection.close()

    return monsters