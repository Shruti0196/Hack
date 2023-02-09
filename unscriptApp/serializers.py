from .models import *                  
# from django.contrib.auth.models import MyUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):  #2,#3
    class Meta:
        model=User
        fields=['username','password']

    def create(self,validated_data):
        # user=User.objects.create(username=validated_data['username'])
        # user.set_password(validated_data['password'])
        # user.save()
        if validate_password(validated_data['password']) == None:
            password = make_password(validated_data['password']) 
            print(password)                         
            user = User.objects.create(username=validated_data['username'],password=password)
            return user