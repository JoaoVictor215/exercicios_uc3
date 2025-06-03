from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True, help_text='Digite o numero de Matrícula')
    nome = models.CharField(max_length=60, help_text='Digite o Nome do Aluno')
    dataInicial = models.DateField(max_length=10, help_text='Informe a Data Inicial')
    dataFinal = models.DateField(max_length=10, help_text='Informe a Data Final')

def __str__(self):
    return f'{self.matricula} - {self.nome} - {self.dataInicial} - {self.dataFinal}'
    