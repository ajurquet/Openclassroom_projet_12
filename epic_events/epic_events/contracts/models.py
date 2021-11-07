from django.db import models
from django.db.models.deletion import RESTRICT
from clients.models import Client
from django.conf import settings

                               
class Contract(models.Model):

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=RESTRICT,
                                      related_name="contract_assigned_to",
                                      blank=True,
                                      null=True)
    client = models.ForeignKey(Client,
                                  on_delete=RESTRICT,
                                  related_name="contract_connected_to")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.CharField(max_length=50)
 
    def __str__(self):
        return f"Contract n°:{self.id} - Client : {self.client.company_name}"