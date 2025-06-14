# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.models.schema import Base

# DATABASE_URL = "postgresql://user:password@db:5432/marketdb"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def init_db():
#     Base.metadata.create_all(bind=engine)

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.schema import Base

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/marketdb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)