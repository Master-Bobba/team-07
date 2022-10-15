from mimetypes import guess_type
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'Team07.settings')
import django
django.setup()
from guitar.models import Guitar, GuitarsWithSong
import requests

def populate():
    response = requests.get("https://services.guitarguitar.co.uk/WebService/api/hackathon/guitars")
    
    for guitar in response.json():
        print(type(guitar), "\n\n")
        g = Guitar.objects.get_or_create(skU_ID = guitar["skU_ID"])[0]
        #for key,value in guitar.Items():
        g.asn = guitar["asn"]
        g.category = guitar["category"]
        g.online = guitar["online"]
        g.itemName = guitar["itemName"]
        g.title = guitar["title"]
        g.brandName = guitar["brandName"]
        g.description = guitar["description"]
        g.productDetail = guitar["productDetail"]
        g.salesPrice = guitar["salesPrice"]
        g.pictureMain = guitar["pictureMain"]
        g.qtyInStock = guitar["qtyInStock"]
        g.qtyOnOrder = guitar["qtyOnOrder"]
        g.colour = guitar["colour"]
        g.pickup = guitar["pickup"]
        g.bodyShape = guitar["bodyShape"]
        g.createOn = guitar["createOn"]
        g.imageUrls = guitar["imageUrls"]
        g.save()


if __name__=='__main__':
    print('Starting population script...')
    populate()
    print('Population Script Complete')
