from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import  UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViewSet(viewsets.ModelViewSet, TokenObtainPairView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
