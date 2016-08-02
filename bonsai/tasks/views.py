from rest_framework import (
    viewsets,
    status,
)
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import (
    Task,
    User,
)
from .serializers import (
    TaskSerializer,
    UserSerializer,
)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(
            owner=self.request.user,
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.filter(
            pk=self.request.user.pk,
        )

    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            user = self.get_object()
            data = serializer.validated_data
            password_valid = user.check_password(data['old_password'])
            new_passwords_match = data['new_password1'] == data['new_password2']
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
