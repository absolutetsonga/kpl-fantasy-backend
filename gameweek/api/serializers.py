from rest_framework.serializers import ModelSerializer
from ..models import GameWeek

from games.api.serializers import GameSerializer

class GameWeekSerializer(ModelSerializer):
    games = GameSerializer(many=True, required=False)

    class Meta:
        model = GameWeek
        fields = '__all__'
