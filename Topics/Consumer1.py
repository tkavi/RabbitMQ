import pika,time

def message_received(ch,method,properties,body):
    print(f"Consumer 1 {body}")

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

queue = channel.queue_declare(queue='',exclusive=True)
channel.queue_bind(exchange='Topic',queue=queue.method.queue, routing_key='*.India.*')
print(queue.method.queue)
# channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue.method.queue,on_message_callback=message_received)
channel.start_consuming()