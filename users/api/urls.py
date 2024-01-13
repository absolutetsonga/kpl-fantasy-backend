from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

custom_user_router = DefaultRouter()
custom_user_router.register(r'custom_users', CustomUserViewSet)