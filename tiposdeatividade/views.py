from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    return HttpResponse("Olá! Eu sou o index")

# def exibe_mensagem(request):
#     t_html = "<DocType html><html><body>Ola Mundo</body></html>"
#     return HttpResponse(t_html)

def test_render(request):
    return render(request, 'escola.html')