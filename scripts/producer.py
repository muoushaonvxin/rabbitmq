import pika

username = 'hitrader'
password = 'hitrader123'

user_pwd = pika.PlainCredentials(username, password)
s_conn = pika.BlockingConnection(pika.ConnectionParameters('10.203.106.234',credentials=user_pwd))
chan = s_conn.channel()
chan.queue_declare(queue='queueVipOrderServer')
chan.queue_bind('queueVipOrderServer','ExDispathToCpp.Dir','DispathToCpp1')
chan.basic_publish(exchange='ExDispathToCpp.Dir',routing_key='DispathToCpp1',body='hello wo shi 10.203.106.250!!!')
print('[生产者] hello hello.')
s_conn.close()
