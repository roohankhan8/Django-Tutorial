# import requests
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.pyplot import text
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')

    if djtext == '':
        messages.error(request, 'Enter Text To Be  Analyzed.')
        return render(request, 'index.html')

    if charcount == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'Count Characters', 'analyzed_text': analyzed}
        return render(request, 'punc.html', params)

    if spaceremove == 'on':
        analyzed = djtext.strip()
        params = {'purpose': 'Space Remove', 'analyzed_text': analyzed}
        return render(request, 'punc.html', params)

    if capitalize == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'Capitalize', 'analyzed_text': analyzed}
        return render(request, 'punc.html', params)

    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'punc.html', params)

    else:
        return HttpResponse('Please Check Boxes')
