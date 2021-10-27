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
                  "amount",
                  ]
                               
