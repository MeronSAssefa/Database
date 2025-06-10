## Database tier for the Players' data manager program

# player records, including retrieving, adding, and deleting
# players using SQLite. It connects to the Player table in
# player_db.sqlite and maps records to Player objects.
#
# Name: Meron Assefa
#Date:June 10 2025
#DEV 128

import sqlite3
from contextlib import closing
from player_objects import Player

# Global connection object
conn = None

def connect():
    """Connect to the SQLite database, if not already connected."""
    global conn
    if not conn:
        DB_FILE = "player_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row  # Access columns by name

def close():
    """Close the database connection."""
    if conn:
        conn.close()

def get_players():
    """
    Returns a list of Player objects, ordered by wins (descending).
    This supports the 'viewall' command in the UI.
    """
    connect()
    with closing(conn.cursor()) as cursor:
        cursor.execute("SELECT * FROM Player ORDER BY wins DESC")  # Table name is capitalized
        rows = cursor.fetchall()
        players = [
            Player(row["name"], row["wins"], row["losses"], row["ties"], row["playerID"])
            for row in rows
        ]
    return players

def get_player(name):
    """
    Returns a Player object with the given name.
    Used by the 'view' command in the UI.
    """
    connect()
    with closing(conn.cursor()) as cursor:
        cursor.execute("SELECT * FROM Player WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            return Player(row["name"], row["wins"], row["losses"], row["ties"], row["playerID"])
    return None

def add_player(player):
    """
    Adds a new player to the database using the provided Player object.
    Supports the 'add' command in the UI.
    """
    connect()
    with closing(conn.cursor()) as cursor:
        cursor.execute(
            "INSERT INTO Player (name, wins, losses, ties) VALUES (?, ?, ?, ?)",
            (player.name, player.wins, player.losses, player.ties)
        )
        conn.commit()

def delete_player(name):
    """
    Deletes a player by name from the database.
    Supports the 'del' command in the UI.
    """
    connect()
    with closing(conn.cursor()) as cursor:
        cursor.execute("DELETE FROM Player WHERE name = ?", (name,))
        conn.commit()






