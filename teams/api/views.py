from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models import Team
from .serializers import TeamSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=False, methods=['get'], url_path='get-by-name')
    def get_by_name(self, request):
        team_name = request.query_params.get('name', None)

        if not team_name:
            return Response({"error": "Team name is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        team = get_object_or_404(Team, name=team_name)
        
        serializer = self.get_serializer(team)

        return Response(serializer.data)
        