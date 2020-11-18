from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

# @login_required(login_url=settings.LOGIN_URL)
def home(request):
    return render(request, 'vfrondend/indexp.html')

def about(request):
    return render(request, 'vfrondend/about.html')

def guru(request):
    return render(request, 'vfrondend/guru.html')