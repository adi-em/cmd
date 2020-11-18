from django.contrib import admin
from django.urls import path
from acounts import views

urlpatterns = [
    path('', views.cregister),
]