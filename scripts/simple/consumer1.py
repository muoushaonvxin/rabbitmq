import pika

username = 'hitrader'
password = 'hitrader123'

user_pwd = pika.PlainCredentials(username, password)
s_conn = pika.BlockingConnection(pika.ConnectionParameters('10.203.11.234', credentials=user_pwd))
chan = s_conn.channel()
chan.queue_declare(queue='hello',durable=True)

def callback(ch, method, properties, body):
    print("[消费者] recv %s" % body)

chan.basic_consume(callback, queue='hello', no_ack=True)
print('[消费者] waiting for msg. ')
chan.start_consuming()
