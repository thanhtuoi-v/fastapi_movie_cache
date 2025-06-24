from fastapi import FastAPI
from app.routes import movie 
from app.config.database import check_mongo_connection
from app.config.redis_client import check_redis_connection
from contextlib import asynccontextmanager
from app.utils.mock_data import seed_movies

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await seed_movies()
    await check_mongo_connection()
    await check_redis_connection()
    yield  

app = FastAPI(lifespan=lifespan)
app.include_router(movie.router)
