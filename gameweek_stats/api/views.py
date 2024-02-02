from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from ..models import GameWeekStats
from players.models import Player
from gameweek.models import GameWeek

from .serializers import GameWeekStatsSerializer

from utils.error_handler import error_handler

class GameWeekStatsViewSet(ModelViewSet):
    queryset = GameWeekStats.objects.all()
    serializer_class = GameWeekStatsSerializer

    def calculate_gameweek_points(self, gameweek_stats):
        points = (
            gameweek_stats.goals_scored * 4 +
            gameweek_stats.assists * 3 +
            gameweek_stats.clean_sheets * 4 -
            gameweek_stats.own_goals_scored * 2 -
            gameweek_stats.yellow_cards * 1 -
            gameweek_stats.red_cards * 3
        )

        return points
    
    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return error_handler.forbidden_error('Permission denied. Only staff members can perform this operation.')
        
        player_id = int(request.data.get('player'))
        gameweek_id = int(request.data.get('gameweek'))

        own_goals_scored = int(request.data.get('own_goals_scored'))
        goals_scored = int(request.data.get('goals_scored'))
        clean_sheets = int(request.data.get('clean_sheets'))
        yellow_cards = int(request.data.get('yellow_cards'))
        assists = int(request.data.get('assists'))
        red_cards = int(request.data.get('red_cards'))

        try:
            player = Player.objects.get(id=player_id)
            gameweek = GameWeek.objects.get(id=gameweek_id)

        except Player.DoesNotExist:
            return error_handler.bad_request_error(f'Player with ID {player_id} does not exist.')
        
        gameweek_stats, created = GameWeekStats.objects.get_or_create(
            player=player, 
            gameweek=gameweek, 
            own_goals_scored=own_goals_scored, 
            goals_scored=goals_scored, 
            clean_sheets=clean_sheets,
            yellow_cards=yellow_cards,
            assists=assists,
            red_cards=red_cards
        )

        if created:
            serializer = self.get_serializer(gameweek_stats)
            
            points = self.calculate_gameweek_points(gameweek_stats)

            print(points)
            
            gameweek_stats.points = points
            gameweek_stats.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        serializer = self.get_serializer(gameweek_stats, data=request.data)