from django.urls import path
from . import views
urlpatterns=[
    path('',views.show_notices,name='main_page'),
]