import pika
import random

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.11.234", 5672, '/', credentials))
channel = connection.channel()

message = "hello world!"

for i in range(1):
	channel.exchange_declare(exchange='test',exchange_type='direct', durable=True)
	channel.basic_publish(exchange='test',routing_key='',body=message)
connection.close()
