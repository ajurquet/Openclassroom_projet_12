from rest_framework.serializers import ModelSerializer

from .models import Contract


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ["sales_contact",
                  "client",
                  "date_created",
                  "date_updated",
                  "status",
                  "date_created",
                  "date_updated",
                  "amount",
                  "event"
                  ]
                               
    

# class Contract(models.Model):

#     sales_contact = models.ForeignKey(User,
#                                       on_delete=RESTRICT,
#                                       related_name="contract_assigned_to")
#     client = models.ForeignKey(Client,
#                                   on_delete=RESTRICT,
#                                   related_name="contract_assigned_to")
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     status = models.BooleanField(default=False)
#     amount = models.FloatField()
#     event = models.ForeignKey(Event,
#                                  on_delete=RESTRICT,
#                                  related_name="event_connected_to")

#     def __str__(self):
#         return f"Contract n°:{self.id} - Event : {self.event.name}"
