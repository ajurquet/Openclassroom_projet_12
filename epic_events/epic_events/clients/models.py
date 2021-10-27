from django.db import models
from django.db.models.deletion import RESTRICT
from users.models import User

class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(User,
                                         on_delete=RESTRICT,
                                         related_name="client_assigned_to",
                                         null=True,
                                         blank=True
                                        )
    already_known = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company_name}"

    class Meta:
        ordering = ("last_name", "first_name")

