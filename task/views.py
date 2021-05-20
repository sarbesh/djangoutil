from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializer, UserTaskSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner

import logging

# Create your views here.

logger = logging.getLogger(__name__)


class TaskList(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    logger.debug("#TaskList query:{}".format(queryset))
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Task.objects.all()
    logger.debug("#TaskDetails query:{}".format(queryset))
    serializer_class = TaskSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    logger.debug("#UserList query:{}".format(queryset))
    serializer_class = UserTaskSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    logger.debug("#UserDetail query:{}".format(queryset))
    serializer_class = UserTaskSerializer
