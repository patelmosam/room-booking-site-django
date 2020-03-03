from django.db import models

# Create your models here.

class login_data(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class rooms_data(models.Model):
	room_id = models.IntegerField()
	time_in = models.TimeField()
	time_out = models.TimeField()
	is_booked = models.BooleanField()