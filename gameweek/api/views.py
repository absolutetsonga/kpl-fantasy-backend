from rest_framework.viewsets import ModelViewSet
from ..models import GameWeek
from .serializers import GameWeekSerializer

class GameWeekViewSet(ModelViewSet):
    queryset = GameWeek.objects.all()
    serializer_class = GameWeekSerializer