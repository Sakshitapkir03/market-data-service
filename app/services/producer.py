# from confluent_kafka import Producer
# import json

# p = Producer({'bootstrap.servers': 'kafka:9092'})

# def produce_price_event(event):
#     p.produce('price-events', json.dumps(event).encode('utf-8'))
#     p.flush()

# app/services/producer.py
from confluent_kafka import Producer
import json
import os

conf = {'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")}
producer = Producer(**conf)

def produce_price_event(data: dict):
    producer.produce("price-events", json.dumps(data).encode("utf-8"))
    producer.flush()