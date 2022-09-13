# djsr/authentication/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['fav_color'] = user.username
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    # email = serializers.EmailField(
    #     required=True
    # )
    username = serializers.CharField()
    password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class StopLossSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopLoss
        fields = ['entry']

class TakeProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeProfit
        fields = ['entry']

class AdviceSerializer(serializers.ModelSerializer):
    stop_losses = StopLossSerializer(many=True)
    take_profits = TakeProfitSerializer(many=True)

    def get_stop_losses(self, obj):
        return StopLossSerializer(obj.stop_losses_set.all(), many=True).data

    def get_take_profits(self, obj):
        return TakeProfitSerializer(obj.take_profits_set.all(), many=True).data

    class Meta:
        model = Advice
        fields = [
            'currency',
            'operation_type',
            'entry',
            'stop_losses',
            'take_profits',
            'datetime',
            'source'
        ]