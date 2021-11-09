from datetime import datetime
from django.utils import timezone
import factory
from faker import Faker
fake = Faker('fr_FR')

from clients.models import Client
from django.contrib.auth import get_user_model
from contracts.models import Contract
from events.models import Event


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ("email",)

    email = fake.safe_email()
    password = "pytest"
    first_name = fake.first_name()
    last_name = fake.last_name()
    # role = ""
  

class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client
        # django_get_or_create = ("sales_contact",)

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.company_email()
    phone = fake.phone_number()
    mobile = fake.phone_number()
    company_name = fake.company()
    sales_contact = factory.SubFactory(UserFactory)


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract

    sales_contact = factory.SubFactory(UserFactory)
    client = factory.SubFactory(ClientFactory)
    amount = fake.pricetag()


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    name = fake.company()
    contract = factory.SubFactory(ContractFactory)
    support_contact = factory.SubFactory(UserFactory)
    attendees = fake.random_int(min = 30)
    notes = fake.text()
    event_date = "2022-11-09 15:55:56.741854+00:00"
