from django.db import models
from django.contrib.auth.models import User


class Tile(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    genres = models.JSONField(blank=True, null=True)
    countries = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    rating = models.JSONField(blank=True, null=True)
    is_saved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    poster_db_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tiles = models.ManyToManyField(Tile)


class Query(models.Model):
    tiles = models.ManyToManyField(Tile, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
