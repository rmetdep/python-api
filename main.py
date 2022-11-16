from fastapi import FastAPI, Query
from random import randint
import json

app = FastAPI()

# declare variables
# list of formula 1 drivers
drivers = ["Max Verstappen", "Lewis Hamilton", "Valtteri Bottas", "Charles Leclerc", "Carlos Sainz", "Lando Norris", "Daniel Ricciardo", "Pierre Gasly", "Esteban Ocon", "Sergio Perez", "Lance Stroll", "Yuki Tsunoda", "Sebastian Vettel", "Fernando Alonso", "Kimi Raikkonen", "Antonio Giovinazzi", "Nicholas Latifi", "Mick Schumacher", "George Russell"]
# list of formula 1 teams
teams = ["Red Bull", "Mercedes", "Ferrari", "McLaren", "AlphaTauri", "Alpine", "Aston Martin", "Alfa Romeo", "Williams"]
# list of formula 1 circuits
circuits = ["Monza", "Silverstone", "Suzuka", "Interlagos", "Imola", "Baku", "Barcelona", "Monaco", "Hockenheim", "Hungaroring", "Spa", "Nurburgring", "Sochi", "Portimao", "Mexico", "Austin", "Sakhir", "Abu Dhabi", "Jeddah", "Sakhir Short", "Jeddah Short"]

@app.get("/driver") # get a rondom driver back
async def get_driver():
    return {"driver": drivers[randint(1, 19)-1]}

@app.get("/team")   # get a random team back
async def get_team():
    return {"team": teams[randint(1, 9)-1]}

@app.post("/addciruit") # lookup a drivers stats by name
async def add_circuit(circuit: str = Query(...)):
    circuits.append(circuit)
    return {"circuit": circuit[randint(1, 20)-1]}