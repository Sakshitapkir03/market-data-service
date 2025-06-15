# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.models.schema import Base

# DATABASE_URL = "postgresql://user:password@db:5432/marketdb"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def init_db():
#     Base.metadata.create_all(bind=engine)

# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.models.schema import Base

# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/marketdb")

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.models.schema import Base

# DATABASE_URL = "postgresql://postgres:postgres@db:5432/marketdb"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def init_db():
#     Base.metadata.create_all(bind=engine)


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.models.schema import Base

# DATABASE_URL = "postgresql://postgres:postgres@db:5432/marketdb"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)

# def init_db():
#     Base.metadata.create_all(bind=engine)
# from app.models import schema
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql://postgres:postgres@db:5432/marketdb"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def init_db():
#     print("🔥 Running init_db() to create tables...")
#     Base.metadata.create_all(bind=engine)

# from app.models import schema
  # ✅ Use the same Base used in models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.schema import Base

DATABASE_URL = "postgresql://user:password@db:5432/marketdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    print("🔥 Running init_db() to create tables...")
    Base.metadata.create_all(bind=engine)

# def get_db():
#     db: Session = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()