# from fastapi import FastAPI
# from .api.routes import router
# from .core.database import engine
# from .models.models import Base

# # Create tables
# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Market Data Service",
#     description="Production-ready microservice for market data",
#     version="1.0.0"
# )

# app.include_router(router, prefix="/api/v1")

# @app.get("/health")
# async def health_check():
#     return {"status": "healthy"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


# from fastapi import FastAPI
# # from app.api.routes import router as price_router
# from app.core.database import init_db


# app = FastAPI()
# init_db()
# @app.get("/")
# def health():
#     return {"status": "running"}
# # app.include_router(price_router)


# from fastapi import FastAPI
# from app.core.database import init_db

# app = FastAPI()

# print("🔥 Running init_db() to create tables...")
# init_db()

# @app.get("/")
# def root():
#     return {"status": "running"}


from fastapi import FastAPI
from app.core.database import init_db
from app.api.routes import router 
app = FastAPI()

@app.on_event("startup")
def startup_event():
    print("🔥 Running init_db() to create tables...")
    init_db()
app.include_router(router)
@app.get("/")
def root():
    return {"status": "running"}