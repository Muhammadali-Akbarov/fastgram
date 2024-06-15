"""
init celery instance
"""
from celery import Celery

from app.bot.settings.internal.conf import SERVICE_NAME
from app.bot.settings.external.celery import CELERY_BROKER_URL
from app.bot.settings.external.celery import CELERY_RESULT_BACKEND


celery_app = Celery(SERVICE_NAME)
celery_app.conf.broker_url = CELERY_BROKER_URL
celery_app.conf.result_backend = CELERY_RESULT_BACKEND
celery_app.conf.broker_connection_retry_on_startup = True

celery_app.conf.task_routes = {
    'app.bot.services.external.celery.tasks.example.example_task': {
        'queue': 'example_queue'
    },
}

# this task works every 60 second
celery_app.conf.beat_schedule = {
    'example_beat': {
        'task': "app.bot.services.external.celery.tasks.example.example_task",
        'schedule': 60,  # sec
        'args': ('Mincecraft', )
    },
}
