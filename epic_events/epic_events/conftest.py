from django.urls.base import reverse
import pytest
from pytest_factoryboy import register
from tests.factories import ClientFactory, UserFactory, EventFactory, ContractFactory
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User


register(ClientFactory)
register(UserFactory)
register(EventFactory)
register(ContractFactory)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return refresh.access_token


@pytest.fixture
def sales_user(db, user_factory):
    user = user_factory.create(role='SALES')
    return user
    # yield user
    # User.objects.get(id=user.id).delete()

@pytest.fixture
def management_user(db, user_factory):
    user = user_factory.create(role='MANAGEMENT')
    return user
    # yield user
    # User.objects.get(id=user.id).delete()

@pytest.fixture
def support_user(db, user_factory):
    user = user_factory.create(role='SUPPORT')
    return user
    # yield user
    # User.objects.get(id=user.id).delete()

@pytest.fixture
def admin_user(db, user_factory):
    user = user_factory.create(is_superuser=True)
    return user
    # yield user
    # User.objects.get(id=user.id).delete()




@pytest.fixture
def sales_user_client(db, user_factory):
    user = user_factory.create(role='SALES')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client

@pytest.fixture
def management_user_client(db, user_factory):
    user = user_factory.create(role='MANAGEMENT')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client

@pytest.fixture
def support_user_client(db, user_factory):
    user = user_factory.create(role='SUPPORT')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client

@pytest.fixture
def admin_user_client(db, user_factory):
    user = user_factory.create(is_superuser=True)
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


# @pytest.fixture
# def client_with_token_access(user):
#     clt = APIClient()
#     refresh = RefreshToken.for_user(user)
#     clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
#     return clt





# @pytest.fixture
# def new_client(db, client_factory):
#     client =  client_factory.create()
#     return client














# @pytest.fixture
# def api_client(db, user):
#     # user = user_factory.create(role='SALES')
#     client = APIClient()
#     refresh = RefreshToken.for_user(user)
#     client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
#     return client






# @pytest.fixture()
# def new_user_factory(db):
#     def create_user(
#         email: str,
#         password: str = "pytest",
#         first_name: str = "pytest_prenom",
#         last_name: str = "pytest_nom",
#         role: str = "",
#         is_staff: str = False,
#         is_active: str = True,
#         is_superuser: str = False,
#         is_admin: str = False,
#     ):
#         user = User.objects.create_user(
#             email=email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             role=role,
#             is_staff=is_staff,
#             is_active=is_active,
#             is_superuser=is_superuser,
#             is_admin=is_admin
#         )
#         return user
#     return create_user

