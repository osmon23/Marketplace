import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'clear_tariffs': {
        'task': 'apps.payments.tasks.clear_tariffs',
        'schedule': crontab(minute='*'),
        'kwargs': {},
    }
}
#     'activate_payment': {
#         'task': 'apps.payments.tasks.activate_payment',
#         'schedule': crontab(hour=0, minute=0),
#         'kwargs': {},
#     },
# }
#
# app.conf.beat_schedule = {
#     'deduct_funds_daily': {
#         'task': 'apps.payments.tasks.deduct_funds_daily',
#         'schedule': crontab(hour=0, minute=0),
#         'kwargs': {},
#     }
# }
