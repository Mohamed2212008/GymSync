import eel
from .models.owner import Owner

db = None

def set_db(db_instance):
    global db
    db = db_instance

gym = None
def set_gym(gym_instance):
    global gym
    gym = gym_instance

# registraintion handling
@eel.expose
def handle_signup(username, password):
    if Owner.sign_up(db, username, password):
        return {'success': True, 'message': 'Signed Up Successfully'}
    return {'success': False, 'message': "There's account already exists, pleas login"}

@eel.expose
def handle_login(username, password):
    if Owner.log_in(db, username, password):
        return {'success': True, 'message': 'Logined in successfully'}
    return {'success': False, 'message': 'Wrong credentials'}

# sports handling
@eel.expose
def add_sport(sport_title, sport_type):
    gym.add_sport(sport_title, sport_type)

@eel.expose
def load_sports():
    sports = []
    for sport in gym.sports:
        coaches_in_sport = gym.count_coaches_in_sport(sport)
        trainees_in_sport = gym.count_trainees_in_sport(sport)
        sports.append(
            {'sport_name': sport.title,
            'sport_type': sport.type,
            'trainees': trainees_in_sport, 
            'coaches': coaches_in_sport})
    return sports

@eel.expose
def delete_sport(sport):
    gym.remove_sport(sport)


# handling coaches

@eel.expose
def add_coach(name, phone_num, specialty):
    gym.add_coach(name, phone_num, specialty)
    print("I'm here")


@eel.expose
def load_coaches():
    coaches = []
    for coach in gym.coaches:
        coaches.append({'name': coach.name, 'phone_num': coach.phone_num, 'specialty': coach.sport})
    return coaches

@eel.expose
def remove_coach(coach):
    gym.remove_coach(coach)

# trainee handling

@eel.expose
def add_trainee(name, age, gender, phone_num, sport, coach):
    gym.add_trainee(name, age, gender, phone_num, sport, coach)

@eel.expose
def load_trainees():
    trainees = []
    for trainee in gym.trainees:
        gender = "Male" if trainee.gender == True else "Female"
        trainees.append(
            {
                "name": trainee.name,
                "age": trainee.age,
                "gender": gender,
                "phone_num": trainee.phone_num,
                "sport": trainee.sport,
                "coach": trainee.coach
            }
        )
    return trainees

@eel.expose
def remove_trainee(trainee):
    gym.remove_trainee(trainee)
    print("done")