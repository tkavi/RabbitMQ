import pika,time
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()
channel.exchange_declare(exchange='Topic', exchange_type=ExchangeType.topic)

while True:
    message = 'Sending message for topic'
    channel.basic_publish(exchange='Topic',routing_key='Asia.India.Delhi',body=message)
    print(message)
    time.sleep(2)
