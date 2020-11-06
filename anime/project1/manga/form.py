from django.forms import ModelForm
from django import forms
from manga.models import Manga

class FormManga(ModelForm):
    class Meta:
        model = Manga
        fields ="__all__"


        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'rilis' : forms.DateInput({'class':'form-control'}),
            'genre_id' : forms.Select({'class':'form-control'}),
            'pengarang' : forms.TextInput({'class':'form-control'}),
            'format' : forms.Select({'class':'form-control'}),
            'status' : forms.TextInput({'class':'form-control'}),
            'baca' : forms.TextInput({'class':'form-control'}),
            'description' : forms.TextInput({'class':'form-control'}),
        }