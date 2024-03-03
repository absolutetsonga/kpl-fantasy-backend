from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from utils.error_handler import error_handler

from django.contrib.auth import get_user_model

from ..models import Squad
from .serializers import SquadSerializer

User = get_user_model()

class SquadViewSet(ModelViewSet):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

    @action(detail=False, methods=['get'], url_path='get-by-user')
    def get_by_user(self, request):
        
        id = request.query_params.get('user_id', None)

        if not id:
            return error_handler.bad_request_error('Что-то пошло не так')

        try:
            id = int(id)
        except ValueError:
            return error_handler.bad_request_error('Что-то пошло не так')
        
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return error_handler.not_found_error("Что-то пошло не так")
        except ValueError:
            return error_handler.bad_request_error("Что-то пошло не так")

        draft = Squad.objects.filter(user=user).first()

        if draft:
            serializer = self.get_serializer(draft)
            return Response(serializer.data)
        else:
            return error_handler.not_found_error("Что-то пошло не так")

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')

        if not user_id:
            return error_handler.bad_request_error('Что-то пошло не так')

        try:
            user_id = int(user_id)
        except ValueError:
            return error_handler.bad_request_error('Что-то пошло не так')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return error_handler.not_found_error('Что-то пошло не так')

        if not user.is_active:
            return error_handler.bad_request_error('Что-то пошло не так')

        draft_exists = Squad.objects.filter(user=user).exists()

        if draft_exists:
            return error_handler.bad_request_error('Драфт уже создан для данного игрока')
        
        squad, created = Squad.objects.get_or_create(
            user=user, 
            total_budget=100,
            total_points=0,
            activated_bench_boost=False,
            activated_triple_captain=False,
            activated_free_hit=False,
            left_transfers=3
        )

        if created:
            user.has_draft = True
            user.save(update_fields=['has_draft'])

            serializer = self.get_serializer(squad)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Не удалось создать драфт, попробуйте позже или обратитесь в Службу Поддержки.'}, status=status.HTTP_400_BAD_REQUEST)
