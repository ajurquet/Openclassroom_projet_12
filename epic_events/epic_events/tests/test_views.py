from django.contrib.auth import get_user_model
from django import urls
import pytest
from rest_framework.test import APIClient
from conftest import get_tokens_for_user



# @pytest.mark.django_db
# @pytest.mark.parametrize('param', [
#     ('clients-list'),
#     ('contracts-list'),
#     ('events-list'),
#     ('login'),   
#     ])

# def test_render_views(param, sales_user):
#     c = Client()
#     c.force_login(sales_user)
#     temp_url = urls.reverse(param)
#     response = c.get(temp_url)
#     assert response.status_code == 200

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
    response = sales_user_client.get("/clients/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_sales_user_access_to_contracts(sales_user_client):
    response = sales_user_client.get("/contracts/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_sales_user_access_to_events(sales_user_client):
    response = sales_user_client.get("/events/")
    assert response.status_code == 200




# @pytest.mark.django_db
# def test_sales_user_access_to_clients(sales_user_client):
#     clients_url = urls.reverse('clients-list')
#     response = sales_user_client.get(clients_url)
#     assert response.status_code == 200

# clt = APIClient()
#     refresh_token = get_tokens_for_user(sales_user)
#     clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')
#     client = client_factory.create(sales_contact=sales_user)
#     response = clt.patch('/clients/1/', {'first_name': 'Roberto'})