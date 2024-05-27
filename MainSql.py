# MainSql.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from typing import List

from database import engine, Base, SessionLocal
from models import ClassSectionYear

app = FastAPI()

# Create the database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency to get the database session
async def get_db():
    async with SessionLocal() as session:
        yield session

class ClassSectionYearCreate(BaseModel):
    py_id: int
    class_name: str
    section: str
    year: int
    count: int

@app.post("/records/", response_model=ClassSectionYearCreate)
async def create_record(record: ClassSectionYearCreate, db: AsyncSession = Depends(get_db)):
    db_record = ClassSectionYear(**record.dict())
    db.add(db_record)
    await db.commit()
    await db.refresh(db_record)
    return db_record

@app.get("/records/", response_model=List[ClassSectionYearCreate])
async def read_records(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ClassSectionYear))
    records = result.scalars().all()
    return records

@app.get("/records/{class_name}/{section}/{year}", response_model=ClassSectionYearCreate)
async def read_record(class_name: str, section: str, year: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ClassSectionYear).filter_by(class_name=class_name, section=section, year=year))
    record = result.scalar_one_or_none()
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

@app.put("/records/{class_name}/{section}/{year}", response_model=ClassSectionYearCreate)
async def update_record(class_name: str, section: str, year: int, updated_record: ClassSectionYearCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ClassSectionYear).filter_by(class_name=class_name, section=section, year=year))
    record = result.scalar_one_or_none()
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    for key, value in updated_record.dict().items():
        setattr(record, key, value)
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record

@app.delete("/records/{class_name}/{section}/{year}", response_model=ClassSectionYearCreate)
async def delete_record(class_name: str, section: str, year: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ClassSectionYear).filter_by(class_name=class_name, section=section, year=year))
    record = result.scalar_one_or_none()
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    await db.delete(record)
    await db.commit()
    return record