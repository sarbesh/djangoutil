from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializer, UserTaskSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner


# Create your views here.


class TaskList(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserTaskSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserTaskSerializer
