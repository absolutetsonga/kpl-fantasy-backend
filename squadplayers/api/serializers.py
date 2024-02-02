from rest_framework.serializers import ModelSerializer
from ..models import SquadPlayer

class SquadPlayerSerializer(ModelSerializer):
    class Meta:
        model = SquadPlayer
        fields = '__all__'