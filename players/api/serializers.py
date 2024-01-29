from rest_framework.serializers import ModelSerializer
from ..models import Player
from gameweek_stats.api.serializers import GameWeekStatsSerializer

class PlayerSerializer(ModelSerializer):
    gameweek_stats = GameWeekStatsSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Player
        fields = '__all__'
