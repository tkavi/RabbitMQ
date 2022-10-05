import time
import pika

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()
channel.queue_declare(queue='letterbox')

message = 'Hello World'

while True:
    channel.basic_publish(exchange='',routing_key='letterbox',body=message)
    print("msg sent")
    time.sleep(5)
