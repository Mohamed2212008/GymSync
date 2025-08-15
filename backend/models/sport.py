class Sport:
    def __init__(self, id, title, type):
        self.id = id
        self.title = title
        self.type = type
    
    @staticmethod
    def add(db, title, type):
        db.execute("INSERT INTO sport(title, type) VALUES(?,?)", (title, type))

    @staticmethod
    def load(db):
        sports = db.fetchall("sport")
        return [Sport(sport[0], sport[1], sport[2]) for sport in sports]
    
    @staticmethod
    def remove(db, sport_id):
        db.remove("sport", "id", sport_id)