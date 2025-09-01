from backend.db.database import Database
from backend.setup.schema import setup_schema
from backend.models.gym import Gym
from backend import bridge
import eel

db = Database('GymSync')
setup_schema(db)
bridge.set_db(db)

gym = Gym(db)
bridge.set_gym(gym)

eel.init('gui')
if db.fetchall("owner") != []:
    eel.start('registration/login.html')
else:
    eel.start('registration/signup.html')

db.close_con()