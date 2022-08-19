# from email.headerregistry import Group
# from django.contrib import admin
# from django.contrib.auth.models import Group
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User,Group
from .views import IndexView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
