from django import forms

class login_form(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class booking_form(forms.Form):
	room_no = forms.IntegerField()
	date_opted = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
	time_in = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}))
	time_out = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}))

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
