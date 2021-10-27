from django.shortcuts import render
from rest_framework import viewsets

from .models import Contract
from .serializers import ContractSerializer
from rest_framework.permissions import IsAuthenticated


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contract.objects.all()