from django.urls import path, include
from user.views import RegisterView, UserViewSet
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
#from rest_framework_simplejwt.views import TokenRefreshView


router = routers.DefaultRouter()
router.register('list-user', UserViewSet, basename='listuser')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
]