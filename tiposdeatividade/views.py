from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Olá! Eu sou o index")

def exibe_mensagem(request):
    t_html = ""
    return HttpResponse(t_html)

'<!DOCType html><body>Olá</body></!DOCType>'