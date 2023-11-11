from uuid import uuid4
from persistence import ThreadReporistory
from fastapi import FastAPI, status, Body
from models import Thread

app = FastAPI()
threads_repo = ThreadReporistory()

@app.get("/threads")
def list_threads() -> list[Thread]:
    return threads_repo.get_all()

@app.post("/threads", status_code=status.HTTP_201_CREATED)
def create_threads(input: Thread = Body(...)):
    threads_repo.add(input)
    return { "status": "Thread Created" }