from django.shortcuts import render
from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSupportEmployeeOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupportEmployeeOrReadOnly]

    def get_queryset(self):

        events = (Event.objects.filter(support_contact=self.request.user) # Affiche les évènements pour l'équipe de support
                     | Event.objects.filter(event_connected_to__sales_contact=self.request.user)) # Affiche les évènements pour les equipes de ventes 

        return events


# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     client = models.ForeignKey(Client,
#                                   on_delete=RESTRICT,
#                                   related_name="event_assigned_to")
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     support_contact = models.ForeignKey(User,
#                                         on_delete=RESTRICT,
#                                         related_name="event_assigned_to")
#     # event_status = models.ForeignKey(Contract,
#     #                                  on_delete=RESTRICT,
#     #                                  related_name="event_connected_to")
#     attendees = models.IntegerField()
#     event_date = models.DateTimeField()
#     notes = models.TextField(max_length=500)
#     ended = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.name} - Date : {self.event_date}"
                            