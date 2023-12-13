from django.http import JsonResponse
from rest_framework.serializers import ModelSerializer
from base.models import Message, User, Item, Doacao
from rest_framework import serializers


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'motivo', 'quantidade', 'fotos', 'tempoDeUso', 'condicao', 'titulo', 'categoria', 'dono', 'recebido']


class UserSerializer(ModelSerializer):
    # listaDeDoacao = DoacaoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'foto', 'bio', 'listaDeDoacao', 'telefone', 'cpf', 'idade', 'sexo', 'nota', 'countAvaliacao', 'rua', 'numero', 'logradouro', 'cidade', 'estado', 'cep', 'pais', 'punicao', 'is_active']
    
    def create(self, validated_data):
        listaDeDoacao_data = validated_data.pop('listaDeDoacao', None)
        user = User.objects.create_user(**validated_data)
        if listaDeDoacao_data is not None:
            for doacao_id in listaDeDoacao_data:
                doacao = Doacao.objects.get(id=doacao_id)
                user.listaDeDoacao.add(doacao)
        return JsonResponse("Added Successfully!", safe=False)


class DoacaoSerializer(ModelSerializer):
    doador_detail = UserSerializer(source='doador', read_only=True)
    doador = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    donatario_detail = UserSerializer(source='donatario', read_only=True)
    donatario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    item_detail = ItemSerializer(source='item', read_only=True)
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    pedidos_detail = UserSerializer(source='pedidos', read_only=True, many=True)
    pedidos = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Doacao
        fields = ['id', 'item', 'item_detail', 'doador', 'doador_detail', 'donatario', 'donatario_detail', 'dataDoacao', 'recebido', 'pedidos', 'pedidos_detail']

class MessageSerializer(ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    print(user_detail)

    class Meta:
        model = Message
        fields = ['id', 'user', 'user_detail', 'message', 'type', 'created_at', 'donationId']