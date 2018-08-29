from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings
# �������� ��������� Django ��� celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recycleProject.settings')
app = Celery('recycleProject')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)