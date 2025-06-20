# from sqlalchemy import Column, Integer, String, Float, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# import datetime

# Base = declarative_base()

# class Price(Base):
#     __tablename__ = "prices"
#     id = Column(Integer, primary_key=True, index=True)
#     symbol = Column(String, index=True)
#     price = Column(Float)
#     timestamp = Column(DateTime, default=datetime.datetime.utcnow)
#     provider = Column(String)

# class MovingAverage(Base):
#     __tablename__ = "symbol_averages"
#     id = Column(Integer, primary_key=True, index=True)
#     symbol = Column(String, index=True)
#     average = Column(Float)
#     timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# class RawResponse(Base):
#     __tablename__ = "raw_responses"
#     id = Column(String, primary_key=True)  # UUID from API response
#     content = Column(String)
#     timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# class PollingJob(Base):
#     __tablename__ = "polling_jobs"
#     job_id = Column(String, primary_key=True)
#     symbols = Column(String)
#     interval = Column(Integer)
#     provider = Column(String)
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)

# from sqlalchemy import Column, Integer, String, Float, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# import datetime

# Base = declarative_base()

# class RawMarketData(Base):
#     __tablename__ = "raw_market_data"
#     id = Column(Integer, primary_key=True, index=True)
#     symbol = Column(String, index=True)
#     price = Column(Float)
#     timestamp = Column(DateTime, default=datetime.datetime.utcnow)
#     provider = Column(String)

# class MovingAverage(Base):
#     __tablename__ = "symbol_averages"
#     id = Column(Integer, primary_key=True, index=True)
#     symbol = Column(String)
#     average = Column(Float)
#     timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# class PollingJob(Base):
#     __tablename__ = "polling_jobs"
#     id = Column(Integer, primary_key=True, index=True)
#     symbols = Column(String)  # comma-separated list
#     interval = Column(Integer)  # seconds
#     provider = Column(String)


from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class RawMarketData(Base):
    __tablename__ = "raw_market_data"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    provider = Column(String)

class MovingAverage(Base):
    __tablename__ = "symbol_averages"
    id = Column(Integer, primary_key=True)
    symbol = Column(String, index=True)
    average = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

# class PollingJob(Base):
#     __tablename__ = "polling_jobs"
#     id = Column(Integer, primary_key=True, index=True)
#     symbols = Column(String)  # comma-separated list
#     interval = Column(Integer)
#     provider = Column(String)