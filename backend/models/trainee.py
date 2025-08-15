# comment
class Trainee:
    def __init__(self, id, name, age, gender, phone_num, sport, coach):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender # True = male , False = female
        self.phone_num = phone_num
        self.sport = sport
        self.coach = coach

    @staticmethod
    def add(db, name, age, gender, phone_num, sport_id, coach_id):
        db.execute("INSERT INTO trainee(name, age, gender, phone_num, sport_id, coach_id) VALUES (?,?,?,?,?,?)", (name, age, gender, phone_num, sport_id, coach_id))

    @staticmethod
    def load(db):
        trainees = db.cur.execute("""
                SELECT trainee.id, trainee.name, trainee.age, trainee.gender, trainee.phone_num, sport.title, coach.name
                FROM trainee
                INNER JOIN sport ON trainee.sport_id = sport.id
                INNER JOIN coach ON trainee.coach_id = coach.id
        """).fetchall()
        return [Trainee(trainee[0], trainee[1], trainee[2], trainee[3], trainee[4], trainee[5], trainee[6]) for trainee in trainees]

    @staticmethod
    def remove(db, trainee_id):
        db.remove("trainee", "id", trainee_id)