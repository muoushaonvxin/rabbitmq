import pika
import sys

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters('10.203.11.234', 5672, '/', credentials))
channel = connection.channel()
channel.exchange_declare(exchange='ExCppToPhp.Dir',exchange_type='direct',durable=True)
result = channel.queue_declare(exclusive=False)
queue_name = result.method.queue
print(queue_name)

def callback(ch, method, properties, body):
    print("[消费者] recv %s" % body)

try:
	channel.queue_bind(exchange='ExCppToPhp.Dir',queue=queue_name,routing_key='55479')
	channel.basic_consume(callback, queue=queue_name, no_ack=True)
	print('[消费者] waiting for msg. ')
	channel.start_consuming()
except:
	pass
