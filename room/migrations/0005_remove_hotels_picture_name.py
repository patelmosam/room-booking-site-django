# Generated by Django 3.2.16 on 2023-04-28 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_alter_hotels_picture_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='picture_name',
        ),
    ]