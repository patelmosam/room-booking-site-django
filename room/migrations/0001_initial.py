# Generated by Django 3.1.2 on 2020-10-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('rooms', models.IntegerField()),
                ('picture', models.FileField(upload_to='')),
                ('address', models.CharField(max_length=500)),
                ('Type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('discription', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='rooms_added',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('start_room', models.IntegerField()),
                ('end_room', models.IntegerField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='rooms_booked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('is_booked', models.BooleanField()),
                ('user_booked', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=50)),
                ('hotel', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='rooms_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=50)),
                ('room_id', models.IntegerField()),
                ('date_booking', models.DateField()),
                ('date_opted', models.CharField(max_length=100)),
                ('time_booking', models.TimeField()),
                ('time_opted', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
