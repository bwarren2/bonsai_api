from rest_framework import serializers
from .models import (
    Task,
    User,
)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'completed',
            'created_at',
            'befores',
            'afters',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )
