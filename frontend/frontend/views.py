from django.http import HttpResponse                    #Imporración para usar objetos Response
from django.shortcuts import render                     #renderizado de plantillas

def inicio(request):
    return render(request, 'index.html', {})