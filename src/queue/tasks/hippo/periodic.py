from datetime import datetime
from playground.queue import app


@app.task(bind=True)
def periodic(self):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    return f'Time to eat ({current_time}), Hippo!'
