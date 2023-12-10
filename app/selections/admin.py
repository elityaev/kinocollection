from django.contrib import admin

from .models import Collection, Query, Tile


admin.site.register(Tile)
admin.site.register(Collection)
admin.site.register(Query)

