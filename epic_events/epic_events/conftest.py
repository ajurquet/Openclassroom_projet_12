import pytest
from users.models import User
from pytest_factoryboy import register
from tests.factories import ClientFactory, UserFactory


register(ClientFactory)
register(UserFactory)


# @pytest.fixture
# def new_user(db, user_factory):
#     user = user_factory.create()
#     return user

# @pytest.fixture
# def new_client(db, client_factory):
#     client =  client_factory.create()
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


# @pytest.fixture
# def management_user(db, new_user_factory):
#     return new_user_factory("management_test_user@pytest.com", role="MANAGEMENT")

# @pytest.fixture
# def sales_user(db, new_user_factory):
#     return new_user_factory("sales_test_user@pytest.com", role="SALES")

# @pytest.fixture
# def support_user(db, new_user_factory):
#     return new_user_factory("support_test_user@pytest.com", role="SUPPORT")
