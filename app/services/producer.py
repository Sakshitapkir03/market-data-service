from confluent_kafka import Producer
import json

p = Producer({'bootstrap.servers': 'kafka:9092'})

def produce_price_event(event):
    p.produce('price-events', json.dumps(event).encode('utf-8'))
    p.flush()