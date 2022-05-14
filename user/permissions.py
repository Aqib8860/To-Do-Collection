from . import models, serializers
from user.models import User
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

User = get_user_model()
# Create your views here.


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_admin is True:
            return True
        else:
            return False


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_user is True:
            return True
        else:
            return False