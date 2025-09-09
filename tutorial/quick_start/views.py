from django.contrib.auth.models import Group, User
from rest_framework import viewsets, permissions

from .serializers import User_Serializer, Group_Serializer
# Create your views here.


class User_View_Set(viewsets.ModelViewSet):
    """API endpoint that allows user to be viewed or edited"""
    queryset = User.objects.all().order_by("-date-joined")
    serializer_class = User_Serializer
    permission_classes = [permissions.IsAuthenticated] 


class Group_View_Set(viewsets.ModelViewSet):
    """API endpoint that allows user to be viewed or edited"""
    queryset = Group.objects.all().order_by("name")
    serializer_class = Group_Serializer
    permission_classes = [permissions.IsAuthenticated]
