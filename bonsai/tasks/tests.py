from django.test import TestCase
from model_mommy import mommy
from tasks.models import Task


class TestTask(TestCase):

    def setUp(self):
        self.a = mommy.make('tasks.Task', title='a')
        self.b = mommy.make('tasks.Task', title='b', befores=[self.a])
        self.c = mommy.make('tasks.Task', title='c', befores=[self.b])
        self.b_prime = mommy.make(
            'tasks.Task', title='b_prime', afters=[self.c]
        )

    def test_task_descendants(self):
        b = Task.objects.get(title='b')
        assert self.a.afters.all()[0] == b
        assert b.befores.all()[0] == self.a

    def test_subtasks(self):
        tasks = Task.objects.all()
        assert self.a.subtasks_in(tasks) == \
            list(Task.objects.exclude(title='b_prime').order_by('id'))
        self.assertNumQueries(2)
