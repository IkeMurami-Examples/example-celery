from celery import group
from celery.signals import task_success

from playground.queue import app
from playground.queue.tasks.giraffe import HelloTask as GiraffeHelloTask
from playground.queue.tasks.hippo import HelloTask as HippoHelloTask
from playground.queue.tasks.hippo import EatingAlertTask
from playground.queue.tasks.giraffe import IdempotentTask, NotIdempotentTask
from playground.queue.tasks.hippo import PydanticHelloTask


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
    # Calls EatingAlertTask() every 10 seconds.
    # sender.add_periodic_task(10.0, EatingAlertTask.s(), name='eat every 10')

    # ...
    # sender.add_periodic_task(5.0, IdempotentTask.s(), name='idemp every 5')

    # ...
    # sender.add_periodic_task(5.0, NotIdempotentTask.s(), name='not idemp every 5')
    ...


@task_success.connect
def task_success_handler(sender=None, result=None, **kwargs):
    print(f'Task {sender.name} succeeded with result: {result}')
    # group([HippoHelloTask.s()])().get()


if __name__ == '__main__':
    print('Celery app', app)
    # Run worker
    args = [
        'worker',
        '--loglevel=INFO',
        # '--loglevel=DEBUG',
        '-E',  # monitor events for flower
        '-B',  # celery beat for periodic tasks
    ]
    app.worker_main(argv=args)

    # Run tasks
    lazy_group = group([HippoHelloTask.s(), GiraffeHelloTask.s(), PydanticHelloTask.s()])
    promise = lazy_group()
    promise.get()

    if False:
        result1 = HippoHelloTask.delay()
        print(f'Hippo task result: {result1.get()}')

        result2 = GiraffeHelloTask.delay()
        print(f'Giraffe task result: {result2.get()}')
