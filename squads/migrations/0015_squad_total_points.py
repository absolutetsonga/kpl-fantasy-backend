# Generated by Django 5.0.1 on 2024-02-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0014_alter_squad_total_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='total_points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
