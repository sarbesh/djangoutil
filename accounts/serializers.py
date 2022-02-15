from django.contrib.auth.models import User, Group
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'is_active', 'is_staff', 'is_superuser']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['subject'] = user.username
        token['email'] = user.email
        roles = []
        if user.is_superuser == 1:
            roles.append('ADMIN')
        if user.is_staff == 1:
            roles.append('STAFF')
        if user.is_active == 1:
            roles.append('USER')
        token['roles'] = roles
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
