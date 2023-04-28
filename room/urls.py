from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('signup/', views.signup, name="signup"),
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),

	path('rmsignup/', views.rm_signup, name="rmsignup"),
	path('rmlogin/',views.rm_login, name="rmlogin"),

	path('profile/', views.profile, name="profile"),
	path('book_room/', views.book_room, name="book_room"),
	path('view_book/', views.view_book, name='view_book'),
	path('explore/', views.explore, name='explore'),
	

	path('add_rooms/', views.add_rooms, name='add_rooms'),
	path('my_hotel/', views.my_hotel, name='my_hotel'),
	path('booked_rooms/', views.booked_rooms, name='booked_rooms'),

]