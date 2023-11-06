from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    itemId = models.AutoField(primary_key=True, unique=True, serialize=True)
    motivo = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100, default="1")
    fotos = models.CharField(max_length=100)
    tempoDeUso = models.CharField(max_length=100, default="0")
    condicao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

class User(models.Model):
    userId = models.AutoField(primary_key=True, unique=True, serialize=True)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=100)
    foto = models.FileField(upload_to='media', null=True, blank=True)
    bio = models.TextField()
    listaDeDoacao = models.CharField(max_length=100, null=True, blank=True) # Alterado para CharField para armazenar a lista de doações
    telefone = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)  # Alterado para 11 caracteres para representar o CPF
    idade = models.IntegerField(null=True)
    sexo = models.CharField(max_length=100)  # Alterado para 1 caractere para representar o sexo
    nota = models.IntegerField(null=True, blank=True)
    countAvaliacao = models.IntegerField(null=True, blank=True)

    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    logradouro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)  # Alterado para CharField para armazenar o CEP corretamente
    pais = models.CharField(max_length=100)



class Doacao(models.Model):
    doacaoId = models.AutoField(primary_key=True, unique=True, serialize=True)
    item = models.CharField(max_length=100) # Alterado para CharField para armazenar o item
    doador = models.CharField(max_length=100) # Alterado para CharField para armazenar o doador
    donatario = models.CharField(max_length=100) # Alterado para CharField para armazenar o donatário
    dataDoacao = models.CharField(max_length=100) # Alterado para CharField para armazenar a data de doação
    recebido = models.CharField(max_length=100)
    pedidos = models.CharField(max_length=100) # Alterado para CharField para armazenar a lista de pedidos

