from fastapi import APIRouter
from schemas.models import Student,Email
from scripts.core.handlers.student_handler import get_student, insert_student, update_student, delete_student, pipeline
from scripts.core.handlers.email_handler import send_email
app = APIRouter()


@app.get("/show_details")
def show():
    return get_student()


@app.post("/add")
def add(student: Student):
    return insert_student(student)


@app.put("/update")
def update(roll: int, student: Student):
    return update_student(roll, student)


@app.delete("/delete")
def delete(roll: int):
    return delete_student(roll)


@app.post("/send email")
def fun(email:Email):
    total_value = pipeline()
    return send_email(str(total_value), email)


@app.get("/total_amount_collected")
def fun():
    return pipeline()


