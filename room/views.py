from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from room.models import rooms_history, rooms_booked, rooms_added, hotels
from room.forms import login_form, booking_form, deletion, add_room
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import date


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
			owner = request.session['owner']
			room = request.session['room_number']

			print()
			print()
			print(request.session['owner'])
			print()
			print()

			hotel = hotels.objects.get(owner=owner)
			room = rooms_added.objects.get(owner=owner, room_number=room)

			return render(
				request, 'room/book_cust.html', {
					'form': booking_form,
					'hotel': hotel,
					'room': room
				}
			)
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
	rooms_pro = rooms_added.objects.filter(owner=owner)

	if request.method == "POST":
		if (request.POST.get('add_room', False)) is not False:

			if len(request.POST['room_number']) is not 0 and len(request.POST['price']) is not 0:

				room_number = request.POST['room_number']
				price = request.POST['price']
				description = request.POST['description']

				try:
					# when this line generates en error the exception handling catches it and runs the 'except_block'
					error_generation_line = rooms_added.objects.get(owner=owner, room_number=room_number)
					messages.info(request, 'that room was already added')

				except:
					room = rooms_added()
					room.owner = owner
					room.room_number = room_number
					room.date_added = date.today()
					room.price = price
					room.is_booked = 0
					room.room_description = description
					room.save()
					messages.info(request, 'Rooms are added')

				return redirect('/add_rooms/#add_rooms')
			else:
				messages.info(request, 'please enter data')
				return redirect('/add_rooms/#add_rooms')

		elif not request.user.is_superuser:

			rooms = rooms_added.objects.all()

			for room in rooms:
				if (request.POST.get('btnBook_'+str(room.room_number), False)) is not False:

					request.session['owner'] = request.POST['btnBook_'+str(room.room_number)]
					request.session['room_number'] = room.room_number

					return redirect('/book_room/')

		else:
			for rooms_pro in rooms_pro:
				if (request.POST.get('btnDel_' + str(rooms_pro.room_number), False)) is not False:
					room = rooms_added.objects.get(owner=owner, room_number=rooms_pro.room_number)
					room.delete()
					return redirect('/add_rooms/')


				try:
					if (request.POST.get('btnUpload_File_' + str(rooms_pro.room_number), False)) is not False:
						picture = request.FILES['UpLoad_' + str(rooms_pro.room_number)]
						room = rooms_added.objects.get(owner=owner, room_number=rooms_pro.room_number)
						room.room_picture.delete()
						room.room_picture = picture
						room.save()

						return redirect('/add_rooms/')
				except:
					return redirect('/add_rooms/')

	else:
		try:
			owner = request.user.username

			context = {}

			hotel_pro = hotels.objects.get(owner=owner)

			context['hotel_pro'] = hotel_pro
			context['rooms_pro'] = rooms_pro
			return render(request, 'room/addrooms.html', context)

		except:
			hotel = request.GET.get('name')
			context = {}

			hotel_pro = hotels.objects.get(name=hotel)
			rooms = rooms_added.objects.filter(owner=hotel_pro.owner)

			context['hotel_pro'] = hotel_pro
			context['rooms_pro'] = rooms

			return render(request, 'room/addrooms.html', context)



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
