import pika
import random

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.11.234", 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='zhenshiceshi',exchange_type='direct', durable=True)
serverity_list = ["111111", "111112", "111113"]
for i in range(100000):
	serverity = serverity_list[random.randrange(3)]
	message = "Error Level is: %s, Message Number is:%s" % (serverity, {"a":123, "b":456})
	channel.basic_publish(exchange='zhenshiceshi',routing_key=serverity,body=message)
	print(" [x] Sent %r:%r" % (serverity, message))
connection.close()
