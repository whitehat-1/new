from asyncio import Task
from typing import List
from fastapi import FastAPI

from database import create_start_app_handler
from models import Student
from schema import TaskCreate, Taskpublic

def get_application():

    # start the application.
    app = FastAPI()

    # Connect to database.
    app.add_event_handler("startup", create_start_app_handler(app))

    return app

app = get_application()


@app.post("create_task/", response_model=Taskpublic)
async def home(data: TaskCreate):
    Task = await Task.create(
        **data.dict(exclude_unset=True)
    )
    return Task

@app.get("/tasks", response_model=List[Taskpublic])
async def home(data: TaskCreate):
    return await Task.all() 