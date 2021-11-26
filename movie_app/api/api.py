from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer,UserSerializer,GeneresSerializer,MovieSerializer,CollectionSerializer
from django.contrib.auth.models import User
from movie_app.models import Collections
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
import requests
from django.conf import settings
from rest_framework.views import APIView
from django.urls import reverse
from rest_framework import viewsets
from movie_app.models import Generes , Movie , Collections 
from rest_framework import status

#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokenr = TokenObtainPairSerializer().get_token(user)  
        tokena = AccessToken().for_user(user)

        
        return Response({
            #"user": UserSerializer(user,    context=self.get_serializer_context()).data,
            #"message": "User Created Successfully.",
            #"refresh" : str(tokenr),
            "access_token" : str(tokena)
        })



class MovieView(APIView):

    def get(self, request, *args, **kwargs):
        #permission_classes = [permissions.IsAuthenticated,]
        page_number = request.GET['page'] if 'page' in request.GET else None
        url = settings.MOVIE_API_URL if not page_number else "{}?page={}".format(settings.MOVIE_API_URL, page_number)
        user = settings.MOVIE_API_USER
        password = settings.MOVIE_USER_PASS
        movie_data = requests.get( url, auth=(user, password)).json()
        if movie_data.get('next') : movie_data['next'] = movie_data['next'].replace(url, request.build_absolute_uri((reverse('movie'))))
        if movie_data.get('previous') : movie_data['previous'] = movie_data['previous'].replace(url, request.build_absolute_uri((reverse('movie'))))
        return Response(movie_data)
    

class CollectionsView(viewsets.ViewSet):

    serializer_class = CollectionSerializer
    """
    {
   “title”: “<Title of the collection>”,
   “description”: “<Description of the collection>”,
   “movies”: [
            {
                “title”: <title of the movie>,
                “description”: <description of the movie>,
                “genres”: <generes>,
                “uuid”: <uuid>
            }, ...
        ]
        }
    """
    """"""
    
    def list(self, request):
        data = Collections.objects.filter(created_by=request.user)
        return Response(data)


    def create(self, request):
        print(">>>>>>>>>",request.data)
        request.data['created_by'] = request.user.id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):

        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass



    pass