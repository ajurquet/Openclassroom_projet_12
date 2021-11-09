from django.shortcuts import render
from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsSaleEmployeeOrReadOnly


class ClientViewSet(viewsets.ModelViewSet):
    
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsSaleEmployeeOrReadOnly]

    def get_queryset(self):
        return Client.objects.all()

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return [IsAdminUser()]
    #     return [IsSaleEmployeeOrReadOnly()]
