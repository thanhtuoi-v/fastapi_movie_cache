import json
from app.config.redis_client import redis_client

async def get_or_set_cache(key: str, fetch_function, ttl: int):
    cached = await redis_client.get(key)
    if cached:
        print(f"Cache hit for {key}")
        return json.loads(cached)
    data = await fetch_function()
    await redis_client.set(key, json.dumps(data), ex=ttl)
    print(f"Cache miss → Fetched & cached for {key}")
    return data

