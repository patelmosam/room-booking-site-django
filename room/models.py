from django.db import models

# Create your models here.

# class costomer_login(models.Model):
# 	def __str__(self):
# 		return (str([self.username, self.password]))
# 	username = models.CharField(max_length=100)
# 	password = models.CharField(max_length=100)

class rooms_booked(models.Model):
	def __str__(self):
		return (str([self.room_id, self.start, self.end, self.is_booked, 
					self.user_booked, self.owner, self.hotel, self.price]))
	room_id = models.IntegerField()
	start = models.DateField()
	end = models.DateField()
	is_booked = models.BooleanField()
	user_booked = models.CharField(max_length=100)
	owner = models.CharField(max_length=50)
	hotel = models.CharField(max_length=50)
	price = models.IntegerField()


# class manager_login(models.Model):
# 	def __str__(self):
# 		return (str([self.username, self.password]))
# 	username = models.CharField(max_length=100)
# 	password = models.CharField(max_length=100)

class rooms_added(models.Model):
	def __str__(self):
		return (str([self.owner, self.start_room, self.end_room, self.start,
				self.end, self.price, self.is_booked]))
	owner = models.CharField(max_length=50)
	room_number = models.IntegerField()
	start = models.DateField()
	end = models.DateField()
	price = models.IntegerField()
	is_booked = models.IntegerField()

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

class hotels(models.Model):
	def __str__(self):
		return(str([self.name, self.owner, self.rooms,
				self.picture_name, self.picture, self.address, self.Type,
				self.price, self.discription]))
	name = models.CharField(max_length=50)
	owner = models.CharField(max_length=50)
	rooms = models.IntegerField()
	picture = models.FileField(upload_to='static/images/')
	address = models.CharField(max_length=500)
	Type = models.CharField(max_length=10)
	price = models.IntegerField()
	discription = models.CharField(max_length=500)