from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.user_register,name='register'),
    path('register_process/', views.registerProcess),
    path('alumini_login/',views.alumini_login,name="alumini_login"),
    path('login_process/', views.loginProcess),
    path('home_login/', views.home_login,name="home_login"),
    path('alumini_logout/', views.aluminiLogout,name="alumini_logout"),

]