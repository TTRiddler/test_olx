import os
from celery import Celery
 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olx_report.settings')
 
app = Celery('olx_report')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.autodiscover_tasks()