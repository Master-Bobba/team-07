from django.contrib import admin

# Register your models here.
from .models import SpotifyToken, Guitar,GuitarsWithSong

admin.site.register(SpotifyToken)
admin.site.register(Guitar)
admin.site.register(GuitarsWithSong)