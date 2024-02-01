from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer
from .publisher import publish
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response 


        
class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request):  # /api/products :->get
        user = Products.objects.all()
        serializer = ProductSerializer(user, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

        
    def create(self,request):#/api/products    :->post
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        publish('product_created',serializer.data)
        print('product created')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    
    def retrieve(self,request,pk=None):#/api/products/<str:id>    :->get
        user = Products.objects.get(id=pk)
        serializer = ProductSerializer(user)
        return Response(serializer.data)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
