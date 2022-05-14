from django.urls import path, include
from rest_framework import routers
from todo import views


router = routers.DefaultRouter()
router.register('todo', views.ToDoViewSet, basename='todoaddbook')
router.register('list-todo', views.ListToDoViewSet, basename='listtodo')


urlpatterns = [
    path('', include(router.urls)),
]
