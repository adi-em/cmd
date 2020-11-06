from django.shortcuts import render, redirect
from . import models
from manga.form import FormManga
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def tampilmanga(request):
    if request.POST:
        models.Manga.objects.all()
        
    tampilkan = models.Manga.objects.all()
    return render(request, 'indexxx.html',
		{ 'data': tampilkan,
		})

def detailmanga(request, id):
	detail_d = models.Manga.objects.filter(pk=id).first()
	return render(request, 'detailmanga.html',
		{ 'data': detail_d,
		})

def tambahmanga(request, id):
    if request.POST:
        form = FormManga(request.POST)
        if form.is_valid():
            form.save()
            form = FormManga()
            pesan = 'Data Berhasil di Simpan'
            konteks = {
                'form':form,
                'pesan':pesan
            }
            return render(request, 'tambahmanga.html', konteks)
    else:
        form = FormManga()
        konteks = {
            'form':form,
        }
        return render(request, 'tambahmanga.html', konteks)

def editmanga(request, id_judul):
    juduls = models.Manga.objects.get(id=id_judul)
    template = 'editmanga.html'
    if request.POST:
        form = FormManga(request.POST, instance=juduls)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil di Perbarui')
            return redirect('editmanga', id_judul=id_judul)
    else:
        form = FormManga(instance=juduls)
        konteks = {
            'form':form,
            'juduls':juduls
        }
    return render(request, template, konteks)

def deletemanga(request, id):
    delete_d = models.Manga.objects.filter(pk=id).delete()
    return redirect('/manga')