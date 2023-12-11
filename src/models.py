from uuid import UUID

from pydantic import BaseModel


class Record(BaseModel):
    id: UUID
    data: str


class Records(BaseModel):
    records: list[Record]


class IDResponse(BaseModel):
    id: int
