import pika
import random

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.11.234", 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='250test',exchange_type='direct', durable=True)
serverity_list = ["error", "warring", "info"]
for i in range(100):
	serverity = serverity_list[random.randrange(3)]
	message = "Error Level is: %s, Message Number is:%s" % (serverity, i)
	channel.basic_publish(exchange='250test',routing_key=serverity,body=message)
	print(" [x] Sent %r:%r" % (serverity, message))
connection.close()
