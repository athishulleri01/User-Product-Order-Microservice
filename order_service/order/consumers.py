# user_service/user/consumers.py
import pika
import json
from django.core.exceptions import ObjectDoesNotExist
from .models import User

def user_check_callback(ch, method, properties, body):
    print("[x]   Received user data ")
    data = json.loads(body)
    print(data)
    print(properties.content_type)

  
    
    if properties.content_type =='user_created':
        users = User()
        users.id = data['id']
        users.email = data['email']
        users.username = data['username']
        users.save()
        print('[Done]   ',users.username,"successfully created"),
        
    
def start_user_check_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='user_model_queue')
    channel.basic_consume(queue='user_model_queue', on_message_callback=user_check_callback, auto_ack=True)

    print(' [*] Waiting for user registraion. To exit, press CTRL+C')
    channel.start_consuming()
