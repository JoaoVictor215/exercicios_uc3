from django.shortcuts import HttpResponse

# Create your views here.
def turma(request):
    return HttpResponse("Olá! Eu sou a turma")