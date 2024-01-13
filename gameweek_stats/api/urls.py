from rest_framework.routers import DefaultRouter
from .views import GameWeekStatsViewSet

gameweek_stats_router = DefaultRouter()
gameweek_stats_router.register(r'gameweek_stats', GameWeekStatsViewSet)