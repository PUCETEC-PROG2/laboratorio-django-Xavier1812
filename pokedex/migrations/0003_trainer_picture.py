# Generated by Django 4.2 on 2025-01-22 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_alter_pokemon_height_alter_pokemon_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='picture',
            field=models.ImageField(blank=True, default='trainer_images/default.png', null=True, upload_to='trainer_images'),
        ),
    ]
