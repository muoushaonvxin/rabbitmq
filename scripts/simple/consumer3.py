import pika

username = 'hitrader'
password = 'hitrader123'

user_pwd = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(pika.ConnectionParameters('10.203.11.234', credentials=user_pwd))
channel = connection.channel()
channel.exchange_declare(exchange='php_test',exchange_type='direct',durable=True)
channel.queue_declare(exclusive=False)
channel.queue_bind(exchange='php_test',queue='php_ceshi',routing_key="test")

def callback(ch, method, properties, body):
    print("[消费者] recv %s" % body)

channel.basic_consume(callback, queue='php_ceshi', no_ack=True)
print('[消费者] waiting for msg. ')
channel.start_consuming()
