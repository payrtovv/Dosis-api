from rest_framework import serializers

from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only':True},
                        'email':{
                            'error_messages':{
                                'unique':'Ya existe una cuenta con este correo'}}} 
        
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("La contraseña debe contener al menos un número.")
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra.")
        return value
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user 
    
    
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)  
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
        }
        return data