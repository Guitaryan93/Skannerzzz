import sqlite3
from datetime import datetime


DB_NAME = "monster_library.db"


def setup_database():
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