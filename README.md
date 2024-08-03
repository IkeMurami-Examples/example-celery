# Celery Playground

Оформил в виде пакета, не программы, поэтому сначала надо установить локальный пакет:

```
python -m pip install .
```

Потом запускаем код (он сам запустит celery worker и таски):

```
python example/main.py
```

Чтобы удалить пакет:

```
python -m pip uninstall celery-playground
```