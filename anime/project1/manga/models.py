from django.db import models
from anime.models import Genre


class FormatManga(models.Model):
    Nformat = models.CharField(max_length=20)

    def __str__(self):
        return self.Nformat

class Manga(models.Model):
    judul = models.CharField(max_length=25)
    rilis = models.DateField(null=False)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    pengarang = models.CharField(max_length=50)
    formatM = models.ForeignKey(FormatManga, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)
    baca = models.CharField(max_length=25)
    description = models.TextField(null=True)

    def __str__(self):
        return self.judul
