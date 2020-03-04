from django.db import models

# Create your models here.

class costomer_login(models.Model):
	def __str__(self):
		return (str([self.username, self.password]))
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class rooms_data(models.Model):
	def __str__(self):
		return (str([self.room_id, self.time_in, self.time_out, self.is_booked, self.user_booked, self.date_opted]))
	room_id = models.IntegerField()
	time_in = models.CharField(max_length=100)
	time_out = models.CharField(max_length=100)
	date_opted = models.CharField(max_length=100)
	is_booked = models.BooleanField()
	user_booked = models.CharField(max_length=100, null=True)


class manager_login(models.Model):
	def __str__(self):
		return (str([self.username, self.password]))
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)