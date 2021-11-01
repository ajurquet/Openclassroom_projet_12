# from django.contrib.auth import models
import factory
from faker import Faker
fake = Faker('fr_FR')

from clients.models import Client
from users.models import User
from contracts.models import Contract
from events.models import Event


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = fake.safe_email()
    password = "pytest"
    first_name = fake.first_name()
    last_name = fake.last_name()
    role = ""
    is_staff = False
    is_active = True
    is_superuser = True
    is_admin = False


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client
        django_get_or_create = ("sales_contact",)

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

