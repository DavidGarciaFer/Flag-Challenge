from django.shortcuts import render
from django.http import HttpResponse
from names.models import Country
from random import shuffle

def shuffle_countries():
    countries = [c.iso2 for c in list(Country.objects.order_by('name_es'))]
    shuffle(countries)
    return countries

def index(request):
    # Creo una tirada aleatoria
    if 'game' not in request.session:
        request.session['game'] = shuffle_countries()
    if 'started' not in request.session:
        request.session['started'] = True
    context_dict = {'boldmessage': "Probando, probando, un, dos."}
    return render(request, 'start/index.html', context=context_dict)

def about(request):
    del request.session['game']
    return render(request, 'start/about.html')