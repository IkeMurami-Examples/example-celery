#!/bin/sh

echo 'Hello world'
ls -al
python -m celery -A example.main.app flower &
python example/main.py &
