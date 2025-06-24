import redis.asyncio as redis
from app.config.setting import REDIS_URI

redis_client = redis.from_url(REDIS_URI, decode_responses=True)

async def check_redis_connection():
    try:
        await redis_client.ping()
        print("Redis connected")
    except Exception as e:
        print("Redis connection failed:", e)
