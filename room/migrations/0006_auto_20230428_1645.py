# Generated by Django 3.2.16 on 2023-04-28 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_remove_hotels_picture_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms_added',
            old_name='end',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='rooms_added',
            name='start',
        ),
    ]