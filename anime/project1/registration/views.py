from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def tambahuser(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil di Buat")
            return redirect('tambahuser.html')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('tambahuser')
    else:
        form = UserCreationForm()
        kontek = {
            form:'form',
        }
    return render (request, 'tambahuser.html', kontek)