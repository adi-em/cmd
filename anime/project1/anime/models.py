from django.db import models
# Create your models here.

class Genre(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama

class Format(models.Model):
    kualitas = models.CharField(max_length=15)

    def __str__(self):
        return self.kualitas

class Anime(models.Model):
    judul = models.CharField(max_length=25)
    tahun = models.CharField(max_length=100)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    jumlah_episode = models.IntegerField(null=True)
    download = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.judul
