from django.db import models

    

class Item(models.Model):
    itemId = models.AutoField(primary_key=True, unique=True, serialize=True)
    motivo = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    fotos = models.CharField(max_length=100)
    tempoDeUso = models.CharField(max_length=100)
    condicao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

class User(models.Model):
    userId = models.AutoField(primary_key=True, unique=True, serialize=True)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    foto = models.CharField(max_length=100, blank=True)
    bio = models.TextField()
    listaDeDoacao = models.CharField(max_length=100, null=True) # Alterado para CharField para armazenar a lista de doações
    telefone = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)  # Alterado para 11 caracteres para representar o CPF
    nascimento = models.CharField(max_length=20)  # Alterado para DateField para armazenar a data de nascimento
    sexo = models.CharField(max_length=1)  # Alterado para 1 caractere para representar o sexo
    nota = models.IntegerField(null=True)
    countAvaliacao = models.IntegerField(null=True)

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
