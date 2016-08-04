from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Task(models.Model):
    title = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(default=now, null=True)
    created_at = models.DateTimeField(default=now)
    befores = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='afters',
        blank=True,
    )
    owner = models.ForeignKey(User)
    details = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.title)
