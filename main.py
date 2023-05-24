import uvicorn
from fastapi import FastAPI
from scripts.core.services.services_student import app as student_id
from scripts.constants.app_configurations import *

app_main = FastAPI()


app_main.include_router(student_id)


if __name__ == "__main__":
    uvicorn.run("main:app_main" ,host=SERVICE_HOST ,port=int(SERVICE_PORT),reload=True)