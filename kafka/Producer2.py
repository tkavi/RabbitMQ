from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(1,11):
    str = f'message {i} from producer2'
    bytes_array = bytes(str,'utf-8')
    producer.send('topic2',bytes_array)
    time.sleep(1)
    producer.flush()