from rest_framework.viewsets import ModelViewSet

from ..models import Squad
from .serializers import SquadSerializer

class SquadViewSet(ModelViewSet):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer