from fastapi import FastAPI

from database.connection import Base, engine
from database import models

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Financial News & Sentiment Analysis Engine",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Financial News Sentiment Analysis API is Running"
    }