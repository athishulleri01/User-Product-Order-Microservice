# amqps://rpqwkxml:4tTcurda2kDqPtwiQMSUcar7vFhA_W9a@armadillo.rmq.cloudamqp.com/rpqwkxml
import pika
import json

from django.conf import settings

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


def publish(method,body):
    properties = pika.BasicProperties(method)
    print("[product] data sented to order service")
    channel.basic_publish(exchange='', routing_key='order_service',body=json.dumps(body),properties=properties)
    
