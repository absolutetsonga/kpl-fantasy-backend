# Generated by Django 5.0.1 on 2024-02-28 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gameweek', '0004_alter_gameweek_number'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('home_score', models.IntegerField(null=True)),
                ('away_score', models.IntegerField(null=True)),
                ('sofascore_id', models.IntegerField(null=True, unique=True)),
                ('away_team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='away_game_id', to='teams.team')),
                ('gameweek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='gameweek.gameweek')),
                ('home_team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='home_game_id', to='teams.team')),
            ],
        ),
    ]
