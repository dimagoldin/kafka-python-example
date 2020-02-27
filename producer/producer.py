from kafka import KafkaProducer
import json, random, os, time
topic = 'my_topic'
bootstrap_servers = ['localhost:9092']


producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    key_serializer=lambda v: v.encode('utf-8'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

names = ["dima", "ziv", "miri", "shay"]
for i in range(0,int(os.environ.get("COUNT", 20))):
    print(f'Producing {str(i)}th message', flush=True)
    producer.send(
        topic,
        key=str(f'test_message_{str(i)}'),
        value={
            "name": names[random.randint(0, len(names) - 1)],
            "age": random.randint(18, 40)
        }
    )
    producer.flush()
    time.sleep(1)




