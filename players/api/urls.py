from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet

player_router = DefaultRouter()
player_router.register(r'players', PlayerViewSet)