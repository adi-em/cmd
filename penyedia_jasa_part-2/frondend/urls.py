from django.contrib import admin
from django.urls import path
from frondend import views

urlpatterns = [
    path('', views.home),
    path('about', views.about, name='about'),
    path('guru', views.guru, name='guru'),
    
]