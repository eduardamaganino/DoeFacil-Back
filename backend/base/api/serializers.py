from rest_framework.serializers import ModelSerializer
from base.models import User, Item, Doacao


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'email', 'senha', 'nome', 'foto', 'bio', 'telefone', 'cpf', 'nascimento', 'sexo', 'nota', 'countAvaliacao', 'rua', 'numero', 'logradouro', 'cidade', 'estado', 'cep', 'pais']
        

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['itemId', 'motivo', 'quantidade', 'fotos', 'tempoDeUso', 'condicao', 'titulo', 'categoria']

class DoacaoSerializer(ModelSerializer):
    class Meta:
        model = Doacao
        fields = ['doacaoId', 'item', 'doador', 'donatario', 'dataDoacao', 'recebido', 'pedidos']