from django.shortcuts import render

# Create your views here.
# user_service/user/views.py
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .publisher import publish
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response 


# class UserListView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
#     def perform_create(self, serializer):
#         # Call the publish method when a new user is created
#         instance = serializer.save()
#         print(instance)
#         publish("user created", serializer.data)
#         print(instance)
        
        
class UserViewSet(viewsets.ViewSet):
    
    def list(self, request):  # /api/products :->get
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

        
    def create(self,request):#/api/products    :->post
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        publish('user_created',serializer.data)
        print('user created')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    
    def retrieve(self,request,pk=None):#/api/products/<str:id>    :->get
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
