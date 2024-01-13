from rest_framework.serializers import ModelSerializer
from gameweek_stats.models import GameWeekStats

class GameWeekStatsSerializer(ModelSerializer):
    class Meta:
        model = GameWeekStats
        fields = '__all__'
