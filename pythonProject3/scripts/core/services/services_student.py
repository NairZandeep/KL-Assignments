from fastapi import APIRouter
from schemas.models import Student,Email
from scripts.core.handlers.student_handler import get_student, insert_student, update_student, delete_student, pipeline
from scripts.core.handlers.email_handler import send_email
app = APIRouter()


@app.get("/show_details")
def show():
    try:
        return get_student()
    except Exception as e:
        print(e)
        return {"failed"}


@app.post("/add")
def add(student: Student):
    try:
        return insert_student(student)
    except Exception as e:
        print(e)
        return {"failed"}



@app.put("/update")
def update(roll: int, student: Student):
    try:
        return update_student(roll, student)
    except Exception as e:
        print(e)
        return {"failed"}


@app.delete("/delete")
def delete(roll: int):
    try:
        return delete_student(roll)
    except Exception as e:
        print(e)
        return {"failed"}


@app.post("/send email")
def fun(email:Email):
    try:
        total_value = pipeline()
        return send_email(str(total_value), email)
    except Exception as e:
        print(e)
        return {"failed"}


@app.get("/total_amount_collected")
def fun():
    try:

        return pipeline()
    except Exception as e:
        print(e)
        return {"failed"}


