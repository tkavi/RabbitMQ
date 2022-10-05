import time
import pika

def message_received(ch,method,properties,body):
    time.sleep(1)
    print("msg received")
    print(f'Received {body}')
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("msg processed and acknowledged")

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()
channel.queue_declare(queue='letterbox')
channel.basic_qos(prefetch_count=1) #helps in load balancing
channel.basic_consume(queue='letterbox',on_message_callback=message_received)
channel.start_consuming()