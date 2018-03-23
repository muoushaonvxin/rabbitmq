import pika
import random

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.11.234", 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='zhenshiceshi',exchange_type='direct', durable=True)

# serverity_list = ["111111", "111112"]

for i in range(100):
	# serverity = serverity_list[random.randrange(2)]
	message = "Message Number is:%s" % (i)
	channel.basic_publish(exchange='zhenshiceshi',routing_key='111113',body=message)
	print(" [x] Sent %r:%r" % (i, message))
connection.close()
