# Generated by Django 3.2.16 on 2023-05-03 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0015_auto_20230504_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms_booked',
            name='room_id',
            field=models.IntegerField(default=0),
        ),
    ]