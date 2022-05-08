from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class Taskpublic(BaseModel):
    task_id: UUID
    Property: str
    description: str
    created_at: datetime
    updated_at: datetime


class TaskCreate(BaseModel):
    Property: str = Field(..., max_length=399)
    description: str = Field(..., max_length=399)

