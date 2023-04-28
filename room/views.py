from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from room.models import rooms_history, rooms_booked, rooms_added, hotels
from datetime import datetime
from room.forms import login_form, booking_form, deletion, add_room
from django.contrib.auth.models import User, auth
from django.contrib import messages



#__________________User Authentication________________________________________________________________________# 

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
		
		if user is not None:
			if not user.is_superuser:
				auth.login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'can\'t login through manager id')
				return redirect('login')
		else:
			messages.info(request, 'invalid username or password')
			return redirect('login')
	else:
		return render(request, 'room/login.html')

def signup(request):
	if request.method =="POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			if User.objects.filter(username=username):
				messages.info(request, 'Username is Taken')
				return redirect("signup")
			elif User.objects.filter(email=email):
				messages.info(request, 'This email has been allready registered')
				return redirect("signup")
			else:	
				messages.info(request, 'user is created')
				user = User.objects.create_user(username=username, 
												first_name = first_name,
												last_name = last_name,
												email = email,
												password = password1)
				user.save()
				return redirect('login')
		else:
			messages.info(request, 'Password does not match')
			return redirect('signup')
		return redirect('/')
		
	else:
		return render(request, 'room/signup.html')

def rm_signup(request):
	if request.method =="POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			if User.objects.filter(username=username):
				messages.info(request, 'Username is Taken')
				return redirect("rmsignup")
			elif User.objects.filter(email=email):
				messages.info(request, 'This email has been allready registered')
				return redirect("rmsignup")
			else:	
				messages.info(request, 'user is created')
				user = User.objects.create_user(username = username, 
												first_name = first_name,
												last_name = last_name,
												email = email,
												password = password1,
												is_superuser = True)
				user.save()
				return redirect('rmlogin')
		else:
			messages.info(request, 'Password does not match')
			return redirect('rmsignup')
		return redirect('/')
		
	else:
		return render(request, 'room/rmsignup.html')

def rm_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password) 
		
		if user is not None:
			if user.is_superuser:
				auth.login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'can\'t login through customer id')
				return redirect('rmlogin')
		else:
			messages.info(request, 'invalid username or password')
			return redirect('rmlogin')
	else:
		return render(request, 'room/rmlogin.html')


def logout(request):
	auth.logout(request)
	return redirect('/')

#_______________End Authentication____________________________________________________________________________#

#_______________costomer backend______________________________________________________________________________#

def index(request):
	# return HttpResponseRedirect('/index/')
	return render(request, 'room/index.html')

def explore(request):
	if request.method == 'POST':
		pass
	else:
		data = hotels.objects.all()
		return render(request, 'room/explore.html', {'data':data})

def profile(request):
	return render(request, 'room/profile.html')


def book_room(request):
	user = request.user.username
	if request.method == "POST":
		hotel = request.POST['hotel']
		start = request.POST['start']
		end = request.POST['end']
		guest = request.POST['guest']
		rno = request.POST['from']
		price = request.POST['price']
		hdata = hotels.objects.get(name=hotel)
		owner = hdata.owner

		try:	
			r =rooms_booked.objects.get(owner=owner, room_id=rno)
			messages.info(request, 'room is already booked')
			return render(request, 'room/book_cust.html')
		except:
			room = rooms_booked()
			room.room_id = rno
			room.owner = owner
			room.start = start
			room.end = end
			room.is_booked = True
			room.user_booked = user
			room.hotel = hotel
			room.price = price
			room.save()
			messages.info( request, 'room booked sucessfully')
			return render(request, 'room/book_cust.html')
		
			
	else:
		try:
			hotel = request.GET.get('name')
			# price = request.GET.get('price')
			data = hotels.objects.get(name=hotel)
			# rooms_booked.objects.filter(id=2).delete()
			return render(request, 'room/book_cust.html', {'data':data})
		except:
			return redirect('/explore/')

