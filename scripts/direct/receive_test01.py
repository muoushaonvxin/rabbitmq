import pika
import sys

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters('10.203.11.234', 5672, '/', credentials))
channel = connection.channel()
channel.exchange_declare(exchange='test',exchange_type='direct',durable=True)
result = channel.queue_declare(exclusive=True)
queue_name = "test01"

channel.queue_bind(exchange='test',queue=queue_name,routing_key='')

def callback(ch, method, properties, body):
    print(" [x] %r" % (body))

channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()
