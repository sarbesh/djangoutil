from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Task, STATUS_CHOICES


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'name', 'status', 'report', 'pushNotification', 'owner']


class UserTaskSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']
