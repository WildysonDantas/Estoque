from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

#Foram definidos 4 campos para o banco de dados, todos obrigatorios
class Estoque(models.Model):
    codigo = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 50, null =  False, blank = False)
    quantidade = models.IntegerField(null = False, blank = False)
    categoria = models.CharField(max_length=20, null = False, blank = False)

    def __str__ (self):
        return self.nome

class Historico(models.Model):
    fk_codigo = models.ForeignKey(Estoque, related_name='movimentacao', on_delete=models.CASCADE, null=True, )
    entrada = models.DateTimeField(null= True)
    saida = models.DateTimeField(null = True)
    quantidade = models.IntegerField(null= False, blank = False)
