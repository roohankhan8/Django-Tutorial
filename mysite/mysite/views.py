# import requests
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.pyplot import text

def index(request):
    params = {
        'name': 'Roohan',
    }
    return render(request, 'index.html', params)
    # return HttpResponse('Hello')

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)

    return HttpResponse('removepunc')

def capitalize(request):
    return HttpResponse('capitalize')

def spaceremove(request):
    return HttpResponse('spaceremove')

def newlineremove(request):
    return HttpResponse('newlineremove')

def charcount(request):
    return HttpResponse('charcount')
