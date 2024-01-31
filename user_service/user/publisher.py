# amqps://rpqwkxml:4tTcurda2kDqPtwiQMSUcar7vFhA_W9a@armadillo.rmq.cloudamqp.com/rpqwkxml
import pika
import json



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def publish(method,body):
    properties = pika.BasicProperties(method)
    print(properties,"......................")
    channel.basic_publish(exchange='', routing_key='user_model_queue',body=json.dumps(body),properties=properties)
    
