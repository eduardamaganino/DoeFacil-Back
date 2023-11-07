from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response


from base.models import User, Item, Doacao
from .serializers import UserSerializer, ItemSerializer, DoacaoSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([])
def createUser(request):
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    user_serializer.create(user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return JsonResponse("Added Successfully!", safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([])
def userApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            user = User.objects.get(userId=id)
            user_serializer = UserSerializer(user)
            return Response('Fucniona')
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        # file = request.FILES['file']
        # mf = file.name.split('.')
        # file.name = str(user_data['userId']) + '.' + mf[1]
        # user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(userId=user_data['userId'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(userId=id)
        user.delete()
        return JsonResponse("Deleted Succeffully!", safe=False)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def itemApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            item = Item.objects.get(itemId=id)
            item_serializer = ItemSerializer(item)
            return JsonResponse(item_serializer.data, safe=False)
        items = Item.objects.all()
        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        file = request.FILES['file']
        mf = file.name.split('.')
        file.name = str(item_data['itemId']) + '.' + mf[1]
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = Item.objects.get(itemId=item_data['itemId'])
        item_serializer = ItemSerializer(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        item = Item.objects.get(itemId=id)
        item.delete()
        return JsonResponse("Deleted Succeffully!", safe=False)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def doacaoApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            doacao = Doacao.objects.get(doacaoId=id)
            doacao_serializer = DoacaoSerializer(doacao)
            return JsonResponse(doacao_serializer.data, safe=False)
        doacoes = Doacao.objects.all()
        doacoes_serializer = DoacaoSerializer(doacoes, many=True)
        return JsonResponse(doacoes_serializer.data, safe=False)
    elif request.method == 'POST':
        doacao_data = JSONParser().parse(request)
        doacao_serializer = DoacaoSerializer(data=doacao_data)
        if doacao_serializer.is_valid():
            doacao_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        doacao_data = JSONParser().parse(request)
        doacao = Doacao.objects.get(doacaoId=doacao_data['doacaoId'])
        doacao_serializer = DoacaoSerializer(doacao, data=doacao_data)
        if doacao_serializer.is_valid():
            doacao_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        doacao = Doacao.objects.get(doacaoId=id)
        doacao.delete()
        return JsonResponse("Deleted Succeffully!", safe=False)
