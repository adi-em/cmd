from django.contrib import admin
from .models import Anime, Genre, Format

# Register your models here.

class profilku(admin.ModelAdmin):
    list_display = ['judul', 'tahun', 'genre_id', 'jumlah_episode']
    search_fields = ['judul', 'genre_id']
    list_filter = ('genre_id', 'tahun')
    list_per_page = 4

admin.site.register(Anime, profilku)
admin.site.register(Genre)
admin.site.register(Format)