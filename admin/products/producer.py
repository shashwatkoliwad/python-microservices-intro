import pika, json

params = pika.URLParameters("amqps://iilpqvlm:hauPfMQoP6JI7Qi1rAE_WajV9BtQVbyY@puffin.rmq2.cloudamqp.com/iilpqvlm")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)