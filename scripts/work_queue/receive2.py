import time
import pika

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters('10.203.106.234', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue',)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(body.count(b'.'))
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_consume(callback, queue='task_queue',)
print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()
