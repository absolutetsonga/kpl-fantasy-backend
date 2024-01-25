# Generated by Django 5.0.1 on 2024-01-25 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0012_squad_activated_bench_boost_squad_activated_free_hit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='left_transfers',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
