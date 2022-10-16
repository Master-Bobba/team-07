from http.client import HTTPResponse
import re
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from .models import GuitarsWithSong, SpotifyToken, Guitar
from django.template import RequestContext
import random

from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from .DictCategories import CATEGORIES
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from .util import is_spotify_authenticated, update_or_create_user_tokens, is_spotify_authenticated

class AuthURL(APIView):
    def get(self, request, format= None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

        url = Request('GET', 'https://accounts.spotify.com/authorize', params = {
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return Response({'url': url}, status = status.HTTP_200_OK)

def spotify_callback(request, format = None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    response = post('https://accounts.spotify.com/api/token', data = {
        'grant_type': 'authorization_code',
        'code': code, 
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    return redirect('guitar:index')


class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(self.request.session.session_key)
        return Response({'status': is_authenticated}, status = status.HTTP_200_OK)

def index(request):

    songGuitars = GuitarsWithSong.objects.all().values_list("skU_ID")[:3]
    print(songGuitars)

    guitars = []

    for guitar in songGuitars:
        guitars.append(Guitar.objects.get(skU_ID = guitar[0]))    

    print(guitars)
    #guitars = Guitar.objects.all().order_by('salesPrice')[:3]
  

    return render(request, "guitar/index.html", {
        'guitars': guitars
    })


# def get_token(request):

#     if request.method == 'GET':
#         access_token = SpotifyToken.objects.get(user = request.session.session_key).access_token

#         response = requests.get(
#         'https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl?market=ES',
#         headers = {
#             "Authorization": f"Bearer {access_token}"
#         }
#     )
#     json_resp = response.json()

#     print(json_resp['album']['artists'][0]['name'])

#     return JsonResponse({'access_token': access_token}, status = 200)

def brand(request, brand_id):
    guitars = Guitar.objects.filter(brandName = brand_id)[:30]

    return render(request, 'guitar/brand.html', {
        "guitars": guitars,
        "brand" : brand_id,
    })

def brands(request):
    brands = Guitar.objects.order_by().values_list('brandName', flat=True).distinct()
    context = {}
    context['brands'] = []
    count = 0
    for brand in brands:
        b = Guitar.objects.filter(brandName = brand).values_list("pictureMain")
        context['brands'].append([brand , b[0][0] ])
        count += 1
        if count >=24:
            break
    return render(request, 'guitar/brands.html', context= context)

def category(request, category_id):
    
    guitars = Guitar.objects.filter(category = category_id)[:30]

    return render(request, 'guitar/category.html', {
        "guitars": guitars,
        'category': CATEGORIES[category_id]
    })

def categories(request):
    context = {}
    cats = Guitar.objects.order_by().values_list('category', flat=True).distinct()

    context['categories'] = []
    count = 0
    for category in cats:
        p = Guitar.objects.filter(category = category).values_list("pictureMain")
        context['categories'].append([CATEGORIES[category], p[0][0], category  ])
        count+= 1
        if count == 8:
            break
    return render(request, 'guitar/categories.html', context= context)


def guitar(request, guitar_id):

    guitar = Guitar.objects.get(skU_ID = guitar_id)
    print(guitar)

    #spotify stuff
    music_links = GuitarsWithSong.objects.filter(skU_ID = guitar.skU_ID)
    if len(music_links) == 0:
        return render(request, 'guitar/guitar.html', {
        'guitar': guitar,
        })
    else:
        song = music_links[0].spotifyId.split("?", 1)[0]
        track = get_Song(request, song)

        print(type(music_links[0].youtubeUrl.replace("watch?v=", "embed/")))

        return render(request, 'guitar/guitar.html', {
            'guitar': guitar,
            'music_links': music_links[0].youtubeUrl.replace("watch?v=", "embed/"),
            'spotify': track
        })

def song(request):
    context = RequestContext(request)

    return render(request, 'guitar/song.html')

def get_token(request):

    if request.method == 'GET':
        access_token = SpotifyToken.objects.get(user = request.session.session_key).access_token
        

def get_Song(request, song):

    access_token = SpotifyToken.objects.get(user = request.session.session_key).access_token
    songURL = 'https://api.spotify.com/v1/tracks/' + song + '?market=ES'
    response = requests.get(
    songURL,
    headers = {
        "Authorization": f"Bearer {access_token}"
    })
    track = response.json()
    
    trackDict = {}

    trackDict["artistName"] = track['artists'][0]['name']
    trackDict["songName"] = track['name']
    trackDict["albumCover"] = track['album']['images'][2]['url']
    trackDict["songUrl"] = track['external_urls']['spotify']
    trackDict["songId"] = song

    return trackDict