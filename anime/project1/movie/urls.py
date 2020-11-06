from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from movie import views

urlpatterns = [
    path('', views.tampilmovie),
    path('<id>/tambahmovie', views.tambahmovie),
    path('<id>/detailmovie', views.detailmovie),
    path('<id_judul>/editmovie', views.editmovie, name='editmovie'),
    path('<id>/deletemovie', views.deletemovie),
]
