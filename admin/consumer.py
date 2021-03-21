import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

params = pika.URLParameters("amqps://iilpqvlm:hauPfMQoP6JI7Qi1rAE_WajV9BtQVbyY@puffin.rmq2.cloudamqp.com/iilpqvlm")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('product like incremented')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')

channel.start_consuming()

channel.close()
