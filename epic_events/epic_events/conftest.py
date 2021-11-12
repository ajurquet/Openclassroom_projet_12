import pytest
from pytest_factoryboy import register
from tests.factories import ClientFactory, UserFactory, EventFactory, ContractFactory
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


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
