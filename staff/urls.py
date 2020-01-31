from django.urls import path
from . import views


urlpatterns=[
    path('staff_home/',views.staffHome,name='staff_home'),
    path('verification/', views.verify,name='verification'),
    path('verification/verifyYes/', views.verifyYes, name='verify-yes'),
    path('verification/verifyNo/', views.verifyNo, name='verify-no'),
    path('', views.loginPage,name='staff_login'),
#path('login_process/', views.loginPro ,name='staff_login'),
    path('logout/', views.logoutPage,name='staff_logout'),
    path('notice_paste/',views.Notice_Paste,name="Notice_Paste"),
    path('pasting_notices',views.pastingNotices,name="paste_notice"),
]