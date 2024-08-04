from celery import group

from playground.queue import app
from playground.queue.tasks.giraffe import HelloTask as GiraffeHelloTask
from playground.queue.tasks.hippo import HelloTask as HippoHelloTask
from playground.queue.tasks.hippo import EatingAlertTask


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
    # Calls EatingAlertTask() every 10 seconds.
    sender.add_periodic_task(10.0, EatingAlertTask.s(), name='eat every 10')


if __name__ == '__main__':
    print('Celery app', app)
    # Run worker
    args = [
        'worker',
        # '--loglevel=INFO',
        '--loglevel=DEBUG',
        '-E',  # monitor events for flower
        '-B',  # celery beat for periodic tasks
    ]
    app.worker_main(argv=args)

    # Run tasks
    lazy_group = group([HippoHelloTask.s(), GiraffeHelloTask.s()])
    promise = lazy_group()
    promise.get()

    if False:
        result1 = HippoHelloTask.delay()
        print(f'Hippo task result: {result1.get()}')

        result2 = GiraffeHelloTask.delay()
        print(f'Giraffe task result: {result2.get()}')
