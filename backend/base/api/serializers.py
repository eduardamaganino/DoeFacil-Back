from rest_framework.serializers import ModelSerializer
from base.models import User, Item, Doacao


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'email', 'password', 'username', 'foto', 'bio', 'listaDeDoacao', 'telefone', 'cpf', 'idade', 'sexo', 'nota', 'countAvaliacao', 'rua', 'numero', 'logradouro', 'cidade', 'estado', 'cep', 'pais', 'is_active']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['itemId', 'motivo', 'quantidade', 'fotos', 'tempoDeUso', 'condicao', 'titulo', 'categoria']

class DoacaoSerializer(ModelSerializer):
    class Meta:
        model = Doacao
        fields = ['doacaoId', 'item', 'doador', 'donatario', 'dataDoacao', 'recebido', 'pedidos']