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
    context_dict = {'boldmessage': "Probando, probando, tres, cuatro.", 'list': prueba(1)}
    return render(request, 'names/flag.html', context=context_dict)
