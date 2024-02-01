# user_service/user/consumers.py
import pika
import json
from django.core.exceptions import ObjectDoesNotExist
from .models import User,Product
from django.conf import settings

def user_check_callback(ch, method, properties, body):
    print("............................................")
    print("[x]   Received user data ")
    data = json.loads(body)
    # print(data)
    print(properties.content_type)

  
    
    if properties.content_type =='user_created':
        users = User()
        users.id = data['id']
        users.email = data['email']
        users.username = data['username']
        users.save()
        print('[Done]   ',users.username,"successfully created"),
    elif properties.content_type =='product_created':
        product = Product()
        product.product_id = data['id']
        product.name = data['name']
        product.price = data['price']
        product.save()        
        print('[Done]   ',product.name,"successfully created"),
    print("............................................")
    

def start_user_check_consumer():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD),
            virtual_host=settings.RABBITMQ_VHOST,
        ))
    except pika.exceptions.AMQPConnectionError as e:
        print(f"[order] Error connecting to RabbitMQ: {e}")
        raise
    channel = connection.channel()

    channel.queue_declare(queue='order_service')
    channel.basic_consume(queue='order_service', on_message_callback=user_check_callback, auto_ack=True)

    print(' [*] Waiting for user registraion. To exit, press CTRL+C')
    channel.start_consuming()
