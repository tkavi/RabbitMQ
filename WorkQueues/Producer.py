import time
import pika

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()
channel.queue_declare(queue='letterbox')

message_id = 1

while True:
    message = f'Sending message {message_id}'
    channel.basic_publish(exchange='',routing_key='letterbox',body=message)
    print(message)
    time.sleep(2)
    message_id += 1