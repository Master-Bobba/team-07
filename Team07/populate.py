from mimetypes import guess_type
import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'Team07.settings')
django.setup()

from guitar.models import Guitar, GuitarsWithSong

def populate():
    guitar_response = requests.get("https://services.guitarguitar.co.uk/WebService/api/hackathon/guitars")
    songs_response = requests.get("https://services.guitarguitar.co.uk/WebService/api/hackathon/guitarswithsongs")
    guitars = guitar_response.json()
    songs = songs_response.json()

    for guitar in guitars:
        g = Guitar.objects.get_or_create(skU_ID = guitar["skU_ID"])[0]
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
        g.createdOn = guitar["createdOn"]
        g.imageUrls = guitar["imageUrls"]
        g.save()

    for song in songs:
        s = GuitarsWithSong.objects.get_or_create(skU_ID=Guitar.objects.get(skU_ID=song["skU_ID"]))[0]
        s.spotifyId = song["spotifyId"]
        s.youtubeUrl = song["youtubeUrl"]
        s.save()







if __name__=='__main__':
    print('Starting population script...')
    populate()
    print('Population Script Complete')
