from django.db import models


class profil(models.Model):
    nama = models.CharField(max_length=25)
    alamat = models.CharField(max_length=100)
    kode = models.IntegerField(null=True)
    negara = models.CharField(max_length=25)

    # def __str__(self):
    #     return self.nama