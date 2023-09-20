from djongo import models as djongo_models
from django.db import models

# Create your models here.

class Endereco(models.Model):
    user = djongo_models.ForeignKey('User', on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    logradouro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.IntegerField()
    pais = models.CharField(max_length=100)


class Fotos(models.Model):
    foto = models.CharField(primary_key=True, max_length=100)


class Item(models.Model):
    motivo = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    usuario = djongo_models.ForeignKey('User', on_delete=models.CASCADE, primary_key=True)
    fotos = djongo_models.ArrayField(model_container=Fotos)
    tempoDeUso = models.CharField(max_length=100)
    condicao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)


class Avaliacao(models.Model):
    nota = models.IntegerField(primary_key=True)


class User(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    nome = models.CharField(max_length=100, primary_key=True)
    foto = models.CharField(max_length=100)
    bio = models.TextField()
    listaDeDoacao = djongo_models.ArrayField(model_container=Item)
    telefone = models.CharField(max_length=100)
    endereco = djongo_models.ForeignKey(Endereco, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    avaliacoes = djongo_models.ArrayField(model_container=Avaliacao)

class Doacao(models.Model):
    item = djongo_models.ForeignKey(Item, on_delete=models.CASCADE, primary_key=True)
    doador = djongo_models.ForeignKey(User, on_delete=models.CASCADE)
    donatario = djongo_models.ForeignKey(User, on_delete=models.CASCADE)
    dataDoacao = models.DateField()
    recebido = models.CharField(max_length=100)
    pedidos = models.ArrayField(model_container=User)
