from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='all_tasks'),
    path('<int:pk>', views.TaskDetails.as_view(), name='task_detail'),
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
