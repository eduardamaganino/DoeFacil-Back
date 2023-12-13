from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response


from base.models import Message, User, Item, Doacao
from .serializers import MessageSerializer, UserSerializer, ItemSerializer
from .serializers import DoacaoSerializer
from .pusher import pusher_client
from rest_framework.views import APIView

from django.core.files.storage import default_storage
from datetime import date


# Create your views here.

@csrf_exempt
@api_view(['POST'])
def handle_uploaded_file(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)

    return JsonResponse({'file_name': file_name})

@api_view(['POST'])
@permission_classes([])
def createUser(request):
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    return user_serializer.create(user_data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, id):
    user_data = JSONParser().parse(request)
    user_data['punicao'] = date.today()  # Atualiza o campo punicao com a data atual
    try:
        user = User.objects.get(id=id)
        user_serializer = UserSerializer(user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Punicao Successfully!", safe=False)
        return JsonResponse(user_serializer.errors, safe=False)
    except User.DoesNotExist:
        return JsonResponse("User not found.", safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def userApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            user = User.objects.get(id=id)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data, safe=False)
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=user_data['id'])
        password = user.password
        user_data['password'] = password
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse(user_serializer.errors, safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Succeffully!", safe=False)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([])
def itemApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            item = Item.objects.get(id=id)
            item_serializer = ItemSerializer(item)
            return JsonResponse(item_serializer.data, safe=False)
        items = Item.objects.all()
        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        # file = request.FILES['file']
        # mf = file.name.split('.')
        # file.name = str(item_data['itemId']) + '.' + mf[1]
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse(item_serializer.errors, safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = Item.objects.get(id=item_data['id'])
        item_serializer = ItemSerializer(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        item = Item.objects.get(id=id)
        item.delete()
        return JsonResponse("Deleted Succeffully!", safe=False)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def doacaoApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            doacao = Doacao.objects.get(id=id)
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
            return Response(doacao_serializer.data, status=201)
        return Response(doacao_serializer.errors, status=400)
    elif request.method == 'PUT':
        doacao_data = JSONParser().parse(request)
        doacao = Doacao.objects.get(id=doacao_data['id'])
        doacao_serializer = DoacaoSerializer(doacao, data=doacao_data)
        if doacao_serializer.is_valid():
            doacao_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        doacao = Doacao.objects.get(id=id)
        doacao.delete()
        return JsonResponse("Deleted Succeffully!", safe=False)
    


# class MessageAPIView(APIView):
#     # permission_classes = (IsAuthenticated,)

#     @api_view(['POST'])
#     def messagePost(self, request, format=None):
        
    
#     @api_view(['GET'])
#     def get(self, request, format=None):
#         messages = Message.objects.filter(donationId=request.data['donationId'])
#         message_serializer = MessageSerializer(messages, many=True)
#         return Response(message_serializer.data, status=200)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def messageApi(request, donationId=None):
    if(request.method == 'POST'):
        pusher_client.trigger('chat', 'message', {
            'message': request.data['message'],
            'username': request.user.username,
            'created_at': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            'type': request.data['type'],
            'donationId': request.data['donationId']
        })

        message_data = {
            'user': request.user.id,
            'message': request.data['message'],
            'type': request.data['type'],
            'donationId': request.data['donationId'],
            'created_at': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }
        message_serializer = MessageSerializer(data=message_data)
        if message_serializer.is_valid():
            message_serializer.save()
            return Response(message_serializer.data, status=201)
        return Response(message_serializer.errors, status=400)

    elif(request.method == 'GET'):
        messages = Message.objects.filter(donationId=donationId)
        message_serializer = MessageSerializer(messages, many=True)
        return Response(message_serializer.data, status=200)
    
    elif(request.method == 'DELETE'):
        messages = Message.objects.filter(donationId=donationId)
        messages.delete()
        return Response("Deleted Succeffully!", status=200)
