from celery import shared_task

from selections.models import Tile
from selections.services import save_posters

@shared_task
def download_img():
    tiles = Tile.objects.filter(is_saved=False).values('id', 'poster_url')
    if tiles:
        save_posters(tiles)
    print('Нет данных для обновления')