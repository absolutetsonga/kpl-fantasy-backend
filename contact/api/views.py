from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from ..models import Contact
from .serializers import ContactSerializer
from utils.error_handler import error_handler

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user_email = request.data.get('email', None)

        if user_email:
            previous_messages = Contact.objects.filter(email=user_email)

            if previous_messages.filter(is_responded=False).exists():
                return error_handler.bad_request_error({'detail': 'You must wait for a response to your previous messages before sending a new one.'})

        return super().create(request, *args, **kwargs)