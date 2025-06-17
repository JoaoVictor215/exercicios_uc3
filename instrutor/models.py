from django.db import models
from django.utils import timezone

from titulo.models import Titulo

# Create your models here.
class Instrutor(models.Model):
    id = models.AutoField(primary_key=True, help_text='Identificacao do Instrutor')
    rg = models.CharField(max_length=15, help_text='Informe o RG do Instrutor')
    nome = models.CharField(max_length=70, help_text='Informe o nome do Instrutor')
    dataNascimento = models.DateField(null=True, blank=True, default=timezone.now(), help_text='Informe a data de Nascimento')
    telefone = models.CharField(max_length=9, help_text='Informe o número de telefone')
    ddd = models.CharField(max_length=3, help_text='Informe o DDD')

    codigo_titulo = models.ForeignKey(Titulo, null=True, blank=True, related_name='titulos', on_delete=models.SET_NULL, db_column='titulo_codigo')

    def __str__(self):
        return f'{self.id} - {self.rg} - {self.nome} - {self.dataNascimento} - {self.telefone} - {self.ddd}'