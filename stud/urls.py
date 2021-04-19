from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('studregister',views.studregister,name='studregister'),
    path('studlogin',views.studlogin,name='studlogin'),
    path('adminpage',views.adminpage,name="adminpage"),
    path('admindashboard',views.admindashboard,name="admindashboard"),
    path('adminprofile',views.adminprofile,name="adminprofile"),
    path('studentpage',views.studentpage,name="studentpage"),
    path('studdashboard',views.studdashboard,name="studdashboard"),
    path('studprofile',views.studprofile,name="studprofile"),
    path('signup',views.signup,name="signup"),


]