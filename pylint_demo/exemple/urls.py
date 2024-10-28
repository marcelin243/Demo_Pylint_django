# myapp/urls.py

# from django.urls import path
from rest_framework import routers  # Import tiers
from .views import UserListCreateView  # Import local

router = routers.DefaultRouter()
router.register("users", UserListCreateView)

# urlpatterns = [
#     path('users/', UserListCreateView.as_view(), name='user-list-create'),
# ]
