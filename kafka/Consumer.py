from kafka import KafkaConsumer

topics = ['topic_demo','topic2','topic3']
consumer = KafkaConsumer()

consumer.subscribe(topics)

for message in consumer:
    print(message)

