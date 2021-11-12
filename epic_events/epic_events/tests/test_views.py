import pytest


##############################
# Tests for support team
##############################


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


##############################
# Tests for support team
##############################


@pytest.mark.django_db
def test_support_user_access_to_clients(support_user_client):
    response = support_user_client.get("/clients/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_support_user_access_to_contracts(support_user_client):
    response = support_user_client.get("/contracts/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_support_user_access_to_events(support_user_client):
    response = support_user_client.get("/events/")
    assert response.status_code == 200


##############################
# Tests for management team
##############################


@pytest.mark.django_db
def test_management_user_access_to_clients(management_user_client):
    response = management_user_client.get("/clients/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_management_user_access_to_contracts(management_user_client):
    response = management_user_client.get("/contracts/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_management_user_access_to_events(management_user_client):
    response = management_user_client.get("/events/")
    assert response.status_code == 200
