from django.contrib import admin

from .models import Collection, Query, Tile

for model in (Collection, Query, Tile):
    admin.site.register(model)
