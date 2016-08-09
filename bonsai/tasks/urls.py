from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authtoken_views


router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'decks', views.DeckViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),
    url(r'^token-auth/', authtoken_views.obtain_auth_token),
]
