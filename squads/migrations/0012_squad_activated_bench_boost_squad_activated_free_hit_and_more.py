# Generated by Django 5.0.1 on 2024-01-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0011_alter_squad_total_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='activated_bench_boost',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squad',
            name='activated_free_hit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squad',
            name='activated_triple_captain',
            field=models.BooleanField(default=False),
        ),
    ]