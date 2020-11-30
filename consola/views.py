from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):    
    #return HttpResponse("Iniciando consola... Vamos de compras.")
    return render(request, 'consola/consola.html', {})
