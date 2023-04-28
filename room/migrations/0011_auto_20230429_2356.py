# Generated by Django 3.2.16 on 2023-04-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0010_auto_20230429_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms_added',
            name='default_path',
        ),
        migrations.AlterField(
            model_name='rooms_added',
            name='room_picture',
            field=models.FileField(blank=True, upload_to='static/images/rooms/'),
        ),
    ]
