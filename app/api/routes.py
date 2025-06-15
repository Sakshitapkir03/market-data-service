# from fastapi import APIRouter, Query
# from app.schemas.price_schema import LatestPriceResponse, PollRequest, PollResponse
# from app.services import polling

# router = APIRouter()

# @router.get("/prices/latest", response_model=LatestPriceResponse)
# def get_latest_price(symbol: str, provider: str = "yfinance"):
#     # Mock response — replace with real API logic later
#     return {
#         "symbol": symbol,
#         "price": 150.25,
#         "timestamp": "2024-03-20T10:30:00Z",
#         "provider": provider
#     }

# @router.post("/prices/poll", response_model=PollResponse, status_code=202)
# def post_poll_job(payload: PollRequest):
#     job_info = polling.create_polling_job(
#         symbols=payload.symbols,
#         interval=payload.interval,
#         provider=payload.provider
#     )
#     return job_info

# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.models.schema import RawMarketData
# from app.core.database import SessionLocal
# from pydantic import BaseModel
# from typing import List
# import datetime

# router = APIRouter()

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Pydantic schema for request
# class MarketDataIn(BaseModel):
#     symbol: str
#     price: float
#     provider: str

# # POST endpoint to insert data
# @router.post("/market-data")
# def insert_market_data(data: MarketDataIn, db: Session = Depends(get_db)):
#     record = RawMarketData(
#         symbol=data.symbol,
#         price=data.price,
#         provider=data.provider,
#         timestamp=datetime.datetime.utcnow()
#     )
#     db.add(record)
#     db.commit()
#     return {"status": "inserted"}

# # GET endpoint to fetch all data
# @router.get("/market-data", response_model=List[MarketDataIn])
# def get_all_data(db: Session = Depends(get_db)):
#     records = db.query(RawMarketData).all()
#     return records

# from app.services.producer import produce_price_event
# from datetime import datetime
# from fastapi import APIRouter

# router = APIRouter()
# @router.post("/market-data")
# def insert_market_data(data: MarketDataIn, db: Session = Depends(get_db)):
#     record = RawMarketData(
#         symbol=data.symbol,
#         price=data.price,
#         provider=data.provider,
#         timestamp=datetime.utcnow()
#     )
#     db.add(record)
#     db.commit()
#     db.refresh(record)

#     # ⬇️ Produce message to Kafka after inserting
#     produce_price_event({
#         "symbol": record.symbol,
#         "price": record.price,
#         "timestamp": record.timestamp.isoformat(),
#         "source": record.provider,
#         "raw_response_id": str(record.id)
#     })

#     return {"status": "inserted"}


# from fastapi import APIRouter, HTTPException
# from app.schemas.price_schema import MarketDataIn
# from app.core.database import SessionLocal
# from app.models.schema import RawMarketData
# # from sqlalchemy.orm import Session
# from datetime import datetime



# # from app.services.producer import produce_price_event
# # from app.core.database import get_db

# router = APIRouter()

# @router.post("/market-data", response_model=MarketDataIn)
# def insert_market_data(data: MarketDataIn):
#     record = RawMarketData(
#         symbol=data.symbol,
#         price=data.price,
#         provider=data.provider,
#         timestamp=datetime.utcnow()
#     )
#     db.add(record)
#     db.commit()
#     db.refresh(record)

#     # ⬇️ Produce message to Kafka after inserting
#     produce_price_event({
#         "symbol": record.symbol,
#         "price": record.price,
#         "timestamp": record.timestamp.isoformat(),
#         "source": record.provider,
#         "raw_response_id": str(record.id)
#     })

#     return {"status": "inserted"}


from fastapi import APIRouter, HTTPException
from app.schemas.price_schema import MarketDataIn, LatestPriceResponse
from app.core.database import SessionLocal
from app.models.schema import MovingAverage
from app.models.schema import RawMarketData
from datetime import datetime

router = APIRouter()

@router.post("/market-data", response_model=MarketDataIn)
def create_market_data(data: MarketDataIn):
    db = SessionLocal()
    record = RawMarketData(
        symbol=data.symbol,
        price=data.price,
        provider=data.provider,
        timestamp=datetime.utcnow()
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return data

@router.get("/prices/latest", response_model=LatestPriceResponse)
def get_latest_price(symbol: str):
    db = SessionLocal()
    result = db.query(RawMarketData)\
               .filter(RawMarketData.symbol == symbol)\
               .order_by(RawMarketData.timestamp.desc())\
               .first()
    if not result:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return LatestPriceResponse(
        symbol=result.symbol,
        price=result.price,
        timestamp=result.timestamp.isoformat(),
        provider=result.provider
    )

@router.get("/moving-average/{symbol}")
def get_moving_average(symbol: str):
    db = SessionLocal()
    avg = db.query(MovingAverage).filter(MovingAverage.symbol == symbol).order_by(MovingAverage.id.desc()).first()
    if avg:
        return {"symbol": symbol, "moving_average": avg.average, "timestamp": avg.timestamp}
    return {"error": "No data"}