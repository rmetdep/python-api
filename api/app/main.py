from fastapi import FastAPI, Query                  # Import FastAPI and Query
from random import randint                          # for random number generation
import json                                         # to read and create json
import mysql.connector                              # mysql db connector
from pydantic import BaseModel                      # base model for data validation
from fastapi.middleware.cors import CORSMiddleware  # CORS

# post class
class Circuit(BaseModel):
    name: str

# init app
app = FastAPI()

# CORS allow all origins
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# test function - deprecated
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
        if x.circuitName == circuit.name:
            return {"response": "circuit already exists"}
    cursor.execute("INSERT INTO api.circuits (circuitName) VALUES ('" + circuit.name + "')")
    db.commit()
    return {"response": circuit.name + " added"}