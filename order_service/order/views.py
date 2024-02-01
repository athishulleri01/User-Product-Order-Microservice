from rest_framework import generics, serializers
from rest_framework.response import Response
from .models import Order, User,Product
from .serializers import OrderSerializer
import pika
from .publisher import publish
class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    RABBITMQ_HOST = "localhost"
    
    def perform_create(self, serializer):
        user = serializer.validated_data['user_email']  
        product = serializer.validated_data['product_name'] 
        try:
            
            user = User.objects.get(email=user.email)
            
            try:
                product = Product.objects.get(product_id = product.product_id)
                print(product," Product created") 
            except Product.DoesNotExist:
                raise serializers.ValidationError("Product does not exist")
        except User.DoesNotExist:
            raise serializers.ValidationError("User email does not exist")

       
        serializer.save()
        publish("sent_email", serializer.data)
        print("........................................................")
        



class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
