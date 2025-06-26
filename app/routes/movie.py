from fastapi import APIRouter, HTTPException
from app.models.movie import Movie,MovieCreate
from app.schemas.schema import individual_serial, list_serial
from app.config import database
from typing import List
from app.utils.cache import get_or_set_cache
from bson import ObjectId
router = APIRouter()


@router.get("/movies")
async def get_all_movies():
    async def fetch_movies():
        return await list_serial(database.collection.find())
    return await get_or_set_cache("movies:all", fetch_movies,120)

@router.get("/movies/{movie_id}")
async def read_movie(movie_id: str):
    cache_key = f"movie:{movie_id}"
    async def fetch_movie():
        movie = await database.collection.find_one({"_id": ObjectId(movie_id)})
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return individual_serial(movie)
    return await get_or_set_cache(cache_key, fetch_movie, 120)


@router.post("/movies/")
async def create_movie(movie: MovieCreate):
    result = await database.collection.insert_one(movie.model_dump())
    return {"id": str(result.inserted_id)}



@router.delete("/movies/{movie_id}")
async def delete_movie(movie_id: str):
    result = await database.collection.delete_one({"_id": ObjectId(movie_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted"}


