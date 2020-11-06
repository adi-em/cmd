from django.shortcuts import render, redirect
from . import models
from movie.form import FormMovie
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def tampilmovie(request):
    if request.POST:
        models.Movie.objects.all()
        
    tampilkan = models.Movie.objects.all()
    return render(request, 'indexmovie.html',
		{ 'data': tampilkan,
		})

def detailmovie(request, id):
	detail_d = models.Movie.objects.filter(pk=id).first()
	return render(request, 'detailmovie.html',
		{ 'data': detail_d,
		})

def tambahmovie(request, id):
    if request.POST:
        form = FormMovie(request.POST)
        if form.is_valid():
            form.save()
            form = FormMovie()
            pesan = 'Data Berhasil di Simpan'
            konteks = {
                'form':form,
                'pesan':pesan
            }
            return render(request, 'tambahmovie.html', konteks)
    else:
        form = FormMovie()
        konteks = {
            'form':form,
        }
        return render(request, 'tambahmovie.html', konteks)

def editmovie(request, id_judul):
    juduls = models.Movie.objects.get(id=id_judul)
    template = 'editmovie.html'
    if request.POST:
        form = FormMovie(request.POST, instance=juduls)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil di Perbarui')
            return redirect('editmovie', id_judul=id_judul)
    else:
        form = FormMovie(instance=juduls)
        konteks = {
            'form':form,
            'juduls':juduls
        }
    return render(request, template, konteks)

def deletemovie(request, id):
    delete_d = models.Movie.objects.filter(pk=id).delete()
    return redirect('/movie')