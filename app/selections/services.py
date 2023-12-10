import asyncio

import environ
import httpx
from django.conf import settings

from .models import Tile, Query

env = environ.Env()


async def get_tile(genre: str):
    headers = {'X-API-KEY': env('API_KEY')}
    params = {
        'genres.name': genre,
        **settings.ADDITIONAL_REQUEST_PARAM,
    }
    url = settings.KINOPOISK_API_URL

    async with httpx.AsyncClient(timeout=20.0) as client:
        res = await client.get(url, headers=headers, params=params)
        if res.status_code == 200:
            response = res.json()
            if response:
                tile, created = await Tile.objects.aget_or_create(
                    id=response.get('id'),
                    name=response.get('name'),
                    year=response.get('year'),
                    genres=[gen.get('name') for gen in response.get('genres')],
                    countries=[country.get('name') for country in response.get('countries')],
                    description=response.get('description'),
                    poster_url=response.get('poster').get('url')
                )
                tile.rating = response.get('rating')
                await tile.asave()
                return tile
        return


async def request_random_tile(genre: str, count: int):

    tiles = set(await asyncio.gather(
        *(get_tile(genre) for count in range(count)),
        return_exceptions=True
    ))
    if tiles == {None}:
        return 'Проблемы с API кинопоиска'
    query = await Query.objects.acreate()
    await query.tiles.aadd(*tiles)
    return query


def download_file(tile_id: int, url: str):
    file_name = f'posters/{url.split("/")[-2]}.webp'
    file_path = f'static/{file_name}'
    res = httpx.get(url)
    with open(file_path, 'wb+') as f:
        f.write(res.read())
    tile = Tile.objects.get(id=tile_id)
    tile.poster_db_url = file_name
    tile.is_saved = True
    tile.save()


def save_posters(tiles):
    for tile in tiles:
        download_file(tile['id'], tile['poster_url'])