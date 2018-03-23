import pika

username = 'hitrader'
password = 'hitrader123'

user_pwd = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(pika.ConnectionParameters('10.203.11.234',credentials=user_pwd))
channel = connection.channel()
channel.basic_publish(exchange='php_test',routing_key='test',body='{"a":"123", "b":"456"}')
print('[生产者] hello adfkajfl.')
connection.close()
