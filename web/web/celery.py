# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

redis_url = "redis://@redis:6379/0"
redis_url_1 = "redis://@redis:6379/1"

app = Celery("web", broker=redis_url, result_backend=redis_url_1)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()