from django.shortcuts import render

# Create your views here.
def listarInstrutor(request):
    return render(request, 'instrutor/listarInstrutor.html')

def cadastroInstrutor(request):
    return render(request, 'instrutor/cadastrarInstrutor.html')