import pytest

from django.urls import reverse

# @pytest.mark.django_db
# def test_create_management_user(user_factory):
#     user = user_factory.create(role='MANAGEMENT')
#     print(user.email)
#     assert True

# @pytest.mark.django_db
# def test_create_management_user1(user_factory):
#     user = user_factory.create(role='SALES')
#     print(user.email)
#     assert True



@pytest.mark.django_db
def test_employee_vente_modification_client(client, user_factory, client_factory):

    sales_user = user_factory.create(role="SALES")
    print(sales_user.email)
    clt = client_factory.create()
    print(clt.email)
    client.login(username=sales_user.email, password=sales_user.password)
    url = reverse("clients")
    response = client.get(url)
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_employee_vente_modification_client01(client):
    
#     def new_sales_user(user_factory):
#         sales_user = user_factory.create(role="SALES")
#         return sales_user
#     def new_clt(client_factory):
#         clt = client_factory.create(sales_contact=new_sales_user)
#         return clt
    
#     print(new_sales_user)
#     # print(clt.email)

#     response = client.get("/clients/")
#     assert response.status_code == 200





# def test_set_check_password(management_user):
#     print(management_user)
#     print(management_user.password)
#     management_user.set_password("new_password")
#     print(management_user.password)
#     assert management_user.check_password("new_password")

# @pytest.mark.django_db
# def test_new_client(client_factory):
    
#     client = client_factory.build() # Permet de créer un objet sans le sauvegarder dans la base de données
#     client = client_factory.create()
    
#     print(client.first_name)
#     print(client.last_name)
#     print(client.mobile)
#     print(client.company_name)
    
    
#     assert True

# def test_new_client(new_client):
#     print(new_client.email)
#     assert True






# from django.contrib.auth.models import User
# from users.models import User


# @pytest.mark.django_db  # Donne accès à la base de données
# def test_user_create():
#     user = User.objects.create_user(email="test@pytest.com",
#                                     first_name="pytest_prenom",
#                                     last_name="pytest_nom",
#                                     role="MANAGEMENT",
#                                     password="pytest")
#     count = User.objects.all().count()
#     print(count)
#     print(user)
#     assert User.objects.count() == 1









# def test_example1(fixture_1):
#     num = fixture_1
#     assert num == 1



# class User(AbstractBaseUser, PermissionsMixin):
#     ROLE = [
#         ('SALES', 'Sales'),
#         ('SUPPORT', 'Support'),
#         ('MANAGEMENT', 'Management')
#         ]

#     username = None
#     email = models.EmailField(('Email'), unique=True)
#     first_name = models.CharField(max_length=25, blank=False)
#     last_name = models.CharField(max_length=25, blank=False)
#     role = models.CharField(max_length=10, choices=ROLE)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
