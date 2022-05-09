from asyncio import Task
from typing import List
from fastapi import FastAPI ,HTTPException

from database import create_start_app_handler
from models import Task
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
        **data.dict(exclude_unset=True) #convert a pydantic model to a dictionary
    )
    return Task

@app.put('/task_get/{id}', response_model=Taskpublic)
async def update_task(id: str):
    get_task = await Task.get(id=id)
    if not get_task:
        return  HTTPException(status_code=404, detail="User ID Not Found!!")
    get_task.task_completed=True
    await get_task.save()
    return await get_task




@app.get("/tasks", response_model=List[Taskpublic])
async def home(data: TaskCreate):
    return await Task.all() 