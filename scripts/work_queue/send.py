import pika

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters('10.203.106.234', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue',)
for i in range(100):
	message = '%s Message ' % i or "Hello World!"
	channel.basic_publish(exchange='',routing_key='task_queue',body=message,properties=pika.BasicProperties(delivery_mode=2, ))
	print(" [x] Sent %r" % message)
channel.close()
