from django import forms

class login_form(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class info_form(forms.Form):
	no_of_rooms = forms.CharField(max_length=10)
	slot_time = forms.TimeField()
