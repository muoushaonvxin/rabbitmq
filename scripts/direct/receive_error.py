import pika
import sys

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.11.234", 5672, '/', credentials))

channel = connection.channel()
channel.exchange_declare(exchange='250test',exchange_type='direct',durable=True)

result = channel.queue_declare(exclusive=True)
queue_name = "error_test"

serverities = ["error",]

for serverity in serverities:
	channel.queue_bind(exchange='250test',queue=queue_name,routing_key=serverity)
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()
