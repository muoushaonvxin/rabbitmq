import pika
import random
import json

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters("10.203.11.234", 5672, '/', credentials))
channel = connection.channel()

message = {
	'aid': 42558,
 	'data': '{"balance":-1640275.70,"comment":"default buy #40694","commission":0.0,"dataaccuracy":5,"equity":-1640275.70,"freemargin":0.0,"lots":0.10,"opendate":"2018    .03.07","openprice":1.608650,"opentime":"17:00:00","ordernumber":"EURCAD-40694-20180307170000","realaid":40694,"stoploss":1.60540,"swap":3.0,"symbolid":17,"takeprofit":1.61150,"trade    type":0}\n',
  	'from': 'mt4',
   	'type': 20602
}

message = json.dumps(message)

channel.exchange_declare(exchange='ExMt4ToCpp.Dir',exchange_type='direct', durable=True)
channel.basic_publish(exchange='ExMt4ToCpp.Dir',routing_key='Mt4ToCpp',body=message)
