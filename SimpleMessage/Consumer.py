import pika

def message_received(ch,method,properties,body):
    print("msg received")

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()
channel.queue_declare(queue='letterbox')
channel.basic_consume(queue='letterbox',on_message_callback=message_received,auto_ack=True)
channel.start_consuming()