from django.shortcuts import render
from django.http import HttpResponse
from names.models import Country
from random import shuffle

def shuffle_countries():
    countries = list(Country.objects.order_by('name_es'))
    shuffle(countries)
    return countries

def prueba(n):
    ret = []
    count = shuffle_countries()
    for c in count[:n]:
        ret.append(c.iso2.lower()+'.svg')
    return ret

def index(request):
    if len(request.session['game']) > 0:
        country = request.session['game'][0]
        request.session['game'] = request.session['game'][1:]
    context_dict = {'boldmessage': "Probando, probando, tres, cuatro.", 'country': country}
    return render(request, 'names/flag.html', context=context_dict)
