import pika,time,uuid

def message_received(ch,method,properties,body):
    print(f'Client {body}')

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='requestQueue')
channel.queue_declare(queue='replyQueue')
# id = str(uuid.uuid4())
channel.basic_publish(exchange='',routing_key='requestQueue',body='message from server',
                      properties=pika.BasicProperties(reply_to='replyQueue'))

channel.basic_consume(queue='replyQueue',on_message_callback=message_received)

channel.start_consuming()