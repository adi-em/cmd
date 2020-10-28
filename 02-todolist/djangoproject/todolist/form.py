from django import forms
from .models import profil

class tambah_profil(forms.ModelForm):
    class Meta:
        model = profil
        fields = "__all__"
        error_messages = {
            'nama': {
                'required': 'Anda harus mengisi form nama'
            },
            'alamat' : {
                'required': "Anda harus mengisi form alamat"
            },
            'kode' : {
                'required': "Anda harus menset form kode"
            },
            'negara':{
                'required': "Anda harus mengisi form negara"
            }
        }