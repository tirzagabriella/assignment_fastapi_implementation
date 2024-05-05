from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = {}

class Todo(BaseModel):
    id: str
    task: str
    completed: Optional[bool] = None
    datetime: Optional[str] = None
    userId: str

@app.get("/")
def index():
    return {"message": "Welcome to todolist FastAPI!"}

# Get all todos by user id
@app.get("/todos/all/{user_id}")
def get_todos_by_userid(
    user_id: str = Path(..., description="The ID of the user owning the list.")
):
    todoRes = [todo for todo in todos.values() if todo.userId == user_id]
    if todoRes:
        return todoRes
    else:
        return {"Error": f"Todos with User ID {user_id} doesn't exist."}

# Get todo by task
@app.get("/todos/{task}")
def get_todos_by_task(
    task: str = Path(..., description="The task name.")
):
    todoRes = [todo for todo in todos.values() if todo.task == task]
    if todoRes:
        return todoRes
    else:
        return {"Error": f"Task doesn't exist"}

# Post todos (create new todos object in list)
@app.post("/todos/create")
def create_todos(newTodo: Todo):
    todoRes = [todo for todo in todos.values() if todo.task == newTodo.task]
    if todoRes: 
        return {"Error": "Task exists."}
    newTodo.completed = bool(0)
    todos[newTodo.task] = newTodo
    return todos[newTodo.task]

# Update todos
# @app.put("/todos/put/{todos_id}")
# def update_todos(todos_id: int, task: Todo):
#     if todos_id not in todos:
#         return {"Error": f"ID {todos_id} does not exist."}

#     if task.title != None:
#         todos[todos_id].title = task.title
#     if task.completed != None:  
#         todos[todos_id].completed = task.completed

#     return todos[todos_id]

# Delete todos by id
# @app.delete("/todos/delete/{todos_id}")
# def delete_todos(todos_id: int):
#     if todos_id not in todos:
#         return {"Error": f"ID {todos_id} does not exist."}
#     del todos[todos_id]
#     return {"Message": "Task deleted successfully."}