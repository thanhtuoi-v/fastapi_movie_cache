from app.config import database
async def seed_movies():
    sample_movies = [
        {
            "title": "One Piece Film: Red",
            "year": 2022,
            "genres": ["Action", "Adventure", "Animation"],
            "duration": 115,
            "description": "Uta, the world's most beloved singer, reveals herself to the world — including Luffy.",
            "director": "Goro Taniguchi"
        },
        {
            "title": "One Piece: Stampede",
            "year": 2019,
            "genres": ["Action", "Adventure", "Fantasy"],
            "duration": 101,
            "description": "Pirates gather at the Pirates Expo for a treasure hunt honoring Gold Roger.",
            "director": "Takashi Otsuka"
        },
        {
            "title": "One Piece Film: Z",
            "year": 2012,
            "genres": ["Action", "Adventure", "Animation"],
            "duration": 108,
            "description": "The Straw Hat crew faces off against former Marine Admiral 'Z'.",
            "director": "Tatsuya Nagamine"
        }
    ]

    count = await database.collection.count_documents({})
    if count == 0:
        await database.collection.insert_many(sample_movies)
