from django.shortcuts import render
from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsEventFinish, IsSupportEmployeeOrReadOnly, IsSaleEmployeeConnectedToTheEventOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupportEmployeeOrReadOnly, IsSaleEmployeeConnectedToTheEventOrReadOnly, IsEventFinish]


    def get_queryset(self):
        return Event.objects.all()



    # def get_queryset(self):

    #     events = (Event.objects.filter(support_contact=self.request.user) # Affiche les évènements pour l'équipe de support
    #                  | Event.objects.filter(event_connected_to__sales_contact=self.request.user)) # Affiche les évènements pour les equipes de ventes 

    #     return events
                            