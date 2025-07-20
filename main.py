from db.database import Database
from models.coach import Coach
from models.owner import Owner
from models.trainee import Trainee

db = Database('GymSync')

# create the main tables
db.execute("CREATE TABLE IF NOT EXISTS coach(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone_num TEXT, sport TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS trainee(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, gender TEXT, sport TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS owner(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, hashed_password TEXT NOT NULL)")

# Owner.sign_up(db, "MohamedHamdy", '123')
# print(Owner.log_in(db, "MohamedHamdy1", "123"))

db.close_con()