from random import randrange

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    enable_keyboard_shortcuts = models.BooleanField(default=False)
    show_help = models.BooleanField(default=True)
    show_help_brainstorm = models.BooleanField(default=True)
    show_help_refine = models.BooleanField(default=True)
    show_help_plan = models.BooleanField(default=True)
    show_help_execute = models.BooleanField(default=True)
    show_help_review = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        return super().save(*args, **kwargs)


class Deck(models.Model):
    title = models.CharField(max_length=128)
    owner = models.ForeignKey(User)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class Task(models.Model):
    class Meta:
        ordering = (
            '-created_at',
        )

    title = models.CharField(max_length=128)
    completed_at = models.DateTimeField(null=True)
    approved_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(default=now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    befores = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='afters',
        blank=True,
    )
    owner = models.ForeignKey(User)
    deck = models.ForeignKey(Deck, null=True)
    details = models.TextField(blank=True)

    graph_x = models.FloatField(null=True)
    graph_y = models.FloatField(null=True)

    def __str__(self):
        return '{}'.format(self.title)

    def descendants_in(self, task_set):
        """
        This takes a candidate task set, which is assumed to include this task, and returns a list of any task that appears in the afters of anything after this task, this task and its afters included.  See the test for an example.  We do it this way to minimize number of queries, and allow the calling code to make whatever restrictions it wants (ex only tasks in a particular deck for a particular user.)
        """

        # Why a task set?  So we can use few queries.
        hashmap = {t.id: t.afters.all() for t in task_set}

        # This is effectively a depth-first graph traversal.
        # Use a deque for breadth-first.

        # Any nodes that needs to have their data handled get added here.
        additions = [self]

        # All the nodes in the answer set go here.
        descendants = []

        # While we have any nodes to look at
        while additions:
            # Take one
            task = additions.pop()

            # Add it to the answer set if needed (uniqueness check here)
            if task not in descendants:
                descendants.append(task)

            # Add all the downstream nodes to the look-at list.
            additions.extend(hashmap[task.id])

        return descendants

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
                # We step to make it a bit less squidgy.
                self.graph_x = randrange(0, 400, 30)
                self.graph_y = randrange(0, 250, 30)
        return super().save(*args, **kwargs)
