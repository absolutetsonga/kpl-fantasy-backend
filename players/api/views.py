from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from ..models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=False, methods=['delete'], url_path='delete-all')
    def delete_all(self, request):
        Player.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    @action(detail=False, methods=['get'], url_path='get-by-club')
    def get_by_club(self, request):
        club_name = request.query_params.get('club', None)

        if club_name is not None:
            players = Player.objects.filter(club=club_name)  # Filter players by the provided club name
            serializer = self.get_serializer(players, many=True)
            
            return Response(serializer.data)
        else:
            return Response({"error": "Club name parameter is missing."}, status=status.HTTP_400_BAD_REQUEST)