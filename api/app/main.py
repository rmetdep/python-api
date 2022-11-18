from fastapi import FastAPI, Query
from random import randint
import json
import mysql.connector
from pydantic import BaseModel

class Circuit(BaseModel):
    name: str

app = FastAPI()
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

# test function
@app.get("/test")
def test():
    return {"test": "no tests active"}

@app.get("/driver") # get a rondom driver back
async def get_driver():
    file = []
    cursor.execute("SELECT driverName FROM api.driver")
    for x in cursor:
        file.append(x)
    result = file[randint(1, len(file))-1]
    result = str(result).replace("(", "").replace(")", "").replace(",", "").replace("'", "")
    return {"driver": result}

@app.get("/team")   # get a random team back
async def get_team():
    file = []
    cursor.execute("SELECT teamName FROM api.team")
    for x in cursor:
        file.append(x)
    result = file[randint(1, len(file))-1]
    result = str(result).replace("(", "").replace(")", "").replace(",", "").replace("'", "")
    return {"team": result}

@app.post("/addciruit") # lookup a drivers stats by name
async def add_circuit(circuit: Circuit):
    file = []
    cursor.execute("SELECT circuitName FROM api.circuits")
    for x in cursor:
        if x == circuit.name:
            return {"error": "circuit already exists"}
    cursor.execute("INSERT INTO api.circuit (circuitName) VALUES ('" + circuit.name[0] + "')")
    db.commit()
    return {circuit.name[0]: "added"}