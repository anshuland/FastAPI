from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    HIP_HOP = 'hip-hop'

BANDS = [
    {'id': 1, 'name': 'Anshul', 'genre': 'Rock'},
    {'id': 2, 'name': 'Abhinav', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Aditya', 'genre': 'Hip-Hop'},
]

'''
@app.get('/')
async def index():
    return {'hello': 'world'}

@app.get('/about')
async def about():
    return 'An Exceptional Company'
'''

@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS

@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code = 404, detail = 'Band not found')
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]