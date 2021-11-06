from django.contrib import admin
from django.http import response
import pytest
from rest_framework.test import APIClient
from tests.factories import ClientFactory
# from clients.models import Client as Clt
# from django.test import Client
from conftest import get_tokens_for_user

from django.urls import reverse

from django.contrib.auth import get_user_model
from django import urls

# from rest_framework_simplejwt.tokens import RefreshToken

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return refresh.access_token

# Fixtures :
# sales_user_client
# support_user_client
# management_user_client
# admin_user_client
# sales_user
# management_user
# support_user
# admin_user



@pytest.mark.django_db
def test_sales_user_access_to_clients(sales_user_client):
    clients_url = urls.reverse('clients-list')
    response = sales_user_client.get(clients_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_sales_user_update_client(sales_user, client_factory):
    """
    GIVEN a user and a client associated to the user
    WHEN a user try to update the client
    THEN check is the client is correctly updated
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')
    client = client_factory.create(sales_contact=sales_user)
    response = clt.patch('/clients/1/', {'first_name': 'Roberto'})
    assert response.status_code == 200
    assert b'"first_name":"Roberto"' in response.content


@pytest.mark.django_db
def test_sales_user_update_client_not_associated(sales_user, client_factory):
    """
    GIVEN a user and a client NOT associated to the user
    WHEN a user try to update the client
    THEN check if the user is not able to update the client
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')
    client = client_factory.create()
    print(client)
    response = clt.patch('/clients/2/', {'first_name': 'Roberto'})
    assert response.status_code == 403





# @pytest.mark.django_db
# def test_user_login(sales_user):
#     login_url = urls.reverse('login')
#     c = APIClient()
#     c.force_login(sales_user)
#     response = c.post(login_url, {'email': sales_user.email, 'password': sales_user.password}) #  data={'email': sales_user.email, 'password': sales_user.password}
#     assert response.status_code == 302 # 302 redirection


# @pytest.mark.django_db
# def test_sales_user_permission(sales_user, client_factory):
#     c = Client()
#     c.force_login(sales_user)
#     client = client_factory(sales_contact=sales_user)
#     print(client.sales_contact.role)
#     response = c.put('/clients/1/', {'first_name': 'Roberto'})
#     print(response.content)
#     assert response.status_code == 200



# @pytest.mark.django_db
# def test_admin_user_connect_to_admin_interface(admin_user):
#     c = Client()
#     c.force_login(admin_user)
#     print(admin_user.is_superuser)
#     print(admin_user.is_admin)
#     print(admin_user.password)

#     response = c.get('/admin/')
#     print(response.content)
#     assert response.status_code == 200
#     assert b"Administration de Django" in response.content
#     assert b"Authentification et autorisation" in response.content

