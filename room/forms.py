from django import forms
from .models import *

import datetime

now = datetime.datetime.now()
now_string = "{:02d}-{:02d}-{:02d} {:02d}:{:02d}:00".format(now.year, now.month, now.day, now.hour, now.minute)

class login_form(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class booking_form(forms.Form):

	start = forms.DateTimeField(
		widget=forms.widgets.DateTimeInput(
			attrs={
				'type': 'datetime-local',
				'placeholder': 'when do you want to check in',
				'title': 'Enter the date you want to start your stay in this room',
				'class': 'date-input-1',
				'id': 'date-input-1',
				"min": now_string
 			}
		))

	end = forms.DateTimeField(
		widget=forms.widgets.DateTimeInput(
			attrs={
				'type': 'datetime-local',
				'placeholder': 'when do you want to check in',
				'title': 'Enter the date you want to start your stay in this room',
				'class': 'date-input-2',
				'id': 'date-input-2',
				"min": now_string
			}
		))

	class Meta:
		model = rooms_booked
		fields = ('start', 'end')


class add_room(forms.Form):
	start_room = forms.IntegerField()
	end_room = forms.IntegerField()
	time_in = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}))
	time_out = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}))
	buffer_days = forms.IntegerField()

class deletion(forms.Form):
	room_no = forms.IntegerField()
	date_opted = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
	time_in = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}))
	time_out = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}))
