
from django.shortcuts import render
from . models import *

def index(request):
    artigos = Artigo.objects.all()


    return render(request, 'index.html', {
        'artigos': artigos
         
    
    })