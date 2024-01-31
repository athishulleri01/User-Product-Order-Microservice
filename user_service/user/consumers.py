# user_service/user/consumers.py
import pika
from django.core.exceptions import ObjectDoesNotExist
from .models import User

def user_check_callback(ch, method, properties, body):
    user_id = int(body)
    try:
        user = User.objects.get(pk=user_id)
        print(f"User {user_id} exists.")
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
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
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='user_check_queue')
    channel.basic_consume(queue='user_check_queue', on_message_callback=user_check_callback, auto_ack=True)

    print(' [*] Waiting for user check messages. To exit, press CTRL+C')
    channel.start_consuming()
