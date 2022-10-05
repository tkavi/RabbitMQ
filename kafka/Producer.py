from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(1,51):
    str = f"message {i}"
    bytes_array = bytes(str,'utf-8')
    producer.send('topic3',bytes_array)
    time.sleep(1)
    producer.flush()