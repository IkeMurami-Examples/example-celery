from celery import Celery

from playground.queue.configs import MyConfig, CeleryConfig
from playground.queue.base import DebugTask


class MyCelery(Celery):

    def __init__(self, *args, **kwargs):
        self.Task = DebugTask
        super().__init__(*args, **kwargs)


config = MyConfig()
celery_config = CeleryConfig()
app = MyCelery(
    config.name,
    broker=celery_config.broker_url,
    backend=celery_config.result_backend,
)
app.config_from_object(CeleryConfig)
app.autodiscover_tasks()
