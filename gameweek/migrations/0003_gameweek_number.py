# Generated by Django 5.0.1 on 2024-01-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameweek', '0002_gameweek_first_game_gameweek_last_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameweek',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
