from django.contrib import admin
from django.http import response
from django.utils import timezone
import pytest
from rest_framework.test import APIClient
from conftest import get_tokens_for_user, management_user_client
from users.models import User

from django.urls import reverse

from django.contrib.auth import get_user_model
from django import urls


############################
# Tests for sales team
############################


@pytest.mark.django_db
def test_sales_user_update_client(sales_user, client_factory):
    """
    GIVEN a sales user and a client associated to it
    WHEN the user try to update the client
    THEN check is the client is correctly updated
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    client_factory.create(sales_contact=sales_user)
    response = clt.patch('/clients/1/', {'first_name': 'Roberto'})
    assert response.status_code == 200
    assert b'"first_name":"Roberto"' in response.content


@pytest.mark.django_db
def test_sales_user_cant_update_client_not_associated(sales_user, client_factory): 
    """
    GIVEN a sales user and a client NOT associated to it
    WHEN the user try to update the client
    THEN check if the user is not able to update the client
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    sales_user_not_associated = User.objects.create(email="test@test.com",
                                                    first_name="Test",
                                                    last_name="Test",
                                                    role="SALES")
    client_factory.create(sales_contact=sales_user_not_associated)

    response = clt.patch('/clients/2/', {'first_name': 'Roberto'})
    assert response.status_code == 403


@pytest.mark.django_db
def test_sales_user_update_event_associated(sales_user, event_factory, client_factory, contract_factory):
    """
    GIVEN a sales user and an event associated to it 
    WHEN the user try to update the event
    THEN check if the user is able to update the event
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    client = client_factory.create(sales_contact=sales_user)
    contract = contract_factory.create(client=client)
    event_factory.create(contract=contract)

    response = clt.patch('/events/1/', {'name': 'Test_name'})
    assert response.status_code == 200
    assert b'"name":"Test_name"' in response.content


@pytest.mark.django_db
def test_sales_user_cant_update_event_not_associate(sales_user, event_factory, client_factory, contract_factory):
    """
    GIVEN a sales user and an event NOT associated to it 
    WHEN the user try to update the event
    THEN check if the user is not able to update the event
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    sales_user_not_associated = User.objects.create(email="test01@test.com",
                                                    first_name="Test",
                                                    last_name="Test",
                                                    role="SALES")

    client = client_factory.create(sales_contact=sales_user_not_associated)
    contract = contract_factory.create(client=client)
    event_factory.create(contract=contract)

    response = clt.patch('/events/2/', {'name': 'Test_name'})
    assert response.status_code == 403


@pytest.mark.django_db
def test_sales_user_update_contract_associated(sales_user, client_factory, contract_factory):
    """
    GIVEN a sales user and a contract associated to it 
    WHEN the user try to update the contract
    THEN check if the user is able to update the contract
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    client = client_factory.create(sales_contact=sales_user)
    contract = contract_factory.create(client=client)

    response = clt.patch('/contracts/3/', {'amount': 'Test_amount'})
    assert response.status_code == 200
    assert b'"amount":"Test_amount"' in response.content


@pytest.mark.django_db
def test_sales_user_cant_update_contract_not_associated(sales_user, client_factory, contract_factory):
    """
    GIVEN a sales user and a contract NOT associated to it 
    WHEN the user try to update the contract
    THEN check if the user is not able to update the contract
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    sales_user_not_associated = User.objects.create(email="test02@test.com",
                                                    first_name="Test",
                                                    last_name="Test",
                                                    role="SALES")

    client = client_factory.create(sales_contact=sales_user_not_associated)
    contract = contract_factory.create(client=client)
    response = clt.patch('/contracts/4/', {'amount': 'Test_amount'})
    assert response.status_code == 403


@pytest.mark.django_db
def test_sales_user_cant_create_client(sales_user, client_factory):
    """
    GIVEN a sales user 
    WHEN the user try to create a new client
    THEN check if the user is not able create it
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    client = client_factory.build()

    response = clt.post('/clients/', {'first_name': client.first_name,
                                       'last_name': client.last_name,
                                       'email' : client.email,
                                       'phone': client.phone,
                                       'mobile ': client.mobile,
                                       'company_name': client.company_name,
                                       'already_known': client.already_known
                                       })
    assert response.status_code == 201


@pytest.mark.django_db
def sales_user_can_create_event(sales_user, event_factory):
    """
    GIVEN a sales user 
    WHEN the user try to create a new event
    THEN check if the user is  able create it
    """

    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    event = event_factory.build()

    response = clt.post('/events/', {'name': event.name,
                          'attendees': event.attendees,
                          'notes': event.notes})
    assert response.status_code == 201


@pytest.mark.django_db
def sales_user_can_create_contract(sales_user, contract_factory):
    """
    GIVEN a sales user 
    WHEN the user try to create a new event
    THEN check if the user is  able create it
    """

    clt = APIClient()
    refresh_token = get_tokens_for_user(sales_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    contract = contract_factory.build()

    response = clt.post('/contract/', {'sales_contact': contract.sales_contact,
                          'client': contract.client,
                          'amount': contract.amount,
                          })
    
    assert response.status_code == 201


##############################
# Tests for support team
##############################


@pytest.mark.django_db
def test_support_user_update_event_associated(support_user, event_factory, client_factory, contract_factory):
    """
    GIVEN a support user and an event associated to it
    WHEN the user try to update the event
    THEN check if the user able to update the event
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(support_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    client = client_factory.create()
    contract = contract_factory.create(client=client)
    event_factory.create(contract=contract, support_contact=support_user)
    
    response = clt.patch('/events/3/', {'name': 'Test_name'})
    assert response.status_code == 200
    assert b'"name":"Test_name"' in response.content


@pytest.mark.django_db
def test_support_user_cant_update_event_if_its_passed(support_user, event_factory, client_factory, contract_factory):
    """
    GIVEN a support user and a passed event
    WHEN the user try to update the event
    THEN check if the user is not able to update it
    """
    clt = APIClient()
    refresh_token = get_tokens_for_user(support_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    client = client_factory.create()
    contract = contract_factory.create(client=client)
    event = event_factory.create(contract=contract,
                                 support_contact=support_user,
                                 event_date="2020-11-09 15:55:56.741854+00:00")
    
    response = clt.patch('/events/4/', {'name': 'Test_name'})
    assert response.status_code == 403


##############################
# Tests for management team
##############################


@pytest.mark.django_db
def test_management_user_is_admin(management_user):
    clt = APIClient()
    refresh_token = get_tokens_for_user(management_user)
    clt.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    assert management_user.is_admin == True











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

