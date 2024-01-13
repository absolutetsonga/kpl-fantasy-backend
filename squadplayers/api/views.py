from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from squads.models import Squad
from players.models import Player
from ..models import SquadPlayer

from .serializers import SquadPlayerSerializer

from ..utils.create_handler import squad_player_create_handler
from ..utils.validate_create_handler import squad_player_validate_handler
from ..utils.error_handler import error_handler

from ..utils.limit_handler import (
                                TotalLimitChecker, OnBenchLimitChecker, CaptainLimitChecker, 
                                ViceCaptainLimitChecker, GoalkeepersLimitChecker, DefendersLimitChecker, 
                                MiddlefieldersLimitChecker, StrikersLimitChecker, OneClubPlayersLimitChecker
                                )

class SquadPlayerViewSet(ModelViewSet):
    queryset = SquadPlayer.objects.all()
    serializer_class = SquadPlayerSerializer
    limit_checkers = {
        'total': TotalLimitChecker(),
        'on_bench': OnBenchLimitChecker(),
        'captain': CaptainLimitChecker(),
        'vice_captain': ViceCaptainLimitChecker(),
        'goalkeeper': GoalkeepersLimitChecker(),
        'defender': DefendersLimitChecker(),
        'middlefielder': MiddlefieldersLimitChecker(),
        'striker': StrikersLimitChecker(),
        'one_club': OneClubPlayersLimitChecker(),
    }


    def create(self, request, *args, **kwargs):
        squad_id = int(request.data.get('squad'))
        player_id = int(request.data.get('player'))

        try: 
            squad = Squad.objects.get(id=squad_id)
            player = Player.objects.get(id=player_id)

        except (Squad.DoesNotExist, Player.DoesNotExist):
            return error_handler.not_found_error('squad or player not found')
        
        existing_players = SquadPlayer.objects.filter(squad=squad)
        
        validation_error = squad_player_validate_handler.validate_squad_limits(existing_players, self.limit_checkers, request.data)

        if validation_error:
            return validation_error
        
        return squad_player_create_handler.create_and_respond(squad, player, request.data, self.get_serializer)
    
    def update(self, request, *args, **kwargs):
        squad_player_id = request.data.get('id')
        squad = request.data.get('squad')

        try: 
            squad_player = SquadPlayer.objects.get(id=squad_player_id)
            squad = Squad.objects.get(id=squad)

        except (SquadPlayer.DoesNotExist):
            return error_handler.not_found_error('squad or player not found')
        
        existing_players = SquadPlayer.objects.filter(squad=squad)

        serializer = self.get_serializer(squad_player, data=request.data)

        if request.data.get('is_vice_captain') == True and existing_players.filter(is_vice_captain=True).count() >= 1:
            return error_handler.bad_request_error('vice captain already exists')
        
        if request.data.get('is_captain') == True and existing_players.filter(is_captain=True).count() >= 1:
            return error_handler.bad_request_error('captain already exists')
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            squad_player = self.get_object()

            squad_player.delete()

            return Response({'detail': 'Squad player deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except SquadPlayer.DoesNotExist:
            return error_handler.not_found_error('Squad player not found')