import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
REDIS_URI = os.getenv("REDIS_URI", "redis://redis:6379")
