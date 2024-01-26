from rest_framework.routers import DefaultRouter
from .views import GameWeekViewSet

gameweek_router = DefaultRouter()
gameweek_router.register(r'gameweek', GameWeekViewSet)