import pika
import json

credentials = pika.PlainCredentials("cjiajiaHT", "HitHt01.&>")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.11.234", 5672, '/', credentials))
channel = connection.channel()
channel.exchange_declare(exchange='ExCppToDemo.Fan',exchange_type='fanout',durable=True)
result = channel.queue_declare(exclusive=True)
queue_name = "CppToDemoManager_ceshi"
channel.queue_bind(exchange='ExCppToDemo.Fan',queue=queue_name,routing_key='')

def callback(ch, method, properties, body):
    print(json.loads(body.decode()))

try:
	channel.basic_consume(callback,queue=queue_name,no_ack=True)
	channel.start_consuming()
except:
	print("")
