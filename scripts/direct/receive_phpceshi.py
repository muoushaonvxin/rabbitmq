import pika
import sys

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters('10.203.11.234', 5672, '/', credentials))
channel = connection.channel()
channel.exchange_declare(exchange='php_test',exchange_type='direct',durable=True)
result = channel.queue_declare(exclusive=True)
queue_name = "php_ceshi"

channel.queue_bind(exchange='php_test',queue=queue_name,routing_key='test')

def callback(ch, method, properties, body):
    print(" [x] %r" % (body))

channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()
