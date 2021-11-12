from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Vous devez entrer un email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email,
                                password=password,
                                **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_admin = True

        user.save()

        return user
