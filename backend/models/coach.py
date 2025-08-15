class Coach:
    def __init__(self, id, name, phone_num, sport):
        self.id = id
        self.name = name
        self.phone_num = phone_num
        self.sport = sport

    @staticmethod
    def add(db, name, phone_num, sport_id):
        db.execute('INSERT INTO coach(name, phone_num, sport_id) VALUES (?,?,?)', (name, phone_num, sport_id))

    @staticmethod
    def load(db):
        coaches = db.cur.execute("""
                SELECT coach.id, coach.name, coach.phone_num, sport.title
                FROM coach
                INNER JOIN sport ON coach.sport_id = sport.id
        """).fetchall()
        print(coaches)
        return [Coach(coach[0], coach[1], coach[2], coach[3]) for coach in coaches]

    @staticmethod
    def remove(db, coach_id):
        db.remove("coach", "id", coach_id)