from rest_framework import serializers
from .models import User, Item, Doacao

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'senha', 'nome', 'foto', 'bio', 'telefone', 'cpf', 'nascimento', 'sexo', 'nota', 'countAvaliacao', 'rua', 'numero', 'logradouro', 'cidade', 'estado', 'cep', 'pais']
        

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['motivo', 'quantidade', 'fotos', 'tempoDeUso', 'condicao', 'titulo', 'categoria']

class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacao
        fields = ['item', 'doador', 'donatario', 'dataDoacao', 'recebido', 'pedidos']