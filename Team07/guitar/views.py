from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .models import Guitar
import random

# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {}
    guitars = Guitar.objects.order_by('salesPrice')[:3]
    
    context_dict['guitars'] = guitars


    return render(request, 'guitar/index.html')
