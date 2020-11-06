from django.db import models
from django.utils import timezone
from anime.models import Genre, Format
# Create your models here.

class Movie(models.Model):
    judul = models.CharField(max_length=25)
    rilis = models.DateField(null=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    kualitas = models.ForeignKey(Format, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.judul