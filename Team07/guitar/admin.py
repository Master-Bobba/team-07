from django.contrib import admin

# Register your models here.
from .models import SpotifyToken, GuitarsWithSong, Guitar

admin.site.register(SpotifyToken)
admin.site.register(GuitarsWithSong)
admin.site.register(Guitar)