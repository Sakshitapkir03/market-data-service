from fastapi import APIRouter, Query
from app.schemas.price_schema import LatestPriceResponse, PollRequest, PollResponse
from app.services import polling

router = APIRouter()

@router.get("/prices/latest", response_model=LatestPriceResponse)
def get_latest_price(symbol: str, provider: str = "yfinance"):
    # Mock response — replace with real API logic later
    return {
        "symbol": symbol,
        "price": 150.25,
        "timestamp": "2024-03-20T10:30:00Z",
        "provider": provider
    }

@router.post("/prices/poll", response_model=PollResponse, status_code=202)
def post_poll_job(payload: PollRequest):
    job_info = polling.create_polling_job(
        symbols=payload.symbols,
        interval=payload.interval,
        provider=payload.provider
    )
    return job_info