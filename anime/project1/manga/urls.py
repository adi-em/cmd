from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from manga import views

urlpatterns = [
    path('', views.tampilmanga),
    path('<id>/tambahmanga', views.tambahmanga),
    path('<id>/detailmanga', views.detailmanga),
    path('<id_judul>/editmanga', views.editmanga, name='editmanga'),
    path('<id>/deletemanga', views.deletemanga),
]
