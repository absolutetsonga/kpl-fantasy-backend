from rest_framework.routers import DefaultRouter
from .views import TeamViewSet

team_router = DefaultRouter()
team_router.register(r'teams', TeamViewSet)