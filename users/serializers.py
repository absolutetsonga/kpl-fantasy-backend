from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(UserSerializer):
    is_staff = serializers.BooleanField()
    has_draft = serializers.BooleanField()
    team_admin = serializers.IntegerField()

    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = tuple(UserSerializer.Meta.fields) + ('has_draft', 'is_staff', 'team_admin')