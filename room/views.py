from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from room.models import costomer_login

from room.forms import login_form

def index(request):
	return HttpResponseRedirect('/login/')

#_______________costomer backend_________________________________________________ 

def login(request):
	if request.method == "POST":
		form = login_form(request.POST)
		if form.is_valid():
			data = request.POST.copy()
			username = data.get("username")
			password = data.get("password")
			if username == "admin" and password == "anant":
				return HttpResponse("Logged in as admin")
			else:
				return HttpResponse("Login Failed as Admin")
	else:
		form = login_form()
	return render(request, 'room/login.html', {'form':form})

def home(request):
	if request.method == "POST":
		data = request.POST.copy()
		username = data.get("username")
		password = data.get("password")
		q = [x for x in costomer_login.objects.all() if x.username == username]
		if username == "admin" and password == "anant":
			return HttpResponseRedirect("/admin_home/")
		elif len(q) > 0 and q[0].username == username and q[0].password == password:
			return HttpResponseRedirect("/costomer_home/")
		else:
			return HttpResponse("Login Failed")

def cust_home(request):
	#global Username
	username = request.session['username']
	data = rooms_data.objects.all()
	context = {'history':'/history/', 'book':'/book/', 'del_book':'/del_book/', 'view_book':'/cust_book/','username':username, 'data':data, 'table':True}
	
	return render(request, "room/costomer_home.html", context)

def admin_home(request):
	return HttpResponse("ADMIN ACTIVE")

def new_user(request):
	if request.method == "POST":
		form = login_form(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/welcome/")
	else:
		form = login_form()
	return render(request, 'room/signup.html', {'form':form})

def welcome_cst(request):
	data = request.POST.copy()
	username = data.get("username")
	password = data.get("password")
	q = [x for x in costomer_login.objects.all() if x.username == username]
	if len(q) != 0:
		return HttpResponse("Login Failed: Username Already Exists!")
	q = costomer_login()
	q.username = username
	q.password = password
	q.save()
	return HttpResponse("Welcome, {}!".format(username))


def book_room(request):
	if request.method == "POST":
		form = booking_form(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/confirm/")
	else:
		form = booking_form()
	return render(request, 'room/book_cust.html', {'form':form})

def view_book(request):
	
	return render(request, 'polls/history.html', {'data': q})


#____________________manager backend ______________________________________________________-

def new_manager(request):
	if request.method == "POST":
		form = login_form(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/rmwelcome/")
	else:
		form = login_form()
	return render(request, 'room/rmsignup.html', {'form':form})

def rm_welcome(request):
	data = request.POST.copy()
	username = data.get("username")
	password = data.get("password")
	q = [x for x in costomer_login.objects.all() if x.username == username]
	if len(q) != 0:
		return HttpResponse("Login Failed: Username Already Exists!")
	q = costomer_login()
	q.username = username
	q.password = password
	q.save()
	return HttpResponse("Welcome, Manager {}!".format(username))

def rm_login(request):
	if request.method == "POST":
		form = login_form(request.POST)
		if form.is_valid():
			data = request.POST.copy()
			username = data.get("username")
			password = data.get("password")
			if username == "admin" and password == "mosam":
				return HttpResponse("Logged in as admin")
			else:
				return HttpResponse("Login Failed as Admin")
	else:
		form = login_form()
	return render(request, 'room/rmlogin.html', {'form':form})

def rmhome(request):
	if request.method == "POST":
		data = request.POST.copy()
		username = data.get("username")
		password = data.get("password")
		q = [x for x in costomer_login.objects.all() if x.username == username]
		if username == "admin" and password == "mosam":
			return HttpResponseRedirect("/admin_home/")
		elif len(q) > 0 and q[0].username == username and q[0].password == password:
			return HttpResponseRedirect("/rm_home/")
		else:
			return HttpResponse("Login Failed")

def rm_homepage(request):
	form = info_form()
	return render(request, 'room/rmhome.html', {'form':form})

def rm_panel(request):
	if request.method == "POST":
		data = request.POST.copy()
		no_of_rooms = data.get("no_of_rooms")
		slot_time = data.get("slot_time")
		return HttpResponse('NO OF ROOM IS : {}'.format(no_of_rooms))	