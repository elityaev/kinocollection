from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.http import require_POST

from .forms import RequestForm
from .models import Collection, Tile
from .services import request_random_tile


class RandomTileView(View):
    async def get(self, request):
        return await sync_to_async(render)(request, 'selections/index.html', {'form': RequestForm()})

    async def post(self, request):
        form = RequestForm(request.POST)
        if form.is_valid():
            query = await request_random_tile(form.cleaned_data['genre'], form.cleaned_data['count'])
            if isinstance(query, str):
                return HttpResponseServerError(query)
            return await sync_to_async(redirect)(
                'selections:query', query.id
            )


class QueryView(View):
    def get(self, request, query_id):
        tiles = Tile.objects.filter(query__id=query_id )
        return render(request, 'selections/query_tiles.html', {'tiles': tiles})

    def post(self, request, query_id):
        collection, created = Collection.objects.get_or_create(user=request.user)
        tile_list = request.POST.getlist('tile')
        tiles = Tile.objects.filter(id__in=tile_list)
        collection.tiles.add(*tiles)
        return redirect('selections:collection', request.user.id)


@login_required
def collection(request, user_id):
    tiles = Tile.objects.filter(collection__user_id=user_id)
    return render(request, 'selections/collection.html', {'tiles': tiles})



@require_POST
def tile_remove(request, tile_id):
    collection = Collection.objects.get(user=request.user)
    tile = Tile.objects.get(id=tile_id)
    collection.tiles.remove(tile)
    return redirect('selections:collection', request.user.id)

