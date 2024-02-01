from rest_framework.serializers import ModelSerializer
from gameweek_stats.api.serializers import GameWeekStatsSerializer
from ..models import SquadPlayer

class SquadPlayerSerializer(ModelSerializer):
    gameweek_stats = GameWeekStatsSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = SquadPlayer
        fields = '__all__'