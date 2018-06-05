
今天遇到一个棘手的问题, 再用python脚本测试rabbitmq队列的时候由于自己太愚蠢创建了几百个随机的队列, 这个时候又不能重启服务器只能动手一个一个到rabbitmq提供的web界面里面去删除, 太累了, 而且不保险, 于是想到了一个办法把那些随机的队列从服务器当中给找出来, 找出来了之后运行一个python脚本将其删除

```shell
[root@zhangyz sbin]# ./rabbitmqctl list_queues | grep "amq.gen" | awk '{print $1}'
amq.gen-9H13Ph5ga_8W6oXc3itTPg
amq.gen-9wNuczJv5ZfTZPW4vm4--A
amq.gen-A8bGrdOZuvUrgUi_Ky97OA
amq.gen-AP9lGljpbnoSDCm7Q9cMNA
amq.gen-Ac0UBpSMczTYqeKLD2jaKA
amq.gen-B5xKhjAFtJWh7BOULRFv9A
amq.gen-BB8-fhPJpigA6czEmrMDqA
amq.gen-BRPRsG2yQQnKRETLwk_ZKA
amq.gen-BSZiZFHDhlPbYw9zWlj9mw
amq.gen-BjDjKQ-KJovRYehdIShj4g
amq.gen-Bs9Xg0bZdhx9FnZ_Of4Y4w
amq.gen-BsL0jOpLmO8FHftDe16nbg
amq.gen-ByJ_dwKlbMFjIzM1PmVGMQ
amq.gen-CB2foG0HHoxPVkYSD4dn-A
amq.gen-CBAyMhL_OH3Jl744zqKbFg
amq.gen-COEI2zicKBlRifoJba2IbQ
amq.gen-CYhbHXkfftuDBGUy-fFusA
amq.gen-CZfHLrF11lhJGkHQ-P-row
amq.gen-Cag6hdM29IlAxkhYHOLBeg
amq.gen-Cp8dcGqEJM38zLtlvI4QsA
amq.gen-CysWMxWZuSP24IRpmBzeVQ
amq.gen-DDyqffgWSSg1CQvj_SinIg
amq.gen-DEXxFWpcTUXhpvuK-p2eQQ
amq.gen-DIYbPtvwp75F6u6LGTRM-g
amq.gen-DTJryLpJBdvLkUAU51I8Kg
amq.gen-D_IOd4h6V01Pt8Dhq1k9OQ
amq.gen-DaQInbGAIC1t_d6LvVtPiA
amq.gen-DbrtdKVJcwFk9weGAlGVUw
amq.gen-DshSiZ8_7WSWgiq7x_pEIg
amq.gen-EW4yoINvRWPIKyUwSXffJQ
amq.gen-FLbKPzX0TW4xUBaCpPVoOQ
amq.gen-FTYZU_ZhPZtuPcn0M-DIBA
......
```

将以上输出的队列信息存到一个文件里面
```shell
[root@zhangyz sbin]# ./rabbitmqctl list_queues | grep "amq.gen" | awk '{print $1}' > /tmp/a.txt
```

然后运行python脚本
```python
import pika

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.1', 5672, '/', credentials))
channel = connection.channel()

f = open('./a.txt', 'r')
var01 = f.read()
var02 = var01.strip().split('\n')
for queueName in var02:
    channel.queue_delete(queue=queueName)
channel.close()
```
