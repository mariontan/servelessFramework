from fastapi import FastAPI

from controller import PersonController

app = FastAPI()

app.include_router(PersonController.router)
