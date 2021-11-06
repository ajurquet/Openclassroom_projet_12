from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from users.models import User
from contracts.models import Contract
from django.conf import settings


class Event(models.Model):
    name = models.CharField(max_length=100)
    contract = models.ForeignKey(Contract,
                                  on_delete=CASCADE,
                                  related_name="event_linked_to",
                                  null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=RESTRICT,
                                        related_name="event_assigned_to")

    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=500)
    ended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - Date : {self.event_date}"



 