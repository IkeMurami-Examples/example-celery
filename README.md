# Celery Playground

Оформил в виде пакета, не программы, поэтому сначала надо установить локальный пакет:

```
python -m pip install .
```

В качестве celery broker и celery backend использую redis, поднимем его:

```
docker run -d -p 6379:6379 redis
```

Потом запускаем код. Он сам настроит celery приложения (прокину в него в виде конфигов настройки), запустит celery worker и таски:

```
python example/main.py
```

Чтобы удалить пакет:

```
python -m pip uninstall celery-playground
```

## Monitoring

Чтобы удобно было мониторить celery таски, можно включить отслеживание событий (ключ `-E` при запуске worker'а или на уровне конфига celery приложения проставить `worker_send_task_events = True`).

Смотреть это удобно, например, через [flower](https://flower.readthedocs.io/en/latest/install.html#installation). Вот так можно запустить flower, потом запускаем наше приложение:

```
python -m celery -A example.main.app flower
python example/main.py
```

В браузере открываем https://localhost:5555/, на странице `tasks` видим наши таски и результат их выполнения 
