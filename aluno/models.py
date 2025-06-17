from django.db import models
from django.utils import timezone

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True, help_text='Digite o numero de Matrícula')
    nome = models.CharField(max_length=60, help_text='Digite o Nome do Aluno')
    dataInicial = models.DateField(null=False, default=timezone.now(), help_text='Informe a Data Inicial')
    dataFinal = models.DateField(null=True, blank=True, default=timezone.now(), help_text='Informe a Data Final')

def __str__(self):
    return f'{self.matricula} - {self.nome} - {self.dataInicial} - {self.dataFinal}'