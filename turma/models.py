from django.db import models

# Create your models here.
class Aluno(models.Model):
    numero = models.AutoField(primary_key=True, help_text='Digite o Numero')





def __str__(self):
    return f'{self.} - {self.}'