from rest_framework import serializers
from .models import User, Item, Doacao

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'email', 'senha', 'nome', 'foto', 'bio', 'telefone', 'cpf', 'nascimento', 'sexo', 'nota', 'countAvaliacao', 'rua', 'numero', 'logradouro', 'cidade', 'estado', 'cep', 'pais']
        

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['itemId', 'motivo', 'quantidade', 'fotos', 'tempoDeUso', 'condicao', 'titulo', 'categoria']

class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacao
        fields = ['doacaoId', 'item', 'doador', 'donatario', 'dataDoacao', 'recebido', 'pedidos']