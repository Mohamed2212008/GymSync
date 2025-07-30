from backend.db.database import Database
from backend.models.coach import Coach
from backend.models.owner import Owner
from backend.models.trainee import Trainee
from backend import bridge
import eel

db = Database('GymSync')

# create the main tables
db.execute("CREATE TABLE IF NOT EXISTS coach(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone_num TEXT, sport TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS trainee(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, gender TEXT, sport TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS owner(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, hashed_password TEXT NOT NULL)")

bridge.set_db(db)

eel.init('gui')
eel.start('signup.html')

db.close_con()