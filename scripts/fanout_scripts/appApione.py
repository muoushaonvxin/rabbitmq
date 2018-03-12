import pika
import json

credentials = pika.PlainCredentials("hxt_rabbitmq_en", "hxt_212106_hq")
connection = pika.BlockingConnection(pika.ConnectionParameters('10.25.154.52', 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='broadweb',exchange_type='fanout',durable=True)
result = channel.queue_declare(exclusive=True)
queue_name = "appApione"

channel.queue_bind(exchange='broadweb',queue=queue_name,routing_key='11408')

def callback(ch, method, properties, body):
    var01 = json.loads(body.decode())
    print(var01)

channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()
