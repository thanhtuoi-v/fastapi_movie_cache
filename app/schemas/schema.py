def individual_serial(movie) -> dict:
    return {
        "id": str(movie["_id"]),
        "title": movie["title"],
        "year": movie["year"],
        "genres": movie["genres"],
        "duration": movie["duration"],
        "description": movie["description"],
        "director": movie["director"]
    }

async def list_serial(movies) -> list:
    return [individual_serial(movie) async for movie in movies]



