from django.shortcuts import render, redirect
from . import models
from anime.form import TambahForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def home(request):
    return render(request, 'home.html')

def tampil(request):
    if request.POST:
        models.Anime.objects.all()
        
    tampilkan = models.Anime.objects.all()
    return render(request, 'indexx.html',
		{ 'data': tampilkan,
		})

def detail(request, id):
	detail_d = models.Anime .objects.filter(pk=id).first()
	return render(request, 'detail.html',
		{ 'data': detail_d,
		})

def tambah(request):
    if request.POST:
        form = TambahForm(request.POST)
        if form.is_valid():
            form.save()
            form = TambahForm()
            pesan = 'Data Berhasil di Simpan'
            konteks = {
                'form':form,
                'pesan':pesan
            }
            return render(request, 'tambah.html', konteks)
    else:
        form = TambahForm()
        konteks = {
            'form':form,
        }
        return render(request, 'tambah.html', konteks)

def edit(request, id_judul):
    juduls = models.Anime.objects.get(id=id_judul)
    template = 'edit.html'
    if request.POST:
        form = TambahForm(request.POST, instance=juduls)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil di Perbarui')
            return redirect('edit', id_judul=id_judul)
    else:
        form = TambahForm(instance=juduls)
        konteks = {
            'form':form,
            'juduls':juduls
        }
    return render(request, template, konteks)

def delete(request, id):
    delete_d = models.Anime.objects.filter(pk=id).delete()
    return redirect('/indexx')



# def tambah(request):
#     if request.POST:
#         models.Anime.objects.create(
#             judul=request.POST['judul'],
#             tahun=request.POST['tahun'],
#             genre_id=request.POST['genre'],
#             jumlah_episode=request.POST['episode']
#         )
#         return redirect('/')

#     tambahkan = models.Anime.objects.all()
#     keterangan = models.Genre.objects.all()

#     return render(request, 'tambah.html', 
#     {'tambahkan':tambahkan,
#     'keterangan':keterangan
#     })