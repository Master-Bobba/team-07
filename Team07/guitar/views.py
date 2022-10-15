from http.client import HTTPResponse
import re
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .models import Guitar
import random

def index(request):
    context = RequestContext(request)
    context_dict = {}
    guitars = Guitar.objects.order_by('id')[:3]
    
    context_dict['guitars'] = guitars


    return render(request, 'guitar/index.html')
