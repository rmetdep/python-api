from fastapi import FastAPI, Query
from random import randint
import json
import mysql.connector

app = FastAPI()

# declare variables
# list of formula 1 drivers
drivers = ["Max Verstappen", "Lewis Hamilton", "Valtteri Bottas", "Charles Leclerc", "Carlos Sainz", "Lando Norris", "Daniel Ricciardo", "Pierre Gasly", "Esteban Ocon", "Sergio Perez", "Lance Stroll", "Yuki Tsunoda", "Sebastian Vettel", "Fernando Alonso", "Kimi Raikkonen", "Antonio Giovinazzi", "Nicholas Latifi", "Mick Schumacher", "George Russell"]
# list of formula 1 teams
teams = ["Red Bull", "Mercedes", "Ferrari", "McLaren", "AlphaTauri", "Alpine", "Aston Martin", "Alfa Romeo", "Williams"]
# list of formula 1 circuits
circuits = ["Monza", "Silverstone", "Suzuka", "Interlagos", "Imola", "Baku", "Barcelona", "Monaco", "Hockenheim", "Hungaroring", "Spa", "Nurburgring", "Sochi", "Portimao", "Mexico", "Austin", "Sakhir", "Abu Dhabi", "Jeddah", "Sakhir Short", "Jeddah Short"]

# db setup
db = mysql.connector.connect(
  host="sql-service",
  user="apiaccess",
  password="apidev1!"
)
cursor = db.cursor()

# return link to docs if people are lazy and didn't read the docs
@app.get("/")
def read_root():
    return {"docs": "https://github.com/rmetdep/python-api"}

# test
@app.get("/test")
def test():
    file = []
    cursor.execute("SELECT driverName FROM api.driver")
    for x in cursor:
        file.append(x)
    # to string for json

    return {"query": str(file[randint(1, len(file))-1])}

@app.get("/driver") # get a rondom driver back
async def get_driver():
    return {"driver": drivers[randint(1, 19)-1]}

@app.get("/team")   # get a random team back
async def get_team():
    return {"team": teams[randint(1, 9)-1]}

@app.post("/addciruit") # lookup a drivers stats by name
async def add_circuit(circuit: str = Query(...)):
    circuits.append(circuit)
    return {"added": circuit}