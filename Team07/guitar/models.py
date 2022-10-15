from enum import unique
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class SpotifyToken(models.Model):
    user = models.CharField(max_length= 50, unique=True, default='')
    created_at = models.DateTimeField(auto_now_add = True)
    refresh_token = models.CharField(max_length = 150, default='')
    access_token = models.CharField(max_length = 150, default='')
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length = 50, default='')


class Guitar(models.Model):
    skU_ID = models.CharField(max_length=64, unique = True, primary_key = True)
    asn = models.CharField(default="", max_length=64)
    category = models.CharField(max_length = 64)
    online = models.BooleanField(default = True)
    itemName = models.CharField(max_length = 64)
    title = models.CharField(default="", max_length=64)
    brandName = models.CharField(max_length = 64)
    description = models.CharField(default = "", max_length = 256)
    productDetail = models.CharField(max_length = 512)
    salesPrice = models.FloatField(),
    pictureMain = models.URLField()
    qtyInStock = models.IntegerField(default = 0)
    qtyOnOrder = models.IntegerField(default = 0)
    colour = models.IntegerField(default = 0)
    pickup = models.IntegerField(default = 0)
    bodyShape = models.IntegerField(default = 0)
    createdOn = models.DateTimeField(null=True)
    imageUrls = models.URLField(null=True)

class GuitarsWithSong(models.Model):
    skU_ID = models.OneToOneField(Guitar, on_delete=models.CASCADE, primary_key=True)
    spotifyId = models.CharField(max_length = 128)
    youtubeUrl = models.URLField()

