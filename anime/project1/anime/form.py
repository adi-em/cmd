from django.forms import ModelForm
from django import forms
from anime.models import Anime

class TambahForm(ModelForm):
    class Meta:
        model = Anime
        fields ="__all__"


        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'tahun' : forms.NumberInput({'class':'form-control'}),
            'genre_id' : forms.Select({'class':'form-control'}),
            'jumlah_epidose' : forms.NumberInput({'class':'form-control'}),
        }