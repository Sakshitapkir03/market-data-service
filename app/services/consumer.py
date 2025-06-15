# from confluent_kafka import Consumer
# import json

# c = Consumer({
#     'bootstrap.servers': 'kafka:9092',
#     'group.id': 'ma-consumer',
#     'auto.offset.reset': 'earliest'
# })

# c.subscribe(['price-events'])

# while True:
#     msg = c.poll(1.0)
#     if msg is not None and not msg.error():
#         data = json.loads(msg.value().decode('utf-8'))
#         # Calculate moving average and upsert to DB

# app/services/consumer.py
from confluent_kafka import Consumer
import json
from app.core.database import SessionLocal
from app.models.schema import RawMarketData, MovingAverage
import numpy as np

def calculate_ma(symbol):
    db = SessionLocal()
    prices = db.query(RawMarketData.price)\
        .filter(RawMarketData.symbol == symbol)\
        .order_by(RawMarketData.timestamp.desc())\
        .limit(5).all()
    values = [p[0] for p in prices]
    return round(np.mean(values), 2) if values else None

def consume():
    c = Consumer({
        'bootstrap.servers': 'kafka:9092',
        'group.id': 'ma-group',
        'auto.offset.reset': 'earliest'
    })
    c.subscribe(['price-events'])

    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        data = json.loads(msg.value().decode('utf-8'))
        avg = calculate_ma(data['symbol'])

        if avg is not None:
            db = SessionLocal()
            record = MovingAverage(symbol=data['symbol'], average=avg)
            db.add(record)
            db.commit()