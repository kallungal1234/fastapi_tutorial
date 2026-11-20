from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from crud import router as crud_router

app = FastAPI()
app.include_router(crud_router)

@app.get("/")
def read_root():
    return{"message": "helooooooooooooooo"}

@app.get("/greet")
def read_greet(name: str, age: Optional[int] = None):
    return{
        "message": f"Name is {name} lets welcome ang age is {age}"
    }
    
    
class Student(BaseModel):
    name: str
    age: int
    roll: int
    
@app.post("/create")
def create_student(student: Student):
    return{
        "name": student.name,
        "age": student.age,
        "roll": student.roll
    }