from motor.motor_asyncio import AsyncIOMotorClient
from app.config.setting import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["movies_db"]
collection = db["movies"]

async def check_mongo_connection():
    try:
        await client.admin.command("ping")
        print("MongoDB connected")
    except Exception as e:
        print("MongoDB connection failed:", e)