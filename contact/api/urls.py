from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

contact_router = DefaultRouter()
contact_router.register(r'contact', ContactViewSet)