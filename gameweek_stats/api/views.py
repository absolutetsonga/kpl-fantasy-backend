from rest_framework.viewsets import ModelViewSet
from ..models import GameWeekStats
from .serializers import GameWeekStatsSerializer

class GameWeekStatsViewSet(ModelViewSet):
    queryset = GameWeekStats.objects.all()
    serializer_class = GameWeekStatsSerializer