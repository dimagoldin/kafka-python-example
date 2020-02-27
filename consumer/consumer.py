from kafka import KafkaConsumer
import json

topic = 'my_topic'
bootstrap_servers = ['localhost:9092']
try:
    consumer = KafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        group_id='kafka-example-consumer',
        # enable_auto_commit=True,
        key_deserializer=lambda v: v.decode('utf-8'),
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )
except:
    exit(1)

consumer.subscribe(topics=[topic])


for message in consumer:
    # print(message)
    print(f'Received message offset: {str(message.offset)} with key: {message.key} name: {message.value.get("name","no-name")} age: {message.value.get("age",str(0))}', flush=True)

print("Exiting?")