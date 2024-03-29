from django.db import IntegrityError
from rest_framework import serializers
from .models import (
    Task,
    Deck,
    User,
)


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'deleted_at',
            'completed_at',
            'approved_at',
            'created_at',
            'befores',
            'afters',
            'deck',
            'owner',
            'details',
            'graph_x',
            'graph_y',
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


class DeckSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Deck
        fields = (
            'id',
            'title',
            'owner',
            'task_set',
            'deleted_at',
        )
        read_only_fields = (
            'task_set',
        )


class UserChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
    )
    new_password1 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
    )
    new_password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'old_password',
            'new_password1',
            'new_password2',
        )
        read_only_fields = (
            'username',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'enable_keyboard_shortcuts',
            'show_help',
            'show_help_brainstorm',
            'show_help_refine',
            'show_help_plan',
            'show_help_execute',
            'show_help_review',
        )
        read_only_fields = (
            'username',
        )
