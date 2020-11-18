from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tampil),
    path('tampilmurid/', views.tampilmurid, name='murid'),
    path('tampilguru/', views.tampilguru, name='pengajar'),
    path('detailguru/', views.detailguru, name='gdetail'),
    path('detailmurid/', views.detailmurid, name='mdetail'),

]