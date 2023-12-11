from contextlib import asynccontextmanager
from uuid import UUID

from fastapi import FastAPI

from src.db import SimpleDB
from src.models import Record, Records

db = SimpleDB()


@asynccontextmanager
async def lifespan(_: FastAPI):
    db.read_db()
    yield
    db.write_db()


app = FastAPI(lifespan=lifespan)


@app.post("/records", status_code=201)
def save_record(record: Record) -> dict:
    db.save(record)
    return {"message": "success"}


@app.get("/records")
def get_records() -> Records:
    return db.get_records()


@app.get("/records/{record_id}")
def get_record(record_id: UUID) -> Record:
    return db.get_record(record_id)
