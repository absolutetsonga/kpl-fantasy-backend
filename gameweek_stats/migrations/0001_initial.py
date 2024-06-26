# Generated by Django 5.0 on 2023-12-24 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameWeekStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('game_week_number', models.IntegerField()),
                ('goals_scored', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('own_goals_scored', models.IntegerField(default=0)),
                ('clean_sheets', models.IntegerField(default=0)),
                ('yellow_cards', models.IntegerField(default=0)),
                ('red_cards', models.IntegerField(default=0)),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gameweek_stats', to='players.player')),
            ],
        ),
    ]
