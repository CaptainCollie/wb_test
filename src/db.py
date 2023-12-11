import json
import os
from pathlib import Path
from uuid import UUID

from fastapi import HTTPException
from pydantic import BaseModel

from src.models import Record, Records

DB_PATH = os.getenv("DB_PATH", "db/db.json")


class SimpleDB(BaseModel):
    db: dict[UUID, Record] = {}

    def save(self, record: Record):
        if record.id in self.db:
            raise HTTPException(status_code=409, detail="Record already exist")

        self.db[record.id] = record

    def get_record(self, record_id: UUID) -> Record:
        print(self.db)
        if record_id not in self.db:
            raise HTTPException(status_code=404, detail="Record not found")

        return self.db[record_id]

    def get_records(self) -> Records:
        return Records(records=list(self.db.values()))

    def read_db(self):
        path = Path(DB_PATH)
        if path.exists():
            self.db = SimpleDB(**json.loads(path.read_text(encoding="utf-8"))).db

    def write_db(self):
        path = Path(DB_PATH)
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(self.model_dump_json(), encoding="utf-8")
