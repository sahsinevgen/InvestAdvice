from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView



from django.db.models import query
from django.http import response
from rest_framework import generics
from rest_framework import permissions
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
# from .serializers import NoteSerializer
from django.conf import settings
import jwt

from .serializers import AdviceSerializer, MyTokenObtainPairSerializer, CustomUserSerializer

class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloWorldView(APIView):

    def get(self, request):
        return Response(data={"hello":"world"}, status=status.HTTP_200_OK)


class SettingsView(APIView):

    def get(self, request):
        token = request.headers['Authorization'][4:]
        print(token)
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        user = CustomUser.objects.get(id=payload['user_id'])
        print(user)
        return Response({'source': user.source, 'currency': user.currency})
    
    def post(self, request):
        token = request.headers['Authorization'][4:]
        print(token)
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        user = CustomUser.objects.get(id=payload['user_id'])
        print(payload)
        data=request.data
        print(data)
        user.source = data['source']
        user.currency = data['currency']
        user.save()
        return Response()

class AdvicesView(APIView):

    def post(self, request):
        token = request.headers['Authorization'][4:]
        print(token)
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        user = CustomUser.objects.get(id=payload['user_id'])
        source = user.source
        currency = user.currency
        data = request.data
        count = data['count']

        advices = Advice.objects
        if currency:
            advices = advices.filter(currency=currency)
        if source != 'both':
            if source == 'prediction':
                advices = advices.filter(source=source)
            else:
                advices = advices.filter(source__startswith='channel')
        advices = advices.order_by('-datetime')
        advices = advices.all()
        if count:
            advices = advices[:count]

        serializer = AdviceSerializer(advices, many=True)
        return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

