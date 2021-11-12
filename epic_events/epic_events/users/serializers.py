from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'role',
                  'is_active',
                  'is_admin',)

        extra_kwargs = {'password': {'write_only': True}}
