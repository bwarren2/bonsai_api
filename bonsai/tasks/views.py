from rest_framework import (
    viewsets,
    status,
)
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import (
    Task,
    Deck,
    User,
)
from .serializers import (
    TaskSerializer,
    DeckSerializer,
    UserSerializer,
    UserChangePasswordSerializer,
)


class LimitToOwnerMixin:
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(LimitToOwnerMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        parent_id = self.request.query_params.get('parent', None)
        if parent_id:
            parent = Task.objects.get(pk=parent_id)
            deck = parent.deck
            tasks = self.queryset.filter(
                deleted_at=None,
                deck=deck,
            ).select_related().prefetch_related('afters')
            return parent.subtasks_in(tasks)

        else:
            return super().get_queryset()


class DeckViewSet(LimitToOwnerMixin, viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.filter(
            pk=self.request.user.pk,
        )

    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        serializer = UserChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_object()
            data = serializer.validated_data
            password_valid = user.check_password(data['old_password'])
            new_passwords_match = (
                data['new_password1'] == data['new_password2']
            )
            if password_valid and new_passwords_match:
                user.set_password(data['new_password1'])
                user.save()
                return Response(None, status=status.HTTP_204_NO_CONTENT)
            else:
                errors = {
                    'non_field_errors': [
                        'Bad passwords',
                    ],
                }
        else:
            errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
