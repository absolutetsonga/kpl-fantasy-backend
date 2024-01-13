from rest_framework.routers import DefaultRouter
from .views import SquadPlayerViewSet

squad_player_router = DefaultRouter()
squad_player_router.register(r'squad_players', SquadPlayerViewSet)