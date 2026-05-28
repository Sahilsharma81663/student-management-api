from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows your frontend on port 5500 to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []

class Student(BaseModel):
    student_id: int
    student_name: str
    student_age: int
    course: str
    marks: float  = Field(
        ...,
        ge = 0,
        le =100
    )
    contact: str = Field(
        ...,
        pattern="^[0-9]{10}$"
    )

    city: Optional[str] = None

@app.get("/")
def home():
    return {
        "message": "Welcome to student management API"
    }

@app.post("/students",status_code=201)
def create_student(student: Student):
    for existing_student in students:
        if existing_student["student_id"] == student.student_id:
            raise HTTPException(
                status_code=400,
                detail="Student with this ID is already exists"
            )
    students.append(student.dict())
    return{
        "message": "Student created successfully",
        "data" : student
    }

@app.get("/students")
def get_students():
    return{
        "total_students" : len(students),
        "student" : students
    }

@app.get("/students/{student_id}")
def get_single_student(student_id: int):
    for student in students:
        if student["student_id"] == student_id:
            return {
                "student" : student
            }
    
    raise HTTPException(
        status_code= 404,
        detail= "Student Not Found"
    )


@app.put("/students/{student_id}")
def update_students(
    student_id: int,
    update_student: Student
):
    for student in students:
        if student["student_id"] == student_id:
            student.update(update_student.dict())

            return{
                "message" : "Student details updated ",
                "data" : student
            }
    raise HTTPException(
        status_code=404,
        detail = "Student Not Found"
    )  

@app.delete("/students/{student_id}")
def remove_student(
    student_id: int
):
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            return{
                "message" : "student removed successfully"
            }
    raise HTTPException(
        status_code=404,
        detail= "Student detail not found"
    )


@app.get("/search")
def search_students(
    course:Optional[str] = None,
    city: Optional[str] = None
):
    filtered_students = students

    if course:
        filtered_students = [
            student for student in filtered_students
            if student["course"].lower() == course.lower()
        ]

    if city:
        filtered_students = [
            student for student in filtered_students
            if student["city"].lower() == city.lower()
        ]

    return{
        "results" : filtered_students
    }