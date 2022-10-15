from http.client import HTTPResponse
import re
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from .models import SpotifyToken, Guitar
from django.template import RequestContext
import random

from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from .util import is_spotify_authenticated, update_or_create_user_tokens, is_spotify_authenticated

class AuthURL(APIView):
    def get(self, request, format= None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

        url = Request('GET', 'https://accounts.spotify.com/authorize', parama = {
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
    context = RequestContext(request)
    context_dict = {}
    guitars = Guitar.objects.order_by('salesPrice')[:3]

    context_dict['guitars'] = guitars

    return render(request, 'guitar/index.html', context=context_dict)


def get_token(request):

    if request.method == 'GET':
        access_token = SpotifyToken.objects.get(user = request.session.session_key).access_token

        response = requests.get(
        'https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl?market=ES',
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    print(json_resp['album']['artists'][0]['name'])

    return JsonResponse({'access_token': access_token}, status = 200)

def brand(request):
    context = RequestContext(request)

    return render(request, 'guitar/brand.html')

def brands(request):
    context = RequestContext(request)

    return render(request, 'guitar/brands.html')

def category(request):
    context = RequestContext(request)

    return render(request, 'guitar/category.html')

def categories(request):
    context = RequestContext(request)

    return render(request, 'guitar/categories.html')

def guitar(request):
    context = RequestContext(request)

    return render(request, 'guitar/guitar.html')

def song(request):
    context = RequestContext(request)

    return render(request, 'guitar/song.html')

