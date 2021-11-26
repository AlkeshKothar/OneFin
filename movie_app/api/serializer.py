from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer

from movie_app.models import Collections, Generes, Movie

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],password = validated_data['password'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GeneresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generes
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GeneresSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

        
class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Collections
        #fields = ('title','description','movies','description')
        fields = '__all__'
    
    def create(self, validated_data):
       print(">>>>>>",self.__dict__, validated_data)
       
       request = self.context.get('request')
       validated_data['created_by'] = request.user
       Collections_obj = Collections(validated_data)
       return Collections_obj