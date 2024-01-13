from rest_framework.serializers import ModelSerializer
from ..models import Team

from players.api.serializers import PlayerSerializer 

class TeamSerializer(ModelSerializer):
    players = PlayerSerializer(many=True, required=False)

    class Meta:
        model = Team
        fields = '__all__'