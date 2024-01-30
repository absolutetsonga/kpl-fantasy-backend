from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from ..models import Player
from teams.models import Team

from .serializers import PlayerSerializer
from utils.error_handler import error_handler

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
            players = Player.objects.filter(club=club_name)
            serializer = self.get_serializer(players, many=True)
            
            return Response(serializer.data)
        else:
            return Response({"error": "Club name parameter is missing."}, status=status.HTTP_400_BAD_REQUEST)
        
    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return error_handler.forbidden_error({'detail': 'Permission denied. Only staff members can perform this operation.'},
                            status=status.HTTP_403_FORBIDDEN)

        player_data = request.data.copy()

        serializer = self.get_serializer(data=player_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return error_handler.forbidden_error({'detail': 'Permission denied. Only staff members can perform this operation.'},
                            status=status.HTTP_403_FORBIDDEN)
        
        player_instance = self.get_object()

        serializer = self.get_serializer(player_instance, data=request.data, partial=True)  # Set partial=True to allow partial updates

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return error_handler.forbidden_error({'detail': 'Permission denied. Only staff members can perform this operation.'},
                            status=status.HTTP_403_FORBIDDEN)
        
        player_instance = self.get_object()
        player_instance.delete()

        return Response({'detail': 'Player deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
