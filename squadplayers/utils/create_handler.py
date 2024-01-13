from rest_framework import status
from rest_framework.response import Response

from ..models import SquadPlayer

class SquadPlayerCreateHandler:
    def player_already_in_squad(self, squad_id, player_id):
        return SquadPlayer.objects.filter(squad=squad_id, player=player_id).exists()
    
    def create_and_respond(self, squad, player, data, get_serializer):
        squad_player, created = SquadPlayer.objects.get_or_create(
            squad=squad, player=player, 
            position=data.get('position'), 
            is_captain=data.get('is_captain') == True, 
            is_vice_captain=data.get('is_vice_captain') == True, 
            on_bench=data.get('on_bench') == True
        )
        
        if created:
            serializer = get_serializer(squad_player)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def create_error_response(self, message):
        return Response({'detail': message}, status=status.HTTP_400_BAD_REQUEST)
    
squad_player_create_handler = SquadPlayerCreateHandler()