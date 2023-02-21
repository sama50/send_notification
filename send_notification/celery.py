import os
from django.conf import settings
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_notification.settings')

app = Celery('send_notification')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

app.conf.beat_schedule = {
    'get_joke_3s':{
        'task':'app.tasks.send_notification_user',
        'schedule':4.0
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

