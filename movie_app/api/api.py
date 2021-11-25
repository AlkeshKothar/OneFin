from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer, EmployeeSerializer
from django.contrib.auth.models import User
from movie_app.models import Collections



#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
           # "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


# Employee Create API
class EmployeeCreateApi(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Collections.objects.all()
    serializer_class = EmployeeSerializer


# Employee List API
class EmployeeApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Collections.objects.all()
    serializer_class = EmployeeSerializer


# Employe Update API
class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Collections.objects.all()
    serializer_class = EmployeeSerializer


# Employee Delete API
class EmployeeDeleteApi(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Collections.objects.all()
    serializer_class = EmployeeSerializer