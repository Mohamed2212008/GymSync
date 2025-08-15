def setup_schema(db):
    db.execute("""
        CREATE TABLE IF NOT EXISTS owner(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                hashed_password TEXT NOT NULL
               )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS sport(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               type TEXT
               )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS coach(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               phone_num TEXT,
               sport_id INTEGER,
               FOREIGN KEY (sport_id) REFERENCES sport(id)
               )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS trainee(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               gender BOOLEAN,
               phone_num TEXT,
               sport_id INTEGER,
               coach_id INTEGER,
               FOREIGN KEY (sport_id) REFERENCES sport(id),
               FOREIGN KEY (coach_id) REFERENCES coach(id)
               )
    """)