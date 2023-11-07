from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True, unique=True, serialize=True)
    motivo = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100, default="1")
    fotos = models.CharField(max_length=100)
    tempoDeUso = models.CharField(max_length=100, default="0")
    condicao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True, unique=True, serialize=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    foto = models.FileField(upload_to='media', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    listaDeDoacao = models.ManyToManyField(to='Doacao',null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)  # Alterado para 11 caracteres para representar o CPF
    idade = models.IntegerField(null=True)
    sexo = models.CharField(max_length=100,null=True, blank=True)  # Alterado para 1 caractere para representar o sexo
    nota = models.IntegerField(null=True, blank=True)
    countAvaliacao = models.IntegerField(null=True, blank=True)

    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    logradouro = models.CharField(max_length=100,null=True, blank=True)
    cidade = models.CharField(max_length=100,null=True, blank=True)
    estado = models.CharField(max_length=100,null=True, blank=True)
    cep = models.CharField(max_length=10,null=True, blank=True)  # Alterado para CharField para armazenar o CEP corretamente
    pais = models.CharField(max_length=100,null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    is_anonymous = False
    is_authenticated = True




class Doacao(models.Model):
    id = models.AutoField(primary_key=True, unique=True, serialize=True)
    item = models.CharField(max_length=100) # Alterado para CharField para armazenar o item
    doador = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='doador') # Alterado para ForeignKey para armazenar o doador
    donatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donatario') # Alterado para ForeignKey para armazenar o donatário
    dataDoacao = models.DateField(auto_now_add=True)
    recebido = models.CharField(max_length=100)
    pedidos = models.ManyToManyField(User, related_name='pedidos') # Alterado para ManyToManyField para armazenar os pedidos

