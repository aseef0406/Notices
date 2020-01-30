from django.shortcuts import render,HttpResponse
# Create your views here.
from .models import Notices,Events


def show_notices(request):
    notice_list=Notices.objects.raw("select * from notice_notices")
    event_list = Events.objects.raw("select * from notice_events")
    '''e=Events(e_date='2020-01-20 20:20',e_title='asdfghjkl',e_data='datatatatatatatatatatattatattatatatatattaatt')
    e.save()'''
    args={'notice_list':notice_list,'event_list':event_list}
    return render(request,"index.html",args)
