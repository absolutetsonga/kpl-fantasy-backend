# Generated by Django 5.0.1 on 2024-02-01 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameweek_stats', '0003_alter_gameweekstats_gameweek_and_more'),
        ('squadplayers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameweekstats',
            name='player',
        ),
        migrations.AddField(
            model_name='gameweekstats',
            name='is_captain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gameweekstats',
            name='is_vice_captain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gameweekstats',
            name='on_bench',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gameweekstats',
            name='squad_player',
            field=models.ForeignKey(default=229, on_delete=django.db.models.deletion.CASCADE, related_name='gameweek_stats', to='squadplayers.squadplayer'),
            preserve_default=False,
        ),
    ]
