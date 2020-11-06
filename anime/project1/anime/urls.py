from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from anime import views

urlpatterns = [
    path('', views.home),
    path('indexx', views.tampil),
    path('tambah/', views.tambah),
    path('<id>/delete/', views.delete),
    path('<id_judul>/edit', views.edit, name='edit'),
    path('<id>/detail/', views.detail),
]
