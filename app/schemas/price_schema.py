from pydantic import BaseModel
from typing import List, Optional

class LatestPriceResponse(BaseModel):
    symbol: str
    price: float
    timestamp: str
    provider: str

class PollRequest(BaseModel):
    symbols: List[str]
    interval: int
    provider: Optional[str] = "yfinance"

class PollResponse(BaseModel):
    job_id: str
    status: str
    config: dict