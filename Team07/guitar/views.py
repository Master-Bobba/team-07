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
    guitars = Guitar.objects.order_by('salesPrice')[:3]
    
    context_dict['guitars'] = guitars


    return render(request, 'guitar/index.html', context=context_dict)

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