from django.shortcuts import render
from .models import profil

def index(request):
    context = {
        'todolist': profil.objects.all()
    }
    return render(request, 'index.html', context)
