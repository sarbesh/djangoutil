from django.urls import path

'''
here the name of my app is updater so I add the import my view from there
replace updater with your app-name where you have your views.py
'''
from . import views

urlpatterns = [
    path("update_server/", views.update, name="update"),
]
