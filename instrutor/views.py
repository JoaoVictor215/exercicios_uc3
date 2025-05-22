from django.shortcuts import HttpResponse

# Create your views here.
def instrutor(request):
    return HttpResponse("Olá! Eu sou o Instrutor")