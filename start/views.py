from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Probando, probando, un, dos."}
    return render(request, 'start/index.html', context=context_dict)

def about(request):
    return render(request, 'start/about.html')