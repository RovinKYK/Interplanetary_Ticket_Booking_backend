# Generated by Django 4.2.4 on 2023-08-20 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_planet_planet_photo_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinations',
            name='destination_photo_link',
        ),
    ]
