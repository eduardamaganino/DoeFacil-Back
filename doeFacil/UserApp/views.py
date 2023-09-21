from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import User, Item, Doacao
from .serializers import UserSerializer, ItemSerializer, DoacaoSerializer

# Create your views here.

@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(email=user_data['email'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(email=id)
        user.delete()
        return JsonResponse("Deleted Succeffully!", safe=False)

@csrf_exempt
def itemApi(request, id=0):
    if request.method == 'GET':
        items = Item.objects.all()
        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = Item.objects.get(titulo=item_data['titulo'])
        item_serializer = ItemSerializer(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        item = Item.objects.get(titulo=id)
        item.delete()
        return JsonResponse("Deleted Succeffully!", safe=False)
    
@csrf_exempt
def doacaoApi(request, id=0):
    if request.method == 'GET':
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
        doacao = Doacao.objects.get(item=doacao_data['item'])
        doacao_serializer = DoacaoSerializer(doacao, data=doacao_data)
        if doacao_serializer.is_valid():
            doacao_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        doacao = Doacao.objects.get(item=id)
        doacao.delete()
        return JsonResponse("Deleted Succeffully!", safe=False)
