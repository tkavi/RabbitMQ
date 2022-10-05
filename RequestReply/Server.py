import pika,time,uuid

def message_received(ch,method,properties,body):
    print(f'Server {body}')
    ch.basic_publish('',routing_key=properties.reply_to,body='Here is response')

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='requestQueue')
channel.basic_consume(queue='requestQueue',on_message_callback=message_received)

channel.start_consuming()
