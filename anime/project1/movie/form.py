from django.forms import ModelForm
from django import forms
from movie.models import Movie

class FormMovie(ModelForm):
    class Meta:
        model = Movie
        fields ="__all__"


        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'rilis' : forms.DateInput({'class':'form-control'}),
            'genre_id' : forms.Select({'class':'form-control'}),
            'kualitas' : forms.Select({'class':'form-control'}),
            'description' : forms.TextInput({'class':'form-control'}),
        }