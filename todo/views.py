from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from django.core.exceptions import ObjectDoesNotExist
from todo.serializers import ToDoSerializer
from user.models import User
from .models import ToDo
from user.permissions import IsAdmin, IsUser
from django.contrib.auth import get_user_model


User = get_user_model()


class ToDoViewSet(viewsets.ModelViewSet):
	queryset = ToDo.objects.all()
	serializer_class = ToDoSerializer
	#permission_classes = [permissions.IsAuthenticated, IsAdmin]
	#http_method_names = ['get', 'post', 'options', 'head']


class ListToDoViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = ToDo.objects.all()
	serializer_class = ToDoSerializer

