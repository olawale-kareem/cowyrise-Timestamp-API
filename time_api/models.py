import uuid
from django.db import models


class TimestampedModel(models.Model):
    stamp_time_now = models.CharField(max_length=255)
    stamp_uuid_now = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "TimestampedModel"
