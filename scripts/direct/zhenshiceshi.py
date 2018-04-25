import pika
import random

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.206.234", 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='zhenshiceshi',exchange_type='direct', durable=True)
serverity_list = ["111111", "111112", "111113"]
for i in range(1000):
	serverity = serverity_list[random.randrange(3)]
	message = '{"ordernumber":"1779","price":"1.59991","profit":"0.64","spreadprofit":"8.4"},{"ordernumber":"1837","price":"0.76713","profit":"-0.64","spreadprofit":"-6.4"},{"ordernumber":"1855","price":"1.22682","profit":"0.2","spreadprofit":"0.1"},{"ordernumber":"1899","price":"0.72093","profit":"294.6","spreadprofit":"147.3"},{"ordernumber":"1934","price":"0.97838","profit":"2.46","spreadprofit":"31.4"},{"ordernumber":"1939","price":"107.808","profit":"0.85","spreadprofit":"9.2"}'
	channel.basic_publish(exchange='zhenshiceshi',routing_key=serverity,body=message)
	print(" [x] Sent %r:%r" % (serverity, message))
connection.close()
