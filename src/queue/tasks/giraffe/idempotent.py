from playground.queue import app
from celery_singleton import Singleton
import random


@app.task(base=Singleton, bind=True, acks_late=False, )
def idempotent(self, *args, **kwargs):
    x = random.randint(3, 9999)
    lock = self.generate_lock(self.name, args, kwargs)
    existing_task_id = self.get_existing_task_id(lock)
    # cor_id = self.request.correlation_id
    return f'Time to eat, Giraffe1 (lock: {lock}, extask_id {existing_task_id}, res: {self.AsyncResult(existing_task_id)}, task: {self.name}, {args}, {kwargs}, x: {x}, backend: {self.singleton_backend})!'


@app.task
def not_idempotent():
    return f'Time to eat, Giraffe!'
