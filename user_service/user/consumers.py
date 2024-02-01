# user_service/user/consumers.py
import pika
from django.core.exceptions import ObjectDoesNotExist
from .models import User
from django.conf import settings

def user_check_callback(ch, method, properties, body):
    user_id = int(body)
    try:
        user = User.objects.get(pk=user_id)
        print(f"User {user_id} exists.")
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST,
                port=settings.RABBITMQ_PORT,
                credentials=pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD),
                virtual_host=settings.RABBITMQ_VHOST,
            ))
        except pika.exceptions.AMQPConnectionError as e:
            print(f"[user] Error connecting to RabbitMQ: {e}")
            raise
        channel = connection.channel()

        # Declare the queue
        channel.queue_declare(queue='order_processing_queue')

        # Send a message to the order processing queue
        channel.basic_publish(exchange='', routing_key='order_processing_queue', body=str('yes'))

        # Close the connection
        connection.close()
        
    except ObjectDoesNotExist:
        print(f"User {user_id} does not exist.")

def start_user_check_consumer():
    # connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='rabbitmq',
            port=5673,
            credentials=pika.PlainCredentials('guest', 'guest'),
            virtual_host=settings.RABBITMQ_VHOST,
           ))
    except pika.exceptions.AMQPConnectionError as e:
        print(f"[product] Error connecting to RabbitMQ: {e}")
        raise 
    channel = connection.channel()

    channel.queue_declare(queue='user_check_queue')
    channel.basic_consume(queue='user_check_queue', on_message_callback=user_check_callback, auto_ack=True)

    print(' [*] Waiting for user check messages. To exit, press CTRL+C')
    channel.start_consuming()
