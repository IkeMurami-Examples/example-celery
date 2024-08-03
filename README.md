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