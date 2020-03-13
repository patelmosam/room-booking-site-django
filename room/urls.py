from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('admin_home/', views.admin_home, name="a_home"),
	path('welcome/', views.welcome_cst, name="welcome"),
	path('signup/', views.new_user, name="signup"),
	path('login/', views.login, name="login"),
	path('auth/', views.home, name="auth"),
	path('costomer_home/', views.cust_home, name="c_home"),
	path('book/', views.book_room, name="book_room"),
	path('confirm_book/', views.confirm_book, name="confirm_book"),
	path('view_book/', views.view_book, name='view_book'),
	path('del_book/', views.render_delete, name="delete"),
	path('delete/', views.delete, name='delete'),
	
	path('rmwelcome/', views.rm_welcome, name="rmwelcome"),
	path('rmsignup/', views.new_manager, name="rmsignup"),
	path('rmlogin/',views.rm_login, name="rmlogin"),
	path('rmauth/', views.rm_auth, name="rmauth"),
	path('rm_home/', views.rm_home, name="rm_home"),
	path('room/', views.add_rooms, name='add_rooms'),
	path('checkroom/', views.check_added_room, name='checkroom'),
	path('del_room/', views.delete_room, name='del_room'),
	path('del_auth/', views.delete_auth, name='del_auth'),
	path('edit_room/', views.edit_rooms, name='edit_room'),
	
]