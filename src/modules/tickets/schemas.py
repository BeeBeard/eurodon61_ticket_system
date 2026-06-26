from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


Status = Literal["open", "in_progress", "closed"]
Priority = Literal["low", "medium", "high"]


class TicketCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    priority: Priority = "medium"


class TicketUpdateStatus(BaseModel):
    status: Status


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: Status
    priority: Priority
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
