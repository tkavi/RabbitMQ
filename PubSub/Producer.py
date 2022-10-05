import pika,time
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

while True:
    channel.exchange_declare(exchange='PubSub',exchange_type=ExchangeType.fanout)
    message = 'Sending message for PubSub'
    channel.basic_publish(exchange='PubSub',routing_key='',body=message)
    print(message)
    time.sleep(2)
