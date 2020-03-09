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

class added_rooms(models.Model):
	def __str__(self):
		return (str([self.start_room, self.end_room, self.in_time,
				self.out_time, self.buffer_days]))
	start_room = models.IntegerField()
	end_room = models.IntegerField()
	in_time = models.CharField(max_length=100)
	out_time = models.CharField(max_length=100)
	buffer_days = models.IntegerField()

class rooms_history(models.Model):
	def __str__(self):
		return (str([self.action, self.room_id, 
				 self.date_booking, self.date_opted, 
				 self.time_booking, self.time_opted, self.username]))
	action = models.CharField(max_length=50)
	room_id = models.IntegerField()
	date_booking = models.DateField()
	date_opted = models.CharField(max_length=100)
	time_booking = models.TimeField()
	time_opted = models.CharField(max_length=50)
	username = models.CharField(max_length=100)