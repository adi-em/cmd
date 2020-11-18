from django.db import models

# Create your models here.

class KtgAmpu(models.Model):
    nama=models.CharField(max_length=10)

    def __str__(self):
        return self.nama

class pengajar(models.Model):
    nama=models.CharField(max_length=30)
    no=models.CharField(max_length=15)
    alamat=models.CharField(max_length=225)
    biaya=models.IntegerField()
    ampu=models.ForeignKey(KtgAmpu, on_delete=models.CASCADE, null=True)
    kelamin=models.BooleanField(default=True)
    usia=models.IntegerField(null=False)
    catatan=models.TextField(null=True)
    foto=models.ImageField(upload_to='img/')
    portofolio=models.FileField(upload_to='document/')

    def __str__(self):
        return self.nama

class murid(models.Model):
    nama=models.CharField(max_length=30)
    alamat=models.CharField(max_length=225)
    no=models.CharField(max_length=15)
    pendidikan=models.ForeignKey(KtgAmpu, on_delete=models.CASCADE, null=True)
    kelamin=models.BooleanField(default=True)

    def __str__(self):
        return self.nama