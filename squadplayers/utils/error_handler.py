from rest_framework.response import Response
from rest_framework import status

class ErrorHandler:
    def bad_request_error(self, message):
        return Response({'detail': message}, status=status.HTTP_400_BAD_REQUEST)

    def not_found_error(self, message):
        return Response({'detail': message}, status=status.HTTP_404_NOT_FOUND)
    
error_handler = ErrorHandler()