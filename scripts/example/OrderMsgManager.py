import pika
import sys
import json

credentials = pika.PlainCredentials("cjiajiaHT", "HitHt01.&>")
connection = pika.BlockingConnection(pika.ConnectionParameters('10.203.11.234', 5672, '/', credentials))
channel = connection.channel()
channel.exchange_declare(exchange='ExConvertToCpp.Dir',exchange_type='direct',durable=True)
result = channel.queue_declare(exclusive=True)
queue_name = "queueMt4ToOMM"

channel.queue_bind(exchange='ExConvertToCpp.Dir',queue=queue_name,routing_key='Mt4ToCpp')

def callback(ch, method, properties, body):
    var01 = json.loads(body.decode())
    print(var01)

channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()
