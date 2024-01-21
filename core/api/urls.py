from rest_framework.routers import DefaultRouter

from players.api.urls import player_router
from teams.api.urls import team_router
from squads.api.urls import squad_router
from squadplayers.api.urls import squad_player_router
from gameweek_stats.api.urls import gameweek_stats_router

from django.urls import path, include

router = DefaultRouter()

# router.registry.extend(custom_user_router.registry)
router.registry.extend(player_router.registry)
router.registry.extend(team_router.registry)
router.registry.extend(squad_router.registry)
router.registry.extend(squad_player_router.registry)
router.registry.extend(gameweek_stats_router.registry)

urlpatterns = [
    path('', include(router.urls))
]