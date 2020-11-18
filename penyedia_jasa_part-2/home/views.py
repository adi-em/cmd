from django.shortcuts import render

# Create your views here.

def Htampil(request):
    return render(request, 'vhome/index.html')

def Hguru(request):
    return render(request, 'vhome/guru.html')

def Habout(request):
    return render(request, 'vhome/about.html')

def sd(request):
    return render(request, 'vhome/sd.html')

def smp(request):
    return render(request, 'vhome/smp.html')

def sma(request):
    return render(request, 'vhome/sma.html')

def form(request):
    return render(request, 'vhome/form.html')
