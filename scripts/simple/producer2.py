import pika

username = 'hitrader'
password = 'hitrader123'

user_pwd = pika.PlainCredentials(username, password)
s_conn = pika.BlockingConnection(pika.ConnectionParameters('10.203.11.234',credentials=user_pwd))
chan = s_conn.channel()
chan.queue_declare(queue='hello',durable=True)
chan.queue_bind('hello','test','test')
chan.basic_publish(exchange='test',routing_key='test',body='{ "a":"123", "b":"456"}')
print('[生产者] hello adfkajfl.')
s_conn.close()
