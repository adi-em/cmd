from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.Htampil, name='home'),
    path('Hguru', views.Hguru, name='Hguru'),
    path('Habout', views.Habout, name='Habout'),
    path('sd', views.sd, name='sd'),
    path('smp', views.smp, name='smp'),
    path('sma', views.sma, name='sma'),
    path('form', views.form, name='form'),
]