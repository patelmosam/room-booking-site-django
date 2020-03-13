from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from room.models import costomer_login, rooms_history, rooms_data, added_rooms, manager_login
from datetime import datetime
from room.forms import login_form, booking_form, deletion, add_room

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
			request.session["username"] = username
			return HttpResponseRedirect("/costomer_home/",{'username':username})
		else:
			return HttpResponse("Login Failed")
# done
def cust_home(request):
	username = request.session['username']
	data = rooms_data.objects.all()
	context = {'view_book':'/view_book/','book':'/book/', 'del_book':'/del_book/','username':username, 'data':data, 'table':True}
	
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
	return render(request, 'room/view_book.html', {'data': q})

#done
def confirm_book(request):
	if request.method == "POST":
		data = request.POST.copy()
		date_opted = data.get("date_opted")
		time_opted_in = data.get("time_in")
		tin = time_opted_in.split(':')
		time_opted_out = data.get("time_out")
		tout = time_opted_out.split(':')
		room_no = data.get("room_no")
		today = str(datetime.date(datetime.now()))
		bdate = date_opted.split('-')
		tdate = today.split('-')
		
		for x in added_rooms.objects.all():
			
			if x.start_room <= int(room_no) and x.end_room >= int(room_no):
				itime = x.in_time.split(':')
				otime = x.out_time.split(':')
				if int(tin[0]) < int(tout[0]):
					print(itime[0],otime[0],tin[0])
					if int(itime[0]) <= int(tin[0]) and int(otime[0]) >= int(tin[0]):
						if int(otime[0]) >= int(tout[0]):
							if int(tdate[2])+x.buffer_days <= int(bdate[2]):
		 # checking in rooms_data	
		 		
								for d in rooms_data.objects.all():
									idate = d.date_opted.split('-')
									if int(idate[1]) == int(bdate[1]) and int(idate[2]) == int(bdate[2]) and int(idate[0]) == int(bdate[0]):
										print(d.room_id,room_no)
										if d.room_id == int(room_no):
											it = d.time_in.split(':')
											ot = d.time_out.split(':')
											print(it,ot,tin)
											if int(it[0]) <= int(tin[0]) and int(ot[0]) >= int(tin[0]):
												return HttpResponse('room is already booked!!')
											else:
												if int(it[0]) <= int(tout[0]) and int(ot[0]) >= int(tout[0]):
													return HttpResponse('room is already booked!!')
									
								context = add_booking(request, room_no, date_opted, time_opted_in, time_opted_out)
								return render(request, "room/customer_home.html", context)
			#   end checking in rooms_data
				else:
					return HttpResponse('please enter valid time slot')	
			
		return HttpResponse('room is not available for booking...')

#done
def add_booking(request, room_no, date_opted, time_opted_in, time_opted_out):
	q = rooms_history()
	q.action = "booking"
	q.room_id = room_no
	q.date_booking = datetime.date(datetime.now())
	q.time_booking = datetime.time(datetime.now())
	q.date_opted = str(date_opted)
	q.time_opted = str('{} - {}'.format(time_opted_in, time_opted_out))
	q.username = request.session["username"]
	q.save()
	q = rooms_data()
	q.room_id = room_no
	q.date_opted = str(date_opted)
	q.time_in = str(time_opted_in)
	q.time_out = str(time_opted_out)
	q.is_booked = True
	q.user_booked = request.session["username"]
	q.save()
	username = request.session["username"]
	rdata = rooms_data.objects.all()
	context = {'view_book':'/view_book/', 'book':'/book/', 'del_book':'/del_book/','username':username, 'data':rdata, 'table':True}
	return context


#done
def render_delete(request):
	q = [x for x in rooms_data.objects.all() if x.user_booked == request.session["username"]]
	return render(request, 'room/delete_book.html', {'data': q})

#done
def delete(request):
	if request.method == "POST":
		username = request.session['username']
		data = request.POST.copy()
		id = int(data.get('id'))
		rooms_data.objects.filter(id=id).delete()
		data = rooms_data.objects.all()
		context = {'view_book':'/view_book/', 'book':'/book/', 'del_book':'/del_book/', 'username':username, 'data':data, 'table':True}
	
	return render(request, "room/costomer_home.html", context)



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
	q = [x for x in manager_login.objects.all() if x.username == username]
	if len(q) != 0:
		return HttpResponse("Login Failed: Username Already Exists!")
	q = manager_login()
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
		form = add_room(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/checkroom/")
	else:
		form = add_room()
	return render(request, 'room/addrooms.html', {'form':form,'username':username})

#done
def check_added_room(request):
	if request.method == "POST":
		data = request.POST.copy()
		try:
			id = int(data.get('id'))
			type_ = 'edit'
		except:
			id = None
			type_ = 'new'
		start_room = data.get("start_room")
		end_room = data.get("end_room")
		time_in = data.get("time_in")
		tin = time_in.split(':')
		time_out = data.get("time_out")
		tout = time_out.split(':')
		bdays = data.get("buffer_days")
		if len(added_rooms.objects.all()) == 0:
			context = add_slot(request, id, start_room, end_room, time_in, time_out, bdays, type_)
			return render(request, 'room/manager_home.html', context)
		else:
			for x in added_rooms.objects.all():
				if int(start_room) < int(end_room):
					if x.start_room <= int(start_room) and x.end_room >= int(start_room):
						if x.end_room >= int(end_room):
							itime = x.in_time.split(':')
							otime = x.out_time.split(':')
							if int(tin[0]) < int(tout[0]):
								if int(itime[0]) <= int(tin[0]) and int(otime[0]) >= int(tin[0]):
									if int(otime[0]) >= int(tout[0]):
										return HttpResponse('time slots are already added!')
									else:
										return HttpResponse('time slots is overlape with another one, please try again!!! ')
							
							else:
								return HttpResponse('enter valid time slot')
						else:
							itime = x.in_time.split(':')
							otime = x.out_time.split(':')
							if int(tin[0]) < int(tout[0]):
								if int(itime[0]) <= int(tin[0]) and int(otime[0]) >= int(tin[0]):
									if int(otime[0]) >= int(tout[0]):
										return HttpResponse('time slots are already added!')
									else:
										return HttpResponse('time slots is overlape with another one, please try again!!! ')
				else:
					return HttpResponse('enter valid rooms!')
			context = add_slot(request, id, start_room, end_room, time_in, time_out, bdays, type_)
			return render(request, 'room/manager_home.html', context)

#done
def add_slot(request, id, start_room, end_room, time_in, time_out, bdays, type_):
	username = request.session["rmname"]	
	if type_ == 'new':
		q = added_rooms()
		q.start_room = start_room
		q.end_room = end_room
		q.in_time = str(time_in)
		q.out_time = str(time_out)
		q.buffer_days = bdays
		q.save()
	elif type_ == 'edit':
		table = added_rooms.objects.get(id=id)
		table.start_room = start_room
		table.end_room = end_room
		table.in_time = time_in
		table.out_time = time_out
		table.buffer_days = bdays
		table.save()
	data = added_rooms.objects.all()
	context = {'room':'/room/', 'del_room':'/del_room/', 'edit_room':'/edit_room/', 'table': True, 'data': data, 'username':username}
	return context


#done
def delete_room(request):
	if request.method == "POST":
		return HttpResponseRedirect("/checkroom/")
	else:
		data = added_rooms.objects.all()
		return render(request, 'room/delete_room.html', {'data':data})

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
	return render(request, 'room/edit_rooms.html', {'form':form, 'data':data})




