from rest_framework import generics, serializers
from rest_framework.response import Response
from .models import Order, User
from .serializers import OrderSerializer
import pika

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    RABBITMQ_HOST = "localhost"
    
    def perform_create(self, serializer):
        email = serializer.validated_data['user_email']

        # Check if the email already exists in the User model
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email does not exist")

        # If the email exists, save the order
        serializer.save()

    def check_user_exists(self, user_email):
        # Connect to RabbitMQ to send a message for user existence check
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        # Declare the queue
        channel.queue_declare(queue='user_check_queue')

        # Send a message to the user check queue
        channel.basic_publish(exchange='', routing_key='user_check_queue', body=str(user_id))

        # Close the connection
        connection.close()

        return True 



class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
