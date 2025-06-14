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


from fastapi import FastAPI
from app.api.routes import router as price_router
from app.core.database import init_db

init_db()
app = FastAPI()
app.include_router(price_router)