# user_service/user/consumers.py
import pika
import json
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

def user_check_callback(ch, method, properties, body):
    print("............................................")
    print("[x]   Received order data ")
    data = json.loads(body)
    print(data)
    print(properties.content_type)

  
    
    if properties.content_type =='sent_email':
               
        print("[Done]   successfully created"),
    print("............................................")
    

def start_user_check_consumer():
   # email_service/emails/consumers.py
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD),
            virtual_host=settings.RABBITMQ_VHOST,
        ))
    except pika.exceptions.AMQPConnectionError as e:
        print(f"[product] Error connecting to RabbitMQ: {e}")
        raise
    channel = connection.channel()

    channel.queue_declare(queue='email_service')
    channel.basic_consume(queue='email_service', on_message_callback=user_check_callback, auto_ack=True)

    print(' [*] Waiting for Order conformation. To exit, press CTRL+C')
    channel.start_consuming()
