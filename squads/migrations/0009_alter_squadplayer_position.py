# Generated by Django 5.0 on 2023-12-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0008_alter_squadplayer_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squadplayer',
            name='position',
            field=models.CharField(choices=[('GK', 'Goalkeeper'), ('LD', 'Left Defender'), ('LCD', 'Left Center Defender'), ('RCD', 'Right Center Defender'), ('RD', 'Right Defender'), ('LM', 'Left Midfielder'), ('CM', 'Center Midfielder'), ('RM', 'Right Midfielder'), ('LS', 'Left Striker'), ('CS', 'Center Striker'), ('RS', 'Right Striker'), ('SGK', 'Substitute Goalkeeper'), ('SD', 'Substitute Defender'), ('SM', 'Substitute Midfielder'), ('SS', 'Substitute Striker')], max_length=255),
        ),
    ]