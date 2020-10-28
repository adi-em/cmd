from django.shortcuts import render, redirect
from .models import profil
from .form import tambah_profil
from django.shortcuts import get_object_or_404, render

def index(request):
    context = {
        'todolist': profil.objects.all()
    }
    return render(request, 'index.html', context)

def tambah(request):
    form = tambah_profil(request.POST or None, request.FILES or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/")
    context['form']=form
    return render(request,"tambah.html", context)

def detail(request, id):
	detail_d = profil.objects.filter(pk=id).first()
	return render(request, 'detail.html',
		{ 'data': detail_d,
		})

def edit(request, id):
    if request.POST:
        profil.objects.filter(pk=id).update(nama=request.POST['nama'])
        return redirect('/')

    edit_d = profil.objects.filter(pk=id).first()
    return render(request, 'editdata.html', {'data': edit_d})

def delete(request, id):
    delete_d = profil.objects.filter(pk=id).delete()
    return redirect('/')

# def edit(request, pk, template_name='templates/editdata.html'):
#     post= get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, template_name, {'form':form})
