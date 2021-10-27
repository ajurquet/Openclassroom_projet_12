from django.db import models
from django.db.models.deletion import RESTRICT
from users.models import User
from clients.models import Client
from events.models import Event

                               
class Contract(models.Model):

    sales_contact = models.ForeignKey(User,
                                      on_delete=RESTRICT,
                                      related_name="contract_assigned_to")
    client = models.ForeignKey(Client,
                                  on_delete=RESTRICT,
                                  related_name="contract_assigned_to")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    event = models.ForeignKey(Event,
                                 on_delete=RESTRICT,
                                 related_name="event_connected_to")

    def __str__(self):
        return f"Contract n°:{self.id} - Event : {self.event.name}"