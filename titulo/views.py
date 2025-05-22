from django.shortcuts import HttpResponse

# Create your views here.
def titulo(request):
    return HttpResponse("Olá! Eu sou o titulo")
