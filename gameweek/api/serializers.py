from rest_framework.serializers import ModelSerializer
from ..models import GameWeek

class GameWeekSerializer(ModelSerializer):
    class Meta:
        model = GameWeek
        fields = '__all__'
