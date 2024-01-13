from rest_framework.serializers import ModelSerializer
from ..models import Squad
from squadplayers.api.serializers import SquadPlayerSerializer

class SquadSerializer(ModelSerializer):
    players = SquadPlayerSerializer(source='squadplayer_set',many=True, required=False)

    class Meta:
        model = Squad
        fields = '__all__'