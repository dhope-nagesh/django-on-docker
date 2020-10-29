from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField


class Webhook(models.Model):
    recorded_time = models.DateTimeField(auto_now_add=True, blank=True, db_column='recorded_time')
    payload = JSONField(default=None, db_column='payload')
