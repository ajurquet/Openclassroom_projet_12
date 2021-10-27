from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from users.models import User
from clients.models import Client
from contracts.models import Contract


class Event(models.Model):
    name = models.CharField(max_length=100)
    contract = models.ForeignKey(Contract,
                                  on_delete=CASCADE,
                                  related_name="event_linked_to",
                                  null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(User,
                                        on_delete=RESTRICT,
                                        related_name="event_assigned_to")

    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=500)
    ended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - Date : {self.event_date}"



 