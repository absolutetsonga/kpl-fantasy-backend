from rest_framework.routers import DefaultRouter
from .views import GameViewSet

game_router = DefaultRouter()
game_router.register(r'game', GameViewSet)