from pydantic import BaseModel, Field
from playground.queue import app


class Message(BaseModel):
    message: str


@app.task(bind=True)
def pydantic_hello(self):
    return Message(message='Hello, Hippo!').model_dump_json()
