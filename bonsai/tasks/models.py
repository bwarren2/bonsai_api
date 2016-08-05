from random import randrange

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        return super().save(args, kwargs)


class Task(models.Model):
    title = models.CharField(max_length=128)
    completed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(default=now)
    befores = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='afters',
        blank=True,
    )
    owner = models.ForeignKey(User)
    details = models.TextField(blank=True)

    graph_x = models.FloatField(null=True)
    graph_y = models.FloatField(null=True)

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        if self.pk is None:
            # If we are creating this for the first time, let's also make sure
            # it has decent graph_x and graph_y values, so that it doesn't sit
            # in a pile overlapping with all the rest of the tasks in the
            # corner.
            if self.graph_x is None and self.graph_y is None:
                # Magic values for the ranges intended to fit the nodes on the
                # initial planning area in the frontend.
                #
                # We step by ten to make it a bit less squidgy.
                self.graph_x = randrange(0, 400, 10)
                self.graph_y = randrange(0, 250, 10)
        return super().save(*args, **kwargs)
