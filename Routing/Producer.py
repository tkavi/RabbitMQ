import pika,time
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

while True:
    channel.exchange_declare(exchange='Routing',exchange_type=ExchangeType.direct)
    message = 'Sending message for Routing'
    channel.basic_publish(exchange='Routing',routing_key='India',body=message)
    print(message)
    time.sleep(2)
