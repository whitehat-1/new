from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class Taskpublic(BaseModel):
    task_id: UUID
    property: str
    description: str
    created_at: datetime
    updated_at: datetime


class TaskCreate(BaseModel):
    property: str = Field(..., max_length=399)
    description: str = Field(..., max_length=399)