#done
def view_book(request):
	username = request.user.username
	data = [x for x in rooms_booked.objects.all() if x.user_booked==username]
	# print(data.
	return render(request, 'room/view_book.html', {'data': data})



#____________________manager backend ______________________________________________________-

def add_rooms(request):
	# username = request.session["rmname"]
	owner = request.user.username
	if request.method == "POST":
		from_ = request.POST['from']
		to = request.POST['to']
		start = request.POST['start']
		end = request.POST['end']
		price = request.POST['price']
		
		sy, ey = int(start.split('-')[0]), int(end.split('-')[0])
		sd, sm = int(start.split('-')[2]), int(start.split('-')[1])  
		ed, em = int(start.split('-')[2]), int(start.split('-')[1]) 
		if sy <= ey and sm <= em and sd <= ed:
			if rooms_added.objects.filter(owner=owner):
				r = rooms_added.objects.get(owner=owner)
			
				# for r in rdata:
				if r.end_room < int(from_) :
					room = rooms_added()
					room.owner = owner
					room.start_room = from_
					room.end_room = to
					room.start = start
					room.end = end
					room.price = price
					room.save()
					messages.info(request, 'Rooms are added')
				else:
					messages.info(request, 'rooms are already added')
					return render(request, 'room/addrooms.html')

			else:
				room = rooms_added()
				room.owner = owner
				room.start_room = from_
				room.end_room = to
				room.start = start
				room.end = end
				room.price = price
				room.save()
				messages.info(request, 'Rooms are added')
				return render(request, 'room/addrooms.html')
		else:
			messages.info(request, 'rooms con\'t be add')
			return render(request, 'room/addrooms.html')
			# return HttpResponseRedirect("/checkroom/")
		return render(request, 'room/addrooms.html')
	else:
		owner = request.user.username
		data = hotels.objects.get(owner=owner)
		return render(request, 'room/addrooms.html', {'data':data})



def my_hotel(request):
	if request.method == 'POST':
		user = request.user.username

		if (request.POST.get('btnUpload_File_2', False)) is not False:

			picture = request.FILES['UpLoad']
			hdata = hotels.objects.get(owner=user)
			hdata.picture.delete()
			hdata.picture = picture
			hdata.save()

			return render(request, "room/my_hotel.html", {'data': hdata})

		if (request.POST.get('save', False)) is not False:
			name = request.POST['name']
			address = request.POST['adderss']

			messages.info(request, 'Profile saved')

			if hotels.objects.filter(owner=user):
				hotel = hotels.objects.get(owner=user)
				hotel.name = name
				hotel.address = address
				hotel.save()
			else:
				hotel = hotels()
				hotel.name = name
				hotel.owner = user
				hotel.address = address
				hotel.rooms = 0
				hotel.price = 0
				hotel.Type = ""
				hotel.discription = ""
				hotel.save()

		if (request.POST.get('save2', False)) is not False:
			totel = request.POST['totel']
			price = request.POST['price']
			Type = request.POST['type']
			discription = request.POST['discription']
			messages.info(request, 'settings saved')
			# print(totel, price, Type, discription)
			hotel = hotels.objects.get(owner=user)
			hotel.rooms = totel
			hotel.price = price
			hotel.Type = Type
			hotel.discription = discription
			hotel.save()

		hdata = hotels.objects.get(owner=user)
		return render(request, "room/my_hotel.html", {'data':hdata})
	else:
		# hotels.objects.filter(id=2).delete()
		user = request.user.username
		if hotels.objects.filter(owner=user):
			hdata = hotels.objects.get(owner=user)
			return render(request, "room/my_hotel.html", {'data':hdata})
		else:
			return render(request, "room/my_hotel.html")

def booked_rooms(request):
	user = request.user.username
	hotel = hotels.objects.get(owner=user)
	hotel = hotel.name
	data = [x for x in rooms_booked.objects.all() if x.hotel==hotel]
	return render(request, 'room/booked_rooms.html', {'data': data})
