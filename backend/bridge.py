import eel

from .models.owner import Owner
db = None

def set_db(db_instance):
    global db
    db = db_instance

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