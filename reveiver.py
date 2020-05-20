import pika
import time

# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
# channel.exchange_declare(exchange='logs', exchange_type='fanout')
# result = channel.queue_declare(queue='', exclusive=True)
# queue_name = result.method.queue
# channel.queue_bind(exchange='logs', queue=queue_name)
#
# print(' [*] Waiting for logs. To exit press CTRL+C')
#
# def callback(ch, method, properties, body):
#     print("Going to sleep for 15 sec")
#     time.sleep(15)
#     #print(" [x] %r" % body)
#     print("Done - sleep for 15 sec")
#
# channel.basic_consume(
#     queue=queue_name, on_message_callback=callback, auto_ack=True)
# channel.start_consuming()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello', exclusive=False)

def callback(ch, method, properties, body):
    print(" [x] Received %r now going to sleep 15 sec's" % body)
    time.sleep(15)
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='hello', on_message_callback=callback)
channel.start_consuming()