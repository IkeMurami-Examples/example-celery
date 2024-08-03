from playground.queue import app


@app.task(bind=True)
def hello(self):
    return 'Hello, Giraffe!'
