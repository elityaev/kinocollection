# Generated by Django 4.2.7 on 2023-12-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("selections", "0003_remove_query_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="query",
            name="tiles",
            field=models.ManyToManyField(blank=True, to="selections.tile"),
        ),
    ]
