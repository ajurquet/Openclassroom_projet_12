from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from clients.models import Client


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ["id",
                  "first_name",
                  "last_name",
                  "email",
                  "phone",
                  "mobile",
                  "company_name",
                  "date_created",
                  "date_updated",
                  "sales_contact",
                  "already_known"
                  ]
