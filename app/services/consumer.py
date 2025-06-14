from confluent_kafka import Consumer
import json

c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'ma-consumer',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['price-events'])

while True:
    msg = c.poll(1.0)
    if msg is not None and not msg.error():
        data = json.loads(msg.value().decode('utf-8'))
        # Calculate moving average and upsert to DB