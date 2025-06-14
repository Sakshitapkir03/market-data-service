import uuid
from typing import List

def create_polling_job(symbols: List[str], interval: int, provider: str = "yfinance") -> dict:
    job_id = f"poll_{uuid.uuid4().hex[:6]}"
    return {
        "job_id": job_id,
        "status": "accepted",
        "config": {
            "symbols": symbols,
            "interval": interval,
            "provider": provider
        }
    }