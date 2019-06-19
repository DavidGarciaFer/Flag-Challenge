from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Probando, probando, tres, cuatro."}
    return render(request, 'names/index.html', context=context_dict)