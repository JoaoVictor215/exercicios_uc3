from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'tiposdeatividade/listarTiposAtividade.html')

def cadastrar(request):
    return render(request, 'tiposdeatividade/cadastrarTiposAtividade.html')