from django.contrib import admin
from .models import Notices,Events
from django.contrib.auth.models import Group
# Register your models here.

############################################

'''
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'Aseef Administration'

admin_site = MyAdminSite(name='myadmin')
'''

############################################

admin.site.site_header = "Aseef"
admin.site.register(Notices)
admin.site.register(Events)

#admin.site.unregister(Group)