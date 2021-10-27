from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.expressions import F
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class User(AbstractUser):
    ROLE = [
        ('SALES', 'Sales'),
        ('SUPPORT', 'Support'),
        ('MANAGEMENT', 'Management')
        ]

    username = None
    email = models.EmailField(_('Email'), unique=True)
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    role = models.CharField(max_length=10, choices=ROLE)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Role : {self.role}"

    def save(self):
        user = super(User, self)
        user.set_password(self.password)
        user.save()
        return user


    class Meta:
        ordering = ("last_name", "first_name")
