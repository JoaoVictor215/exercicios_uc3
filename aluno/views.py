from django.shortcuts import HttpResponse

# Create your views here.
def aluno(request):
    return HttpResponse("Olá! Eu sou o João")
    
    