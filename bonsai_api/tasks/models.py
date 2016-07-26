from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Task(models.Model):
    title = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
