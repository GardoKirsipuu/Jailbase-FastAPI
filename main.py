from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Criminals(BaseModel):
    id: int
    name: str
    crime: str
    img_link: Optional[str] = "placeholder-300x300.webp"
    dob: str
    long_desc: str

class UpdateCriminals(BaseModel):
    id: Optional[int] = None
    name: str = None
    crime: Optional[str] = None
    img_link: Optional[str] = "placeholder-300x300.webp"
    dob: Optional[str] = None
    long_desc: Optional[str] = None

criminals = { "id": 1, "name": "Vin Diesel", "crime": "Speeding", "img_link": "vin-diesel.jpg", "dob": "1976-01-12", "long_desc": "Wanted for speeding" }, { "id": 2, "name": "Henry", "crime": "Hate crimes", "img_link": "henry.jpg", "dob": "2004-02-18", "long_desc": "Has commited multiple hate crimes" }, { "id": 3, "name": "Jason Vorhees", "crime": "Murder", "img_link": "jason-vorhees.jpg", "dob": "1956-06-24", "long_desc": "Wanted for multiple murders. His prime spot is a camping site" }


@app.get("/criminals")
def home():
    print()
    return criminals

@app.get("/criminals/{criminal_id}")
def getCriminalById(criminal_id: int):
    return criminals[criminal_id]

@app.post("/criminals")
def addCriminal(criminal: Criminals):
    crim_id = len(criminals) + 1
    criminals[crim_id] = {"id": crim_id, "name": criminal.name, "crime": criminal.crime, "img_link": criminal.img_link, "dob": criminal.dob, "long_desc": criminal.long_desc}
    return criminals[crim_id]

@app.patch("/criminals/{criminal_id}")
def editCriminal(criminal_id: int, criminal: UpdateCriminals):
    criminals[criminal_id - 1].update({"id": criminal_id, "name": criminal.name, "crime": criminal.crime, "img_link": criminal.img_link, "dob": criminal.dob, "long_desc": criminal.long_desc})
    return criminals[criminal_id]

@app.delete("/criminals/{criminal_id}")
def deleteCriminal(criminal_id: int):
    print(criminals[1])
    #if criminal_id not in criminals.items("id"):
    #    return {"error": "ID does not exists"}

    #del criminals[criminal_id]
    #i = 1
    #for x in criminals.items():
    #    i = i + 1
    #    print(criminals[i])