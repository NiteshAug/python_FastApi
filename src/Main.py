from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ClassSectionYearInMemory(BaseModel):
    class_name: str
    section: str
    year: int
    count: int

# In-memory database simulation
database = []

@app.post("/records/", response_model=ClassSectionYearInMemory)
def create_record(record: ClassSectionYearInMemory):
    database.append(record)
    return record

@app.get("/records/", response_model=List[ClassSectionYearInMemory])
def read_records():
    return database

@app.get("/records/{class_name}/{section}/{year}", response_model=ClassSectionYearInMemory)
def read_record(class_name: str, section: str, year: int):
    for record in database:
        if record.class_name == class_name and record.section == section and record.year == year:
            return record
    raise HTTPException(status_code=404, detail="Record not found")

@app.put("/records/{class_name}/{section}/{year}", response_model=ClassSectionYearInMemory)
def update_record(class_name: str, section: str, year: int, updated_record: ClassSectionYearInMemory):
    for i, record in enumerate(database):
        if record.class_name == class_name and record.section == section and record.year == year:
            database[i] = updated_record
            return updated_record
    raise HTTPException(status_code=404, detail="Record not found")

@app.delete("/records/{class_name}/{section}/{year}", response_model=ClassSectionYearInMemory)
def delete_record(class_name: str, section: str, year: int):
    for i, record in enumerate(database):
        if record.class_name == class_name and record.section == section and record.year == year:
            deleted_record = database.pop(i)
            return deleted_record
    raise HTTPException(status_code=404, detail="Record not found")

@app.get("/")
async def root():
    return {"Message": "Hello World"}
