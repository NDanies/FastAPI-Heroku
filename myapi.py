from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name" : "john",
        "age" : 17,
        "year" : "year 12"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
    

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description = "The ID of the student")):
    return students[student_id]
