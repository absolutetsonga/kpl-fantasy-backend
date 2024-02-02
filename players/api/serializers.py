from rest_framework.serializers import ModelSerializer
from gameweek_stats.api.serializers import GameWeekStatsSerializer
from ..models import Player

class PlayerSerializer(ModelSerializer):
    gameweek_stats = GameWeekStatsSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Player
        fields = '__all__'
