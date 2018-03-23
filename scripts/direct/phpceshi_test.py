import pika
import random

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.11.234", 5672, '/', credentials))
channel = connection.channel()

message = "php_ceshi!"

for i in range(100000):
	channel.exchange_declare(exchange='php_test',exchange_type='direct', durable=True)
	channel.basic_publish(exchange='php_test',routing_key='test',body=message)
connection.close()
