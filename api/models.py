import ast
import json
import os

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Email(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default="queued")

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-id"]
