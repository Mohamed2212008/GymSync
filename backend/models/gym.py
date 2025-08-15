from .sport import Sport
from .coach import Coach
from .trainee import Trainee


# comment
class Gym:
    def __init__(self, db):
        self.db = db
        self.sports = []
        self.coaches = []
        self.trainees = []

        self.load_sports()
        self.load_coaches()
        self.load_trainees()

    def add_sport(self, title, type):
        Sport.add(self.db, title, type)
        self.load_sports()

    def load_sports(self):
        self.sports = Sport.load(self.db)

    def return_sport_id(self, sport_title):
        for sport in self.sports:
            if sport.title == sport_title:
                return sport.id
        return False

    def remove_sport(self,sport):
        sport_id = self.return_sport_id(sport)
        if sport_id != False:
            Sport.remove(self.db, sport_id)
            self.load_sports()

    def add_coach(self, name, phone_num, specialty):
        sport_id = self.return_sport_id(specialty)
        if sport_id != False:
            Coach.add(self.db, name, phone_num, sport_id)
            self.load_coaches()

    def load_coaches(self):
        self.coaches = Coach.load(self.db)

    def return_coach_id(self, coach_name):
        for coach in self.coaches:
            if coach.name ==  coach_name:
                return coach.id
        return False

    def remove_coach(self, coach_name):
        coach_id = self.return_coach_id(coach_name)
        if coach_id != False:
            Coach.remove(self.db, coach_id)
            self.load_coaches()

    def add_trainee(self, name, age, gender, phone_num, sport, coach):
        sport_id = self.return_sport_id(sport)
        coach_id = self.return_coach_id(coach)
        if sport_id != False and coach_id != False:
            Trainee.add(self.db, name, age, gender, phone_num, sport_id, coach_id)
            self.load_trainees()

    def load_trainees(self):
        self.trainees = Trainee.load(self.db)
    
    def return_trainee_id(self, trainee_name):
        for trainee in self.trainees:
            if trainee.name == trainee_name:
                return trainee.id
        return False

    def remove_trainee(self, trainee_name):
        trainee_id = self.return_trainee_id(trainee_name)
        if trainee_id != False:
            Trainee.remove(self.db, trainee_id)