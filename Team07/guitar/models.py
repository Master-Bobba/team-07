from django.db import models

# Create your models here.
class Guitar(models.Model):
    sku_id = models.CharField(max_length=64),
    asn = models.CharField(default="", max_length=64),
    category = models.CharField(max_length = 64),
    online = models.BooleanField(default = True),
    itemName = models.CharField(max_length = 64),
    title = models.CharField(default="", max_length=64),
    brandName = models.CharField(max_length = 64),
    description = models.CharField(default = "", max_length = 256)
    productDetail = models.CharField(max_length = 512),
    salesPrice = models.FloatField(), 
    pictureMain = models.URLField(unique=True),
    qtyInStock = models.IntegerField(default = 0),
    qtyOnOrder = models.IntegerField(default = 0),
    colour = models.IntegerField(default = 0),
    pickup = models.IntegerField(default = 0),
    bodyShape = models.IntegerField(default = 0),
    createOn = models.DateTimeField(),
    imageUrls = models.URLField(unique=True)
    


