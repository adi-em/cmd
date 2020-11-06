from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import tambahuser

urlpatterns = [
    path('', tambahuser, name='tambahuser'),
]
