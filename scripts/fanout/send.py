import sys
import pika

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.106.234", 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout',durable=True)
for i in range(100):
	message = "Logs Number:%s" % i
	channel.basic_publish(exchange="logs",routing_key="",body=message,)
	print(" [x] Sent %r" % message)
connection.close()
