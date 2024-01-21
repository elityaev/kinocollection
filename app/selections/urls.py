from django.urls import path

from . import views

app_name = 'selections'


urlpatterns = [
    path('', views.RandomTileView.as_view(), name='random_tile'),
    path('query/<int:query_id>/', views.QueryView.as_view(), name='query'),
    path('collection/<int:user_id>/', views.collection, name='collection'),
    path('tile_remove/<int:tile_id>/', views.tile_remove, name='tile_remove'),
]
