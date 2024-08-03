from celery import group

from playground.queue import app
from playground.queue.tasks.giraffe import HelloTask as GiraffeHelloTask
from playground.queue.tasks.hippo import HelloTask as HippoHelloTask


if __name__ == '__main__':
    print('Celery app', app)
    # Run worker
    args = ['worker', '--loglevel=INFO']
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
