from django import forms

# classe formulario inclusao
class TituloForm(forms.Form):
    descricao = forms.CharField(max_length=100,
                                required=True,
                                help_text='informe a descrição do Título')

class TituloAtualizarForm(forms.Form):
    codigo = forms.IntegerField(required=True,
                                help_text='informe o código do Título')

    descricao = forms.CharField(max_length=100,
                                required=True,
                                help_text='informe a descrição do Título')