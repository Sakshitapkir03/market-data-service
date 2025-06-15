# import uuid
# from typing import List

# def create_polling_job(symbols: List[str], interval: int, provider: str = "yfinance") -> dict:
#     job_id = f"poll_{uuid.uuid4().hex[:6]}"
#     return {
#         "job_id": job_id,
#         "status": "accepted",
#         "config": {
#             "symbols": symbols,
#             "interval": interval,
#             "provider": provider
#         }
#     }

# app/services/polling.py
import time
import threading
import random
from app.services.producer import produce_price_event

def poll_prices(symbols, interval, provider):
    def fetch():
        while True:
            for symbol in symbols:
                # Simulate fetching real-time price
                price = round(random.uniform(100, 300), 2)
                event = {
                    "symbol": symbol,
                    "price": price,
                    "timestamp": datetime.utcnow().isoformat(),
                    "source": provider,
                    "raw_response_id": f"poll_{symbol}"
                }
                produce_price_event(event)
            time.sleep(interval)

    thread = threading.Thread(target=fetch)
    thread.daemon = True
    thread.start()