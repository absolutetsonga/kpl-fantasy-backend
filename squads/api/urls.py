from rest_framework.routers import DefaultRouter
from .views import SquadViewSet

squad_router = DefaultRouter()
squad_router.register(r'squads', SquadViewSet)
