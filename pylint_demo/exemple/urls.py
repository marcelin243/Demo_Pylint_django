# myapp/urls.py

from django.urls import path,include
from rest_framework import routers  # Import tiers
from .views import UserListCreateView  # Import local

router = routers.DefaultRouter()

router.register(r'api/utilisateur', UserListCreateView)

urlpatterns = [
    path('', include(router.urls)),  # Inclure les URLs du routeur
]

