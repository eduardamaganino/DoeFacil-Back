from djongo import models

    

class Item(models.Model):
    motivo = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    fotos = models.CharField(max_length=100)
    tempoDeUso = models.CharField(max_length=100)
    condicao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100, primary_key=True, unique=True)
    categoria = models.CharField(max_length=100)

class User(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    senha = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    foto = models.CharField(max_length=100)
    bio = models.TextField()
    listaDeDoacao = models.CharField(max_length=100) # Alterado para CharField para armazenar a lista de doações
    telefone = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)  # Alterado para 11 caracteres para representar o CPF
    nascimento = models.DateField()  # Alterado para DateField para armazenar a data de nascimento
    sexo = models.CharField(max_length=1)  # Alterado para 1 caractere para representar o sexo
    nota = models.IntegerField()
    countAvaliacao = models.IntegerField()

    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    logradouro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)  # Alterado para CharField para armazenar o CEP corretamente
    pais = models.CharField(max_length=100)



class Doacao(models.Model):
    item = models.CharField(max_length=100) # Alterado para CharField para armazenar o item
    doador = models.CharField(max_length=100) # Alterado para CharField para armazenar o doador
    donatario = models.CharField(max_length=100) # Alterado para CharField para armazenar o donatário
    dataDoacao = models.DateField()
    recebido = models.CharField(max_length=100)
    pedidos = models.CharField(max_length=100) # Alterado para CharField para armazenar a lista de pedidos
