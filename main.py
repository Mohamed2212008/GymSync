from backend.db.database import Database
from backend.setup.schema import setup_schema
from backend.models.gym import Gym
from backend import bridge
import eel

db = Database('GymSync')
setup_schema(db)
bridge.set_db(db)

gym = Gym(db)

# eel.init('gui')
# eel.start('signup.html')

db.close_con()