from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from room.models import costomer_login

from room.forms import login_form, booking_form, add_room 

def index(request):
	return HttpResponseRedirect('/login/')

#_______________costomer backend_________________________________________________ 

# done
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

# done
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

# done
def cust_home(request):
	username = request.session['username']
	data = rooms_data.objects.all()
	context = {'history':'/history/', 'book':'/book/', 'del_book':'/del_book/', 'view_book':'/cust_book/','username':username, 'data':data, 'table':True}
	
	return render(request, "room/costomer_home.html", context)

#done
def admin_home(request):
	return HttpResponse("ADMIN ACTIVE")

# done
def new_user(request):
	if request.method == "POST":
		form = login_form(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/welcome/")
	else:
		form = login_form()
	return render(request, 'room/signup.html', {'form':form})

# done
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

#  done
def book_room(request):
	if request.method == "POST":
		form = booking_form(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/confirm/")
	else:
		form = booking_form()
	return render(request, 'room/book_cust.html', {'form':form})

#done
def view_book(request):
	q = [x for x in rooms_history.objects.all() if x.username == request.session["username"]]
	return render(request, 'room/history.html', {'data': q})

#done
def render_delete(request):
	q = [x for x in rooms_data.objects.all() if x.user_booked == request.session["username"]]
	return render(request, 'room/delete.html', {'data': q})

#done
def delete(request):
	if request.method == "POST":
		username = request.session['username']
		data = request.POST.copy()
		id = int(data.get('id'))
		rooms_data.objects.filter(id=id).delete()
		data = rooms_data.objects.all()
		context = {'history':'/history/', 'book':'/book/', 'del_book':'/del_book/', 'view_book':'/cust_book/','username':username, 'data':data, 'table':True}
	
	return render(request, "room/customer_home.html", context)



#____________________manager backend ______________________________________________________-

# done
def new_manager(request):
	if request.method == "POST":
		form = login_form(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/rmwelcome/")
	else:
		form = login_form()
	return render(request, 'room/rmsignup.html', {'form':form})

# done
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

# done
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

#done
def rm_auth(request):
	if request.method == "POST":
		data = request.POST.copy()
		username = data.get("username")
		password = data.get("password")
		q = [x for x in manager_login.objects.all() if x.username == username]
		if username == "admin" and password == "mosam":
			return HttpResponseRedirect("/admin_home/")
		elif len(q) > 0 and q[0].username == username and q[0].password == password:
			request.session["rmname"] = username
			return HttpResponseRedirect("/rm_home/",{'username':username})
		else:
			return HttpResponse("Login Failed")

#done
def rm_home(request):
	username = request.session["rmname"]
	data = added_rooms.objects.all()
	context = {'room':'/room/', 'del_room':'/del_room/', 'edit_room':'/edit_room/','data': data, 'username': username}
	return render(request, "room/manager_home.html", context)


#done
def add_rooms(request):
	username = request.session["rmname"]
	if request.method == "POST":
		form = add_rooms(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/checkslot/")
	else:
		form = add_room()
	return render(request, 'room/addrooms.html', {'form':form,'username':username})

#done
def delete_room(request):
	if request.method == "POST":
		return HttpResponseRedirect("/checkslot/")
	else:
		data = added_rooms.objects.all()
		return render(request, 'room/deleteroom.html', {'data':data})

#done
def delete_auth(request):
	if request.method == "POST":
		data = request.POST.copy()
		id = int(data.get('id'))
		added_rooms.objects.filter(id=id).delete()
		data = added_rooms.objects.all()
		context = {'room':'/room/', 'del_room':'/del_room/', 'edit_room':'/edit_room/', 'table': True, 'data': data}
	return render(request, 'room/manager_home.html', context)

#done
def edit_rooms(request):
	form = add_room()
	data = added_rooms.objects.all()
	return render(request, 'room/editrooms.html', {'form':form, 'data':data})




