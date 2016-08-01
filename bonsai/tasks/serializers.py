from django.db import IntegrityError
from rest_framework import serializers
from .models import (
    Task,
    User,
)


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'completed',
            'created_at',
            'befores',
            'afters',
            'owner',
        )

    def save(self, *args, **kwargs):
        try:
            return super().save(*args, **kwargs)
        except IntegrityError as excp:
            # Sometimes, the Ember frontend causes a race, sending two PUTs in
            # quick succession and making the DB yell at us. Let's silence it.
            msg = excp.args[0]
            reciprocal_relationship_race_error = (
                "duplicate key value violates unique constraint"
            )
            if msg.startswith(reciprocal_relationship_race_error):
                pass
            else:
                raise excp


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )