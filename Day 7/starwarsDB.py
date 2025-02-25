import sqlite3

def create_starwars_db():
    # Creating Table
    with sqlite3.connect("starwars.db") as conn:
        c = conn.cursor()
        c.execute("""
                CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                height INTEGER,
                mass TEXT,
                hair_color TEXT
                )
                """)
        conn.commit()

