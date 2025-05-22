from django.shortcuts import HttpResponse

# Create your views here.
def utilitarios(request):
    return HttpResponse("Olá! Eu sou o utilitario")